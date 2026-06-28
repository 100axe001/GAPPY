"""Single source of truth for a conversation's workspace + working directory.

Both the agent run and the approval executor must run in the *same* workspace
session and cwd, so the resolution lives here instead of being duplicated. The
location is configurable per conversation via ``metadata``:

- ``cwd`` — explicit working directory; defaults to ``/workspace/conversations/{id}``.
- ``workspace_name`` / ``workspace_id`` — selects the workspace; defaults to the
  single per-user workspace today. Kept metadata-driven so multi-workspace
  switching becomes a metadata-only change later.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.modules.agent.domain.entities import Conversation


@dataclass(slots=True)
class WorkspaceLocation:
    workspace_id: str
    cwd: str


def resolve_workspace_location(conversation: Conversation) -> WorkspaceLocation:
    metadata = conversation.metadata if isinstance(conversation.metadata, dict) else {}
    workspace = metadata.get("workspace")
    workspace = workspace if isinstance(workspace, dict) else {}
    workspace_id = str(
        workspace.get("id")
        or metadata.get("workspace_id")
        or metadata.get("workspace_name")
        or "default"
    )
    cwd = str(
        workspace.get("cwd")
        or metadata.get("cwd")
        or f"/workspace/conversations/{conversation.id}"
    )
    return WorkspaceLocation(workspace_id=workspace_id, cwd=cwd)
