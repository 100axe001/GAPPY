from __future__ import annotations

from pydantic import BaseModel, Field

from app.modules.agent_surfaces.platforms.common import SurfaceFileAttachment


class TelegramToolResult(BaseModel):
    success: bool = False
    error: str | None = None
    message: str | None = None


class TelegramFileAttachment(SurfaceFileAttachment):
    file_id: str | None = None


class TelegramCurrentChatParams(BaseModel):
    pass


class TelegramCurrentChatResult(TelegramToolResult):
    chat_id: str | None = None
    chat_type: str | None = None
    message_thread_id: str | None = None
    is_topic_message: bool = False
    attachment_names: list[str] = Field(default_factory=list)
