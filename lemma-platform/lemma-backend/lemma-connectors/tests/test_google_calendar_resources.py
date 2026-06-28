from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lemma_connectors.google_calendar.resources.events import (
    EventsInsertInput,
    GoogleCalendarEventsResource,
)


class FakeGeneratedResult:
    def __init__(self, payload: dict):
        self._payload = payload

    def to_dict(self) -> dict:
        return self._payload


@dataclass
class FakeToolInput:
    fields: str | None = None
    calendar_id: str | None = None
    conference_data_version: int | None = None
    max_attendees: int | None = None
    send_notifications: bool | None = None
    send_updates: str | None = None
    supports_attachments: bool | None = None
    body: dict | None = None


class FakeInsertTool:
    input_type = FakeToolInput

    def __init__(self):
        self.seen = None

    async def execute(self, data):
        self.seen = data
        return FakeGeneratedResult({"id": "evt-1", "summary": "Standup"})


class FakeClient:
    def __init__(self, tool):
        self.tool = tool

    def get_tool(self, name: str):
        assert name == "calendar_events_insert"
        return self.tool


@pytest.mark.asyncio
async def test_events_insert_resource_operation_forwards_body():
    tool = FakeInsertTool()
    resource = GoogleCalendarEventsResource(FakeClient(tool))
    operations = resource.build_operations()

    result = await operations["events_insert"].execute(
        EventsInsertInput(
            calendar_id="primary",
            send_updates="all",
            body={"summary": "Standup"},
        )
    )

    assert result.id == "evt-1"
    assert tool.seen["calendar_id"] == "primary"
    assert tool.seen["body"] == {"summary": "Standup"}
