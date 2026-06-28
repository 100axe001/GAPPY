from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.modules.datastore.domain.events import (
    DatastoreRecordEvent,
    DatastoreRecordOperation,
)
from app.modules.schedule.domain.schedule import ScheduleEntity, ScheduleType
from app.modules.schedule.services.datastore_event_handler import DatastoreEventHandler


@pytest.mark.asyncio
async def test_datastore_event_handler_processes_matching_triggers():
    repo = AsyncMock()
    processor = AsyncMock()

    schedule = ScheduleEntity(
        id=uuid4(),
        user_id=uuid4(),
        pod_id=uuid4(),
        schedule_type=ScheduleType.DATASTORE,
        config={"table_name": "users", "operations": ["INSERT"]},
    )
    repo.find_by_pod_table_event.return_value = [schedule]
    processor.process_event.return_value = True

    handler = DatastoreEventHandler(
        schedule_repository=repo,
        schedule_processor=processor,
    )

    event = DatastoreRecordEvent.create(
        pod_id=schedule.pod_id,
        table_name="users",
        record_id="rec_1",
        operation=DatastoreRecordOperation.INSERT,
        payload={"id": "rec_1"},
        actor_id=schedule.user_id,
    )

    result = await handler.handle_datastore_event(event)

    assert result == [schedule.id]
    processor.process_event.assert_called_once()


@pytest.mark.asyncio
async def test_datastore_event_handler_returns_empty_when_no_matches():
    repo = AsyncMock()
    processor = AsyncMock()
    repo.find_by_pod_table_event.return_value = []

    handler = DatastoreEventHandler(
        schedule_repository=repo,
        schedule_processor=processor,
    )

    event = DatastoreRecordEvent.create(
        pod_id=uuid4(),
        table_name="users",
        record_id="rec_1",
        operation=DatastoreRecordOperation.INSERT,
        payload={"id": "rec_1"},
        actor_id=uuid4(),
    )

    result = await handler.handle_datastore_event(event)

    assert result == []
    processor.process_event.assert_not_called()
