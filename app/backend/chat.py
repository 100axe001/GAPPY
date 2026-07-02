"""
Chat — powered by the native `chat-assistant` Lemma agent.

Each app conversation is bound to a Lemma agent conversation (id stored in the app
conversation's metadata) so multi-turn context lives in the pod. The agent runs its own
tool loop with real capabilities: pod tables (tasks/notes), web search, and connected
integrations (Gmail / Calendar / Slack). Conversation history + the sidebar stay in Postgres.
"""
import json
import asyncio
import logging
from typing import Dict, Any, List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .sdk_client import get_lemma_pod, run_sync

logger = logging.getLogger("lifeos.chat")

CHAT_AGENT = "chat-assistant"
POLL_TICKS = 180  # up to ~90s


def _norm_messages(resp) -> List[Dict[str, Any]]:
    data = resp.to_dict() if hasattr(resp, "to_dict") else resp
    return data.get("items", []) if isinstance(data, dict) else []


def _clean_final(text: str) -> str:
    """chat-assistant has no output schema, so replies are plain text; unwrap if enveloped."""
    if not text:
        return ""
    stripped = text.strip()
    if stripped.startswith("{") and '"args"' in stripped:
        try:
            data = json.loads(stripped)
            args = data.get("args", {})
            if isinstance(args, dict):
                out = args.get("output")
                if isinstance(out, str):
                    return out
                if isinstance(out, dict):
                    return out.get("message") or out.get("text") or json.dumps(out)
                return args.get("message") or stripped
        except Exception:
            return text
    return text


async def _run_agent_turn(lemma_conv_id, user_message: str) -> Tuple[str, str, List[str]]:
    """Send to the agent conversation; return (lemma_conv_id, final_text, tools_used)."""
    pod = get_lemma_pod()

    if not lemma_conv_id:
        conv = await run_sync(pod.conversations.create_for_agent, CHAT_AGENT, title="LifeOS Chat")
        lemma_conv_id = str(conv.id)

    before = _norm_messages(await run_sync(pod.conversations.messages, lemma_conv_id, limit=200))
    baseline = len(before)

    await run_sync(pod.conversations.send, lemma_conv_id, user_message)

    for _ in range(POLL_TICKS):
        detail = await run_sync(pod.conversations.get, lemma_conv_id)
        if getattr(detail, "status", None) in ("COMPLETED", "FAILED", "STOPPED"):
            break
        await asyncio.sleep(0.5)

    msgs = _norm_messages(await run_sync(pod.conversations.messages, lemma_conv_id, limit=200))
    new_msgs = msgs[baseline:] if len(msgs) > baseline else msgs

    tools_used: List[str] = []
    final_text = ""
    for m in new_msgs:
        tn = m.get("tool_name")
        if tn and tn not in ("final_result",) and tn not in tools_used:
            tools_used.append(tn)
        if m.get("role") == "assistant" and m.get("text"):
            final_text = m["text"]

    return lemma_conv_id, _clean_final(final_text), tools_used


async def send_message(db: AsyncSession, user_id: int, conversation, user_message: str,
                       settings: Dict[str, str]):
    """Persist user msg, run the chat-assistant agent, persist assistant msg."""
    user_row = await crud.add_message(db, conversation.id, "user", user_message)

    if (conversation.title or "New Chat") == "New Chat":
        snippet = user_message.strip().splitlines()[0][:48]
        conversation.title = snippet or "New Chat"

    meta = dict(conversation.metadata_json or {})
    lemma_conv_id = meta.get("lemma_conversation_id")

    tools_used: List[str] = []
    try:
        lemma_conv_id, assistant_text, tools_used = await _run_agent_turn(lemma_conv_id, user_message)
        if lemma_conv_id and meta.get("lemma_conversation_id") != lemma_conv_id:
            meta["lemma_conversation_id"] = lemma_conv_id
            conversation.metadata_json = meta
            await db.flush()
    except Exception as e:
        logger.error(f"Chat turn failed: {e}", exc_info=True)
        assistant_text = f"Sorry, something went wrong: {e}"

    if not assistant_text:
        assistant_text = "I wasn't able to complete that — please try rephrasing."

    tool_invocations = [{"tool": t} for t in tools_used]
    assistant_row = await crud.add_message(
        db, conversation.id, "assistant", assistant_text,
        tool_calls=tool_invocations, metadata={"tools_used": tools_used},
    )
    await crud.touch_conversation(db, conversation)

    return user_row, assistant_row, tools_used
