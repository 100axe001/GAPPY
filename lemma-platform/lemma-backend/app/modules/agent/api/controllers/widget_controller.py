"""Conversation widget serving + embed-URL minting.

A conversation widget and an app are the same primitive: a pod-authenticated
HTML page that reads ``window.__LEMMA_CONFIG__`` and uses the browser SDK. This
serves the widget's stored fragment as a full document with pod context injected
— the same serve+inject path apps use — so the frontend embeds it by URL and it
can be promoted to an app verbatim.

Unlike app assets, widget HTML can carry agent-baked data, so the serve route is
**not public**: it requires a pod-member session, or a short-lived signed token
for the iframe document load when the session cookie is not sent cross-site. The
token is minted per-view by the authenticated mint endpoint.
"""

from __future__ import annotations

import json
import time
from typing import Any
from urllib.parse import quote
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import Response
from pydantic import BaseModel
from supertokens_python.recipe.session.asyncio import get_session

from app.core.api.dependencies import UoWDep
from app.core.api.html_response import build_injected_html_response
from app.core.authorization.context import ResourceRef
from app.core.authorization.current import reset_current_context, set_current_context
from app.core.authorization.dependencies import PodContextDep
from app.core.authorization.permissions import Permissions
from app.core.authorization.service import AuthorizationDataService
from app.core.config import settings
from app.modules.agent.config import agent_settings
from app.core.html_document import wrap_html_fragment
from app.modules.agent.api.dependencies import get_conversation_service
from app.modules.agent.domain.errors import ConversationNotFoundError
from app.modules.agent.services.widget_asset_service import WidgetAssetService
from app.modules.agent.services.widget_token import (
    InvalidWidgetToken,
    mint_widget_token,
    verify_widget_token,
    widget_serve_path,
)

# Self-validating serve route (session-or-token); excluded from global verify_auth.
serve_router = APIRouter(prefix="/widgets", tags=["Widgets"], redirect_slashes=False)

# Authenticated, pod-scoped mint route.
router = APIRouter(
    prefix="/pods/{pod_id}/widgets", tags=["Widgets"], redirect_slashes=False
)


class WidgetEmbedUrlResponse(BaseModel):
    url: str


class WidgetSubmitRequest(BaseModel):
    payload: Any = None
    text: str | None = None


class WidgetSubmitResponse(BaseModel):
    ok: bool = True


def _widget_submit_content(body: WidgetSubmitRequest) -> str:
    """Render a widget submission as the body of a new user message."""
    text = (body.text or "").strip()
    if text:
        return text
    if body.payload is None:
        return "Submitted the widget."
    try:
        rendered = json.dumps(body.payload, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        rendered = str(body.payload)
    return f"Submitted from the widget:\n{rendered}"


async def _resolve_widget_viewer(
    request: Request,
    conversation_id: UUID,
    tool_call_id: str,
    token: str | None,
) -> UUID | None:
    """The viewer's ``user_id`` from a session cookie, else a valid signed token."""
    try:
        session = await get_session(request, session_required=False)
    except Exception:
        session = None
    if session is not None:
        try:
            return UUID(session.get_user_id())
        except Exception:
            pass
    if token:
        try:
            return verify_widget_token(
                token, conversation_id=conversation_id, tool_call_id=tool_call_id
            )
        except InvalidWidgetToken:
            return None
    return None


async def _require_conversation_owner(
    uow: UoWDep,
    conversation_id: UUID,
    *,
    viewer_id: UUID,
    pod_id: UUID,
) -> None:
    """Enforce that ``viewer_id`` owns the conversation backing this widget.

    A widget lives inside a per-user conversation, but ``CONVERSATION_READ`` is a
    pod-level permission held by every pod member — so the pod check alone lets
    any member read another member's widget HTML. Re-use the canonical ownership
    check (``conversation.user_id == viewer``) and 404 on mismatch so existence
    is not leaked.
    """
    conversation_service = get_conversation_service(uow)
    conversation = await conversation_service.conversation_repository.get_conversation(
        conversation_id
    )
    try:
        conversation_service._validate_conversation_access(
            conversation, user_id=viewer_id, pod_id=pod_id, agent_id=None
        )
    except ConversationNotFoundError:
        raise HTTPException(status_code=404, detail="Widget not found")


@serve_router.get(
    "/serve/{conversation_id}/{tool_call_id}",
    operation_id="widget.serve",
    summary="Serve Conversation Widget HTML",
    include_in_schema=False,
)
async def serve_widget(
    conversation_id: UUID,
    tool_call_id: str,
    request: Request,
    uow: UoWDep,
    token: str | None = Query(default=None),
) -> Response:
    artifact = await WidgetAssetService(uow).get_widget(
        conversation_id, tool_call_id
    )
    if artifact is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    viewer_id = await _resolve_widget_viewer(
        request, conversation_id, tool_call_id, token
    )
    if viewer_id is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    ctx = await AuthorizationDataService(uow.session).build_user_context(
        user_id=viewer_id, pod_id=artifact.pod_id
    )
    await ctx.require(Permissions.CONVERSATION_READ, ResourceRef.pod(artifact.pod_id))
    await _require_conversation_owner(
        uow, conversation_id, viewer_id=viewer_id, pod_id=artifact.pod_id
    )

    document = wrap_html_fragment(artifact.content, title=artifact.title, embed=True)
    return build_injected_html_response(document, artifact.pod_id)


@serve_router.post(
    "/serve/{conversation_id}/{tool_call_id}/submit",
    response_model=WidgetSubmitResponse,
    operation_id="widget.submit",
    summary="Submit Widget Input To Chat",
    include_in_schema=False,
)
async def submit_widget(
    conversation_id: UUID,
    tool_call_id: str,
    request: Request,
    uow: UoWDep,
    body: WidgetSubmitRequest,
    token: str | None = Query(default=None),
) -> WidgetSubmitResponse:
    """Inject a widget's submitted value into its conversation as a user message.

    Used by the standalone (non-embedded) widget submit bridge. Authenticated the
    same way as the serve route — a pod-member session or the per-view signed
    token — so a surface user opening the widget link can submit back. The web
    iframe path posts to its parent instead and never hits this endpoint.
    """
    artifact = await WidgetAssetService(uow).get_widget(conversation_id, tool_call_id)
    if artifact is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    viewer_id = await _resolve_widget_viewer(
        request, conversation_id, tool_call_id, token
    )
    if viewer_id is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    ctx = await AuthorizationDataService(uow.session).build_user_context(
        user_id=viewer_id, pod_id=artifact.pod_id
    )
    await ctx.require(Permissions.CONVERSATION_READ, ResourceRef.pod(artifact.pod_id))

    content = _widget_submit_content(body)
    conversation_service = get_conversation_service(uow)
    ctx_token = set_current_context(ctx)
    try:
        await conversation_service.add_user_message_and_start_run(
            conversation_id=conversation_id,
            user_id=viewer_id,
            content=content,
            pod_id=artifact.pod_id,
            message_metadata={
                "source": "widget_submit",
                "tool_call_id": tool_call_id,
                "widget_payload": body.payload,
            },
        )
        await uow.commit()
    finally:
        reset_current_context(ctx_token)
    return WidgetSubmitResponse(ok=True)


@router.post(
    "/{conversation_id}/{tool_call_id}/embed-token",
    response_model=WidgetEmbedUrlResponse,
    operation_id="widget.embed_token",
    summary="Mint Widget Embed URL",
)
async def mint_widget_embed_url(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
    uow: UoWDep,
    ctx: PodContextDep,
) -> WidgetEmbedUrlResponse:
    """Mint a short-lived, signed embed URL for a widget the caller may view.

    Per-view (not baked into the persisted tool result) so the token stays
    ephemeral and membership is re-checked each time the widget is opened.
    """
    artifact = await WidgetAssetService(uow).get_widget(
        conversation_id, tool_call_id
    )
    if artifact is None or artifact.pod_id != pod_id:
        raise HTTPException(status_code=404, detail="Widget not found")
    await ctx.require(Permissions.CONVERSATION_READ, ResourceRef.pod(pod_id))

    if ctx.user_id is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    await _require_conversation_owner(
        uow, conversation_id, viewer_id=ctx.user_id, pod_id=pod_id
    )

    expires_at = int(time.time()) + agent_settings.widget_url_expiry_seconds
    token = mint_widget_token(
        conversation_id=conversation_id,
        tool_call_id=tool_call_id,
        user_id=ctx.user_id,
        expires_at_epoch=expires_at,
    )
    base = settings.api_url.rstrip("/")
    path = widget_serve_path(conversation_id, tool_call_id)
    return WidgetEmbedUrlResponse(url=f"{base}{path}?token={quote(token)}")
