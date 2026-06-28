from dataclasses import dataclass
from typing import Any, Dict, Optional
from enum import Enum

from pydantic import BaseModel

from app.core.log.log import get_logger

logger = get_logger(__name__)


@dataclass
class SandboxInfo:
    """Information about a user code sandbox."""

    sandbox_id: str
    namespace: str
    status: str
    image: str
    created_at: Optional[str] = None
    endpoint: Optional[str] = None
    name: Optional[str] = None

    @property
    def container_name(self) -> str:
        """Compatibility alias for older call sites."""
        return self.name or self.sandbox_id

    @property
    def pod_name(self) -> str:
        """Compatibility alias for older call sites."""
        return self.name or self.sandbox_id


ContainerInfo = SandboxInfo


class WorkspaceStatus(str, Enum):
    """Status of a workspace container."""

    CREATING = "CREATING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    ERROR = "ERROR"


@dataclass
class ExecutionResult:
    """Result from code execution."""

    success: bool
    output: str
    error: Optional[str] = None
    execution_count: Optional[int] = None
    data: Optional[dict[str, Any]] = None  # For rich outputs like images, dataframes


class ShellCommandResult(BaseModel):
    success: bool
    exit_code: Optional[int] = None
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    error: Optional[str | Dict[str, Any]] = None
    current_working_directory: Optional[str] = None

    def __str__(self):
        return f"""
# ShellCommandResult
## IsSuccess
{self.success}
## Exit Code
{self.exit_code}
## Stdout
{self.stdout}
## Stderr
{self.stderr}
## Error
{self.error}
## Current Working Directory
{self.current_working_directory}
        """

    @property
    def full_error_message(self) -> Optional[str]:
        """Combines stdout, stderr, and error into a single message if the command failed."""
        if self.success:
            return None

        message_parts = []
        if self.stdout and self.stdout.strip():
            message_parts.append(f"Stdout: {self.stdout.strip()}")
        if self.stderr and self.stderr.strip():
            message_parts.append(f"Stderr: {self.stderr.strip()}")
        if self.error:
            if isinstance(self.error, str) and self.error.strip():
                message_parts.append(f"Error: {self.error.strip()}")
            elif isinstance(self.error, dict):
                message_parts.append(f"Error: {self.error}")

        if not message_parts:
            return f"Command failed with exit code {self.exit_code} but no output."

        return "\\n".join(message_parts)


class PythonExecutionResult(BaseModel):
    """Represents the result of a Python code execution."""

    success: bool
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    result: Optional[str] = None  # The result value from the last expression
    error_in_exec: Optional[Dict[str, Any]] = (
        None  # Full error details (ename, evalue, traceback)
    )
    execution_count: Optional[int] = None  # Jupyter execution count
    data: Optional[Dict[str, Any]] = None  # Rich outputs like images, dataframes

    @property
    def error(self) -> Optional[str]:
        """Get error message if execution failed"""
        if self.error_in_exec:
            ename = self.error_in_exec.get("ename", "")
            evalue = self.error_in_exec.get("evalue", "")
            traceback = self.error_in_exec.get("traceback", [])
            if traceback:
                return f"{ename}: {evalue}\n" + "\n".join(traceback)
            return f"{ename}: {evalue}"
        return None
