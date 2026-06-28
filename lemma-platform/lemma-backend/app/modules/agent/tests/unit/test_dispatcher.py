"""Unit tests for AgentToolDispatcher resolve + invoke mechanics."""

from __future__ import annotations

from uuid import uuid4

import pytest
from pydantic_ai.tools import RunContext
from pydantic_ai.toolsets import FunctionToolset

from app.modules.agent.tools.context import BaseAgentContext
from app.modules.agent.tools.dispatcher import AgentToolDispatcher, UnknownToolError


async def echo_tool(ctx: RunContext[BaseAgentContext], value: int) -> dict:
    """Echo a value back along with the pod id from context."""
    return {"value": value, "pod_id": str(ctx.deps.pod_id)}


_TOOLSET = FunctionToolset[BaseAgentContext](tools=[echo_tool])


def _ctx() -> BaseAgentContext:
    return BaseAgentContext(user_id=uuid4(), pod_id=uuid4(), conversation_id=uuid4())


@pytest.mark.asyncio
async def test_lists_tools_from_explicit_toolsets():
    dispatcher = AgentToolDispatcher(uow_factory=object())

    tools = await dispatcher.list_tools(ctx=_ctx(), toolsets=[_TOOLSET])

    by_name = {tool.name: tool for tool in tools}
    assert "echo_tool" in by_name
    assert by_name["echo_tool"].description.startswith("Echo a value")


@pytest.mark.asyncio
async def test_calls_tool_with_run_context_deps():
    ctx = _ctx()
    dispatcher = AgentToolDispatcher(uow_factory=object())

    result = await dispatcher.call_tool(
        ctx=ctx,
        toolsets=[_TOOLSET],
        name="echo_tool",
        arguments={"value": 7},
    )

    assert result == {"value": 7, "pod_id": str(ctx.pod_id)}


@pytest.mark.asyncio
async def test_unknown_tool_raises():
    dispatcher = AgentToolDispatcher(uow_factory=object())

    with pytest.raises(UnknownToolError):
        await dispatcher.call_tool(
            ctx=_ctx(),
            toolsets=[_TOOLSET],
            name="does_not_exist",
            arguments={},
        )
