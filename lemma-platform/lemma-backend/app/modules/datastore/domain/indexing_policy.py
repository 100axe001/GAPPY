"""Datastore file-indexing eligibility policy (document-only allow-list).

This module is the single source of truth for *which* files the datastore will
index for search. It is applied EARLY — at write time, when an entity's status
is set — so the persisted ``FileStatus`` is correct from the start and only
genuinely indexable files are ever enqueued/extracted.

Only prose / document formats are indexed. The following are intentionally
EXCLUDED and never indexed:

- spreadsheets / tabular data: csv, tsv, json, yaml, ``.log``, xlsx, ods
- presentations: pptx, odp
- images (png, jpeg, gif, webp, ...) — no OCR
- email (``.eml`` / message/rfc822, Outlook ``.msg``)
- audio, video, archives, and any other binary

To change what gets indexed, edit ``INDEXABLE_DOCUMENT_MIME_TYPES`` below —
that is the only set that governs eligibility. This module imports only
``mimetypes`` and deliberately does NOT import ``file_entities`` (or anything
else in the datastore) to stay cycle-free.
"""

from __future__ import annotations

import mimetypes

# Document-only allow-list. NOTHING outside this set is indexed.
INDEXABLE_DOCUMENT_MIME_TYPES: frozenset[str] = frozenset(
    {
        # PDF
        "application/pdf",
        # Word processing documents
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # docx
        "application/msword",  # doc
        "application/vnd.oasis.opendocument.text",  # odt
        # Rich text
        "application/rtf",
        "text/rtf",
        # Markdown
        "text/markdown",
        "text/x-markdown",
        # Plain text / markup
        "text/plain",
        "text/html",
        # E-books
        "application/epub+zip",
    }
)


def normalize_mime_type(mime_type: str | None, name: str | None) -> str | None:
    """Normalize a MIME type for indexability checks.

    Strips parameters (e.g. ``; charset=utf-8``), trims, and lowercases. When no
    explicit MIME type is given, falls back to ``mimetypes.guess_type(name)``.
    Returns ``None`` when the type is still unknown.
    """
    if mime_type:
        base = mime_type.split(";", 1)[0].strip().lower()
        if base:
            return base
    if name:
        guessed, _ = mimetypes.guess_type(name)
        if guessed:
            return guessed.lower()
    return None


def is_indexable_mime_type(mime_type: str | None, name: str | None) -> bool:
    """Return ``True`` iff the (mime_type, name) resolves to an indexable
    document format. Unknown / unresolved types are NOT indexable."""
    return normalize_mime_type(mime_type, name) in INDEXABLE_DOCUMENT_MIME_TYPES
