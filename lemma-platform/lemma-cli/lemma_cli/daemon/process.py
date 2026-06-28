from __future__ import annotations

import asyncio
import contextlib
from pathlib import Path

# Fixes "ValueError: Separator is found, but chunk is longer than limit".
# Claude Code can output JSON lines exceeding the default 64 KB asyncio.StreamReader
# limit when tool results contain large file contents.
STREAM_READER_LIMIT = 10 * 1024 * 1024  # 10 MB


async def create_subprocess(
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    stdin: bool = False,
) -> asyncio.subprocess.Process:
    """Create a subprocess with a 10 MB StreamReader limit on stdout/stderr."""
    return await asyncio.create_subprocess_exec(
        *command,
        stdin=asyncio.subprocess.PIPE if stdin else None,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=str(cwd),
        env=env,
        limit=STREAM_READER_LIMIT,
    )


async def drain_stream(stream: asyncio.StreamReader | None) -> str:
    if stream is None:
        return ""
    data = await stream.read()
    return data.decode(errors="replace")


async def terminate_gracefully(process: asyncio.subprocess.Process) -> None:
    if process.returncode is not None:
        return
    with contextlib.suppress(ProcessLookupError):
        process.terminate()
    try:
        await asyncio.wait_for(process.wait(), timeout=5)
    except asyncio.TimeoutError:
        with contextlib.suppress(ProcessLookupError):
            process.kill()
        await process.wait()
