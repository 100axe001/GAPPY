"""Domain events for agent orchestration and streaming."""

from __future__ import annotations

from typing import ClassVar
from uuid import UUID

from app.core.domain.events import DomainEvent
from app.modules.agent.domain.value_objects import AgentRunStatus, JsonObject

AGENT_EVENTS_STREAM = "agent_events"


class AgentDomainEvent(DomainEvent):
    _stream_name: ClassVar[str] = AGENT_EVENTS_STREAM

    @classmethod
    def stream_name(cls) -> str:
        return cls._stream_name


class AgentRunStartedEvent(AgentDomainEvent):
    event_type: str = "agent.run.started"
    conversation_id: UUID
    agent_run_id: UUID
    user_id: UUID
    pod_id: UUID
    agent_name: str | None = None


class AgentRunStopRequestedEvent(AgentDomainEvent):
    event_type: str = "agent.run.stop_requested"
    conversation_id: UUID
    agent_run_id: UUID
    user_id: UUID


class AgentRunCompletedEvent(AgentDomainEvent):
    event_type: str = "agent.run.completed"
    conversation_id: UUID
    agent_run_id: UUID
    status: AgentRunStatus
    data: JsonObject | None = None
