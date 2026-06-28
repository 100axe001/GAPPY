"""Telegram surface adapter."""

from __future__ import annotations

from typing import Any

from app.modules.agent_surfaces.domain.entities import ParsedInboundSurfaceEvent
from app.modules.agent_surfaces.domain.models import (
    SurfaceContextMessage,
    SurfaceDisplayRenderPlan,
    SurfaceSenderProfile,
)
from app.modules.agent_surfaces.platforms.base import BaseSurfaceAdapter
from app.modules.agent_surfaces.platforms.telegram.parser import TelegramMessageParser
from app.modules.agent_surfaces.platforms.telegram.service import (
    TelegramPlatformService,
)

_CONTACT_REQUEST_MARKUP = {
    "keyboard": [
        [
            {
                "text": "Share my phone number",
                "request_contact": True,
            }
        ]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True,
}


class TelegramSurfaceAdapter(BaseSurfaceAdapter):
    platform = "TELEGRAM"

    def __init__(self) -> None:
        self._parser = TelegramMessageParser()

    async def parse_inbound_event(
        self, payload: dict[str, Any], headers: dict[str, str] | None = None
    ) -> ParsedInboundSurfaceEvent | None:
        return self._parser.parse(payload, headers)

    async def fetch_sender_profile(
        self, *, credentials: dict[str, Any], event: ParsedInboundSurfaceEvent
    ) -> SurfaceSenderProfile | None:
        return await TelegramPlatformService(credentials).fetch_sender_profile(event)

    async def send_message(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        message: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        await TelegramPlatformService(credentials).send_message(
            event, message, metadata
        )

    async def send_display_resource(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        render_plan: SurfaceDisplayRenderPlan,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        await TelegramPlatformService(credentials).send_display_resource(
            event,
            render_plan,
            metadata,
        )

    async def add_processing_indicator(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        await TelegramPlatformService(credentials).add_processing_indicator(
            event, metadata
        )

    async def stream_progress(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        progress_text: str,
        progress_handle: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        return await TelegramPlatformService(credentials).stream_progress(
            event, progress_text, progress_handle
        )

    async def end_progress(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        progress_handle: dict[str, Any] | None = None,
    ) -> None:
        await TelegramPlatformService(credentials).end_progress(event, progress_handle)

    async def download_attachment(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        attachment: dict[str, Any],
    ) -> tuple[bytes, str, str] | None:
        return await TelegramPlatformService(credentials).download_attachment_bytes(
            event, attachment
        )

    async def fetch_thread_context(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        limit: int = 15,
    ) -> list[SurfaceContextMessage]:
        # Telegram bots cannot read group history; the only context available is
        # the message this one replies to (delivered inline in the update).
        del credentials, limit
        message = (event.raw_payload or {}).get("message") or {}
        reply = message.get("reply_to_message") or {}
        text = (reply.get("text") or reply.get("caption") or "").strip()
        if not text:
            return []
        from_user = reply.get("from") or {}
        author = (
            from_user.get("username") or from_user.get("first_name") or ""
        ).strip() or None
        if from_user.get("is_bot") and not author:
            author = "Lemma"
        return [
            SurfaceContextMessage(
                author=author, text=text, ts=str(reply.get("date") or "") or None
            )
        ]

    async def send_file_attachment(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        file_name: str,
        file_bytes: bytes,
        mime_type: str,
        caption: str | None = None,
    ) -> bool:
        return await TelegramPlatformService(credentials).send_file_bytes(
            event,
            file_name=file_name,
            file_bytes=file_bytes,
            mime_type=mime_type,
            caption=caption,
        )

    async def send_voice_note(
        self,
        *,
        credentials: dict[str, Any],
        event: ParsedInboundSurfaceEvent,
        file_name: str,
        audio_bytes: bytes,
        mime: str,
        caption: str | None = None,
    ) -> bool:
        # Telegram renders a true voice bubble only via sendVoice (OGG/Opus);
        # sendAudio/sendDocument would attach it as a music/file instead.
        return await TelegramPlatformService(credentials).send_voice_bytes(
            event,
            file_name=file_name,
            audio_bytes=audio_bytes,
            mime_type=mime,
            caption=caption,
        )

    def unresolved_sender_reply(
        self, event: ParsedInboundSurfaceEvent
    ) -> tuple[str, dict[str, Any]] | None:
        # Telegram DMs can link the sender via a shared contact; ask for it
        # instead of pointing an unknown sender at the signup page. Once a
        # phone is known the default signup prompt applies.
        if not event.is_dm or event.sender_phone:
            return None
        if event.metadata.get("contact_shared_by_sender") is False:
            message = (
                "Please use the button below to share your own phone number so I can "
                "link your Telegram account."
            )
        else:
            message = (
                "Please share your phone number once so I can link your Telegram account "
                "to your Lemma user."
            )
        return message, {"reply_markup": _CONTACT_REQUEST_MARKUP}

    def linked_sender_confirmation(
        self, event: ParsedInboundSurfaceEvent
    ) -> tuple[str, dict[str, Any]] | None:
        # A bare contact-share update carries no message text; confirm the link
        # instead of starting an agent run on an empty prompt.
        if not event.metadata.get("contact_shared_by_sender"):
            return None
        if str(event.message_text or "").strip():
            return None
        return (
            "Your phone number is linked now. You can continue chatting with me here.",
            {"reply_markup": {"remove_keyboard": True}},
        )
