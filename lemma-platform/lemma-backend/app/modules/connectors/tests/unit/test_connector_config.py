"""Golden test for connector config: env-var names + defaults preserved."""

from __future__ import annotations

import pytest

from app.modules.connectors.config import ConnectorSettings

pytestmark = pytest.mark.unit

EXPECTED = [
    ("composio_api_key", "COMPOSIO_API_KEY", None),
    ("composio_webhook_secret", "COMPOSIO_WEBHOOK_SECRET", None),
    ("connector_operation_timeout_seconds", "CONNECTOR_OPERATION_TIMEOUT_SECONDS", 45.0),
    ("connector_encryption_key", "CONNECTOR_ENCRYPTION_KEY", None),
]


def _clear(monkeypatch):
    for _, env, _default in EXPECTED:
        monkeypatch.delenv(env, raising=False)


def test_connector_settings_defaults():
    # Declared defaults only — immune to a developer's local .env / os.environ.
    for field, _env, default in EXPECTED:
        assert ConnectorSettings.model_fields[field].default == default, field


def test_connector_settings_field_set_is_exact():
    assert set(ConnectorSettings.model_fields) == {f for f, _e, _d in EXPECTED}


@pytest.mark.parametrize("field,env,_default", EXPECTED)
def test_connector_settings_reads_legacy_env_var(monkeypatch, field, env, _default):
    _clear(monkeypatch)
    monkeypatch.setenv(env, "5" if "timeout" in field else "sentinel")
    value = getattr(ConnectorSettings(), field)
    assert value == (5.0 if "timeout" in field else "sentinel")
