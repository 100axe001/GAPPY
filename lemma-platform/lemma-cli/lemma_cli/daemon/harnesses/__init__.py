from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any, Protocol, TypedDict


class HarnessResult(TypedDict):
    command: list[str]
    cwd: str
    returncode: int
    stdout: str
    stderr: str
    streamed_tokens: bool
    streamed_messages: bool


# event_sink signature: async (event_type: str, data: Any) -> None
EventSink = Callable[[str, Any], Awaitable[None]]


class HarnessProvider(Protocol):
    kind: str

    async def run(
        self,
        *,
        model_name: str,
        system_prompt: str,
        user_prompt: str,
        session_id: str | None,
        mcp: dict[str, Any],
        event_sink: EventSink | None,
        stop_event: asyncio.Event,
    ) -> HarnessResult: ...

    async def close(self) -> None: ...
