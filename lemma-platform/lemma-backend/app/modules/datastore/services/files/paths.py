"""Canonical datastore path/name normalization.

Single source of truth shared by the file path policy and the system-skills
overlay. Paths are always absolute (leading ``/``), have no empty/relative
segments, and never end in a trailing slash (except the root ``/``).
"""

from __future__ import annotations

from app.modules.datastore.domain.errors import DatastoreValidationError


def normalize_datastore_name(name: str) -> str:
    """Validate a single path segment (a file or folder name)."""
    cleaned = name.strip()
    if not cleaned:
        raise DatastoreValidationError("File name cannot be empty")
    if "/" in cleaned:
        raise DatastoreValidationError("Names cannot contain '/'")
    if cleaned in {".", ".."}:
        raise DatastoreValidationError("Invalid path segment")
    return cleaned


def normalize_datastore_path(path: str | None) -> str:
    """Normalize an absolute datastore path; reject relative segments."""
    if path is None:
        return "/"
    raw = path.strip()
    if not raw:
        return "/"
    if not raw.startswith("/"):
        raw = f"/{raw}"
    parts = [segment for segment in raw.split("/") if segment]
    normalized_parts: list[str] = []
    for part in parts:
        if part in {".", ".."}:
            raise DatastoreValidationError("Relative path segments are not allowed")
        normalized_parts.append(normalize_datastore_name(part))
    if not normalized_parts:
        return "/"
    return "/" + "/".join(normalized_parts)
