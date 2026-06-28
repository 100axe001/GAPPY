"""Round-2: default-server bootstrap, daemon wss derivation, session selection."""

from __future__ import annotations

from pathlib import Path

from lemma_sdk.config import DEFAULT_AUTH_URL, DEFAULT_BASE_URL, load_config

from lemma_cli.daemon.config import daemon_ws_url
from lemma_cli.cli_core.context import render_session_selection
from lemma_cli.cli_core.state import CliState


def _state(output: str = "pretty") -> CliState:
    return CliState(
        config_path=Path("/tmp/none.json"),
        config={},
        base_url=None,
        auth_url=None,
        token=None,
        timeout=30.0,
        no_verify_ssl=False,
        output=output,
    )


def test_fresh_config_seeds_and_selects_cloud_server(tmp_path):
    cfg = load_config(tmp_path / "does-not-exist.json")
    assert cfg["active_server"] == "default"
    default = cfg["servers"]["default"]
    assert default["base_url"] == DEFAULT_BASE_URL == "https://api.lemma.work"
    assert default["auth_url"] == DEFAULT_AUTH_URL == "https://lemma.work/auth"


def test_daemon_ws_url_scheme_derivation():
    assert daemon_ws_url("https://api.lemma.work") == (
        "wss://api.lemma.work/me/agent-runtime/daemon/ws"
    )
    assert daemon_ws_url("http://localhost:8711/") == (
        "ws://localhost:8711/me/agent-runtime/daemon/ws"
    )
    # Bare host (no scheme) assumes TLS.
    assert daemon_ws_url("api.lemma.work").startswith("wss://api.lemma.work/")


def test_session_selection_export_mode_emits_eval_safe_lines(capsys):
    render_session_selection(
        _state(),
        env={"LEMMA_POD_ID": "pod-1", "LEMMA_ORG_ID": "org-1"},
        label="pod",
        name="linear-pm",
        command_hint="lemma pods select linear-pm",
        export_only=True,
        saved=False,
    )
    out = capsys.readouterr().out.strip().splitlines()
    # Export mode prints ONLY plain `export …` lines (so `eval "$(...)"` is safe).
    assert out == ['export LEMMA_POD_ID=pod-1', 'export LEMMA_ORG_ID=org-1']


def test_session_selection_human_mode_shows_session_hint(capsys):
    render_session_selection(
        _state(),
        env={"LEMMA_POD_ID": "pod-1"},
        label="pod",
        name="linear-pm",
        command_hint="lemma pods select linear-pm",
        export_only=False,
        saved=False,
    )
    out = capsys.readouterr().out
    assert "this shell only" in out
    assert 'eval "$(lemma pods select linear-pm -x)"' in out


def test_humanize_error_unwraps_422_field_errors():
    from lemma_sdk.errors import api_error

    from lemma_cli.cli_core.state import humanize_error

    err = api_error(
        422,
        "Validation error",
        details=[
            {
                "loc": ["body", "column"],
                "msg": "ENUM columns must define options",
                "type": "value_error",
            }
        ],
    )
    out = humanize_error(err)
    assert "Validation error" in out
    assert "column: ENUM columns must define options" in out
    assert "loc" not in out  # no raw {'loc': ...} dict dump
