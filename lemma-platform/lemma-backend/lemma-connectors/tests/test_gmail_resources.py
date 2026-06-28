from __future__ import annotations

import base64
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lemma_connectors.gmail.resources.messages import (
    GmailMessagesResource,
    MessagesSendInput,
)


class FakeGeneratedResult:
    def __init__(self, payload: dict):
        self._payload = payload

    def to_dict(self) -> dict:
        return self._payload


@dataclass
class FakeToolInput:
    fields: str | None = None
    user_id: str | None = None
    body: dict | None = None


class FakeSendTool:
    input_type = FakeToolInput

    def __init__(self):
        self.seen = None

    async def execute(self, data):
        self.seen = data
        return FakeGeneratedResult(
            {
                "id": "msg-123",
                "threadId": "thread-1",
                "labelIds": ["SENT"],
            }
        )


class FakeClient:
    def __init__(self, tool):
        self.tool = tool

    def get_tool(self, name: str):
        assert name == "gmail_users_messages_send"
        return self.tool


@pytest.mark.asyncio
async def test_send_resource_operation_builds_raw_message_payload():
    tool = FakeSendTool()
    resource = GmailMessagesResource(FakeClient(tool))
    operations = resource.build_operations()

    result = await operations["messages_send"].execute(
        MessagesSendInput(
            user_id="me",
            body={
                "raw": base64.urlsafe_b64encode(b"Subject: Hello\n\nHi").decode("utf-8"),
            },
        )
    )

    assert result.id == "msg-123"
    assert tool.seen["user_id"] == "me"
    assert "raw" in tool.seen["body"]
