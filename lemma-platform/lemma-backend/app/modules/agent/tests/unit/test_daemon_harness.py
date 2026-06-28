from __future__ import annotations

import asyncio
from uuid import uuid4

import pytest
from pydantic_ai.tools import RunContext, Tool
from pydantic_ai.toolsets import FunctionToolset

from app.modules.agent.domain.context import AgentContext
from app.modules.agent.domain.entities import Agent, Conversation, Message
from app.modules.agent.domain.value_objects import (
    AgentEventType,
    HarnessKind,
    HarnessOptions,
    MessageKind,
    MessageRole,
)
from app.modules.agent.infrastructure.daemon_hub import agent_runtime_daemon_hub
from app.modules.agent.infrastructure.harnesses.daemon import (
    DEFAULT_DAEMON_EVENT_TIMEOUT_SECONDS,
    DaemonHarness,
    _mcp_payload,
    _run_start_payload,
)


class _FakeWorkspaceSandboxService:
    async def get_env_vars(self, **kwargs):
        del kwargs
        return {"LEMMA_TOKEN": "workspace-token"}

    async def close(self):
        return None


def test_daemon_harness_default_event_timeout_is_two_hours():
    harness = DaemonHarness(HarnessKind.CODEX)

    assert harness.event_timeout_seconds == DEFAULT_DAEMON_EVENT_TIMEOUT_SECONDS
    assert harness.event_timeout_seconds == 7200.0


class _FakeWebSocket:
    def __init__(self) -> None:
        self.sent: list[dict] = []

    async def send_json(self, payload: dict) -> None:
        self.sent.append(payload)


@pytest.mark.asyncio
async def test_daemon_harness_forwards_run_start_and_yields_events(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(
        "app.modules.agent.infrastructure.harnesses.daemon.WorkspaceSandboxService",
        _FakeWorkspaceSandboxService,
    )

    # The hub forwards run events to the harness via its local in-process queue;
    # _publish_run_event is only a secondary Redis broadcast for other
    # subscribers. Stub it so this stays a true unit test (no Redis needed).
    async def _noop_publish(*_args, **_kwargs):
        return None

    monkeypatch.setattr(
        agent_runtime_daemon_hub, "_publish_run_event", _noop_publish
    )

    async def daemon_tool(ctx: RunContext[AgentContext]) -> dict[str, str]:
        return {"agent_name": ctx.deps.agent_name or ""}

    daemon_id = uuid4()
    daemon_user_id = uuid4()
    actor_user_id = uuid4()
    pod_id = uuid4()
    agent_run_id = uuid4()
    websocket = _FakeWebSocket()
    await agent_runtime_daemon_hub.register(
        daemon_id=daemon_id,
        user_id=daemon_user_id,
        websocket=websocket,  # type: ignore[arg-type]
    )
    harness = DaemonHarness(HarnessKind.CODEX, event_timeout_seconds=1)
    agent = Agent(
        pod_id=pod_id,
        user_id=actor_user_id,
        name="Daemon Agent",
        instruction="Answer through the daemon.",
    )
    conversation = Conversation(
        user_id=actor_user_id,
        pod_id=pod_id,
        organization_id=uuid4(),
        title="Daemon run",
    )
    message = Message.create(
        conversation_id=conversation.id,
        sequence=0,
        agent_run_id=None,
        role=MessageRole.USER,
        text="hello",
    )
    ctx = AgentContext(
        user_id=actor_user_id,
        pod_id=pod_id,
        conversation_id=conversation.id,
        agent_run_id=agent_run_id,
    )
    options = HarnessOptions(
        model_name="gpt-5.5",
        toolsets=[
            FunctionToolset(
                tools=[Tool(daemon_tool, name="daemon_tool", takes_ctx=True)]
            )
        ],
        extra={
            "runtime_profile": {
                "user_id": str(daemon_user_id),
                "daemon_id": str(daemon_id),
                "scope": "ORGANIZATION",
                "config": {},
            }
        },
    )

    events = []

    async def collect_events() -> None:
        async for event in harness.run(
            agent=agent,
            conversation=conversation,
            messages=[message],
            ctx=ctx,
            options=options,
            agent_run_id=agent_run_id,
        ):
            events.append(event)

    task = asyncio.create_task(collect_events())
    for _ in range(20):
        if websocket.sent:
            break
        await asyncio.sleep(0.01)

    assert websocket.sent[0]["type"] == "run.start"
    assert websocket.sent[0]["agent_run_id"] == str(agent_run_id)
    start_payload = websocket.sent[0]["payload"]
    assert start_payload["agent_run_id"] == str(agent_run_id)
    assert start_payload["runtime"] == {
        "profile_id": None,
        "harness_kind": "CODEX",
        "model_name": "gpt-5.5",
    }
    assert start_payload["mcp"]["server_name"] == "lemma_tools"
    assert start_payload["mcp"]["run_id"] == str(agent_run_id)
    assert start_payload["mcp"]["conversation_id"] == str(conversation.id)
    assert start_payload["mcp"]["url"].endswith(
        f"/agent-runtime/conversations/{conversation.id}/mcp"
    )
    assert start_payload["mcp"]["workspace"] == {
        "id": "default",
        "cwd": f"/workspace/conversations/{conversation.id}",
    }
    assert start_payload["mcp"]["token"] == "workspace-token"
    assert start_payload["mcp"]["authorization"] == f"Bearer {start_payload['mcp']['token']}"
    assert start_payload["mcp"]["tool_names"] == ["lemma_daemon_tool"]
    assert "provider_configs" not in start_payload["mcp"]
    assert start_payload["prompt"]["structured"] is False
    assert "Answer through the daemon." in start_payload["prompt"]["system_prompt"]
    # The working directory + cwd are stated by build_agent_instructions' Working
    # Directory section (shared by both harnesses); the daemon adds only the
    # provider-scratch clarification.
    assert "# Working Directory" in start_payload["prompt"]["system_prompt"]
    assert (
        f"/workspace/conversations/{conversation.id}"
        in start_payload["prompt"]["system_prompt"]
    )
    assert (
        "provider process cwd is daemon scratch space"
        in start_payload["prompt"]["system_prompt"]
    )
    assert "USER:\nhello" == start_payload["prompt"]["user_prompt"]
    assert "session_id" not in start_payload["prompt"]
    assert "text" not in start_payload["prompt"]
    assert "messages" not in start_payload

    await agent_runtime_daemon_hub.handle_run_event(
        daemon_id=daemon_id,
        user_id=daemon_user_id,
        message={
            "type": "run.event",
            "agent_run_id": str(agent_run_id),
            "event": {
                "type": "message",
                "data": {
                    "role": "assistant",
                    "kind": "text",
                    "text": "hi from daemon",
                },
            },
        },
    )
    await agent_runtime_daemon_hub.handle_run_event(
        daemon_id=daemon_id,
        user_id=daemon_user_id,
        message={
            "type": "run.event",
            "agent_run_id": str(agent_run_id),
            "event": {"type": "completed", "data": {}},
        },
    )
    await task

    assert [event.type for event in events] == [
        AgentEventType.MESSAGE,
        AgentEventType.COMPLETED,
    ]
    assert events[0].data.kind == MessageKind.TEXT
    assert events[0].data.text == "hi from daemon"
    await agent_runtime_daemon_hub.unregister(
        daemon_id=daemon_id,
        user_id=daemon_user_id,
    )


@pytest.mark.asyncio
async def test_daemon_mcp_payload_points_to_conversation_fastmcp_server(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(
        "app.modules.agent.infrastructure.harnesses.daemon.WorkspaceSandboxService",
        _FakeWorkspaceSandboxService,
    )

    # The hub forwards run events to the harness via its local in-process queue;
    # _publish_run_event is only a secondary Redis broadcast for other
    # subscribers. Stub it so this stays a true unit test (no Redis needed).
    async def _noop_publish(*_args, **_kwargs):
        return None

    monkeypatch.setattr(
        agent_runtime_daemon_hub, "_publish_run_event", _noop_publish
    )

    async def daemon_tool(ctx: RunContext[AgentContext]) -> dict[str, str]:
        return {"agent_name": ctx.deps.agent_name or ""}

    conversation_id = uuid4()
    agent_run_id = uuid4()
    ctx = AgentContext(
        user_id=uuid4(),
        pod_id=uuid4(),
        conversation_id=conversation_id,
        agent_run_id=agent_run_id,
    )
    payload = await _mcp_payload(
        agent_run_id=agent_run_id,
        conversation_id=conversation_id,
        ctx=ctx,
        options=HarnessOptions(
            model_name="gpt-5.5",
            toolsets=[
                FunctionToolset(
                    tools=[Tool(daemon_tool, name="daemon_tool", takes_ctx=True)]
                )
            ],
        ),
        prompt="Use daemon_tool.",
    )

    assert payload["server_name"] == "lemma_tools"
    assert payload["run_id"] == str(agent_run_id)
    assert payload["conversation_id"] == str(conversation_id)
    assert payload["url"].endswith(f"/agent-runtime/conversations/{conversation_id}/mcp")
    assert payload["token"] == "workspace-token"
    assert payload["authorization"] == f"Bearer {payload['token']}"
    assert payload["tool_names"] == ["lemma_daemon_tool"]


def test_daemon_harness_attaches_cached_session_and_recovery_prompt():
    daemon_id = uuid4()
    daemon_user_id = uuid4()
    actor_user_id = uuid4()
    pod_id = uuid4()
    agent_run_id = uuid4()
    agent = Agent(
        pod_id=pod_id,
        user_id=actor_user_id,
        name="Daemon Agent",
        instruction="Stay concise.",
    )
    conversation = Conversation(
        user_id=actor_user_id,
        pod_id=pod_id,
        organization_id=uuid4(),
        title="Daemon run",
        metadata={
            "daemon_session": {
                "harness_kind": "CODEX",
                "session_id": "thread-cached",
            }
        },
    )
    message = Message.create(
        conversation_id=conversation.id,
        sequence=0,
        agent_run_id=None,
        role=MessageRole.USER,
        text="continue",
    )
    ctx = AgentContext(
        user_id=actor_user_id,
        pod_id=pod_id,
        conversation_id=conversation.id,
        agent_run_id=agent_run_id,
    )

    payload = _run_start_payload(
        agent=agent,
        conversation=conversation,
        messages=[message],
        ctx=ctx,
        options=HarnessOptions(
            model_name="gpt-5.5",
            extra={
                "runtime_profile": {
                    "user_id": str(daemon_user_id),
                    "daemon_id": str(daemon_id),
                    "scope": "ORGANIZATION",
                    "config": {},
                }
            },
        ),
        agent_run_id=agent_run_id,
        harness_kind=HarnessKind.CODEX,
    )

    assert payload["prompt"]["session_id"] == "thread-cached"
    assert "system_prompt" not in payload["prompt"]
    recovery_prompt = payload["prompt"]["recovery_system_prompt"]
    assert "Stay concise." in recovery_prompt
    assert "You are running through a Lemma user daemon." in recovery_prompt
    assert payload["prompt"]["user_prompt"] == "USER:\ncontinue"
