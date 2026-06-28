from __future__ import annotations

import pytest

from app.modules.datastore.domain.indexing_policy import (
    INDEXABLE_DOCUMENT_MIME_TYPES,
    is_indexable_mime_type,
    normalize_mime_type,
)


@pytest.mark.parametrize(
    "mime_type, name",
    [
        ("application/pdf", "report.pdf"),
        (
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "memo.docx",
        ),
        ("application/msword", "legacy.doc"),
        ("application/vnd.oasis.opendocument.text", "notes.odt"),
        ("application/rtf", "rich.rtf"),
        ("text/rtf", "rich.rtf"),
        ("text/markdown", "readme.md"),
        ("text/x-markdown", "readme.md"),
        (None, "readme.md"),  # guessed from name
        ("text/plain", "notes.txt"),
        ("text/html", "page.html"),
        ("application/epub+zip", "book.epub"),
    ],
)
def test_indexable_document_types_are_indexable(mime_type, name):
    assert is_indexable_mime_type(mime_type, name) is True


@pytest.mark.parametrize(
    "mime_type, name",
    [
        ("text/csv", "data.csv"),
        ("text/tab-separated-values", "data.tsv"),
        ("application/json", "config.json"),
        ("application/yaml", "config.yaml"),
        ("text/x-log", "server.log"),
        (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "budget.xlsx",
        ),
        ("application/vnd.oasis.opendocument.spreadsheet", "sheet.ods"),
        (
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "deck.pptx",
        ),
        ("image/png", "diagram.png"),
        ("image/jpeg", "photo.jpeg"),
        ("image/gif", "anim.gif"),
        ("image/webp", "pic.webp"),
        ("message/rfc822", "message.eml"),
        (None, "noextension"),  # unknown type, no extension
    ],
)
def test_non_document_types_are_not_indexable(mime_type, name):
    assert is_indexable_mime_type(mime_type, name) is False


def test_normalize_strips_charset_parameters():
    assert normalize_mime_type("text/markdown; charset=utf-8", None) == "text/markdown"
    assert normalize_mime_type("TEXT/PLAIN ; charset=UTF-8", None) == "text/plain"


def test_normalize_guesses_from_name_when_mime_missing():
    assert normalize_mime_type(None, "notes.txt") == "text/plain"
    assert normalize_mime_type("", "report.pdf") == "application/pdf"


def test_normalize_returns_none_for_unknown():
    assert normalize_mime_type(None, None) is None
    assert normalize_mime_type(None, "binary-blob") is None
    assert normalize_mime_type("", "") is None


def test_none_mime_and_name_is_not_indexable():
    assert is_indexable_mime_type(None, None) is False


def test_allowlist_contents_are_documents_only():
    # Guard against accidental re-introduction of tabular/binary types.
    forbidden = {
        "text/csv",
        "application/json",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "image/png",
        "message/rfc822",
    }
    assert forbidden.isdisjoint(INDEXABLE_DOCUMENT_MIME_TYPES)
