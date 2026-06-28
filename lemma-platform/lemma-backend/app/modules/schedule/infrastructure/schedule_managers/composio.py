from __future__ import annotations

from typing import Optional, Any
from composio import Composio

from app.modules.connectors.domain.account import AccountEntity
from app.modules.connectors.domain.connector_trigger import ConnectorTriggerEntity
from app.modules.schedule.domain.ports.schedule_manager import ExternalScheduleManager
from app.modules.schedule.domain.errors import ScheduleInfrastructureError
from app.modules.connectors.config import connector_settings
from app.core.log.log import get_logger

logger = get_logger(__name__)


class ComposioScheduleManager(ExternalScheduleManager):
    """Schedule subscription manager for Composio."""

    async def create_schedule(
        self,
        account: AccountEntity,
        app_trigger: ConnectorTriggerEntity,
        config: dict,
    ) -> str:
        """Create a schedule subscription on Composio."""
        if not account.credentials or not hasattr(account.credentials, "connection_id"):
            raise ValueError("Account not connected to Composio")

        connection_id = account.credentials.connection_id
        composio = Composio(api_key=connector_settings.composio_api_key)

        try:
            provider_event_slug = app_trigger.event_type
            response = composio.triggers.create(
                slug=provider_event_slug,
                connected_account_id=connection_id,
                trigger_config=config or {},
            )
            logger.info(f"Composio schedule subscription created: {response}")
            return response.trigger_id

        except Exception as e:
            logger.error(f"Failed to create Composio subscription: {str(e)}")
            raise RuntimeError(
                f"Failed to create Composio subscription: {str(e)}"
            ) from e

    async def delete_schedule(self, account: AccountEntity, provider_id: str) -> None:
        """Delete a schedule subscription from Composio."""
        logger.info(f"Deleting Composio subscription: {provider_id}")
        composio = Composio(api_key=connector_settings.composio_api_key)
        try:
            composio.triggers.delete(provider_id)
        except Exception as e:
            logger.error(f"Failed to delete Composio subscription: {str(e)}")
            raise ScheduleInfrastructureError(
                f"Failed to delete Composio subscription {provider_id}: {e}"
            ) from e

    async def get_schedule(
        self, account: AccountEntity, provider_id: str
    ) -> Optional[Any]:
        """Get schedule subscription details from Composio."""
        composio = Composio(api_key=connector_settings.composio_api_key)
        try:
            # Assuming get method exists
            return composio.triggers.get(provider_id)
        except Exception as e:
            logger.error(f"Failed to get Composio subscription: {str(e)}")
            return None
