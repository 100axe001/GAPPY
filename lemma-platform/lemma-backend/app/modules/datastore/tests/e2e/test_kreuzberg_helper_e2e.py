from __future__ import annotations

from pathlib import Path

import pytest

from app.modules.datastore.infrastructure.kreuzberg_helper import KreuzbergHelper


pytestmark = pytest.mark.e2e


@pytest.mark.asyncio
async def test_kreuzberg_extracts_markdown_for_pdf(e2e_settings):
    """Kreuzberg extracts markdown text and chunks from a real arXiv PDF.

    Uses the shared session-scoped Kreuzberg container via ``e2e_settings``
    (which already points ``datastore_settings.kreuzberg_url`` at it). An earlier version
    started its OWN second container and overwrote the shared
    ``datastore_settings.kreuzberg_url`` without restoring it — once this test's container
    was torn down, every later indexing test in the module pointed at a dead URL
    and failed with ConnectionRefused. Reusing the session container keeps the
    setting intact for the rest of the suite.
    """
    fixture_path = (
        Path(__file__).resolve().parents[1] / "fixtures" / "arxiv" / "seq2seq.pdf"
    )

    helper = KreuzbergHelper()
    result = await helper.process_file(
        fixture_path.read_bytes(),
        fixture_path.name,
    )

    assert result.content.strip()
    assert "NEURAL MACHINE TRANSLATION" in result.content
    assert result.get_chunks()
