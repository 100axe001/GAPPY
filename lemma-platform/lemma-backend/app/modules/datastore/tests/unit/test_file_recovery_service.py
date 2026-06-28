from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.modules.datastore.domain.file_entities import FileStatus
from app.modules.datastore.services.file_recovery_service import (
    DatastoreFileRecoveryService,
)


@pytest.mark.asyncio
async def test_recover_stale_files_resets_processing_and_reenqueues_all():
    pending_file = SimpleNamespace(
        id=uuid4(),
        pod_id=uuid4(),
        metadata={"source": "pending"},
        status=FileStatus.PENDING,
    )
    processing_file = SimpleNamespace(
        id=uuid4(),
        pod_id=uuid4(),
        metadata={"source": "processing"},
        status=FileStatus.PROCESSING,
    )
    file_repository = AsyncMock()
    file_repository.list_stale_recovery_candidates.return_value = [
        pending_file,
        processing_file,
    ]
    file_repository.bulk_update_status.return_value = 1

    reindex_queue = AsyncMock()
    reindex_queue.enqueue = AsyncMock(side_effect=[True, False])
    uow = AsyncMock()

    service = DatastoreFileRecoveryService(
        file_repository=file_repository,
        reindex_queue=reindex_queue,
        uow=uow,
    )

    summary = await service.recover_stale_files(
        now=datetime(2026, 4, 9, 14, 0, tzinfo=timezone.utc)
    )

    assert summary.examined_count == 2
    assert summary.reset_count == 1
    assert summary.enqueued_count == 1
    file_repository.bulk_update_status.assert_awaited_once_with(
        file_ids=[processing_file.id],
        status=FileStatus.PENDING,
    )
    assert reindex_queue.enqueue.await_count == 2
    uow.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_recover_stale_files_resets_and_reenqueues_failed_files():
    failed_file = SimpleNamespace(
        id=uuid4(),
        pod_id=uuid4(),
        metadata={"source": "failed"},
        status=FileStatus.FAILED,
    )
    file_repository = AsyncMock()
    file_repository.list_stale_recovery_candidates.return_value = [failed_file]
    file_repository.bulk_update_status.return_value = 1
    reindex_queue = AsyncMock()
    reindex_queue.enqueue = AsyncMock(return_value=True)
    uow = AsyncMock()

    service = DatastoreFileRecoveryService(
        file_repository=file_repository,
        reindex_queue=reindex_queue,
        uow=uow,
    )

    summary = await service.recover_stale_files(
        now=datetime(2026, 4, 9, 14, 0, tzinfo=timezone.utc)
    )

    # FAILED files must be reset to PENDING and re-enqueued, and a failed_cutoff
    # must be passed to the candidate query.
    file_repository.bulk_update_status.assert_awaited_once_with(
        file_ids=[failed_file.id],
        status=FileStatus.PENDING,
    )
    call = file_repository.list_stale_recovery_candidates.await_args
    assert call.kwargs["failed_cutoff"] is not None
    assert summary.reset_count == 1
    assert summary.enqueued_count == 1
    uow.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_recover_stale_files_skips_commit_when_nothing_processing():
    pending_file = SimpleNamespace(
        id=uuid4(),
        pod_id=uuid4(),
        metadata={},
        status=FileStatus.PENDING,
    )
    file_repository = AsyncMock()
    file_repository.list_stale_recovery_candidates.return_value = [pending_file]
    reindex_queue = AsyncMock()
    reindex_queue.enqueue = AsyncMock(return_value=True)
    uow = AsyncMock()

    service = DatastoreFileRecoveryService(
        file_repository=file_repository,
        reindex_queue=reindex_queue,
        uow=uow,
    )

    summary = await service.recover_stale_files(
        now=datetime(2026, 4, 9, 14, 0, tzinfo=timezone.utc)
    )

    assert summary.reset_count == 0
    file_repository.bulk_update_status.assert_not_awaited()
    uow.commit.assert_not_awaited()
