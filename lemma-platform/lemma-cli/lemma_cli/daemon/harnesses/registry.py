from __future__ import annotations

from .claude_code import ClaudeCodeHarness
from .codex import CodexHarness
from .opencode import OpenCodeHarness

_REGISTRY = {
    "CLAUDE_CODE": ClaudeCodeHarness(),
    "CODEX": CodexHarness(),
    "OPENCODE": OpenCodeHarness(),
}


def get_harness(kind: str) -> ClaudeCodeHarness | CodexHarness | OpenCodeHarness:
    harness = _REGISTRY.get(kind)
    if harness is None:
        raise RuntimeError(f"Unsupported daemon harness kind: {kind!r}")
    return harness
