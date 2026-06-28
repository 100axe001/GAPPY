"""Schedule module dependencies."""

from typing import Annotated
from uuid import UUID
from fastapi import Depends, Request

from app.core.api.dependencies import UoWDep
from app.modules.connectors.infrastructure.repositories.connector_trigger_repository import (
    ConnectorTriggerRepository,
)
from app.modules.schedule.repositories.schedule_repository import ScheduleRepository
from app.modules.schedule.infrastructure.adapters.composio_webhook_verifier import (
    ComposioWebhookVerifier,
)
from app.modules.schedule.services.schedule_service import ScheduleService
from app.modules.schedule.services.webhook_schedule_matcher import WebhookScheduleMatcher
from app.modules.schedule.services.webhook_handler import WebhookHandler
from app.modules.schedule.domain.interfaces import WebhookVerifier


def get_schedule_service(uow: UoWDep) -> ScheduleService:
    """Provide schedule service."""
    return ScheduleService(uow=uow)

def get_webhook_handler(uow: UoWDep) -> WebhookHandler:
    """Provide webhook handler."""
    schedule_repository = ScheduleRepository(uow=uow)
    matcher = WebhookScheduleMatcher(
        schedule_repository=schedule_repository,
        connector_trigger_repository=ConnectorTriggerRepository(uow=uow),
    )
    return WebhookHandler(
        schedule_repository=schedule_repository,
        schedule_matcher=matcher,
    )


def get_composio_webhook_verifier() -> WebhookVerifier:
    """Provide Composio webhook verifier."""
    return ComposioWebhookVerifier()


def get_current_user_id(request: Request) -> UUID:
    """Get current user ID from request state."""
    # Assuming verify_auth middleware/dependency has run
    return request.state.user.id


ScheduleServiceDep = Annotated[ScheduleService, Depends(get_schedule_service)]
WebhookHandlerDep = Annotated[WebhookHandler, Depends(get_webhook_handler)]
ComposioWebhookVerifierDep = Annotated[
    WebhookVerifier, Depends(get_composio_webhook_verifier)
]
