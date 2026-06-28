"""Workspace entity compatibility exports."""

from app.modules.agent.tools.workspace_entities import (
    ContainerInfo,
    ExecutionResult,
    PythonExecutionResult,
    SandboxInfo,
    ShellCommandResult,
    WorkspaceStatus,
)

__all__ = [
    "ContainerInfo",
    "ExecutionResult",
    "PythonExecutionResult",
    "SandboxInfo",
    "ShellCommandResult",
    "WorkspaceStatus",
]
