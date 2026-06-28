from typing import Dict, List
from .base import BaseIntegrationAdapter
from .google_calendar import GoogleCalendarAdapter
from .mock_adapters import (
    GoogleTasksAdapter,
    GmailAdapter,
    NotionAdapter,
    SlackAdapter,
    GitHubAdapter,
    JiraAdapter,
    LinearAdapter,
    TrelloAdapter
)

class IntegrationRegistry:
    def __init__(self):
        self._adapters: Dict[str, BaseIntegrationAdapter] = {}
        # Auto-register default adapters
        self.register(GoogleCalendarAdapter())
        self.register(GoogleTasksAdapter())
        self.register(GmailAdapter())
        self.register(NotionAdapter())
        self.register(SlackAdapter())
        self.register(GitHubAdapter())
        self.register(JiraAdapter())
        self.register(LinearAdapter())
        self.register(TrelloAdapter())

    def register(self, adapter: BaseIntegrationAdapter):
        """Registers a new integration adapter."""
        self._adapters[adapter.name] = adapter

    def get_adapter(self, name: str) -> BaseIntegrationAdapter:
        """Returns the integration adapter by name."""
        return self._adapters.get(name)

    def list_adapters(self) -> List[BaseIntegrationAdapter]:
        """Lists all registered integration adapters."""
        return list(self._adapters.values())

# Global registry instance
registry = IntegrationRegistry()
