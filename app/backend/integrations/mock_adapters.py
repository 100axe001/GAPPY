import logging
from typing import List, Any
from .base import BaseIntegrationAdapter, ToolDefinition

logger = logging.getLogger("lifeos.mock_adapters")

class BaseMockAdapter(BaseIntegrationAdapter):
    def get_auth_url(self, redirect_uri: str, state: str) -> str:
        # We redirect to our own callback with a mock code to simulate connection completion
        import urllib.parse
        params = {
            "code": f"mock_code_{self.name}",
            "state": state
        }
        return f"{redirect_uri}?" + urllib.parse.urlencode(params)

    async def exchange_code(self, redirect_uri: str, code: str) -> dict:
        return {
            "access_token": f"mock_access_{self.name}",
            "refresh_token": f"mock_refresh_{self.name}",
            "email": f"demo-{self.name}@lifeos.ai"
        }

    async def test_connection(self, credentials: dict) -> bool:
        return True

    async def refresh_token(self, refresh_token: str) -> dict:
        return {
            "access_token": f"mock_refreshed_{self.name}"
        }

    def get_tools(self) -> List[ToolDefinition]:
        return []

    async def execute_tool(self, action: str, credentials: dict, arguments: dict) -> Any:
        return {}

class GoogleTasksAdapter(BaseMockAdapter):
    name = "google_tasks"
    display_name = "Google Tasks"
    description = "Sync task lists and organize subtasks directly from your Life Ops board."
    scopes = ["tasks:read", "tasks:write"]

class GmailAdapter(BaseMockAdapter):
    name = "gmail"
    display_name = "Gmail"
    description = "Read email notifications and convert them to task loops or Second Brain drafts."
    scopes = ["gmail:read", "gmail:modify"]

class NotionAdapter(BaseMockAdapter):
    name = "notion"
    display_name = "Notion"
    description = "Sync notes, databases, and structured pages into your Second Brain."
    scopes = ["notion:pages", "notion:databases"]

class SlackAdapter(BaseMockAdapter):
    name = "slack"
    display_name = "Slack"
    description = "Monitor channels, capture notifications, and talk to your team."
    scopes = ["slack:channels", "slack:chat:write"]

class GitHubAdapter(BaseMockAdapter):
    name = "github"
    display_name = "GitHub"
    description = "Track issues, pull requests, and code modifications."
    scopes = ["repo:status", "repo:read"]

class JiraAdapter(BaseMockAdapter):
    name = "jira"
    display_name = "Jira"
    description = "Manage Jira tickets, backlog items, and project sprints."
    scopes = ["jira:read", "jira:write"]

class LinearAdapter(BaseMockAdapter):
    name = "linear"
    display_name = "Linear"
    description = "Keep your software issues, cycles, and roadmaps in sync."
    scopes = ["linear:read", "linear:write"]

class TrelloAdapter(BaseMockAdapter):
    name = "trello"
    display_name = "Trello"
    description = "Map boards, lists, and cards into your Life Board."
    scopes = ["trello:read", "trello:write"]
