from __future__ import annotations

import base64
from typing import Sequence, TypeVar
from uuid import UUID

from app.core.domain.errors import BadRequestError


T = TypeVar("T")


def encode_offset_page_token(offset: int) -> str:
    raw = f"offset:{offset}".encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii")


def decode_offset_page_token(page_token: str | None) -> int:
    if not page_token:
        return 0

    try:
        decoded = base64.urlsafe_b64decode(page_token.encode("ascii")).decode("utf-8")
        prefix, raw_offset = decoded.split(":", 1)
        if prefix != "offset":
            raise ValueError("Unsupported page token")
        offset = int(raw_offset)
    except Exception as exc:  # pragma: no cover - defensive validation
        raise BadRequestError("Invalid page_token") from exc

    if offset < 0:
        raise BadRequestError("Invalid page_token")
    return offset


def paginate_items(
    items: Sequence[T],
    *,
    limit: int,
    page_token: str | None,
) -> tuple[list[T], str | None]:
    offset = decode_offset_page_token(page_token)
    page = list(items[offset : offset + limit])
    next_offset = offset + len(page)
    next_page_token = (
        encode_offset_page_token(next_offset) if next_offset < len(items) else None
    )
    return page, next_page_token


def parse_uuid_page_token(page_token: str | None) -> UUID | None:
    if page_token is None:
        return None

    try:
        return UUID(page_token)
    except ValueError as exc:  # pragma: no cover - defensive validation
        raise BadRequestError("Invalid page_token") from exc
