"""
Second Brain memory for the chat agent.

Two responsibilities:
  1. build_memory_context — pull a few relevant saved notes to ground a reply.
  2. maybe_save_memory   — after each exchange, let the LLM decide whether
                            anything durable (a preference, fact, commitment,
                            decision) is worth persisting to the Second Brain,
                            and save it automatically if so.
"""
import logging
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, schemas
from .ai import extract_json
from . import llm

logger = logging.getLogger("lifeos.memory")


async def build_memory_context(db: AsyncSession, user_id: int, query: str, limit: int = 5) -> str:
    """Returns a short text block of the most relevant saved notes for grounding."""
    notes = await crud.get_items(db, limit=200, item_type="note")
    if not notes:
        return ""
    tokens = [t for t in (query or "").lower().split() if len(t) > 2]
    scored = []
    for n in notes:
        hay = f"{n.title} {n.content or ''}".lower()
        score = sum(1 for t in tokens if t in hay)
        scored.append((score, n))
    # Prefer keyword matches, then most recent (get_items already returns newest-first)
    scored.sort(key=lambda x: x[0], reverse=True)
    chosen = [n for score, n in scored if score > 0][:limit]
    if not chosen:
        chosen = notes[:limit]  # fall back to most recent notes
    lines = [f"- {n.title}: {(n.content or '')[:200]}" for n in chosen]
    return "\n".join(lines)


async def maybe_save_memory(db: AsyncSession, user_id: int, user_message: str,
                            assistant_message: str, settings: Dict[str, str]) -> Optional[Dict[str, Any]]:
    """Asks the LLM whether this exchange contains something worth remembering.
    Saves it as a Second Brain note when so. Returns the saved record or None."""
    if (settings.get("auto_memory_enabled") or "true").lower() not in ("1", "true", "yes"):
        return None

    system = (
        "You are the memory manager for a personal assistant's Second Brain. "
        "Decide if the user's message contains a DURABLE fact worth remembering long term: "
        "a stable preference, personal detail, ongoing project, relationship, decision, or commitment. "
        "Do NOT save small talk, transient questions, web-search lookups, or things the user only asked about. "
        'Respond ONLY with JSON: {"save": true|false, "title": "<short>", '
        '"content": "<the fact in third person>", "tag": "<one word category>"}'
    )
    convo = [{"role": "user", "content": f"User said: {user_message}\n\nAssistant replied: {assistant_message}"}]
    try:
        raw = await llm.complete(system, convo, settings)
        decision = extract_json(raw)
    except Exception as e:
        logger.info(f"Memory judge skipped: {e}")
        return None

    if not decision.get("save"):
        return None

    title = (decision.get("title") or "Remembered note").strip()[:120]
    content = (decision.get("content") or user_message).strip()
    tag = (decision.get("tag") or "general").strip()

    note = await crud.create_item(db, schemas.ItemCreate(
        type="note", title=title, content=content, status="todo",
        metadata_json={"source": "chat_memory", "tag": tag, "auto_saved": True}
    ))
    logger.info(f"Auto-saved memory note #{note.id}: {title}")
    return {"id": note.id, "title": title, "tag": tag}
