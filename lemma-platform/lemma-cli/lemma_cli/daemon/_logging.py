from __future__ import annotations

import json
import os
import re

from ..cli_core.state import console

_DAEMON_DEBUG = False


def set_debug(enabled: bool) -> None:
    global _DAEMON_DEBUG
    _DAEMON_DEBUG = enabled or os.getenv("LEMMA_DAEMON_DEBUG") == "1"


def is_debug() -> bool:
    return _DAEMON_DEBUG


def log(label: str, payload: object | None = None) -> None:
    if payload is None:
        console.print(f"[daemon] {label}")
        return
    if not _DAEMON_DEBUG:
        console.print(f"[daemon] {label}{_compact_suffix(payload)}")
        return
    console.print(f"[daemon] {label}: {json.dumps(redact(payload), default=str)}")


def _compact_suffix(payload: object) -> str:
    if isinstance(payload, dict):
        method = payload.get("method")
        path = payload.get("path")
        if isinstance(method, str) and isinstance(path, str):
            return f": {method} {path}"
        for key in ("type", "event_type", "method", "status"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return f": {value}"
        error = payload.get("error")
        if isinstance(error, str) and error:
            return f": {preview(error, limit=800)}"
        event = payload.get("event")
        if isinstance(event, dict):
            value = event.get("type")
            if isinstance(value, str) and value:
                return f": {value}"
        message = payload.get("message")
        if isinstance(message, dict):
            value = message.get("method") or message.get("type")
            if isinstance(value, str) and value:
                return f": {value}"
    if isinstance(payload, str) and payload:
        return f": {preview(payload, limit=160)}"
    return ""


def redact(value: object) -> object:
    if isinstance(value, dict):
        redacted: dict[str, object] = {}
        for key, item in value.items():
            key_text = str(key).lower()
            if any(secret in key_text for secret in ("token", "authorization", "api_key", "password")):
                redacted[str(key)] = "<redacted>"
            else:
                redacted[str(key)] = redact(item)
        return redacted
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        return re.sub(r"Bearer\s+[^\"'\s,}]+", "Bearer <redacted>", value)
    return value


def preview(text: object, *, limit: int = 2000) -> str:
    s = str(text)
    if len(s) <= limit:
        return s
    omitted = len(s) - limit
    return s[:limit] + f"... [{omitted} chars omitted]"
