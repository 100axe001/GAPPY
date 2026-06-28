from __future__ import annotations

import base64
import re
from collections.abc import Mapping
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


_FILENAME_RE = re.compile(r'filename\*?=(?:UTF-8\'\')?"?([^";]+)"?')


class BinaryContentResult(BaseModel):
    """Structured binary payload returned by an upstream integration operation."""

    type: Literal["binary_content"] = "binary_content"
    content_base64: str = Field(
        ...,
        description="Binary payload encoded as base64 for safe JSON transport.",
    )
    media_type: str = Field(
        default="application/octet-stream",
        description="MIME type reported by the upstream API response.",
    )
    file_name: str | None = Field(
        default=None,
        description="Filename inferred from the upstream response when available.",
    )
    size_bytes: int = Field(
        ...,
        description="Decoded binary payload size in bytes.",
    )
    content_disposition: str | None = Field(
        default=None,
        description="Raw Content-Disposition header returned by the upstream API.",
    )

    model_config = ConfigDict(extra="forbid")

    @classmethod
    def from_bytes(
        cls,
        data: bytes,
        *,
        media_type: str | None = None,
        file_name: str | None = None,
        content_disposition: str | None = None,
    ) -> "BinaryContentResult":
        return cls(
            content_base64=base64.b64encode(data).decode("ascii"),
            media_type=(media_type or "application/octet-stream").strip()
            or "application/octet-stream",
            file_name=file_name,
            size_bytes=len(data),
            content_disposition=content_disposition,
        )

    @classmethod
    def from_http_response(
        cls,
        response: Any,
        *,
        fallback_media_type: str | None = None,
        fallback_file_name: str | None = None,
    ) -> "BinaryContentResult":
        headers = getattr(response, "headers", {}) or {}
        content = bytes(getattr(response, "content", b"") or b"")
        disposition = _header_get(headers, "content-disposition")
        return cls.from_bytes(
            content,
            media_type=_header_get(headers, "content-type") or fallback_media_type,
            file_name=fallback_file_name or _file_name_from_disposition(disposition),
            content_disposition=disposition,
        )


def _header_get(headers: Mapping[str, Any] | Any, name: str) -> str | None:
    if hasattr(headers, "get"):
        value = headers.get(name) or headers.get(name.title())
        if value is not None:
            return str(value)
    return None


def _file_name_from_disposition(disposition: str | None) -> str | None:
    if not disposition:
        return None
    match = _FILENAME_RE.search(disposition)
    if not match:
        return None
    return match.group(1).strip()
