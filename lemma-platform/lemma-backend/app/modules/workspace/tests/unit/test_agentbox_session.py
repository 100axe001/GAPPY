from __future__ import annotations

from typing import Any

import httpx
import pytest

from app.modules.workspace.agentbox_session import AgentBoxWorkspaceSession


class _FakeAgentBoxClient:
    async def execute_code(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        raise _http_status_error(
            500,
            "Internal Server Error",
            "/sandboxes/s1/sessions/session-1/python",
        )

    async def exec_command(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        raise _http_status_error(
            500,
            "Internal Server Error",
            "/sandboxes/s1/sessions/session-1/exec-command",
        )

    async def write_stdin(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        raise _http_status_error(
            404,
            "Not Found",
            "/sandboxes/s1/sessions/session-1/stdin",
        )


class _ReadTimeoutAgentBoxClient:
    async def exec_command(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        request = httpx.Request(
            "POST",
            "https://api.agentbox.test/sandboxes/s1/sessions/session-1/exec-command",
        )
        raise httpx.ReadTimeout("timed out", request=request)


class _FlakyCreateSessionClient:
    def __init__(self) -> None:
        self.create_calls = 0
        self.deleted = False
        self.closed = False

    async def create_session(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        self.create_calls += 1
        if self.create_calls == 1:
            raise _http_status_error(
                502,
                "Bad Gateway",
                "/sandboxes/s1/sessions/session-1",
            )
        return {"session_id": "session-1"}

    async def delete_session(self, *args: Any, **kwargs: Any) -> bool:
        self.deleted = True
        return True

    async def close(self) -> None:
        self.closed = True


def _http_status_error(
    status_code: int,
    reason: str,
    path: str,
) -> httpx.HTTPStatusError:
    request = httpx.Request("POST", f"https://api.agentbox.test{path}")
    response = httpx.Response(
        status_code,
        json={"detail": reason},
        request=request,
    )
    return httpx.HTTPStatusError(
        f"Server error '{status_code} {reason}'",
        request=request,
        response=response,
    )


@pytest.mark.asyncio
async def test_exec_command_returns_retryable_failure_on_agentbox_500():
    session = AgentBoxWorkspaceSession(
        client=_FakeAgentBoxClient(),  # type: ignore[arg-type]
        sandbox_id="s1",
        session_id="session-1",
    )

    result = await session.exec_command(cmd="pwd")

    assert result["success"] is False
    assert result["completed"] is False
    assert result["exit_code"] is None
    assert "HTTP 500 Internal Server Error" in result["error"]
    assert "retry" in result["error"].lower()


@pytest.mark.asyncio
async def test_exec_command_initial_read_timeout_is_completed_without_process_id():
    session = AgentBoxWorkspaceSession(
        client=_ReadTimeoutAgentBoxClient(),  # type: ignore[arg-type]
        sandbox_id="s1",
        session_id="session-1",
    )

    result = await session.exec_command(cmd="agent-browser snapshot -i -u")

    assert result["success"] is False
    assert result["completed"] is True
    assert result["process_id"] is None
    assert "transport failed" in result["error"]


@pytest.mark.asyncio
async def test_execute_code_returns_python_failure_on_agentbox_500():
    session = AgentBoxWorkspaceSession(
        client=_FakeAgentBoxClient(),  # type: ignore[arg-type]
        sandbox_id="s1",
        session_id="session-1",
    )

    result = await session.execute_code("1 + 1")

    assert result.success is False
    assert result.error_in_exec is not None
    assert result.error_in_exec["ename"] == "TransientAgentBoxError"
    assert "HTTP 500 Internal Server Error" in result.error_in_exec["evalue"]


@pytest.mark.asyncio
async def test_write_stdin_returns_non_retryable_failure_on_agentbox_404():
    session = AgentBoxWorkspaceSession(
        client=_FakeAgentBoxClient(),  # type: ignore[arg-type]
        sandbox_id="s1",
        session_id="session-1",
    )

    result = await session.write_stdin(process_id="proc-1", chars="")

    assert result["success"] is False
    assert result["completed"] is True
    assert result["exit_code"] == 404
    assert result["process_id"] == "proc-1"
    assert "HTTP 404 Not Found" in result["error"]


@pytest.mark.asyncio
async def test_enter_retries_transient_session_create_failure(
    monkeypatch: pytest.MonkeyPatch,
):
    client = _FlakyCreateSessionClient()
    sleeps: list[float] = []

    async def fake_sleep(delay: float) -> None:
        sleeps.append(delay)

    monkeypatch.setattr("app.modules.workspace.agentbox_session.asyncio.sleep", fake_sleep)

    session = AgentBoxWorkspaceSession(
        client=client,  # type: ignore[arg-type]
        sandbox_id="s1",
        session_id="session-1",
        heartbeat_interval_seconds=0,
    )

    async with session:
        pass

    assert client.create_calls == 2
    assert sleeps == [0.25]
    assert client.deleted is True
    assert client.closed is True
