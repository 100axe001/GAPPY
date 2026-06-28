from __future__ import annotations

from pydantic import BaseModel, Field

from app.modules.agent_surfaces.platforms.common import SurfaceFileAttachment


class WhatsAppToolResult(BaseModel):
    success: bool = False
    error: str | None = None
    message: str | None = None
    guidance: str | None = None


class WhatsAppFileAttachment(SurfaceFileAttachment):
    pass


class WhatsAppCurrentContactParams(BaseModel):
    pass


class WhatsAppCurrentContactResult(WhatsAppToolResult):
    wa_id: str | None = None
    display_name: str | None = None
    phone_number_id: str | None = None
    waba_id: str | None = None
    attachment_names: list[str] = Field(default_factory=list)
