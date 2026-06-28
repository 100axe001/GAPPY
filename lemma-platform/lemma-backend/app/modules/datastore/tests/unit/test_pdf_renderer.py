from __future__ import annotations

import io
import os
import tempfile

import pytest
from PIL import Image, ImageDraw

from app.modules.datastore.infrastructure.pdf_renderer import (
    _sample_page_indices,
    get_pdf_page_count,
    get_pdf_text_sample,
    render_pdf_pages,
)


@pytest.fixture
def three_page_pdf_path():
    pages = []
    for i in range(1, 4):
        img = Image.new("RGB", (1240, 1754), "white")
        ImageDraw.Draw(img).text((100, 100), f"PAGE {i} CONTENT", fill="black")
        pages.append(img)
    buffer = io.BytesIO()
    pages[0].save(buffer, format="PDF", save_all=True, append_images=pages[1:])
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(buffer.getvalue())
        path = f.name
    try:
        yield path
    finally:
        os.unlink(path)


def test_get_pdf_page_count(three_page_pdf_path):
    assert get_pdf_page_count(three_page_pdf_path) == 3


def test_render_selected_pages(three_page_pdf_path):
    out = render_pdf_pages(three_page_pdf_path, [1, 3], dpi=150)
    assert sorted(out) == [1, 3]
    for jpeg in out.values():
        img = Image.open(io.BytesIO(jpeg))
        assert img.format == "JPEG"


def test_render_caps_long_edge(three_page_pdf_path):
    out = render_pdf_pages(three_page_pdf_path, [1], dpi=300, max_long_edge=1000)
    img = Image.open(io.BytesIO(out[1]))
    assert max(img.size) <= 1000


def test_render_skips_out_of_range_pages(three_page_pdf_path):
    out = render_pdf_pages(three_page_pdf_path, [2, 99, 0, -1], dpi=72)
    assert sorted(out) == [2]


def test_render_empty_pages_returns_empty(three_page_pdf_path):
    assert render_pdf_pages(three_page_pdf_path, []) == {}


def test_sample_page_indices_returns_all_when_few_pages():
    assert _sample_page_indices(3, 5) == [0, 1, 2]


def test_sample_page_indices_spreads_across_document():
    indices = _sample_page_indices(100, 5)
    assert indices[0] == 0  # always include the first page
    assert indices[-1] == 99  # ...and the last
    assert len(indices) == 5
    assert indices == sorted(set(indices))  # distinct + ordered


def test_sample_page_indices_edge_cases():
    assert _sample_page_indices(50, 1) == [0]
    assert _sample_page_indices(0, 5) == []
    assert _sample_page_indices(5, 0) == []


def test_get_pdf_text_sample_counts_low_text_for_image_pdf(three_page_pdf_path):
    # The fixture is a rasterized (image-only) PDF — no text layer — so the
    # sampler should report ~0 characters, which is how a scanned PDF reads.
    pages_sampled, total_chars = get_pdf_text_sample(three_page_pdf_path, max_pages=5)
    assert pages_sampled == 3
    assert total_chars < 50
