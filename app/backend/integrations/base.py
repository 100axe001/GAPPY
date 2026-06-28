from typing import List, Dict, Any, Optional

class ToolDefinition:
    def __init__(
        self,
        name: str,
        description: str,
        input_schema: Dict[str, Any],
        output_schema: Dict[str, Any],
        required_permissions: List[str]
    ):
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.output_schema = output_schema
        self.required_permissions = required_permissions

class BaseIntegrationAdapter:
    name: str = ""
    display_name: str = ""
    description: str = ""
    scopes: List[str] = []

    def get_auth_url(self, redirect_uri: str, state: str) -> str:
        """Returns the OAuth login URL to redirect the user to."""
        raise NotImplementedError

    async def exchange_code(self, redirect_uri: str, code: str) -> dict:
        """Exchanges authorization code for access/refresh tokens."""
        raise NotImplementedError

    async def refresh_token(self, refresh_token: str) -> dict:
        """Refreshes the OAuth access token using refresh_token."""
        raise NotImplementedError

    async def test_connection(self, credentials: dict) -> bool:
        """Validates that the integration can talk to the third-party API."""
        raise NotImplementedError

    def get_tools(self) -> List[ToolDefinition]:
        """Lists the tools/actions this integration exposes to the AI router."""
        raise NotImplementedError

    async def execute_tool(self, action: str, credentials: dict, arguments: dict) -> Any:
        """Executes a specific action via external API with credentials."""
        raise NotImplementedError
