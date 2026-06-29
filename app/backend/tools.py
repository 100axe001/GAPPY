"""
Unified tool catalog for the chat agent.

Every integration / capability is exposed as a Tool, but tools are NOT all
active on every turn. A regex layer inspects the user's message and only the
tools whose intent patterns match are offered to the LLM for that turn. This
keeps the model focused and means an integration is only "called" when the
user's wording actually implies it.
"""
import re
import json
import logging
import datetime
from typing import Dict, Any, List, Callable, Awaitable, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, schemas
from .integrations.registry import registry
from .integrations.web_search import web_search, WebSearchError
from .integrations import email_adapter

logger = logging.getLogger("lifeos.tools")


class Tool:
    def __init__(self, name: str, description: str, parameters: Dict[str, str],
                 patterns: List[str], executor: Callable[..., Awaitable[Dict[str, Any]]],
                 requires: Optional[str] = None):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.patterns = [re.compile(p, re.IGNORECASE) for p in patterns]
        self.executor = executor
        self.requires = requires  # a settings key that must be set for this tool to be usable

    def matches(self, text: str) -> bool:
        return any(p.search(text) for p in self.patterns)


# ---------------------------------------------------------------------------
# Executors
# ---------------------------------------------------------------------------

async def _exec_web_search(db, user_id, settings, args) -> Dict[str, Any]:
    query = args.get("query") or ""
    if not query:
        return {"error": "Missing 'query' for web search."}
    try:
        res = await web_search(query, settings, max_results=args.get("max_results", 6))
        return res
    except WebSearchError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Web search failed: {e}"}


async def _exec_calendar(action: str, db, user_id, settings, args) -> Dict[str, Any]:
    adapter = registry.get_adapter("google_calendar")
    try:
        result = await adapter.execute_tool(action, {}, args)
        return {"result": result}
    except Exception as e:
        return {"error": f"Google Calendar isn't available ({e}). Connect it under Integrations."}


async def _exec_email_search(db, user_id, settings, args) -> Dict[str, Any]:
    try:
        msgs = await email_adapter.search_emails(settings, args.get("query", ""), args.get("max_results", 8))
        return {"emails": msgs}
    except email_adapter.EmailNotConfigured as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Could not read mailbox: {e}"}


async def _exec_email_send(db, user_id, settings, args) -> Dict[str, Any]:
    to = args.get("to")
    subject = args.get("subject", "")
    body = args.get("body", "")
    if not to:
        return {"error": "Missing recipient 'to' for email."}
    try:
        await email_adapter.send_email(settings, to, subject, body)
        return {"sent": True, "to": to, "subject": subject}
    except email_adapter.EmailNotConfigured as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Failed to send email: {e}"}


async def _exec_memory_search(db, user_id, settings, args) -> Dict[str, Any]:
    query = (args.get("query") or "").lower()
    items = await crud.get_items(db, limit=500)
    hits = []
    for it in items:
        if it.type not in ("note", "task", "deadline"):
            continue
        hay = f"{it.title} {it.content or ''}".lower()
        if not query or any(tok in hay for tok in query.split()):
            hits.append({"id": it.id, "type": it.type, "title": it.title,
                         "content": (it.content or "")[:300]})
        if len(hits) >= 8:
            break
    return {"memories": hits}


async def _exec_create_task(db, user_id, settings, args) -> Dict[str, Any]:
    title = args.get("title")
    if not title:
        return {"error": "Missing 'title' for task."}
    due = None
    if args.get("due_date"):
        try:
            due = datetime.datetime.strptime(args["due_date"], "%Y-%m-%d")
        except ValueError:
            pass
    item = await crud.create_item(db, schemas.ItemCreate(
        type="task", title=title, content=args.get("content", ""),
        priority=args.get("priority", "medium"), status="todo", due_date=due,
        metadata_json={"source": "chat"}
    ))
    return {"created_task": {"id": item.id, "title": item.title}}


# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

CALENDAR_PATTERNS = [
    r"\b(calendar|meeting|meetings|event|events|appointment|schedule|reschedule|"
    r"availability|free\s+slot|am\s+i\s+free|book\b|agenda)\b",
]

TOOLS: List[Tool] = [
    Tool(
        name="web_search",
        description="Search the live web for up-to-date information, news, facts, or anything outside the user's own data.",
        parameters={"query": "string (required) — what to search for"},
        patterns=[r"\b(search|google|look\s*up|find\s+online|latest|news|current|today'?s|"
                  r"weather|price\s+of|stock|who\s+is|what\s+is|how\s+to|when\s+did|recent)\b"],
        executor=_exec_web_search,
    ),
    Tool(
        name="calendar_list_events",
        description="List upcoming events on the user's Google Calendar.",
        parameters={"time_min": "ISO datetime (optional)", "time_max": "ISO datetime (optional)",
                    "max_results": "int (optional)"},
        patterns=CALENDAR_PATTERNS,
        executor=lambda db, u, s, a: _exec_calendar("list_events", db, u, s, a),
    ),
    Tool(
        name="calendar_create_event",
        description="Create a new Google Calendar event.",
        parameters={"summary": "string (required)", "start_time": "ISO datetime (required)",
                    "end_time": "ISO datetime (required)", "description": "string (optional)"},
        patterns=CALENDAR_PATTERNS,
        executor=lambda db, u, s, a: _exec_calendar("create_event", db, u, s, a),
    ),
    Tool(
        name="calendar_find_free_slots",
        description="Check the user's free/busy availability over a time range.",
        parameters={"time_min": "ISO datetime (required)", "time_max": "ISO datetime (required)"},
        patterns=CALENDAR_PATTERNS,
        executor=lambda db, u, s, a: _exec_calendar("find_free_slots", db, u, s, a),
    ),
    Tool(
        name="email_search",
        description="Search / list recent emails in the user's inbox (IMAP).",
        parameters={"query": "string (optional) — text to match", "max_results": "int (optional)"},
        patterns=[r"\b(email|emails|inbox|mailbox|gmail|mail\b|unread|messages?\s+from)\b"],
        executor=_exec_email_search,
        requires="email_address",
    ),
    Tool(
        name="email_send",
        description="Send an email via SMTP.",
        parameters={"to": "string (required)", "subject": "string", "body": "string"},
        patterns=[r"\b(send\s+(an?\s+)?email|email\s+\w+@|reply\s+to|compose|draft\s+an?\s+email)\b"],
        executor=_exec_email_send,
        requires="email_address",
    ),
    Tool(
        name="memory_search",
        description="Search the user's Second Brain (saved notes, tasks, and remembered facts).",
        parameters={"query": "string (required) — what to recall"},
        patterns=[r"\b(remember|recall|did\s+i|what\s+did\s+i|my\s+notes?|second\s+brain|"
                  r"i\s+told\s+you|earlier|previously|my\s+tasks?|what'?s\s+on\s+my)\b"],
        executor=_exec_memory_search,
    ),
    Tool(
        name="create_task",
        description="Add a task / reminder to the user's Life Ops board.",
        parameters={"title": "string (required)", "content": "string (optional)",
                    "priority": "high|medium|low (optional)", "due_date": "YYYY-MM-DD (optional)"},
        patterns=[r"\b(remind\s+me|add\s+(a\s+)?task|create\s+(a\s+)?task|todo|to-do|"
                  r"add\s+to\s+my\s+list|note\s+to\s+self|don'?t\s+let\s+me\s+forget)\b"],
        executor=_exec_create_task,
    ),
]

TOOLS_BY_NAME = {t.name: t for t in TOOLS}


def select_tools(message: str, settings: Dict[str, str]) -> List[Tool]:
    """Regex intent recognition: returns only the tools whose patterns match the message
    and whose required settings (if any) are configured."""
    selected = []
    for tool in TOOLS:
        if not tool.matches(message):
            continue
        if tool.requires and not (settings.get(tool.requires) or ""):
            continue
        selected.append(tool)
    return selected


async def execute_tool(name: str, db: AsyncSession, user_id: int,
                       settings: Dict[str, str], arguments: Dict[str, Any]) -> Dict[str, Any]:
    tool = TOOLS_BY_NAME.get(name)
    if not tool:
        return {"error": f"Unknown tool '{name}'."}
    try:
        return await tool.executor(db, user_id, settings, arguments or {})
    except Exception as e:
        logger.error(f"Tool '{name}' execution error: {e}", exc_info=True)
        return {"error": f"Tool '{name}' failed: {e}"}


def describe_tools(tools: List[Tool]) -> str:
    """Renders the available tools as text for the LLM system prompt."""
    if not tools:
        return "No tools are available for this request. Answer directly and conversationally."
    lines = []
    for t in tools:
        params = json.dumps(t.parameters)
        lines.append(f"- {t.name}: {t.description}\n    parameters: {params}")
    return "\n".join(lines)
