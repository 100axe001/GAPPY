from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.modules.connectors.domain.connector import AuthProvider
from app.modules.connectors.domain.connector_trigger import ConnectorTriggerEntity
from app.modules.connectors.domain.errors import ConnectorTriggerNotFoundError
from app.modules.connectors.services.trigger_service import ConnectorTriggerService

pytestmark = pytest.mark.asyncio


def _service(*, trigger_repository, provider=AuthProvider.COMPOSIO, connector_id="slack"):
    connector_service = AsyncMock()
    connector_service.get_auth_config_by_name = AsyncMock(
        return_value=SimpleNamespace(
            id=uuid4(),
            provider=provider,
            connector_id=connector_id,
        )
    )
    return ConnectorTriggerService(
        trigger_repository=trigger_repository,
        connector_repository=AsyncMock(),
        connector_service=connector_service,
    )


def _trigger(provider: AuthProvider, connector_id: str = "slack") -> ConnectorTriggerEntity:
    return ConnectorTriggerEntity(
        id=f"{connector_id}:{provider.value.lower()}:new_message",
        connector_id=connector_id,
        provider=provider,
        event_type="new_message",
        description="New message",
        config_schema={"type": "object"},
    )


async def test_list_triggers_for_auth_config_passes_provider_to_repo():
    trigger_repository = AsyncMock()
    trigger_repository.list_by_connector_provider.return_value = [
        _trigger(AuthProvider.COMPOSIO)
    ]
    service = _service(trigger_repository=trigger_repository, provider=AuthProvider.COMPOSIO)

    triggers = await service.list_triggers_for_auth_config(
        user_id=uuid4(),
        organization_id=uuid4(),
        auth_config_name="slack-composio",
        search_query="msg",
        limit=25,
    )

    assert [t.provider for t in triggers] == [AuthProvider.COMPOSIO]
    trigger_repository.list_by_connector_provider.assert_awaited_once_with(
        "slack",
        "COMPOSIO",
        search_query="msg",
        limit=25,
    )


async def test_get_trigger_for_auth_config_uses_provider_lookup():
    trigger_repository = AsyncMock()
    trigger_repository.get_by_connector_provider_and_name.return_value = _trigger(
        AuthProvider.LEMMA
    )
    service = _service(trigger_repository=trigger_repository, provider=AuthProvider.LEMMA)

    trigger = await service.get_trigger_for_auth_config(
        user_id=uuid4(),
        organization_id=uuid4(),
        auth_config_name="slack-lemma",
        trigger_name="new_message",
    )

    assert trigger.provider == AuthProvider.LEMMA
    trigger_repository.get_by_connector_provider_and_name.assert_awaited_once_with(
        "slack",
        "LEMMA",
        "new_message",
    )


async def test_get_trigger_for_auth_config_raises_when_missing():
    trigger_repository = AsyncMock()
    trigger_repository.get_by_connector_provider_and_name.return_value = None
    service = _service(trigger_repository=trigger_repository)

    with pytest.raises(ConnectorTriggerNotFoundError):
        await service.get_trigger_for_auth_config(
            user_id=uuid4(),
            organization_id=uuid4(),
            auth_config_name="slack-composio",
            trigger_name="missing",
        )
