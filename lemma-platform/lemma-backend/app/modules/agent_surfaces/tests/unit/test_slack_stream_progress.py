from __future__ import annotations

import pytest
from slack_sdk.web.async_client import AsyncWebClient

from app.modules.agent_surfaces.domain.entities import (
    ConversationType,
    ParsedInboundSurfaceEvent,
)
from app.modules.agent_surfaces.platforms.slack.service import SlackPlatformService

pytestmark = pytest.mark.asyncio


def _event() -> ParsedInboundSurfaceEvent:
    return ParsedInboundSurfaceEvent(
        platform="SLACK",
        conversation_type=ConversationType.EXTERNAL_DM,
        external_channel_id="C1",
        external_thread_id="100.0",
        external_message_id="100.0",
        message_text="hi",
        reply_target={"channel": "C1", "thread_ts": "100.0"},
    )


async def test_slack_stream_progress_posts_updates_then_deletes(monkeypatch):
    posts: list[dict] = []
    updates: list[dict] = []
    deletes: list[dict] = []

    async def fake_post(self, **kwargs):
        posts.append(kwargs)
        return {"ok": True, "ts": "200.5", "channel": "C1"}

    async def fake_update(self, **kwargs):
        updates.append(kwargs)
        return {"ok": True}

    async def fake_delete(self, **kwargs):
        deletes.append(kwargs)
        return {"ok": True}

    monkeypatch.setattr(AsyncWebClient, "chat_postMessage", fake_post)
    monkeypatch.setattr(AsyncWebClient, "chat_update", fake_update)
    monkeypatch.setattr(AsyncWebClient, "chat_delete", fake_delete)

    svc = SlackPlatformService(credentials={"access_token": "xoxb-test"})
    event = _event()

    # First call posts a placeholder and returns its handle.
    handle = await svc.stream_progress(event, "Searching the web")
    assert handle == {"ts": "200.5", "channel": "C1"}
    assert posts and "⏳" in posts[0]["text"]
    assert posts[0]["thread_ts"] == "100.0"

    # Subsequent calls edit the same message in place (chat.update).
    handle2 = await svc.stream_progress(event, "Reading results", handle)
    assert handle2 == handle
    assert updates and updates[0]["ts"] == "200.5"
    assert "Reading results" in updates[0]["text"]

    # end_progress deletes the placeholder.
    await svc.end_progress(event, handle)
    assert deletes and deletes[0]["ts"] == "200.5"
