from __future__ import annotations

from uuid import uuid4

import pytest

from app.core.config import settings
from app.modules.workspace.services.workspace_file_manager import WorkspaceFileManager


class _FakeWorkspaceSession:
    def __init__(self):
        self.commands: list[str] = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        del exc_type, exc_val, exc_tb

    async def exec_command(self, *, cmd: str, timeout: int):
        del timeout
        self.commands.append(cmd)
        if "import json" in cmd:
            return {
                "success": True,
                "stdout": (
                    '[{"name":"note.txt","path":"conversations/abc/note.txt",'
                    '"type":"file","size":4}]'
                ),
            }
        if cmd.startswith("base64"):
            return {"success": True, "stdout": "dGVzdA=="}
        return {"success": True, "stdout": ""}


class _FakeWorkspaceService:
    def __init__(self, session: _FakeWorkspaceSession):
        self.session = session

    async def get_session(self, **kwargs):
        del kwargs
        return self.session


@pytest.mark.asyncio
async def test_workspace_file_manager_uses_sandbox_session(monkeypatch):
    monkeypatch.setattr(settings, "environment", "development")
    session = _FakeWorkspaceSession()
    monkeypatch.setattr(
        "app.modules.workspace.services.workspace_sandbox_service.WorkspaceSandboxService",
        lambda: _FakeWorkspaceService(session),
    )

    manager = WorkspaceFileManager(uuid4(), cwd="conversations/abc")

    listed = await manager.list_files("")
    written = await manager.write_file("note.txt", "test")
    read_back = await manager.read_file("note.txt")
    await manager.delete_file("note.txt")

    assert "conversations/abc" in session.commands[0]
    assert "conversations/abc/note.txt" in session.commands[1]
    assert "conversations/abc/note.txt" in session.commands[2]
    assert "conversations/abc/note.txt" in session.commands[3]
    assert listed[0].path == "note.txt"
    assert written.path == "note.txt"
    assert read_back == "test"
