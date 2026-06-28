"""Background job queue contracts."""

from __future__ import annotations

from typing import Any, Protocol


class JobQueuePort(Protocol):
    """Port for enqueueing and aborting background jobs."""

    async def enqueue(self, job_name: str, **kwargs: Any) -> Any:
        """Enqueue a background job."""
        ...

    async def abort(self, job_id: str, *, timeout_seconds: float | None = None) -> bool:
        """Abort a queued or running background job."""
        ...
