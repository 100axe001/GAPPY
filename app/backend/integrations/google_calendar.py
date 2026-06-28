import os
import logging
from typing import List, Dict, Any
from .base import BaseIntegrationAdapter, ToolDefinition
from ..sdk_client import get_lemma_pod

logger = logging.getLogger("lifeos.google_calendar")

class GoogleCalendarAdapter(BaseIntegrationAdapter):
    name = "google_calendar"
    display_name = "Google Calendar"
    description = "Sync, schedule, and manage events on your Google Calendar."
    scopes = [
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/calendar.events",
        "https://www.googleapis.com/auth/userinfo.email"
    ]

    def get_auth_url(self, redirect_uri: str, state: str) -> str:
        # Use Lemma Connectors to get the connection request URL
        try:
            pod = get_lemma_pod()
            
            client_id = os.getenv("GOOGLE_CLIENT_ID", "")
            client_secret = os.getenv("GOOGLE_CLIENT_SECRET", "")
            
            if not client_id or "your-google-client-id-here" in client_id:
                raise ValueError(
                    "Google Client Credentials are not configured. Please open the `.env` file at the root of "
                    "your workspace, configure GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET, and rebuild the container "
                    "using: docker compose build lifeos-app && docker compose up -d"
                )
            
            # Fetch existing auth config
            auth_configs = pod.connectors.auth_configs.list().items
            auth_config = next((c for c in auth_configs if c.connector_id == "google_calendar"), None)
            
            # Self-healing: recreate auth config if custom credentials are changed or set
            if auth_config:
                if client_id and "your-google-client-id-here" not in client_id:
                    try:
                        pod.connectors.auth_configs.delete(auth_config.name)
                        auth_config = None
                    except Exception as delete_err:
                        logger.warning(f"Could not delete existing auth config: {delete_err}")
            
            if not auth_config:
                from lemma_sdk.openapi_client.models.auth_config_create_schema import AuthConfigCreateSchema
                
                # If custom credentials exist, configure ORG_CUSTOM
                if client_id and "your-google-client-id-here" not in client_id:
                    from lemma_sdk.openapi_client.models.auth_config_create_schema_credential_config_type_0 import AuthConfigCreateSchemaCredentialConfigType0
                    cred_config = AuthConfigCreateSchemaCredentialConfigType0()
                    cred_config.additional_properties = {
                        "client_id": client_id,
                        "client_secret": client_secret
                    }
                    auth_config = pod.connectors.auth_configs.create(
                        AuthConfigCreateSchema(
                            connector_id="google_calendar",
                            name="google_calendar",
                            config_source="ORG_CUSTOM",
                            credential_config=cred_config,
                            provider="LEMMA"
                        )
                    )
                else:
                    auth_config = pod.connectors.auth_configs.create(
                        AuthConfigCreateSchema(
                            connector_id="google_calendar",
                            name="google_calendar",
                            config_source="SYSTEM_DEFAULT",
                            provider="LEMMA"
                        )
                    )
            
            # Initiate connect request
            req = pod.connectors.connect_request(app="google_calendar", auth_config_id=auth_config.id)
            auth_url = req.authorization_url
            print(f"Generated Lemma connect request URL for Google Calendar: {auth_url}", flush=True)
            return auth_url
        except Exception as e:
            logger.error(f"Failed to generate connect request via Lemma: {e}", exc_info=True)
            raise ValueError(f"Lemma connector failed: {e}")

    async def exchange_code(self, redirect_uri: str, code: str) -> dict:
        # No-op since Lemma handles OAuth exchange and token storage
        return {}

    async def refresh_token(self, refresh_token: str) -> dict:
        # No-op since Lemma handles token refresh
        return {}

    async def test_connection(self, credentials: dict) -> bool:
        try:
            pod = get_lemma_pod()
            # Perform a test execution on the connector to verify health
            pod.connectors.execute(
                "google_calendar",
                "calendar_list_list",
                {"max_results": 1}
            )
            return True
        except Exception as e:
            logger.warning(f"Google Calendar connection health test failed: {e}")
            return False

    def get_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="list_calendars",
                description="Lists all calendars in the connected Google account.",
                input_schema={},
                output_schema={"calendars": "array"},
                required_permissions=["calendar.read"]
            ),
            ToolDefinition(
                name="list_events",
                description="Lists upcoming events on a specific calendar. Optionally filter by time start/end.",
                input_schema={
                    "calendar_id": "string (optional, defaults to 'primary')",
                    "time_min": "ISO datetime string (optional, defaults to now)",
                    "time_max": "ISO datetime string (optional)",
                    "max_results": "integer (optional, default 10)"
                },
                output_schema={"events": "array"},
                required_permissions=["calendar.events.read"]
            ),
            ToolDefinition(
                name="create_event",
                description="Creates a new calendar event with summary, description, start time, and end time.",
                input_schema={
                    "summary": "string (required)",
                    "start_time": "ISO datetime string (required, e.g. YYYY-MM-DDTHH:MM:SS)",
                    "end_time": "ISO datetime string (required)",
                    "description": "string (optional)",
                    "calendar_id": "string (optional, defaults to 'primary')"
                },
                output_schema={"event": "object"},
                required_permissions=["calendar.events.write"]
            ),
            ToolDefinition(
                name="update_event",
                description="Updates an existing calendar event details.",
                input_schema={
                    "event_id": "string (required)",
                    "summary": "string (optional)",
                    "start_time": "ISO datetime string (optional)",
                    "end_time": "ISO datetime string (optional)",
                    "description": "string (optional)",
                    "calendar_id": "string (optional, defaults to 'primary')"
                },
                output_schema={"event": "object"},
                required_permissions=["calendar.events.write"]
            ),
            ToolDefinition(
                name="delete_event",
                description="Deletes a calendar event.",
                input_schema={
                    "event_id": "string (required)",
                    "calendar_id": "string (optional, defaults to 'primary')"
                },
                output_schema={"success": "boolean"},
                required_permissions=["calendar.events.write"]
            ),
            ToolDefinition(
                name="find_free_slots",
                description="Checks availability/free-busy status for the primary calendar.",
                input_schema={
                    "time_min": "ISO datetime string (required)",
                    "time_max": "ISO datetime string (required)"
                },
                output_schema={"busy_slots": "array"},
                required_permissions=["calendar.read"]
            )
        ]

    async def execute_tool(self, action: str, credentials: dict, arguments: dict) -> Any:
        pod = get_lemma_pod()
        
        if action == "list_calendars":
            res = pod.connectors.execute("google_calendar", "calendar_list_list", {})
            return res.to_dict().get("result", {}).get("items", [])

        elif action == "list_events":
            cal_id = arguments.get("calendar_id") or "primary"
            time_min = arguments.get("time_min")
            time_max = arguments.get("time_max")
            max_results = arguments.get("max_results") or 10
            
            payload = {
                "calendar_id": cal_id,
                "max_results": int(max_results),
                "single_events": True,
                "order_by": "startTime"
            }
            if time_min:
                payload["time_min"] = time_min
            if time_max:
                payload["time_max"] = time_max
                
            res = pod.connectors.execute("google_calendar", "events_list", payload)
            return res.to_dict().get("result", {}).get("items", [])

        elif action == "create_event":
            cal_id = arguments.get("calendar_id") or "primary"
            summary = arguments.get("summary")
            start_time = arguments.get("start_time")
            end_time = arguments.get("end_time")
            desc = arguments.get("description") or ""
            
            payload = {
                "calendar_id": cal_id,
                "body": {
                    "summary": summary,
                    "description": desc,
                    "start": {"dateTime": start_time},
                    "end": {"dateTime": end_time}
                }
            }
            res = pod.connectors.execute("google_calendar", "events_insert", payload)
            return res.to_dict().get("result", {})

        elif action == "update_event":
            cal_id = arguments.get("calendar_id") or "primary"
            event_id = arguments.get("event_id")
            
            body = {}
            if "summary" in arguments:
                body["summary"] = arguments["summary"]
            if "description" in arguments:
                body["description"] = arguments["description"]
            if "start_time" in arguments:
                body["start"] = {"dateTime": arguments["start_time"]}
            if "end_time" in arguments:
                body["end"] = {"dateTime": arguments["end_time"]}
                
            payload = {
                "calendar_id": cal_id,
                "event_id": event_id,
                "body": body
            }
            res = pod.connectors.execute("google_calendar", "events_patch", payload)
            return res.to_dict().get("result", {})

        elif action == "delete_event":
            cal_id = arguments.get("calendar_id") or "primary"
            event_id = arguments.get("event_id")
            payload = {
                "calendar_id": cal_id,
                "event_id": event_id
            }
            pod.connectors.execute("google_calendar", "events_delete", payload)
            return True

        elif action == "find_free_slots":
            time_min = arguments.get("time_min")
            time_max = arguments.get("time_max")
            payload = {
                "body": {
                    "timeMin": time_min,
                    "timeMax": time_max,
                    "items": [{"id": "primary"}]
                }
            }
            res = pod.connectors.execute("google_calendar", "freebusy_query", payload)
            return res.to_dict().get("result", {}).get("calendars", {}).get("primary", {}).get("busy", [])

        else:
            raise NotImplementedError(f"Action '{action}' is not supported by Google Calendar adapter.")
