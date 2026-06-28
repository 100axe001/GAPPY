"""Lemma user daemon.

Exports are resolved lazily (PEP 562): `runner` pulls in asyncio, http.server,
and the harness implementations, which would otherwise be paid by every CLI
startup just to register the `lemma daemon` command group.
"""
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .runner import (
        handle_run_start,
        run_daemon,
        run_provider_command,
        send_run_event,
    )

__all__ = [
    "handle_run_start",
    "run_daemon",
    "run_provider_command",
    "send_run_event",
]


def __getattr__(name: str):
    if name in __all__:
        value = getattr(importlib.import_module(".runner", __name__), name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
