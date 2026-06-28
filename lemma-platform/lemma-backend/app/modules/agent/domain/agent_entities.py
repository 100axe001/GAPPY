"""Compatibility exports for modules still using legacy agent type names."""

from __future__ import annotations

from enum import Enum

from app.modules.agent.domain.entities import Agent


class ToolSet(str, Enum):
    """Tool sets available to agents and workload resource configs."""

    CODE_EXECUTOR = "CODE_EXECUTOR"
    WORKSPACE_CLI = "WORKSPACE_CLI"
    SKILLS = "SKILLS"
    WEB_SEARCH = "WEB_SEARCH"
    USER_INTERACTION = "USER_INTERACTION"
    SPEECH = "SPEECH"


AgentEntity = Agent

__all__ = ["Agent", "AgentEntity", "ToolSet"]
