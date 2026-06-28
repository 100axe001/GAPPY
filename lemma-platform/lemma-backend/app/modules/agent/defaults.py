"""Config-backed defaults for agent execution."""

from __future__ import annotations

from app.modules.agent.domain.value_objects import AgentRuntimeConfig
from app.modules.agent.agent_runtime_defaults import (
    AgentRuntimeDefaultService,
)


def default_agent_runtime() -> AgentRuntimeConfig:
    return AgentRuntimeDefaultService().get_default()


def default_agent_runtime_profile_id() -> str:
    return AgentRuntimeDefaultService().get_default().profile_id
