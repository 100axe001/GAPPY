import re
import datetime
import logging
from typing import Dict, Any, Tuple
from ..ai import get_lemma_pod, run_agent_until_completed, extract_json

logger = logging.getLogger("lifeos.intent_parser")

# Fast Regex/Keyword patterns for fallback mapping
PATTERNS = {
    "list_events": [
        r"(what'?s\s+on\s+my\s+calendar|upcoming\s+meetings|show\s+my\s+calendar|list\s+events|show\s+meetings)",
        r"(calendar|meetings|events)\s+today",
        r"(upcoming\s+events|agenda)"
    ],
    "create_event": [
        r"(create\s+meeting|schedule|book\s+a|create\s+event|add\s+to\s+my\s+calendar|schedule\s+a)",
        r"(meeting|event|appointment)\s+(tomorrow|at|on|for)"
    ],
    "delete_event": [
        r"(delete.*meeting|cancel.*meeting|remove.*event|delete.*event|cancel.*event)"
    ],
    "update_event": [
        r"(move.*meeting|reschedule|change.*meeting|postpone)"
    ],
    "find_free_slots": [
        r"(when.*available|am\s+i\s+free|check.*availability|free\s+slots|free.*afternoon)"
    ]
}

def regex_classify_intent(query: str) -> str:
    """Uses regex and keyword matching to quickly classify intent."""
    query_lower = query.lower()
    for intent, regex_list in PATTERNS.items():
        for pattern in regex_list:
            if re.search(pattern, query_lower):
                return intent
    return "none"

async def detect_query_intent(query: str) -> Tuple[str, Dict[str, Any]]:
    """
    Detects user intent and extracts parameters using a layered approach:
    Layer 1: LLM Agent parsing (accurate, supports relative date resolution).
    Layer 2: Fast regex fallback if LLM times out or fails.
    """
    now = datetime.datetime.utcnow()
    current_time_str = now.isoformat()
    today_date_str = now.date().strftime("%Y-%m-%d")

    # Layer 1: LLM Agent Routing
    prompt = f"""You are the Natural Language Intent Parser for LifeOS.
Today is {today_date_str}. The current UTC time is {current_time_str}.

Analyze this instruction: "{query}"

You must categorize the query into one of these calendar intents:
1. "create_event": Schedule/create a meeting or event.
2. "list_events": Look up, show, or list upcoming events on the calendar.
3. "update_event": Reschedule, move, or modify an existing meeting/event.
4. "delete_event": Cancel, remove, or delete a meeting/event.
5. "find_free_slots": Check user availability, free spots, or ask "am I free".
6. "none": Not related to Google Calendar.

If intent is "create_event", "update_event", "delete_event", "list_events", or "find_free_slots", resolve all dates/times relative to the current date ({today_date_str}) and time ({current_time_str}) and convert them to ISO format (YYYY-MM-DDTHH:MM:SS). Assume a default duration of 30 minutes for new meetings if not specified.

Return your response ONLY as a JSON block with the following schema:
{{
  "intent": "create_event"|"list_events"|"update_event"|"delete_event"|"find_free_slots"|"none",
  "arguments": {{
    "summary": "<short meeting title>",
    "start_time": "YYYY-MM-DDTHH:MM:SS" (in ISO format),
    "end_time": "YYYY-MM-DDTHH:MM:SS" (in ISO format),
    "calendar_id": "primary",
    "description": "<optional description>",
    "event_id": "<event identifier if deleting/updating>",
    "time_min": "YYYY-MM-DDTHH:MM:SS" (for listing/free-busy searches),
    "time_max": "YYYY-MM-DDTHH:MM:SS" (for listing/free-busy searches),
    "max_results": 10
  }}
}}
"""
    try:
        pod = get_lemma_pod()
        resp_text = await run_agent_until_completed(pod, "hello", prompt)
        parsed = extract_json(resp_text)
        intent = parsed.get("intent", "none")
        arguments = parsed.get("arguments", {})
        logger.info(f"LLM routed query to '{intent}' with arguments: {arguments}")
        return intent, arguments
    except Exception as e:
        logger.warning(f"LLM intent detection failed ({e}). Falling back to regex.")
        
        # Layer 2: Regex/Keyword Fallback
        fallback_intent = regex_classify_intent(query)
        fallback_args = {}
        
        # Populate basic defaults for fallback
        if fallback_intent == "create_event":
            fallback_args = {
                "summary": query,
                "start_time": (now + datetime.timedelta(days=1)).replace(hour=9, minute=0, second=0).isoformat(),
                "end_time": (now + datetime.timedelta(days=1)).replace(hour=9, minute=30, second=0).isoformat()
            }
        elif fallback_intent in ("list_events", "find_free_slots"):
            fallback_args = {
                "time_min": now.isoformat(),
                "time_max": (now + datetime.timedelta(days=7)).isoformat()
            }
            
        return fallback_intent, fallback_args
