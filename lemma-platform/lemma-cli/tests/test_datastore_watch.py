"""Unit tests for `lemma datastore watch` helpers (URL, cursor, rendering)."""

from __future__ import annotations

import json
from pathlib import Path

from lemma_cli.cli_core.state import CliState
from lemma_cli.cli_core.watch import (
    _changes_ws_url,
    _compact_payload,
    _handle_message,
    _short_time,
)


def _state(output: str = "json") -> CliState:
    return CliState(
        config_path=Path("/tmp/lemma-test-config.json"),
        config={},
        base_url="https://api.example.test",
        auth_url=None,
        token="tok",
        timeout=5.0,
        no_verify_ssl=False,
        output=output,
    )


def test_changes_ws_url_scheme_and_query():
    assert (
        _changes_ws_url("https://api.x.dev", "POD", "notes", "5-0")
        == "wss://api.x.dev/pods/POD/datastore/changes?table=notes&since=5-0"
    )
    assert (
        _changes_ws_url("http://localhost:8711/", "POD", None, None)
        == "ws://localhost:8711/pods/POD/datastore/changes"
    )
    # Bare host (no scheme) assumes TLS, like a browser.
    assert (
        _changes_ws_url("//host", "POD", None, "9-0")
        == "wss://host/pods/POD/datastore/changes?since=9-0"
    )


def test_ready_frame_advances_cursor_from_since():
    state = _state()
    cursor = _handle_message(state, json.dumps({"type": "ready", "since": "7-0"}), None)
    assert cursor == "7-0"


def test_record_frame_advances_cursor_from_stream_id_and_prints_ndjson(capsys):
    state = _state(output="json")
    frame = {
        "type": "datastore.record.insert",
        "table_name": "notes",
        "record_id": "abc",
        "operation": "insert",
        "payload": {"body": "hi"},
        "stream_id": "12-0",
    }
    cursor = _handle_message(state, json.dumps(frame), "7-0")
    assert cursor == "12-0"
    out = capsys.readouterr().out.strip()
    assert json.loads(out) == frame


def test_invalid_or_unknown_messages_keep_cursor():
    state = _state()
    assert _handle_message(state, "not json", "3-0") == "3-0"
    assert _handle_message(state, json.dumps([1, 2]), "3-0") == "3-0"


def test_compact_payload_and_short_time():
    assert _compact_payload({"body": "hi", "n": 3}, full=False) == "body=hi, n=3"
    assert _compact_payload({}, full=False) == ""
    long = _compact_payload({"k": "x" * 200}, full=False)
    assert long.endswith("…") and len(long) <= 120
    assert _short_time("2026-06-21T18:49:01.309492Z") == "18:49:01"
    assert _short_time(None) == ""
