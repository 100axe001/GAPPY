"""Shared fixtures for workflow engine unit tests.

These tests exercise engine orchestration against mocked repositories and a
mocked UoW session. The engine's `_require_action` builds a real
`AuthorizationDataService` from `uow.session`, which would issue DB queries
against the mock. Authorization behavior is covered separately by
`test_flow_authz.py` and the e2e suite, so here we neutralize the permission
check and let the orchestration logic be the subject under test.
"""

from __future__ import annotations

import pytest


class _AllowAllContext:
    """Stand-in authorization context that permits every action."""

    async def require(self, *args, **kwargs) -> None:
        return None

    async def can(self, *args, **kwargs) -> bool:
        return True


class _AllowAllAuthzService:
    def __init__(self, *args, **kwargs) -> None:
        pass

    async def build_user_context(self, *args, **kwargs) -> _AllowAllContext:
        return _AllowAllContext()


@pytest.fixture(autouse=True)
def _bypass_workflow_authz(monkeypatch):
    monkeypatch.setattr(
        "app.modules.workflow.execution.engine.AuthorizationDataService",
        _AllowAllAuthzService,
    )
