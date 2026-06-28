"""Golden test for agent config: env-var names + defaults preserved."""

from __future__ import annotations

import pytest

from app.modules.agent.config import AgentSettings

pytestmark = pytest.mark.unit

EXPECTED = [
    ("widget_url_expiry_seconds", "WIDGET_URL_EXPIRY_SECONDS", 1800),
    ("speech_provider", "SPEECH_PROVIDER", "auto"),
    ("deepgram_api_key", "DEEPGRAM_API_KEY", None),
]


def _clear(monkeypatch):
    for _, env, _default in EXPECTED:
        monkeypatch.delenv(env, raising=False)


def test_agent_settings_defaults():
    # Declared defaults only — immune to a developer's local .env / os.environ.
    for field, _env, default in EXPECTED:
        assert AgentSettings.model_fields[field].default == default, field


def test_agent_settings_field_set_is_exact():
    assert set(AgentSettings.model_fields) == {f for f, _e, _d in EXPECTED}


@pytest.mark.parametrize("field,env,default", EXPECTED)
def test_agent_settings_reads_legacy_env_var(monkeypatch, field, env, default):
    _clear(monkeypatch)
    raw, expected = ("123", 123) if isinstance(default, int) else (
        ("deepgram", "deepgram") if field == "speech_provider" else ("sentinel", "sentinel")
    )
    monkeypatch.setenv(env, raw)
    assert getattr(AgentSettings(), field) == expected
