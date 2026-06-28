"""Execution context passed into agent harnesses."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.modules.agent.domain.value_objects import JsonObject


class AgentContext(BaseModel):
    """Request context exposed to tools and framework deps."""

    user_id: UUID
    org_id: UUID | None = None
    pod_id: UUID
    conversation_id: UUID
    agent_name: str | None = None
    agent_run_id: UUID | None = None
    metadata: JsonObject | None = None
    # Rendered runtime brief (pod/user/granted resources) appended to the system
    # prompt. Built once per run by the runner; harness-neutral so it just rides
    # along on the context.
    context_brief: str | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
