from __future__ import annotations

from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.modules.agent_surfaces.config import surface_settings
from app.modules.agent.domain.entities import Conversation
from app.modules.agent_surfaces.domain.entities import (
    SurfacePlatform,
    AgentSurfaceEntity,
    SurfaceConfig,
)
from app.modules.agent_surfaces.services.credential_resolver import (
    SurfaceCredentialResolver,
)
from app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory import (
    SurfacePlatformToolFactory,
)


class _FakeUoW:
    def __init__(self) -> None:
        self.session = AsyncMock()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return None


def _conversation_for_surface(surface: AgentSurfaceEntity) -> Conversation:
    return Conversation(
        id=uuid4(),
        pod_id=surface.pod_id,
        agent_id=surface.agent_id,
        user_id=uuid4(),
        title="external surface chat",
        metadata={
            "source": "agent_surfaces",
            "surface_id": str(surface.id),
            "surface_platform": surface.surface_type.value,
        },
    )


@pytest.mark.asyncio
async def test_platform_tool_factory_uses_native_whatsapp_credentials(
    monkeypatch,
):
    surface = AgentSurfaceEntity.create(
        surface_type=SurfacePlatform.WHATSAPP,
        pod_id=uuid4(),
        agent_id=uuid4(),
        config=SurfaceConfig(),
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    async def fake_get(self, surface_id):
        assert surface_id == surface.id
        return surface

    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.SurfaceRepository.get",
        fake_get,
    )
    monkeypatch.setattr(surface_settings, "whatsapp_access_token", "native-wa-token")
    monkeypatch.setattr(surface_settings, "whatsapp_phone_number_id", "phone-123")
    monkeypatch.setattr(surface_settings, "whatsapp_waba_id", "waba-123")

    toolsets = await factory.build_toolsets(
        conversation=_conversation_for_surface(surface)
    )

    assert len(toolsets) == 1
    assert "whatsapp_get_current_contact" in toolsets[0].tools
    assert "whatsapp_send_file" not in toolsets[0].tools


@pytest.mark.asyncio
async def test_platform_tool_factory_uses_native_telegram_env_credentials(
    monkeypatch,
):
    surface = AgentSurfaceEntity.create(
        surface_type=SurfacePlatform.TELEGRAM,
        pod_id=uuid4(),
        agent_id=uuid4(),
        config=SurfaceConfig(),
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    async def fake_get(self, surface_id):
        assert surface_id == surface.id
        return surface

    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.SurfaceRepository.get",
        fake_get,
    )
    monkeypatch.setattr(surface_settings, "telegram_bot_token", "native-telegram-token")

    toolsets = await factory.build_toolsets(
        conversation=_conversation_for_surface(surface)
    )

    assert len(toolsets) == 1
    assert "telegram_get_current_chat" in toolsets[0].tools
    assert "telegram_send_file" not in toolsets[0].tools


@pytest.mark.asyncio
async def test_platform_tool_factory_adds_native_whatsapp_tools_for_default_agent_conversation(
    monkeypatch,
):
    conversation = Conversation(
        id=uuid4(),
        pod_id=uuid4(),
        agent_id=None,
        user_id=uuid4(),
        title="default agent whatsapp chat",
        metadata={"source": "agent_surfaces", "surface_platform": "WHATSAPP"},
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    monkeypatch.setattr(surface_settings, "whatsapp_access_token", "native-wa-token")
    monkeypatch.setattr(surface_settings, "whatsapp_phone_number_id", "phone-123")
    monkeypatch.setattr(surface_settings, "whatsapp_waba_id", "waba-123")

    toolsets = await factory.build_toolsets(conversation=conversation)

    assert len(toolsets) == 1
    assert "whatsapp_get_current_contact" in toolsets[0].tools
    assert "whatsapp_send_file" not in toolsets[0].tools


@pytest.mark.asyncio
async def test_platform_tool_factory_adds_native_telegram_tools_for_default_agent_conversation(
    monkeypatch,
):
    conversation = Conversation(
        id=uuid4(),
        pod_id=uuid4(),
        agent_id=None,
        user_id=uuid4(),
        title="default agent telegram chat",
        metadata={"source": "agent_surfaces", "surface_platform": "TELEGRAM"},
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    monkeypatch.setattr(surface_settings, "telegram_bot_token", "native-telegram-token")

    toolsets = await factory.build_toolsets(conversation=conversation)

    assert len(toolsets) == 1
    assert "telegram_get_current_chat" in toolsets[0].tools
    assert "telegram_send_file" not in toolsets[0].tools


@pytest.mark.asyncio
async def test_platform_tool_factory_adds_gmail_tools_for_surface_conversation(
    monkeypatch,
):
    account_id = uuid4()
    surface = AgentSurfaceEntity.create(
        surface_type=SurfacePlatform.GMAIL,
        pod_id=uuid4(),
        agent_id=uuid4(),
        account_id=account_id,
        config=SurfaceConfig(),
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    async def fake_get(self, surface_id):
        assert surface_id == surface.id
        return surface

    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.SurfaceRepository.get",
        fake_get,
    )
    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.get_connector_service",
        lambda uow: AsyncMock(),
    )
    monkeypatch.setattr(
        SurfaceCredentialResolver,
        "for_surface",
        AsyncMock(return_value={"access_token": "gmail-token"}),
    )

    toolsets = await factory.build_toolsets(conversation=_conversation_for_surface(surface))

    assert len(toolsets) == 1
    assert "gmail_reply_email" in toolsets[0].tools
    assert "gmail_download_attachment" not in toolsets[0].tools


@pytest.mark.asyncio
async def test_platform_tool_factory_adds_outlook_tools_for_surface_conversation(
    monkeypatch,
):
    account_id = uuid4()
    surface = AgentSurfaceEntity.create(
        surface_type=SurfacePlatform.OUTLOOK,
        pod_id=uuid4(),
        agent_id=uuid4(),
        account_id=account_id,
        config=SurfaceConfig(),
    )
    factory = SurfacePlatformToolFactory(uow_factory=lambda: _FakeUoW())

    async def fake_get(self, surface_id):
        assert surface_id == surface.id
        return surface

    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.SurfaceRepository.get",
        fake_get,
    )
    monkeypatch.setattr(
        "app.modules.agent_surfaces.infrastructure.adapters.platform_tool_factory.get_connector_service",
        lambda uow: AsyncMock(),
    )
    monkeypatch.setattr(
        SurfaceCredentialResolver,
        "for_surface",
        AsyncMock(return_value={"access_token": "outlook-token"}),
    )

    toolsets = await factory.build_toolsets(conversation=_conversation_for_surface(surface))

    assert len(toolsets) == 1
    assert "outlook_reply_email" in toolsets[0].tools
    assert "outlook_download_attachment" not in toolsets[0].tools
