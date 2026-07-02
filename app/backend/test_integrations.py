"""
Smoke tests for the Lemma-native integration layer.

These hit the live local Lemma stack (pod `lifeos`). Run from the app/ directory:
    python -m pytest backend/test_integrations.py -v
Skipped automatically if the Lemma stack / pod is not reachable.
"""
import asyncio
import pytest

from backend.security import encrypt_data, decrypt_data
from backend.integrations import connectors as connectors_service
from backend import ai


def _run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def test_encryption_decryption():
    """Secrets round-trip through Fernet encryption."""
    test_str = "hello-world-oauth-tokens-12345!"
    encrypted = encrypt_data(test_str)
    assert encrypted != test_str
    assert decrypt_data(encrypted) == test_str


def test_connector_catalog_is_live():
    """The connector catalog should be populated (native connectors imported)."""
    try:
        items = _run(connectors_service.list_integrations())
    except Exception as e:
        pytest.skip(f"Lemma stack not reachable: {e}")
    assert isinstance(items, list)
    assert len(items) > 0, "connector catalog is empty — run import_connector_catalog"
    names = {i["name"] for i in items}
    assert "gmail" in names and "google_calendar" in names


def test_commitment_parser_agent():
    """The commitment-parser agent returns a structured task."""
    try:
        out = _run(ai.parse_commitment_inbox("submit the report by next Friday, urgent"))
    except Exception as e:
        pytest.skip(f"Lemma agent not reachable: {e}")
    assert out.get("title")
    assert out.get("priority") in ("low", "medium", "high")
