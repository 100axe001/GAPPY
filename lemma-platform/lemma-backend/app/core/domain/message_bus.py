"""Message bus contracts for domain event publishing."""

from typing import Protocol
from pydantic import BaseModel


class MessageBus(Protocol):
    """Port for publishing integration/domain events."""

    async def publish(self, stream: str, event: BaseModel) -> None:
        """Publish an event payload to a stream/topic."""
        ...
