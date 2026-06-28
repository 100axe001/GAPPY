from __future__ import annotations

import mimetypes
from typing import Any

import httpx
from pydantic_ai.tools import RunContext

from app.modules.agent.tools.context import ConversationContext
from app.modules.agent_surfaces.domain.entities import ParsedInboundSurfaceEvent
from app.modules.agent_surfaces.domain.models import (
    SurfaceDisplayRenderPlan,
    SurfaceSenderProfile,
)
from app.modules.agent_surfaces.domain.surface_event_metadata import (
    WhatsAppSurfaceEventMetadata,
)
from app.modules.agent_surfaces.platforms import common
from app.modules.agent_surfaces.platforms.whatsapp.models import (
    WhatsAppCurrentContactParams,
    WhatsAppCurrentContactResult,
    WhatsAppFileAttachment,
)
from app.core.log.log import get_logger

logger = get_logger(__name__)

_WHATSAPP_API_BASE = "https://graph.facebook.com/v21.0"


class WhatsAppPlatformService:
    def __init__(self, credentials: dict[str, Any]):
        self.credentials = credentials
        self._access_token = credentials.get("access_token") or ""
        self._phone_number_id = credentials.get("phone_number_id") or ""
        self._api_base = credentials.get("api_base_url") or _WHATSAPP_API_BASE

    async def fetch_sender_profile(
        self, event: ParsedInboundSurfaceEvent
    ) -> SurfaceSenderProfile | None:
        return SurfaceSenderProfile(
            phone=event.sender_phone,
            display_name=event.sender_display_name,
        )

    async def send_message(
        self,
        event: ParsedInboundSurfaceEvent,
        message: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        phone_number_id = (
            event.reply_target.get("phone_number_id") or self._phone_number_id
        )
        sender_wa_id = event.reply_target.get("sender_wa_id") or event.sender_phone

        url = f"{self._api_base}/{phone_number_id}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": sender_wa_id,
            "type": "text",
            "text": {"body": message},
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            resp.raise_for_status()

    async def send_display_resource(
        self,
        event: ParsedInboundSurfaceEvent,
        render_plan: SurfaceDisplayRenderPlan,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        del metadata
        phone_number_id = (
            event.reply_target.get("phone_number_id") or self._phone_number_id
        )
        sender_wa_id = event.reply_target.get("sender_wa_id") or event.sender_phone
        if not phone_number_id or not sender_wa_id:
            logger.warning(
                "WhatsApp send_display_resource skipped: missing phone_number_id or "
                "recipient wa_id (phone_number_id=%s)",
                phone_number_id,
            )
            return
        action = render_plan.primary_action
        if action is None:
            await self._post_message_payload(
                phone_number_id=phone_number_id,
                payload=_whatsapp_text_payload(
                    recipient_wa_id=sender_wa_id,
                    body=_whatsapp_display_resource_text(render_plan),
                    preview_url=False,
                ),
            )
            return

        try:
            await self._post_message_payload(
                phone_number_id=phone_number_id,
                payload=_whatsapp_cta_url_payload(
                    recipient_wa_id=sender_wa_id,
                    render_plan=render_plan,
                ),
            )
        except httpx.HTTPStatusError:
            logger.info(
                "WhatsApp display_resource cta_url rejected; falling back to text message"
            )
            await self._post_message_payload(
                phone_number_id=phone_number_id,
                payload=_whatsapp_text_payload(
                    recipient_wa_id=sender_wa_id,
                    body=_whatsapp_display_resource_text(render_plan),
                    preview_url=True,
                ),
            )

    async def add_processing_indicator(
        self,
        event: ParsedInboundSurfaceEvent,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        phone_number_id = (
            event.reply_target.get("phone_number_id") or self._phone_number_id
        )
        sender_wa_id = event.reply_target.get("sender_wa_id") or event.sender_phone

        url = f"{self._api_base}/{phone_number_id}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": sender_wa_id,
            "type": "reaction",
            "reaction": {"emoji": "\U0001f4ac", "action": "react"},
        }

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    url,
                    json=payload,
                    headers={"Authorization": f"Bearer {self._access_token}"},
                )
                resp.raise_for_status()
        except Exception:
            pass

    async def download_attachment_bytes(
        self,
        event: ParsedInboundSurfaceEvent,
        attachment: dict[str, Any],
    ) -> tuple[bytes, str, str] | None:
        """Download a single inbound WhatsApp attachment (no RunContext)."""
        del event
        if not self._access_token:
            return None
        media_id = str(attachment.get("id") or "").strip()
        if not media_id:
            return None
        media_info = await self._get_media_info(media_id)
        if not media_info:
            return None
        download_url = str(media_info.get("url") or "").strip()
        if not download_url:
            return None
        file_name = (
            str(attachment.get("name") or "").strip()
            or _filename_from_url(download_url)
            or "whatsapp_file"
        )
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(
                download_url,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            response.raise_for_status()
            content = response.content
        mime_type = (
            str(attachment.get("mime_type") or media_info.get("mime_type") or "").strip()
            or mimetypes.guess_type(file_name)[0]
            or "application/octet-stream"
        )
        return content, file_name, mime_type

    async def send_file_bytes(
        self,
        event: ParsedInboundSurfaceEvent,
        *,
        file_name: str,
        file_bytes: bytes,
        mime_type: str,
        caption: str | None = None,
    ) -> bool:
        """Upload + send raw file bytes to the inbound chat (egress, no RunContext).

        Returns True on success; False (or on an unsupported-media error raised by
        the upload) so the caller falls back to a URL link.
        """
        phone_number_id = (
            event.reply_target.get("phone_number_id") or self._phone_number_id
        )
        recipient_wa_id = event.reply_target.get("sender_wa_id") or event.sender_phone
        if not self._access_token or not phone_number_id or not recipient_wa_id:
            return False
        send_type = _resolve_whatsapp_send_type(
            delivery_mode="auto", mime_type=mime_type
        )
        media_id = await self._upload_media(
            phone_number_id=phone_number_id,
            file_name=file_name,
            file_bytes=file_bytes,
            mime_type=mime_type,
        )
        if not media_id:
            return False
        message_id = await self._send_media_message(
            phone_number_id=phone_number_id,
            recipient_wa_id=recipient_wa_id,
            media_id=media_id,
            send_type=send_type,
            file_name=file_name,
            caption=caption,
        )
        return bool(message_id)

    async def get_current_contact(
        self,
        *,
        ctx: RunContext[ConversationContext],
        request: WhatsAppCurrentContactParams,
    ) -> WhatsAppCurrentContactResult:
        del request
        metadata = self._whatsapp_metadata(ctx)
        contacts = list(metadata.contacts) if metadata is not None else []
        first_contact = contacts[0] if contacts else {}
        display_name = None
        if isinstance(first_contact, dict):
            display_name = (first_contact.get("profile") or {}).get("name")
        attachment_names = [
            attachment.name
            for attachment in self._current_message_attachments(ctx)
            if attachment.name
        ]
        return WhatsAppCurrentContactResult(
            success=True,
            message="Resolved current WhatsApp contact details.",
            wa_id=self._resolve_recipient_wa_id(ctx),
            display_name=display_name,
            phone_number_id=self._resolve_phone_number_id(ctx),
            waba_id=metadata.waba_id if metadata is not None else None,
            attachment_names=attachment_names,
        )

    def _whatsapp_metadata(
        self,
        ctx: RunContext[ConversationContext],
    ) -> WhatsAppSurfaceEventMetadata | None:
        metadata = ctx.deps.surface_metadata
        if isinstance(metadata, WhatsAppSurfaceEventMetadata):
            return metadata
        return None

    def _current_message_attachments(
        self,
        ctx: RunContext[ConversationContext],
    ) -> list[WhatsAppFileAttachment]:
        metadata = self._whatsapp_metadata(ctx)
        if metadata is None:
            return []
        return common.coerce_attachments(metadata.attachments, WhatsAppFileAttachment)

    def _resolve_phone_number_id(
        self, ctx: RunContext[ConversationContext]
    ) -> str | None:
        metadata = self._whatsapp_metadata(ctx)
        return (
            (metadata.phone_number_id if metadata is not None else None)
            or ctx.deps.external_channel_id
            or self._phone_number_id
            or None
        )

    def _resolve_recipient_wa_id(
        self, ctx: RunContext[ConversationContext]
    ) -> str | None:
        metadata = self._whatsapp_metadata(ctx)
        if metadata is not None:
            for contact in metadata.contacts:
                if isinstance(contact, dict):
                    wa_id = str(contact.get("wa_id") or "").strip()
                    if wa_id:
                        return wa_id
        thread_id = str(ctx.deps.external_thread_id or "")
        if "@" in thread_id:
            candidate = thread_id.split("@", 1)[0].strip()
            if candidate:
                return candidate
        return None

    async def _upload_media(
        self,
        *,
        phone_number_id: str,
        file_name: str,
        file_bytes: bytes,
        mime_type: str,
    ) -> str | None:
        url = f"{self._api_base}/{phone_number_id}/media"
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                data={
                    "messaging_product": "whatsapp",
                    "type": mime_type,
                },
                files={"file": (file_name, file_bytes, mime_type)},
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError:
                response_body = _response_body_excerpt(response)
                logger.error(
                    "WhatsApp media upload rejected phone_number_id=%s file_name=%s "
                    "mime_type=%s status=%s body=%s",
                    phone_number_id,
                    file_name,
                    mime_type,
                    response.status_code,
                    response_body,
                )
                raise
            payload = response.json()
        return str((payload or {}).get("id") or "").strip() or None

    async def _send_media_message(
        self,
        *,
        phone_number_id: str,
        recipient_wa_id: str,
        media_id: str,
        send_type: str,
        file_name: str,
        caption: str | None,
    ) -> str | None:
        url = f"{self._api_base}/{phone_number_id}/messages"
        media_payload: dict[str, Any] = {"id": media_id}
        if send_type == "document":
            media_payload["filename"] = file_name
        if caption and send_type in {"document", "image", "video"}:
            media_payload["caption"] = caption

        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_wa_id,
            "type": send_type,
            send_type: media_payload,
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            response.raise_for_status()
            result = response.json()
        messages = (result or {}).get("messages") or []
        first = messages[0] if messages else {}
        return str(first.get("id") or "").strip() or None

    async def _post_message_payload(
        self,
        *,
        phone_number_id: str,
        payload: dict[str, Any],
    ) -> None:
        url = f"{self._api_base}/{phone_number_id}/messages"
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            response.raise_for_status()

    async def _get_media_info(self, media_id: str) -> dict[str, Any] | None:
        url = f"{self._api_base}/{media_id}"
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(
                url,
                headers={"Authorization": f"Bearer {self._access_token}"},
            )
            response.raise_for_status()
            payload = response.json()
        return payload if isinstance(payload, dict) else None


def _resolve_whatsapp_send_type(*, delivery_mode: str, mime_type: str) -> str:
    requested = str(delivery_mode or "auto").lower()
    if requested != "auto":
        return requested
    if mime_type.startswith("image/"):
        return "image"
    if mime_type.startswith("audio/"):
        return "audio"
    if mime_type.startswith("video/"):
        return "video"
    return "document"


def _whatsapp_cta_url_payload(
    *,
    recipient_wa_id: str,
    render_plan: SurfaceDisplayRenderPlan,
) -> dict[str, Any]:
    action = render_plan.primary_action
    body = _truncate_whatsapp_text(
        _whatsapp_display_resource_text(render_plan, include_action=False),
        1024,
    )
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient_wa_id,
        "type": "interactive",
        "interactive": {
            "type": "cta_url",
            "body": {"text": body},
            "action": {
                "name": "cta_url",
                "parameters": {
                    "display_text": _truncate_whatsapp_button_text(
                        action.label if action else "Open"
                    ),
                    "url": action.url if action else "",
                },
            },
        },
    }


def _whatsapp_text_payload(
    *,
    recipient_wa_id: str,
    body: str,
    preview_url: bool,
) -> dict[str, Any]:
    return {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient_wa_id,
        "type": "text",
        "text": {
            "body": _truncate_whatsapp_text(body, 4096),
            "preview_url": preview_url,
        },
    }


def _whatsapp_display_resource_text(
    render_plan: SurfaceDisplayRenderPlan,
    *,
    include_action: bool = True,
) -> str:
    parts = [f"*{render_plan.title}*"]
    if render_plan.summary:
        parts.append(render_plan.summary)
    parts.extend(render_plan.detail_lines[:5])
    action = render_plan.primary_action
    if include_action and action is not None:
        parts.append(f"{action.label}: {action.url}")
    return "\n\n".join(parts)


def _truncate_whatsapp_button_text(value: str) -> str:
    text = " ".join(str(value or "").split()) or "Open"
    return text if len(text) <= 20 else text[:19].rstrip() + "..."


def _truncate_whatsapp_text(value: str, max_length: int) -> str:
    text = str(value or "").strip()
    return text if len(text) <= max_length else text[: max_length - 1].rstrip() + "..."


def _filename_from_url(url: str) -> str:
    return str(url or "").rstrip("/").split("/")[-1].strip()


def _response_body_excerpt(response: httpx.Response) -> str:
    body = ""
    try:
        body = response.text
    except Exception:
        body = ""
    body = str(body or "").strip()
    if len(body) > 500:
        return body[:500] + "..."
    return body
