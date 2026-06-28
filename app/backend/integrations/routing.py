import logging
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from .intent import detect_query_intent
from .service import get_user_integration, execute_integration_tool
from .. import crud, schemas

logger = logging.getLogger("lifeos.intent_router")

async def route_and_execute_query(db: AsyncSession, user_id: int, query: str) -> dict:
    """
    Orchestrates the AI assistant request:
    1. Detects query intent and arguments.
    2. Routes to appropriate integration (Google Calendar).
    3. Verifies connection health, raises helpful errors if unconnected.
    4. Executes API actions and returns formatted user-friendly message response.
    5. Falls back to Commitment Inbox task parsing if query is non-integrations.
    """
    intent, arguments = await detect_query_intent(query)
    
    if intent == "none":
        # Fallback to Task Commitment Inbox Parsing
        try:
            logger.info("Non-integration query. Falling back to Commitment Inbox parser.")
            parsed_commit = await crud.create_item(db, schemas.ItemCreate(
                type="task",
                title=query,
                status="todo",
                priority="medium",
                metadata_json={"source_prompt": query}
            ))
            return {
                "intent": "create_task",
                "integration": "none",
                "execution_status": "success",
                "response_message": f"Added loop task: '{parsed_commit.title}' directly to your Todo board.",
                "suggested_actions": []
            }
        except Exception as e:
            return {
                "intent": "none",
                "integration": "none",
                "execution_status": "error",
                "response_message": f"Sorry, I couldn't process that query or create a task: {e}",
                "suggested_actions": []
            }

    # Integration intents routing (Google Calendar)
    integration_name = "google_calendar"
    
    # 1. Validate connection
    integration = await get_user_integration(db, user_id, integration_name)
    if not integration or not integration.is_connected:
        return {
            "intent": intent,
            "integration": integration_name,
            "execution_status": "need_connection",
            "response_message": (
                f"Google Calendar isn't connected.\n\n"
                f"To continue:\n\n"
                f"UI:\n"
                f"Sidebar → Integrations → Google Calendar → Connect\n\n"
                f"CLI:\n"
                f"python app-cli.py integrations connect google-calendar\n\n"
                f"After connecting, try the command again."
            ),
            "suggested_actions": []
        }
        
    if integration.health_status == "broken":
        return {
            "intent": intent,
            "integration": integration_name,
            "execution_status": "need_connection",
            "response_message": (
                f"Your Google Calendar connection appears broken (auth expired).\n\n"
                f"Please reconnect to restore access:\n\n"
                f"CLI:\n"
                f"python app-cli.py integrations connect google-calendar"
            ),
            "suggested_actions": []
        }

    # 2. Execute Action
    try:
        result = await execute_integration_tool(db, user_id, integration_name, intent, arguments)
        
        # 3. Format Response
        response_msg = ""
        suggested = []
        
        if intent == "create_event":
            summary = result.get("summary", arguments.get("summary", "Meeting"))
            start_raw = result.get("start", {}).get("dateTime", arguments.get("start_time"))
            end_raw = result.get("end", {}).get("dateTime", arguments.get("end_time"))
            
            # Format readable dates
            try:
                start_dt = datetime.datetime.fromisoformat(start_raw.replace("Z", "+00:00"))
                start_str = start_dt.strftime("%A, %b %d at %I:%M %p")
            except Exception:
                start_str = start_raw
                
            response_msg = f"I've successfully scheduled '{summary}' for {start_str}."
            
        elif intent == "list_events":
            if not result:
                response_msg = "You have no upcoming events scheduled."
            else:
                response_msg = "Here are your upcoming calendar events:\n\n"
                for item in result:
                    summary = item.get("summary", "Untitled Event")
                    start_raw = item.get("start", {}).get("dateTime") or item.get("start", {}).get("date", "")
                    try:
                        start_dt = datetime.datetime.fromisoformat(start_raw.replace("Z", "+00:00"))
                        start_str = start_dt.strftime("%b %d, %I:%M %p")
                    except Exception:
                        start_str = start_raw
                    response_msg += f"- **{summary}** ({start_str})\n"
                    
        elif intent == "delete_event":
            response_msg = "I've successfully deleted the event from your calendar."
            
        elif intent == "update_event":
            summary = result.get("summary", "Event")
            response_msg = f"I've updated the event details for '{summary}' on your calendar."
            
        elif intent == "find_free_slots":
            if not result:
                response_msg = "You are fully available during the queried time range."
            else:
                response_msg = "Here are your busy slots for the requested range:\n\n"
                for slot in result:
                    start_raw = slot.get("start")
                    end_raw = slot.get("end")
                    try:
                        start_dt = datetime.datetime.fromisoformat(start_raw.replace("Z", "+00:00"))
                        end_dt = datetime.datetime.fromisoformat(end_raw.replace("Z", "+00:00"))
                        slot_str = f"{start_dt.strftime('%b %d, %I:%M %p')} to {end_dt.strftime('%I:%M %p')}"
                    except Exception:
                        slot_str = f"{start_raw} to {end_raw}"
                    response_msg += f"- Busy: {slot_str}\n"

        return {
            "intent": intent,
            "integration": integration_name,
            "execution_status": "success",
            "response_message": response_msg,
            "suggested_actions": suggested
        }
        
    except Exception as e:
        logger.error(f"Error executing calendar tool {intent}: {e}", exc_info=True)
        return {
            "intent": intent,
            "integration": integration_name,
            "execution_status": "error",
            "response_message": f"Google Calendar API reported an error: {e}",
            "suggested_actions": []
        }
