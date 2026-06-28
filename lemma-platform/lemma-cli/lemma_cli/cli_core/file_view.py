"""Pure helpers for `lemma file cat` — content selection, page/line slicing,
and output capping.

The CLI fetches bytes through the SDK (`files.download` / `files.download_
converted_markdown`); everything here is side-effect-free so it can be unit
tested without a client. Page slicing mirrors the backend's
``services/files/page_markers.py`` so a page range means the same thing whether
an agent reads a document through the in-process tool or `lemma file cat`.
"""

from __future__ import annotations

import re

# Converted ``document.md`` carries inline ``<!-- PAGE N -->`` markers (1-based)
# that Kreuzberg embeds at extraction time. They are the only way to slice a
# document by page client-side, so we parse the same marker the backend writes.
PAGE_MARKER_RE = re.compile(r"<!--\s*PAGE\s+(\d+)\s*-->")

# Document mime types are never UTF-8 text, but plenty of "data" formats are —
# treat these as text so `auto` shows the source rather than a conversion.
_TEXTLIKE_MIME_EXACT = {
    "application/json",
    "application/x-ndjson",
    "application/xml",
    "application/yaml",
    "application/x-yaml",
    "application/toml",
    "application/javascript",
    "application/x-javascript",
    "application/csv",
    "application/x-sh",
    "image/svg+xml",
}


def is_textlike_mime(mime: str | None) -> bool:
    """True when a mime type denotes UTF-8 text we should show verbatim."""
    if not mime:
        return False
    base = mime.split(";", 1)[0].strip().lower()
    if base.startswith("text/"):
        return True
    if base in _TEXTLIKE_MIME_EXACT:
        return True
    return base.endswith(("+json", "+xml", "+yaml"))


def resolve_mode(requested: str, *, mime: str | None, has_markdown: bool) -> str:
    """Resolve ``auto`` to ``text`` or ``markdown``; pass explicit modes through.

    ``auto`` prefers the converted markdown for document-like files (a PDF or
    DOCX is binary and has a conversion) and the raw bytes for text-like files
    (a ``.md`` or ``.json`` is already readable). When neither signal is decisive
    it falls back to ``text`` and lets the decode step flag a binary file.
    """
    if requested in ("text", "markdown"):
        return requested
    if has_markdown and not is_textlike_mime(mime):
        return "markdown"
    if is_textlike_mime(mime):
        return "text"
    if has_markdown:
        return "markdown"
    return "text"


def parse_range_spec(spec: str) -> tuple[int | None, int | None]:
    """Parse a 1-based range like ``3``, ``3-7``, ``3-``, ``-7`` (or ``:``).

    Returns ``(start, end)`` where either side may be ``None`` for an open
    bound. Raises ``ValueError`` on anything unparseable or non-positive so the
    caller can surface a usage error.
    """
    text = spec.strip()
    if not text:
        raise ValueError("range cannot be empty")
    separator = "-" if "-" in text else (":" if ":" in text else "")
    if separator:
        left, _, right = text.partition(separator)
        start = _parse_bound(left)
        end = _parse_bound(right)
    else:
        start = end = _parse_bound(text)
    if start is None and end is None:
        raise ValueError(f"invalid range {spec!r}")
    if start is not None and end is not None and end < start:
        raise ValueError(f"range end {end} is before start {start}")
    return start, end


def _parse_bound(value: str) -> int | None:
    text = value.strip()
    if not text:
        return None
    number = int(text)  # ValueError propagates to the caller
    if number < 1:
        raise ValueError("range bounds are 1-based and must be >= 1")
    return number


def parse_page_offsets(marked_md: str) -> list[tuple[int, int]]:
    """``(char_offset, page_number)`` for each page marker, in document order."""
    if not marked_md:
        return []
    return [
        (match.start(), int(match.group(1)))
        for match in PAGE_MARKER_RE.finditer(marked_md)
    ]


def count_pages(marked_md: str) -> int:
    """Total page count from the markers (matches the backend's derivation)."""
    offsets = parse_page_offsets(marked_md)
    if offsets:
        return max(page for _, page in offsets)
    return 1 if marked_md.strip() else 0


def slice_pages(
    marked_md: str,
    page_start: int | None,
    page_end: int | None,
) -> str:
    """Return the markdown spanning ``[page_start, page_end]`` (inclusive, 1-based).

    ``page_end`` defaults to ``page_start``. With no markers (plaintext) the full
    content is returned. The leading marker for ``page_start`` is kept so the
    reader can see which page they are on. Mirrors the backend so a page range
    means the same thing everywhere.
    """
    if page_start is None:
        return marked_md
    offsets = parse_page_offsets(marked_md)
    if not offsets:
        return marked_md

    end = page_end if page_end is not None else page_start
    if end < page_start:
        end = page_start

    start_index: int | None = None
    end_index = len(marked_md)
    for marker_offset, page_number in offsets:
        if page_number == page_start and start_index is None:
            start_index = marker_offset
        if page_number == end + 1:
            end_index = marker_offset
            break

    if start_index is None:
        return ""
    return marked_md[start_index:end_index].strip()


def slice_lines(text: str, line_start: int | None, line_end: int | None) -> str:
    """Return the 1-based inclusive line range ``[line_start, line_end]``.

    Open bounds default to the first / last line. An empty selection (start past
    the end, or end before start after clamping) yields an empty string.
    """
    if line_start is None and line_end is None:
        return text
    lines = text.splitlines(keepends=True)
    total = len(lines)
    start = line_start if line_start is not None else 1
    end = line_end if line_end is not None else total
    start = max(start, 1)
    end = min(end, total)
    if end < start:
        return ""
    return "".join(lines[start - 1 : end])


def apply_caps(
    text: str,
    *,
    max_chars: int | None = None,
    max_lines: int | None = None,
) -> tuple[str, bool]:
    """Cap ``text`` to ``max_lines`` (head) then ``max_chars``.

    A bound of ``None`` (or negative) means unlimited. Returns the capped text
    and whether anything was dropped.
    """
    truncated = False
    if max_lines is not None and max_lines >= 0:
        lines = text.splitlines(keepends=True)
        if len(lines) > max_lines:
            text = "".join(lines[:max_lines])
            truncated = True
    if max_chars is not None and max_chars >= 0 and len(text) > max_chars:
        text = text[:max_chars]
        truncated = True
    return text, truncated
