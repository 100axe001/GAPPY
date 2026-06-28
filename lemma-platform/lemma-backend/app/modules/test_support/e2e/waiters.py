"""Shared polling helpers for asynchronous E2E behavior."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

import pytest

T = TypeVar("T")


async def eventually(
    *,
    label: str,
    probe: Callable[[], Awaitable[T]],
    done: Callable[[T], bool],
    timeout_seconds: float = 30.0,
    interval_seconds: float = 0.25,
    fail_fast: Callable[[T], str | None] | None = None,
) -> T:
    """Poll ``probe`` until ``done`` is true or fail with useful context."""

    deadline = asyncio.get_running_loop().time() + timeout_seconds
    last_value: T | None = None
    while asyncio.get_running_loop().time() < deadline:
        last_value = await probe()
        if fail_fast is not None:
            failure = fail_fast(last_value)
            if failure:
                pytest.fail(f"{label} failed: {failure}. Last value: {last_value!r}")
        if done(last_value):
            return last_value
        await asyncio.sleep(interval_seconds)

    pytest.fail(f"Timed out waiting for {label}. Last value: {last_value!r}")


async def wait_for_status(
    *,
    label: str,
    probe: Callable[[], Awaitable[dict]],
    status_field: str = "status",
    expected: set[str],
    failed: set[str] | None = None,
    timeout_seconds: float = 30.0,
    interval_seconds: float = 0.25,
) -> dict:
    failed = failed or {"FAILED", "ERROR"}
    return await eventually(
        label=label,
        probe=probe,
        done=lambda payload: str(payload.get(status_field)) in expected,
        fail_fast=lambda payload: (
            str(payload.get(status_field))
            if str(payload.get(status_field)) in failed
            else None
        ),
        timeout_seconds=timeout_seconds,
        interval_seconds=interval_seconds,
    )

