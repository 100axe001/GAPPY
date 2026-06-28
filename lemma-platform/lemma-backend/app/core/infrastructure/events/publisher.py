from pydantic import BaseModel
from app.core.infrastructure.events.message_bus import get_message_bus
import logging

logger = logging.getLogger(__name__)


class EventPublisher:
    """Backward-compatible wrapper around shared message bus."""

    @classmethod
    async def publish(cls, stream: str, event: BaseModel):
        try:
            message_bus = get_message_bus()
            await message_bus.publish(stream, event)
            logger.info(f"Published event {event.__class__.__name__} to {stream}")
        except Exception as e:
            logger.error(f"Failed to publish event: {e}")
            raise e
