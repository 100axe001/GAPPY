"""Unit tests for RequestIdMiddleware (ASGI correlation-id stamping)."""

from app.app import RequestIdMiddleware


async def _run(inbound_headers):
    captured: dict = {}
    sent: list[dict] = []

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        sent.append(message)

    async def inner_app(scope, _receive, _send):
        captured["request_headers"] = scope.get("headers")
        await _send({"type": "http.response.start", "status": 200, "headers": []})
        await _send({"type": "http.response.body", "body": b""})

    middleware = RequestIdMiddleware(inner_app)
    scope = {"type": "http", "headers": list(inbound_headers)}
    await middleware(scope, receive, send)

    start = next(m for m in sent if m["type"] == "http.response.start")
    response_headers = dict(start["headers"])
    return captured, response_headers


async def test_mints_request_id_when_absent():
    captured, response_headers = await _run([])
    minted = response_headers.get(b"x-request-id")
    assert minted is not None and len(minted) > 0
    # Also injected into the request the inner app/authz sees.
    request_ids = [v for k, v in captured["request_headers"] if k == b"x-request-id"]
    assert request_ids == [minted]


async def test_reuses_inbound_request_id():
    _, response_headers = await _run([(b"x-request-id", b"abc123")])
    assert response_headers[b"x-request-id"] == b"abc123"


async def test_does_not_duplicate_when_inner_app_already_set_it():
    sent: list[dict] = []

    async def receive():
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message):
        sent.append(message)

    async def inner_app(scope, _receive, _send):
        await _send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"x-request-id", b"inner")],
            }
        )

    middleware = RequestIdMiddleware(inner_app)
    await middleware({"type": "http", "headers": [(b"x-request-id", b"inner")]}, receive, send)

    start = next(m for m in sent if m["type"] == "http.response.start")
    ids = [v for k, v in start["headers"] if k == b"x-request-id"]
    assert ids == [b"inner"]  # exactly one, no duplicate
