"""Adapter for external schedule provider lifecycle operations."""

from __future__ import annotations

from app.core.crypto import get_secret_cipher
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.connectors.domain.connector import AuthProvider
from app.modules.connectors.infrastructure.adapters.auth_provider_registry import (
    AuthProviderRegistry,
)
from app.modules.connectors.infrastructure.adapters.env_system_oauth_config import (
    EnvSystemOAuthConfigAdapter,
)
from app.modules.connectors.infrastructure.adapters.organization_access_adapter import (
    SqlAlchemyOrganizationAccessAdapter,
)
from app.modules.connectors.infrastructure.adapters.oauth_redirect_uri_builder import (
    OAuthRedirectUriBuilder,
)
from app.modules.connectors.infrastructure.repositories.account_repository import (
    AccountRepository,
)
from app.modules.connectors.infrastructure.repositories.connector_repository import (
    ConnectorRepository,
)
from app.modules.connectors.infrastructure.repositories.auth_config_repository import (
    AuthConfigRepository,
)
from app.modules.connectors.infrastructure.repositories.connector_trigger_repository import (
    ConnectorTriggerRepository,
)
from app.modules.connectors.infrastructure.repositories.connect_request_repository import (
    ConnectRequestRepository,
)
from app.modules.connectors.services.auth.composio_auth_provider import (
    ComposioAuthProvider,
)
from app.modules.connectors.services.auth.lemma_auth_provider import LemmaAuthProvider
from app.modules.connectors.services.connector_service import ConnectorService
from app.modules.schedule.domain.errors import (
    ScheduleInfrastructureError,
    ScheduleValidationError,
)
from app.modules.schedule.domain.interfaces import ExternalScheduleWriter
from app.modules.schedule.domain.schedule import ScheduleEntity, ScheduleType
from app.modules.schedule.infrastructure.schedule_managers.manager_factory import (
    ManagersFactory,
)
from app.core.log.log import get_logger

logger = get_logger(__name__)


class ExternalScheduleWriterAdapter(ExternalScheduleWriter):
    """Provision/deprovision external webhook triggers via provider managers."""

    def __init__(
        self,
        uow: SqlAlchemyUnitOfWork,
        connector_service: ConnectorService | None = None,
        connector_trigger_repository: ConnectorTriggerRepository | None = None,
    ):
        self.uow = uow
        self._connector_service = connector_service
        self._connector_trigger_repository = connector_trigger_repository

    def _build_connector_service(self) -> ConnectorService:
        connector_repository = ConnectorRepository(self.uow)
        encryption = get_secret_cipher()
        return ConnectorService(
            uow=self.uow,
            connector_repository=connector_repository,
            auth_config_repository=AuthConfigRepository(self.uow, encryption=encryption),
            account_repository=AccountRepository(self.uow, encryption=encryption),
            connect_request_repository=ConnectRequestRepository(self.uow),
            auth_provider_registry=AuthProviderRegistry(
                {
                    AuthProvider.LEMMA.value: LemmaAuthProvider(),
                    AuthProvider.COMPOSIO.value: ComposioAuthProvider(
                        connector_repository=connector_repository
                    ),
                }
            ),
            redirect_uri_builder=OAuthRedirectUriBuilder(),
            organization_access=SqlAlchemyOrganizationAccessAdapter(self.uow),
            system_oauth_config=EnvSystemOAuthConfigAdapter(),
        )

    @property
    def connector_service(self) -> ConnectorService:
        if self._connector_service is None:
            self._connector_service = self._build_connector_service()
        return self._connector_service

    @property
    def connector_trigger_repository(self) -> ConnectorTriggerRepository:
        if self._connector_trigger_repository is None:
            self._connector_trigger_repository = ConnectorTriggerRepository(self.uow)
        return self._connector_trigger_repository

    async def create_provider_trigger(self, schedule: ScheduleEntity) -> str | None:
        if schedule.schedule_type != ScheduleType.WEBHOOK:
            return None
        if not schedule.connector_trigger_id or not schedule.account_id:
            return None

        app_trigger = await self.connector_trigger_repository.get(
            schedule.connector_trigger_id
        )
        if not app_trigger:
            raise ScheduleValidationError(
                f"Connector trigger not found: {schedule.connector_trigger_id}"
            )

        account = await self.connector_service.get_account(
            schedule.account_id,
            schedule.user_id,
        )
        if account.connector_id != app_trigger.connector_id:
            raise ScheduleValidationError("Account does not match trigger connector")

        auth_config = await self.connector_service.auth_config_repository.get(
            account.auth_config_id
        )
        if auth_config is None:
            raise ScheduleValidationError("Account auth config not found")
        connector = await self.connector_service.get_connector(account.connector_id)
        effective_connector = self.connector_service._build_effective_connector(
            connector, auth_config
        )
        auth_provider = (
            auth_config.provider.value
            if hasattr(auth_config.provider, "value")
            else str(auth_config.provider)
        )
        manager = ManagersFactory.get_manager(
            app_trigger,
            auth_provider,
            connector=effective_connector,
        )
        if manager is None:
            logger.info(
                "No manager found for %s; skipping provider trigger creation",
                auth_provider,
            )
            return None

        try:
            return await manager.create_schedule(
                account=account,
                app_trigger=app_trigger,
                config=schedule.config,
            )
        except Exception as exc:
            raise ScheduleValidationError(
                f"Failed to create external trigger: {exc}"
            ) from exc

    async def delete_provider_trigger(self, schedule: ScheduleEntity) -> None:
        if schedule.schedule_type != ScheduleType.WEBHOOK:
            return
        provider_id = schedule.config.get("provider_trigger_id")
        if (
            not provider_id
            or not schedule.connector_trigger_id
            or not schedule.account_id
        ):
            return

        try:
            account = await self.connector_service.get_account(
                schedule.account_id, schedule.user_id
            )
            app_trigger = await self.connector_trigger_repository.get(
                schedule.connector_trigger_id
            )
            if not app_trigger:
                return
            connector = await self.connector_service.get_connector(
                account.connector_id
            )
            auth_config = await self.connector_service.auth_config_repository.get(
                account.auth_config_id
            )
            if auth_config is None:
                return
            effective_connector = self.connector_service._build_effective_connector(
                connector, auth_config
            )
            auth_provider = (
                auth_config.provider.value
                if hasattr(auth_config.provider, "value")
                else str(auth_config.provider)
            )
            manager = ManagersFactory.get_manager(
                app_trigger,
                auth_provider,
                connector=effective_connector,
            )
            if manager is not None:
                await manager.delete_schedule(account, str(provider_id))
        except ScheduleInfrastructureError:
            raise
        except Exception as exc:
            logger.exception(
                "Failed to delete provider trigger for schedule %s", schedule.id
            )
            raise ScheduleInfrastructureError(
                f"Failed to delete provider trigger for schedule {schedule.id}: {exc}"
            ) from exc
