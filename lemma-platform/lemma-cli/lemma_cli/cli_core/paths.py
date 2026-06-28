from __future__ import annotations


def api_path(path: str) -> str:
    if path == "/pod":
        return "/"
    if path.startswith("/pod/"):
        return path.removeprefix("/pod") or "/"
    return path
