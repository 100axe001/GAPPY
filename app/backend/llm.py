"""
Unified LLM completion across providers, chosen per-user in Settings.

Providers:
  - "lemma"     : the local Lemma agent ("hello"), no external key required.
  - "anthropic" : Claude via the Anthropic Messages REST API (needs anthropic_api_key).
  - "openai"    : OpenAI chat completions REST API (needs openai_api_key).

The chat agent loop (chat.py) speaks a provider-agnostic JSON tool protocol on
top of plain-text completion, so every provider only needs to return text.
"""
import logging
from typing import List, Dict, Any
import httpx
from .ai import get_lemma_pod, run_agent_until_completed

logger = logging.getLogger("lifeos.llm")

DEFAULT_ANTHROPIC_MODEL = "claude-opus-4-8"
DEFAULT_OPENAI_MODEL = "gpt-4o-mini"


def _messages_to_prompt(system: str, messages: List[Dict[str, str]]) -> str:
    """Flattens a chat transcript into a single prompt (used for the Lemma agent)."""
    parts = []
    if system:
        parts.append(f"[SYSTEM]\n{system}")
    for m in messages:
        role = m.get("role", "user").upper()
        parts.append(f"[{role}]\n{m.get('content', '')}")
    parts.append("[ASSISTANT]")
    return "\n\n".join(parts)


async def complete(system: str, messages: List[Dict[str, str]], settings: Dict[str, str]) -> str:
    """Returns the assistant's plain-text completion using the configured provider."""
    provider = (settings.get("llm_provider") or "lemma").lower()

    if provider == "anthropic":
        return await _complete_anthropic(system, messages, settings)
    if provider == "openai":
        return await _complete_openai(system, messages, settings)
    return await _complete_lemma(system, messages, settings)


async def _complete_lemma(system: str, messages: List[Dict[str, str]], settings: Dict[str, str]) -> str:
    pod = get_lemma_pod()
    prompt = _messages_to_prompt(system, messages)
    return await run_agent_until_completed(pod, "hello", prompt)


async def _complete_anthropic(system: str, messages: List[Dict[str, str]], settings: Dict[str, str]) -> str:
    api_key = settings.get("anthropic_api_key") or ""
    if not api_key:
        raise ValueError("Anthropic provider selected but no API key is configured in Settings.")
    model = settings.get("llm_model") or DEFAULT_ANTHROPIC_MODEL

    # Anthropic requires alternating user/assistant; collapse anything else into user turns.
    norm = [{"role": "assistant" if m.get("role") == "assistant" else "user",
             "content": m.get("content", "")} for m in messages]
    payload = {
        "model": model,
        "max_tokens": 2048,
        "system": system,
        "messages": norm,
    }
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post("https://api.anthropic.com/v1/messages",
                                 json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
    chunks = [b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"]
    return "".join(chunks).strip()


async def _complete_openai(system: str, messages: List[Dict[str, str]], settings: Dict[str, str]) -> str:
    api_key = settings.get("openai_api_key") or ""
    if not api_key:
        raise ValueError("OpenAI provider selected but no API key is configured in Settings.")
    model = settings.get("llm_model") or DEFAULT_OPENAI_MODEL

    chat_messages = [{"role": "system", "content": system}] if system else []
    for m in messages:
        role = m.get("role", "user")
        if role not in ("user", "assistant", "system"):
            role = "user"
        chat_messages.append({"role": role, "content": m.get("content", "")})

    payload = {"model": model, "messages": chat_messages, "max_tokens": 2048}
    headers = {"Authorization": f"Bearer {api_key}", "content-type": "application/json"}
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post("https://api.openai.com/v1/chat/completions",
                                 json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
    return data["choices"][0]["message"]["content"].strip()
