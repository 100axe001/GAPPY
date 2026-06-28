from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domain.message_bus import MessageBus
from app.core.domain.uow import IUnitOfWork
from app.core.infrastructure.events.publisher import EventPublisher
from app.core.log.log import get_logger

if TYPE_CHECKING:
    from app.core.domain.events import DomainEvent

logger = get_logger(__name__)


class SqlAlchemyUnitOfWork(IUnitOfWork):
    """SQLAlchemy Unit of Work with event publishing.

    Collects domain events during operations and publishes them on commit.
    Repositories call `collect_events()` after saving aggregates.
    """

    def __init__(self, session: AsyncSession, message_bus: MessageBus | None = None):
        self.session = session
        self._message_bus = message_bus
        self._pending_events: list["DomainEvent"] = []

    def set_message_bus(self, message_bus: MessageBus) -> None:
        """Set/override message bus for event publishing."""
        self._message_bus = message_bus

    def collect_events(self, events: list["DomainEvent"]) -> None:
        """Collect domain events for publishing on commit.

        Called by repositories after saving aggregates.
        """
        self._pending_events.extend(events)

    async def __aenter__(self) -> "SqlAlchemyUnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()

    async def commit(self) -> None:
        """Commit transaction and publish all collected events."""
        await self.session.commit()
        await self._publish_all_events()

    async def _publish_all_events(self) -> None:
        """Publish all collected events."""
        for event in self._pending_events:
            try:
                stream = event.stream_name()
                if self._message_bus:
                    await self._message_bus.publish(stream, event)
                else:
                    await EventPublisher.publish(stream, event)
                logger.debug(f"Published {event.event_type} to {stream}")
            except Exception as e:
                logger.error(f"Failed to publish {event.event_type}: {e}")
        self._pending_events.clear()

    async def rollback(self) -> None:
        """Rollback transaction and discard pending events."""
        await self.session.rollback()
        self._pending_events.clear()

    def has_pending_events(self) -> bool:
        """Check if there are pending events."""
        return len(self._pending_events) > 0
