from __future__ import annotations

from faststream import Depends, Logger
from faststream.redis import RedisRouter

from app.core.infrastructure.events.stream_subscriber import redis_stream_sub
from app.modules.identity.domain.events import (
    IdentityEvents,
    OrganizationInvitationAcceptedEvent,
    OrganizationInvitationCreatedEvent,
    UserSignedUpEvent,
)
from app.modules.identity.domain.organization_entities import OrganizationRole
from app.modules.identity.domain.ports import IdentityEmailPort
from app.modules.identity.infrastructure.adapters.email_adapter import (
    SmtpIdentityEmailAdapter,
)

router = RedisRouter()


def provide_identity_email_port() -> IdentityEmailPort:
    return SmtpIdentityEmailAdapter()


@router.subscriber(stream=redis_stream_sub(IdentityEvents.STREAM))
async def handle_identity_event(
    event: dict,
    fs_logger: Logger,
    email_port: IdentityEmailPort = Depends(provide_identity_email_port),
):
    """Dispatch identity events to email adapter."""
    event_type = event.get("event_type")

    if event_type == OrganizationInvitationCreatedEvent.get_event_type():
        parsed = OrganizationInvitationCreatedEvent.model_validate(event)
        await email_port.send_invitation_email(
            to_email=parsed.invited_email,
            organization_name=parsed.organization_name,
            inviter_email=parsed.invited_by_email,
            role=OrganizationRole(parsed.role),
            accept_url=parsed.accept_url,
            pod_name=parsed.pod_name,
            pod_description=parsed.pod_description,
        )
        fs_logger.info(
            f"Processed invitation email event for invitation {parsed.invitation_id}"
        )
        return

    if event_type == UserSignedUpEvent.get_event_type():
        parsed = UserSignedUpEvent.model_validate(event)
        await email_port.send_signup_welcome_email(
            to_email=parsed.email,
            first_name=parsed.first_name,
        )
        fs_logger.info(f"Processed welcome email event for user {parsed.user_id}")
        return

    if event_type == OrganizationInvitationAcceptedEvent.get_event_type():
        parsed = OrganizationInvitationAcceptedEvent.model_validate(event)
        await email_port.send_invitation_accepted_email(
            to_email=parsed.accepted_email,
            organization_name=parsed.organization_name,
            role=OrganizationRole(parsed.role),
        )
        fs_logger.info(
            f"Processed invitation accepted email event for invitation {parsed.invitation_id}"
        )
