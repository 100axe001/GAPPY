from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lemma_connectors.core.auth import OAuth2Credentials
from lemma_connectors.core.errors import IntegrationExecutionError
from lemma_connectors.gmail.client import GmailClient
from lemma_connectors.gmail.generated.pydantic_models import Message, MessagePartBody


def test_gmail_message_models_accept_base64url_fields_as_strings():
    body = MessagePartBody.model_validate(
        {"data": "SGVsbG8td29ybGRf", "size": 12}
    )
    message = Message.model_validate(
        {
            "id": "msg-1",
            "raw": "U3ViamVjdDogSGkKClRlc3Q",
            "payload": {"body": {"data": "VGVzdF9ib2R5", "size": 9}},
        }
    )

    assert body.data == "SGVsbG8td29ybGRf"
    assert message.raw == "U3ViamVjdDogSGkKClRlc3Q"
    assert message.payload is not None
    assert message.payload.body is not None
    assert message.payload.body.data == "VGVzdF9ib2R5"


@pytest.mark.asyncio
async def test_gmail_messages_get_tool_maps_format_field_to_generated_param():
    client = GmailClient(credentials=OAuth2Credentials(access_token="token"))
    tool = client.get_tool("gmail_users_messages_get")
    captured: dict[str, object] = {}

    async def fake_async_detailed(*, client, user_id, id, format_, metadata_headers=None, **kwargs):
        captured.update(
            {
                "user_id": user_id,
                "id": id,
                "format_": format_,
                "metadata_headers": metadata_headers,
            }
        )
        # execute() prefers the *_detailed executor so it can inspect the HTTP
        # status; return a 200 Response-like object carrying the parsed body.
        return SimpleNamespace(
            status_code=200,
            content=b"",
            parsed={"id": id, "labelIds": ["INBOX"], "snippet": "hello"},
        )

    tool._async_detailed_function = fake_async_detailed

    result = await tool.execute(
        {
            "user_id": "me",
            "id": "msg-1",
            "format": "metadata",
            "metadata_headers": ["From", "Subject"],
        }
    )

    assert captured["user_id"] == "me"
    assert captured["id"] == "msg-1"
    assert captured["format_"] == "metadata"
    assert captured["metadata_headers"] == ["From", "Subject"]
    assert result.id == "msg-1"


@pytest.mark.asyncio
async def test_execute_surfaces_upstream_http_error_clearly():
    """A non-2xx upstream response must raise a clear error with the provider's
    message — not a cryptic 'Input should be a valid dictionary ... NoneType'
    from validating a None body."""
    client = GmailClient(credentials=OAuth2Credentials(access_token="token"))
    tool = client.get_tool("gmail_users_messages_get")

    async def fake_async_detailed(*, client, **kwargs):
        return SimpleNamespace(
            status_code=400,
            content=b'{"error": {"code": 400, "message": "Invalid id value"}}',
            parsed=None,
        )

    tool._async_detailed_function = fake_async_detailed

    with pytest.raises(IntegrationExecutionError) as exc_info:
        await tool.execute({"user_id": "me", "id": "bad", "format": "full"})

    message = str(exc_info.value)
    assert "HTTP 400" in message
    assert "Invalid id value" in message
    assert "NoneType" not in message
