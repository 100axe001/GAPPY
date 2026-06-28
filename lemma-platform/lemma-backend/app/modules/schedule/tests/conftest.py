import json
from pathlib import Path

import pytest


def _load_json_or_default(path: Path, default: dict) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return default


@pytest.fixture
def slack_public_channel_event() -> dict:
    root = Path(__file__).resolve().parents[4]
    fixture_path = root / "exp" / "slack_events" / "public_channel.json"
    return _load_json_or_default(
        fixture_path,
        {
            "source": "slack",
            "payload": {
                "team_id": "T0784N82P17",
                "event": {
                    "type": "message",
                    "channel": "C123",
                    "channel_type": "channel",
                    "ts": "1766236791.639079",
                    "user": "U123",
                    "text": "hello",
                },
            },
        },
    )


@pytest.fixture
def slack_user_dm_event() -> dict:
    root = Path(__file__).resolve().parents[4]
    fixture_path = root / "exp" / "slack_events" / "user_dm.json"
    return _load_json_or_default(
        fixture_path,
        {
            "source": "slack",
            "payload": {
                "team_id": "T0784N82P17",
                "event": {
                    "type": "message",
                    "channel": "D123",
                    "channel_type": "im",
                    "ts": "1766236791.639079",
                    "thread_ts": "1766236791.639079",
                    "user": "U123",
                    "text": "hello",
                },
            },
        },
    )


@pytest.fixture
def composio_gmail_event() -> dict:
    root = Path(__file__).resolve().parents[4]
    fixture_path = root / "exp" / "composio.json"
    return _load_json_or_default(
        fixture_path,
        {
            "type": "GMAIL_NEW_EMAIL",
            "data": {
                "trigger_nano_id": "ti_fixture_123",
                "thread_id": "thread_fixture_123",
            },
        },
    )
