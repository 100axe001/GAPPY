from __future__ import annotations

from types import SimpleNamespace
from uuid import UUID

import anyio
import pytest
from pydantic_ai.messages import PartEndEvent, PartStartEvent, TextPart

from app.modules.agent.domain.value_objects import AgentEventType
from app.modules.agent.infrastructure.harnesses.pydantic_ai import PydanticAIHarness
from app.modules.agent.tools.tool_errors import AgentInputRequired


class _ScopedRequestStream:
    def __init__(self) -> None:
        self._events = iter(
            [
                PartStartEvent(index=0, part=TextPart("hello world")),
                PartEndEvent(index=0, part=TextPart("hello world")),
            ]
        )
        self._scope = None

    async def __aenter__(self):
        self._scope = anyio.move_on_after(10)
        self._scope.__enter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        assert self._scope is not None
        return self._scope.__exit__(exc_type, exc, tb)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self._events)
        except StopIteration:
            raise StopAsyncIteration


class _Node:
    def stream(self, ctx):
        return _ScopedRequestStream()


class _Run:
    ctx = object()


@pytest.mark.asyncio
async def test_stream_stop_unwinds_anyio_cancel_scope_in_generator_task() -> None:
    harness = PydanticAIHarness()
    should_stop = False
    events = []

    async def stop_requested() -> bool:
        return should_stop

    with anyio.move_on_after(10, shield=True):
        async for event in harness._stream_model_request(
            _Node(),
            _Run(),
            agent_run_id=UUID("00000000-0000-0000-0000-000000000001"),
            malformed_tool_call_ids=set(),
            should_stop=stop_requested,
        ):
            events.append(event)
            should_stop = True

    assert [event.type for event in events] == [
        AgentEventType.TOKEN,
        AgentEventType.STOPPED,
    ]


@pytest.mark.asyncio
async def test_run_emits_waiting_event_when_tool_requests_input(monkeypatch) -> None:
    """A tool raising AgentInputRequired ends the run with a single WAITING event."""
    harness = PydanticAIHarness()
    conversation_id = UUID("00000000-0000-0000-0000-0000000000aa")
    agent_run_id = UUID("00000000-0000-0000-0000-0000000000bb")

    async def fake_execute(**_kwargs):
        if False:  # pragma: no cover - makes this an async generator
            yield
        raise AgentInputRequired("tool-call-1", "ask_user")

    monkeypatch.setattr(harness, "_execute", fake_execute)

    events = [
        event
        async for event in harness.run(
            agent=SimpleNamespace(),
            conversation=SimpleNamespace(id=conversation_id),
            messages=[],
            ctx=SimpleNamespace(),
            options=SimpleNamespace(should_stop=None),
            agent_run_id=agent_run_id,
        )
    ]

    assert len(events) == 1
    assert events[0].type == AgentEventType.WAITING
    assert events[0].data["tool_call_id"] == "tool-call-1"
    assert events[0].data["kind"] == "ask_user"
    assert events[0].data["conversation_id"] == str(conversation_id)
