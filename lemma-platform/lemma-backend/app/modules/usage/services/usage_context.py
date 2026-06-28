"""Current agent usage context."""

from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class UsageExecutionContext:
    user_id: UUID
    organization_id: UUID | None
    pod_id: UUID | None
    agent_id: UUID | None = None
    conversation_id: UUID | None = None
    agent_run_id: UUID | None = None
    parent_agent_run_id: UUID | None = None
    source_type: str = "agent_run"
    source_id: str | None = None
    workload_type: str | None = None
    workload_id: UUID | None = None


_current_usage_context: ContextVar[UsageExecutionContext | None] = ContextVar(
    "usage_execution_context",
    default=None,
)


def current_usage_context() -> UsageExecutionContext | None:
    return _current_usage_context.get()


@contextmanager
def usage_execution_context(ctx: UsageExecutionContext):
    token = _current_usage_context.set(ctx)
    try:
        yield ctx
    finally:
        _current_usage_context.reset(token)


def usage_context_from_agent_context(
    ctx,
    *,
    source_type: str | None = None,
    source_id: str | None = None,
    parent_agent_run_id: UUID | None = None,
) -> UsageExecutionContext:
    return UsageExecutionContext(
        user_id=ctx.user_id,
        organization_id=getattr(ctx, "org_id", None),
        pod_id=getattr(ctx, "pod_id", None),
        agent_id=(
            getattr(ctx, "workload_id", None)
            if getattr(ctx, "workload_type", None) in {None, "agent", "agent_tool"}
            else None
        ),
        conversation_id=getattr(ctx, "conversation_id", None),
        agent_run_id=getattr(ctx, "agent_run_id", None),
        parent_agent_run_id=parent_agent_run_id,
        source_type=source_type or getattr(ctx, "workload_type", None) or "agent_run",
        source_id=source_id or str(getattr(ctx, "agent_run_id", "") or ""),
        workload_type=getattr(ctx, "workload_type", None),
        workload_id=getattr(ctx, "workload_id", None),
    )
