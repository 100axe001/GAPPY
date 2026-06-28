"""Tests for daemon transport resiliency: reconnect + send guard."""

from __future__ import annotations

import asyncio
import json

import pytest

from lemma_cli.daemon import runner


def test_reconnect_delay_is_bounded():
    for attempt in range(8):
        delay = runner.reconnect_delay_seconds(attempt)
        assert 0.0 <= delay <= runner._RECONNECT_MAX_DELAY_SECONDS
    # First attempt is capped at the base delay.
    assert runner.reconnect_delay_seconds(0) <= runner._RECONNECT_BASE_DELAY_SECONDS


def test_ssl_for_plain_ws_is_none():
    # ws:// has no TLS; websockets only accepts ssl=None for it.
    assert runner.ssl_for_ws_url("ws://example/daemon", verify_ssl=True) is None
    assert runner.ssl_for_ws_url("ws://example/daemon", verify_ssl=False) is None


def test_ssl_for_wss_with_verify_is_true_not_none():
    # Regression: a verified wss:// connection must NOT pass ssl=None, which
    # websockets rejects with "ssl=None is incompatible with a wss:// URI".
    result = runner.ssl_for_ws_url("wss://api.lemma.work/daemon", verify_ssl=True)
    assert result is True


def test_ssl_for_wss_without_verify_is_unverified_context():
    import ssl as ssl_module

    context = runner.ssl_for_ws_url("wss://api.lemma.work/daemon", verify_ssl=False)
    # Must be an SSLContext (not False, which asyncio treats as plaintext on a
    # TLS port) with verification disabled.
    assert isinstance(context, ssl_module.SSLContext)
    assert context.check_hostname is False
    assert context.verify_mode == ssl_module.CERT_NONE


class _FakeWS:
    def __init__(self, incoming=None):
        self.sent: list[str] = []
        self._incoming = list(incoming or [])
        self.send_should_fail = False

    async def send(self, data):
        if self.send_should_fail:
            raise ConnectionError("socket closed")
        self.sent.append(data)

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._incoming:
            return self._incoming.pop(0)
        raise StopAsyncIteration


class _FakeConn:
    def __init__(self, ws):
        self._ws = ws

    async def __aenter__(self):
        return self._ws

    async def __aexit__(self, *_a):
        return False


@pytest.mark.asyncio
async def test_send_json_swallows_send_failure():
    ws = _FakeWS()
    ws.send_should_fail = True
    # Must not raise even though the underlying socket send fails.
    await runner._send_json(ws, {"type": "run.event"})


@pytest.mark.asyncio
async def test_send_run_event_is_guarded():
    ws = _FakeWS()
    ws.send_should_fail = True
    await runner.send_run_event(ws, "run-1", "token", "hi")  # must not raise


@pytest.mark.asyncio
async def test_send_json_reraises_cancellation():
    class _CancelWS:
        async def send(self, _data):
            raise asyncio.CancelledError()

    with pytest.raises(asyncio.CancelledError):
        await runner._send_json(_CancelWS(), {"type": "x"})


@pytest.mark.asyncio
async def test_run_daemon_reconnects_after_drop(monkeypatch):
    # Avoid real config/discovery/sleep.
    monkeypatch.setattr(
        runner, "ensure_config", lambda: {"device_key": "k", "display_name": "t"}
    )
    monkeypatch.setattr(runner, "discover_harness_catalog", lambda: {})
    monkeypatch.setattr(runner, "save_config", lambda _c: None)
    monkeypatch.setattr(runner, "device_info", lambda: {})
    monkeypatch.setattr(runner, "daemon_ws_url", lambda _b: "ws://example/daemon")
    monkeypatch.setattr(runner, "reconnect_delay_seconds", lambda _a: 0.0)

    connections: list[_FakeWS] = []

    def connect_factory(_token):
        # Each connection immediately receives a ready-ack then closes (iter ends),
        # which makes run_daemon reconnect.
        ws = _FakeWS(
            incoming=[json.dumps({"type": "daemon.ready_ack", "daemon_id": "d1"})]
        )
        connections.append(ws)
        return _FakeConn(ws)

    await runner.run_daemon(
        base_url="http://example",
        token="tok",
        verify_ssl=True,
        connect_factory=connect_factory,
        max_reconnect_attempts=1,
    )

    # Initial connect + exactly one reconnect, then it gives up (bounded by test).
    assert len(connections) == 2
    # The ready handshake was sent on every connection.
    for ws in connections:
        assert any('"daemon.ready"' in message for message in ws.sent)


@pytest.mark.asyncio
async def test_run_daemon_uses_token_provider_on_each_connect(monkeypatch):
    monkeypatch.setattr(
        runner, "ensure_config", lambda: {"device_key": "k", "display_name": "t"}
    )
    monkeypatch.setattr(runner, "discover_harness_catalog", lambda: {})
    monkeypatch.setattr(runner, "save_config", lambda _c: None)
    monkeypatch.setattr(runner, "device_info", lambda: {})
    monkeypatch.setattr(runner, "daemon_ws_url", lambda _b: "ws://example/daemon")
    monkeypatch.setattr(runner, "reconnect_delay_seconds", lambda _a: 0.0)

    tokens_used: list[str] = []
    counter = {"n": 0}

    def token_provider() -> str:
        counter["n"] += 1
        return f"token-{counter['n']}"

    def connect_factory(token):
        tokens_used.append(token)
        return _FakeConn(_FakeWS(incoming=[]))

    await runner.run_daemon(
        base_url="http://example",
        token="unused",
        verify_ssl=True,
        token_provider=token_provider,
        connect_factory=connect_factory,
        max_reconnect_attempts=1,
    )

    assert tokens_used == ["token-1", "token-2"]


class _Resp:
    def __init__(self, status, text=""):
        self.status_code = status
        self.text = text

    def json(self):
        return json.loads(self.text) if self.text else None


@pytest.mark.asyncio
async def test_opencode_get_retries_on_5xx(monkeypatch):
    from lemma_cli.daemon.harnesses import opencode

    monkeypatch.setattr(opencode, "_OPENCODE_GET_RETRY_BASE_DELAY", 0.0)

    calls = {"n": 0}

    class _Client:
        async def request(self, method, url, json=None):
            calls["n"] += 1
            if calls["n"] == 1:
                return _Resp(503, "busy")
            return _Resp(200, '{"ok": true}')

    result = await opencode._opencode_request(
        _Client(), "GET", "http://x", "/status", params={}
    )
    assert calls["n"] == 2  # retried once after the 5xx
    assert result == {"ok": True}


@pytest.mark.asyncio
async def test_opencode_post_does_not_retry(monkeypatch):
    from lemma_cli.daemon.harnesses import opencode

    monkeypatch.setattr(opencode, "_OPENCODE_GET_RETRY_BASE_DELAY", 0.0)

    calls = {"n": 0}

    class _Client:
        async def request(self, method, url, json=None):
            calls["n"] += 1
            return _Resp(503, "busy")

    with pytest.raises(RuntimeError):
        await opencode._opencode_request(
            _Client(), "POST", "http://x", "/session", params={}
        )
    assert calls["n"] == 1  # POSTs are never auto-retried
