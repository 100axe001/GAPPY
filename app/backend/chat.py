"""
Chat agent loop.

Flow for one user turn:
  1. Regex intent recognition selects the candidate tools for this message.
  2. Relevant Second Brain context is pulled in to ground the reply.
  3. The configured LLM runs a JSON tool-protocol loop: it either calls one of
     the offered tools or returns a final answer. Tool results are fed back.
  4. The final answer is persisted; the memory manager decides what to remember.
"""
import json
import logging
import datetime
from typing import Dict, Any, List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, llm, memory
from .ai import extract_json
from .tools import select_tools, execute_tool, describe_tools

logger = logging.getLogger("lifeos.chat")

MAX_STEPS = 4          # max tool round-trips before forcing a final answer
HISTORY_LIMIT = 12     # prior messages to include as context


def _build_system_prompt(tool_text: str, memory_ctx: str) -> str:
    today = datetime.date.today().strftime("%Y-%m-%d")
    now = datetime.datetime.utcnow().isoformat()
    return f"""You are LifeOS, a helpful personal assistant. Today is {today} (UTC now: {now}).

You can use tools to act on the user's behalf. AVAILABLE TOOLS FOR THIS MESSAGE:
{tool_text}

How to respond — reply with EXACTLY ONE JSON object and nothing else:
- To use a tool:
  {{"action": "tool", "tool": "<tool_name>", "arguments": {{ ... }}}}
- To answer the user (no tool needed, or after you have tool results):
  {{"action": "final", "message": "<your natural-language reply, markdown allowed>"}}

Rules:
- Only call a tool listed above. Resolve relative dates/times to ISO format using today's date.
- After receiving a tool result, either call another tool or return a final answer that uses the result.
- If no tool is needed, answer directly with an "action": "final" object.
- Keep answers concise and friendly.

RELEVANT NOTES FROM THE USER'S SECOND BRAIN (for grounding; may be empty):
{memory_ctx or '(none)'}"""


def _parse_action(raw: str) -> Dict[str, Any]:
    try:
        data = extract_json(raw)
        if isinstance(data, dict) and data.get("action") in ("tool", "final"):
            return data
    except Exception:
        pass
    # Fallback: treat the whole text as a final answer.
    return {"action": "final", "message": raw.strip()}


async def run_chat_turn(db: AsyncSession, user_id: int, conversation,
                        user_message: str, settings: Dict[str, str]) -> Tuple[str, List[Dict[str, Any]]]:
    """Returns (assistant_text, tool_invocations)."""
    tools = select_tools(user_message, settings)
    tool_text = describe_tools(tools)
    memory_ctx = await memory.build_memory_context(db, user_id, user_message)
    system = _build_system_prompt(tool_text, memory_ctx)

    # Assemble conversation transcript (prior turns + this message).
    prior = await crud.get_messages(db, conversation.id)
    messages: List[Dict[str, str]] = []
    for m in prior[-HISTORY_LIMIT:]:
        if m.role in ("user", "assistant") and m.content:
            messages.append({"role": m.role, "content": m.content})
    messages.append({"role": "user", "content": user_message})

    tool_invocations: List[Dict[str, Any]] = []
    final_text = ""

    for step in range(MAX_STEPS):
        raw = await llm.complete(system, messages, settings)
        action = _parse_action(raw)

        if action.get("action") == "tool" and tools:
            name = action.get("tool", "")
            arguments = action.get("arguments", {}) or {}
            result = await execute_tool(name, db, user_id, settings, arguments)
            tool_invocations.append({"tool": name, "arguments": arguments, "result": result})
            # Feed the model its own call and the result, then loop.
            messages.append({"role": "assistant", "content": json.dumps(action)})
            messages.append({"role": "user",
                             "content": f"TOOL_RESULT for {name}: {json.dumps(result)[:3000]}\n"
                                        f"Now respond with an \"action\":\"final\" answer for the user "
                                        f"(or another tool call if needed)."})
            continue

        final_text = action.get("message", "") or raw.strip()
        break

    if not final_text:
        final_text = "I wasn't able to complete that — please try rephrasing."

    return final_text, tool_invocations


async def send_message(db: AsyncSession, user_id: int, conversation, user_message: str,
                       settings: Dict[str, str]):
    """High-level entry: persist user msg, run the turn, persist assistant msg, auto-save memory."""
    user_row = await crud.add_message(db, conversation.id, "user", user_message)

    # Auto-title a brand-new conversation from its first message.
    if (conversation.title or "New Chat") == "New Chat":
        snippet = user_message.strip().splitlines()[0][:48]
        conversation.title = snippet or "New Chat"

    try:
        assistant_text, tool_invocations = await run_chat_turn(db, user_id, conversation, user_message, settings)
    except Exception as e:
        logger.error(f"Chat turn failed: {e}", exc_info=True)
        assistant_text, tool_invocations = (
            f"Sorry, something went wrong while processing that: {e}", [])

    tools_used = [t["tool"] for t in tool_invocations]
    assistant_row = await crud.add_message(
        db, conversation.id, "assistant", assistant_text,
        tool_calls=tool_invocations, metadata={"tools_used": tools_used}
    )
    await crud.touch_conversation(db, conversation)

    # Decide what (if anything) to remember from this exchange.
    saved = None
    try:
        saved = await memory.maybe_save_memory(db, user_id, user_message, assistant_text, settings)
    except Exception as e:
        logger.info(f"Memory save skipped: {e}")
    if saved:
        meta = dict(assistant_row.metadata_json or {})
        meta["saved_memory"] = saved
        assistant_row.metadata_json = meta
        await db.flush()

    return user_row, assistant_row, tools_used
