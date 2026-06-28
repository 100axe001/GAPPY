"""Workspace CLI tools.

Path convention:
- Tools operate only inside the private current conversation workspace directory.
- Prefer relative paths like `images/output.png`.
- Files created here are sandbox files. Upload user-facing deliverables to pod
  files under `/me/...` before presenting them to the user.
"""

from app.modules.agent.tools.workspace_cli.pydantic_adapter import (
    workspace_cli_toolset,
)

__all__ = ["workspace_cli_toolset"]
