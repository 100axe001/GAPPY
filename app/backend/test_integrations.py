import pytest
from unittest.mock import AsyncMock, patch
from backend.security import encrypt_data, decrypt_data
from backend.integrations.registry import registry
from backend.integrations.intent import regex_classify_intent, detect_query_intent

def test_encryption_decryption():
    """Verify credentials can be securely encrypted and decrypted correctly."""
    test_str = "hello-world-oauth-tokens-12345!"
    encrypted = encrypt_data(test_str)
    assert encrypted != test_str
    
    decrypted = decrypt_data(encrypted)
    assert decrypted == test_str

def test_registry():
    """Verify registry loads default adapters (Google Calendar)."""
    adapters = registry.list_adapters()
    assert len(adapters) >= 1
    
    cal = registry.get_adapter("google_calendar")
    assert cal is not None
    assert cal.name == "google_calendar"

def test_regex_intent_classification():
    """Verify intent classifications fallback keyword patterns."""
    assert regex_classify_intent("Create a meeting tomorrow at 5 PM") == "create_event"
    assert regex_classify_intent("What is on my calendar today?") == "list_events"
    assert regex_classify_intent("Delete tomorrow's meeting") == "delete_event"
    assert regex_classify_intent("When am I available next week?") == "find_free_slots"
    assert regex_classify_intent("Remember to buy milk") == "none"

@pytest.mark.asyncio
@patch("backend.integrations.intent.run_agent_until_completed")
async def test_detect_query_intent_llm(mock_run):
    """Verify intent parser maps LLM JSON response successfully."""
    mock_run.return_value = '{"intent": "create_event", "arguments": {"summary": "Mock Meeting", "start_time": "2026-06-29T17:00:00"}}'
    
    intent, args = await detect_query_intent("Create a mock meeting")
    assert intent == "create_event"
    assert args["summary"] == "Mock Meeting"
