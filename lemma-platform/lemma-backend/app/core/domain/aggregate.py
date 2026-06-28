"""Aggregate Root base class for DDD."""

from typing import TYPE_CHECKING

from pydantic import PrivateAttr

from app.core.domain.entity import Entity

if TYPE_CHECKING:
    from app.core.domain.events import DomainEvent


class AggregateRoot(Entity):
    """Base class for aggregate roots that collect domain events.

    Aggregates are the consistency boundary for domain operations.
    Events are collected during domain operations and published on commit.
    """

    _domain_events: list["DomainEvent"] = PrivateAttr(default_factory=list)

    def add_event(self, event: "DomainEvent") -> None:
        """Register a domain event to be published on commit."""
        self._domain_events.append(event)

    def collect_events(self) -> list["DomainEvent"]:
        """Collect and clear pending domain events.

        Called by repository on save to gather events for publishing.
        """
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events

    def has_pending_events(self) -> bool:
        """Check if there are pending events."""
        return len(self._domain_events) > 0
