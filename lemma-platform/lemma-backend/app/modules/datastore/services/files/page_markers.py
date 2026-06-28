"""Helpers for the ``<!-- PAGE N -->`` markers in converted markdown.

The converted ``document.md`` for a document-like file carries inline page
markers (inserted natively by the document processor — see
``KreuzbergDocumentProcessor``). These helpers let us slice the markdown for a
page range (``slice_pages``) so an agent or viewer can request just the pages it
needs. Chunk-level page numbers come from the processor's native page tracking
(``DocumentChunk.page_start/page_end``), so we no longer re-derive them here.

Page numbers are 1-based, matching the marker text and the conversion manifest.
"""

from __future__ import annotations

import re

PAGE_MARKER_RE = re.compile(r"<!--\s*PAGE\s+(\d+)\s*-->")


def parse_page_offsets(marked_md: str) -> list[tuple[int, int]]:
    """Return ``(char_offset, page_number)`` for each page marker, in order.

    ``char_offset`` is the index of the marker's start in ``marked_md``; content
    for that page begins after the marker.
    """
    if not marked_md:
        return []
    return [
        (match.start(), int(match.group(1)))
        for match in PAGE_MARKER_RE.finditer(marked_md)
    ]


def slice_pages(
    marked_md: str,
    page_start: int | None,
    page_end: int | None,
) -> str:
    """Return the markdown spanning ``[page_start, page_end]`` (inclusive, 1-based).

    ``page_end`` defaults to ``page_start`` when omitted. If there are no markers
    (e.g. plaintext), the full content is returned. The leading marker for
    ``page_start`` is kept so the agent can see which page it is reading.
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
        # Requested start beyond the document — return nothing meaningful.
        return ""
    return marked_md[start_index:end_index].strip()
