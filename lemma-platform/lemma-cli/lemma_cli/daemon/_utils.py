from __future__ import annotations

import contextlib
import json

MAX_DAEMON_ERROR_DETAIL_CHARS = 4000


def bounded_error_detail(detail: str) -> str:
    if len(detail) <= MAX_DAEMON_ERROR_DETAIL_CHARS:
        return detail
    omitted = len(detail) - MAX_DAEMON_ERROR_DETAIL_CHARS
    return detail[:MAX_DAEMON_ERROR_DETAIL_CHARS] + f"\n... truncated {omitted} chars"


def jsonrpc_error_detail(
    *,
    method: str,
    error: object,
    stderr_tail: str = "",
) -> str:
    message = f"JSON-RPC request {method!r} failed"
    if isinstance(error, dict):
        code = error.get("code")
        raw_message = error.get("message")
        data = error.get("data")
        parts = [message]
        if code is not None:
            parts.append(f"code={code}")
        if raw_message:
            parts.append(f"message={raw_message}")
        if data is not None:
            from ._logging import redact
            parts.append(f"data={json.dumps(redact(data), default=str)}")
        detail = "; ".join(parts)
    else:
        detail = f"{message}: {error}"
    if stderr_tail:
        detail += f"\nstderr tail:\n{stderr_tail}"
    return detail


def parse_jsonish(value: object) -> object:
    if isinstance(value, str):
        with contextlib.suppress(json.JSONDecodeError):
            return json.loads(value)
    return value


def strip_prompt_echo_from_text(text: str, *, prompt_candidates: list[str]) -> str:
    if not text:
        return ""
    stripped_text = text.strip()
    for candidate in prompt_candidates:
        candidate = candidate.strip()
        if not candidate:
            continue
        if stripped_text == candidate:
            return ""
        if stripped_text.startswith(candidate):
            return stripped_text[len(candidate):].lstrip()
    return text
