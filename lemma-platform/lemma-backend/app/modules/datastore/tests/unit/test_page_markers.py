from __future__ import annotations

from app.modules.datastore.services.files.page_markers import (
    parse_page_offsets,
    slice_pages,
)

PAGE1 = "Intro text on page one.\n\nMore page one."
PAGE2 = "Chapter two begins here.\n\nSecond page body."
PAGE3 = "Final page three content."

MARKED = (
    f"<!-- PAGE 1 -->\n\n{PAGE1}\n\n"
    f"<!-- PAGE 2 -->\n\n{PAGE2}\n\n"
    f"<!-- PAGE 3 -->\n\n{PAGE3}"
)


def test_parse_page_offsets_returns_each_marker_in_order():
    offsets = parse_page_offsets(MARKED)
    assert [page for _, page in offsets] == [1, 2, 3]
    # Offsets are monotonically increasing marker positions.
    positions = [pos for pos, _ in offsets]
    assert positions == sorted(positions)


def test_parse_page_offsets_empty():
    assert parse_page_offsets("") == []
    assert parse_page_offsets("no markers here") == []


def test_slice_pages_single_page():
    out = slice_pages(MARKED, 2, None)
    assert "Chapter two begins" in out
    assert "Intro text on page one" not in out
    assert "Final page three" not in out
    # Keeps the page's own marker for orientation.
    assert "<!-- PAGE 2 -->" in out


def test_slice_pages_range():
    out = slice_pages(MARKED, 1, 2)
    assert "Intro text on page one" in out
    assert "Chapter two begins" in out
    assert "Final page three" not in out


def test_slice_pages_to_end():
    out = slice_pages(MARKED, 3, 3)
    assert "Final page three" in out
    assert "Chapter two" not in out


def test_slice_pages_no_markers_returns_full():
    plain = "just some text without pages"
    assert slice_pages(plain, 1, 2) == plain


def test_slice_pages_none_start_returns_full():
    assert slice_pages(MARKED, None, None) == MARKED


def test_slice_pages_out_of_range_returns_empty():
    assert slice_pages(MARKED, 9, 10) == ""
