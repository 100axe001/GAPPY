from __future__ import annotations

from uuid import UUID
from datetime import datetime, timezone
from pydantic import BaseModel, Field


class DomainEvent(BaseModel):
    event_type: str
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @classmethod
    def get_event_type(cls) -> str:
        """Return the default event_type value for this event class.

        Pydantic v2 does not expose fields with defaults as class attributes,
        so ``MyEvent.event_type`` raises ``AttributeError``.  Use this
        classmethod instead when comparing against an incoming event dict.
        """
        return cls.model_fields["event_type"].default

    @classmethod
    def stream_name(cls) -> str:
        """Return the stream name for publishing this event.

        Override in subclasses to specify the stream.
        """
        raise NotImplementedError("Subclasses must define stream_name()")


class RawWebhookReceivedEvent(DomainEvent):
    event_type: str = "webhook.received"
    source: str
    payload: dict
    headers: dict | None = None
    surface_id: UUID | None = None

    @classmethod
    def stream_name(cls) -> str:
        return "webhook_events"
