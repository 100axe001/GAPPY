"""Unit: a workload (agent/function) authorizes a pod file via the file alone
(grant cascade covers ancestor-folder grants), while a human still walks the
ancestor chain (RESTRICTED-folder visibility)."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.core.authorization.context import ActorType
from app.modules.datastore.domain.file_entities import (
    DatastoreFileEntity,
    FileKind,
    FileStatus,
)
from app.modules.datastore.services.files.authorizer import FileAuthorizer
from app.modules.datastore.services.files.path_resolver import PathResolver


def _file(pod_id, path: str) -> DatastoreFileEntity:
    return DatastoreFileEntity(
        id=uuid4(),
        pod_id=pod_id,
        owner_user_id=uuid4(),
        kind=FileKind.FILE,
        visibility="POD",
        path=path,
        name=path.rsplit("/", 1)[-1],
        description=None,
        mime_type="text/markdown",
        size_bytes=1,
        search_enabled=False,
        status=FileStatus.NOT_REQUIRED,
    )


def _folder(pod_id, path: str) -> DatastoreFileEntity:
    folder = _file(pod_id, path)
    folder.kind = FileKind.FOLDER
    return folder


@pytest.mark.asyncio
async def test_workload_authorizes_file_only_so_deep_folder_grant_works():
    pod_id = uuid4()
    user_id = uuid4()
    authz = AsyncMock()
    file_repo = AsyncMock()
    authorizer = FileAuthorizer(authz, file_repo, PathResolver())

    file_entity = _file(pod_id, "/docs/eng/runbooks/guide.md")
    ctx = SimpleNamespace(actor_type=ActorType.AGENT, user_id=user_id)
    await authorizer._ensure_pod_document_path_access(file_entity, user_id, ctx=ctx)

    # Exactly one check — the file itself. The grant cascade matches a grant on
    # /docs/eng/runbooks without a separate grant on /docs and /docs/eng.
    assert authz.require_document_read.await_count == 1
    _, kwargs = authz.require_document_read.await_args
    assert kwargs["resource_name"] == "/docs/eng/runbooks/guide.md"
    file_repo.get_by_paths.assert_not_awaited()


@pytest.mark.asyncio
async def test_human_still_walks_the_ancestor_chain():
    pod_id = uuid4()
    user_id = uuid4()
    authz = AsyncMock()
    file_repo = AsyncMock()
    file_repo.get_by_paths.return_value = [
        _folder(pod_id, "/docs"),
        _folder(pod_id, "/docs/eng"),
        _folder(pod_id, "/docs/eng/runbooks"),
    ]
    authorizer = FileAuthorizer(authz, file_repo, PathResolver())

    file_entity = _file(pod_id, "/docs/eng/runbooks/guide.md")
    ctx = SimpleNamespace(actor_type=ActorType.USER, user_id=user_id)
    await authorizer._ensure_pod_document_path_access(file_entity, user_id, ctx=ctx)

    # 3 ancestor folders + the file itself.
    assert authz.require_document_read.await_count == 4
