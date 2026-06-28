from __future__ import annotations

from typing import Optional
from app.modules.connectors.domain.connector import ConnectorEntity, AuthProvider
from app.modules.connectors.domain.connector_trigger import ConnectorTriggerEntity
from app.modules.schedule.domain.ports.schedule_manager import ExternalScheduleManager
from app.modules.schedule.infrastructure.schedule_managers.composio import (
    ComposioScheduleManager,
)
from app.core.log.log import get_logger

logger = get_logger(__name__)


class ManagersFactory:
    """Factory for creating external schedule managers."""

    @staticmethod
    def get_manager(
        app_trigger: ConnectorTriggerEntity,
        auth_provider: str,
        connector: ConnectorEntity | None = None,
    ) -> Optional[ExternalScheduleManager]:
        """
        Get the appropriate external schedule manager for the app event and auth provider.

        Args:
           app_trigger: The connector event entity.
           auth_provider: The auth provider string (e.g. 'LEMMA', 'COMPOSIO').
           connector: Optional connector entity for config-based routing hints.

        Returns:
            An instance of ExternalScheduleManager or None if no manager is needed.
        """

        # Triggers are composio-only. (Native/external providers such as the
        # former Jira manager and the unauthenticated /webhooks/schedules/{id}
        # callback were removed; future trigger support will live in the
        # connector module keyed off a connector account.)
        if connector is not None and connector.composio_toolkit_slug:
            return ComposioScheduleManager()

        if auth_provider == AuthProvider.COMPOSIO.value:
            return ComposioScheduleManager()

        logger.info(f"No manager for auth provider {auth_provider}")
        return None
