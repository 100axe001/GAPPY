from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.widget_embed_url_response import WidgetEmbedUrlResponse
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pods/{pod_id}/widgets/{conversation_id}/{tool_call_id}/embed-token".format(
            pod_id=quote(str(pod_id), safe=""),
            conversation_id=quote(str(conversation_id), safe=""),
            tool_call_id=quote(str(tool_call_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WidgetEmbedUrlResponse | None:
    if response.status_code == 200:
        response_200 = WidgetEmbedUrlResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | WidgetEmbedUrlResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | WidgetEmbedUrlResponse]:
    """Mint Widget Embed URL

     Mint a short-lived, signed embed URL for a widget the caller may view.

    Per-view (not baked into the persisted tool result) so the token stays
    ephemeral and membership is re-checked each time the widget is opened.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        tool_call_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WidgetEmbedUrlResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        conversation_id=conversation_id,
        tool_call_id=tool_call_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | WidgetEmbedUrlResponse | None:
    """Mint Widget Embed URL

     Mint a short-lived, signed embed URL for a widget the caller may view.

    Per-view (not baked into the persisted tool result) so the token stays
    ephemeral and membership is re-checked each time the widget is opened.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        tool_call_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WidgetEmbedUrlResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        conversation_id=conversation_id,
        tool_call_id=tool_call_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | WidgetEmbedUrlResponse]:
    """Mint Widget Embed URL

     Mint a short-lived, signed embed URL for a widget the caller may view.

    Per-view (not baked into the persisted tool result) so the token stays
    ephemeral and membership is re-checked each time the widget is opened.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        tool_call_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WidgetEmbedUrlResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        conversation_id=conversation_id,
        tool_call_id=tool_call_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    conversation_id: UUID,
    tool_call_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | WidgetEmbedUrlResponse | None:
    """Mint Widget Embed URL

     Mint a short-lived, signed embed URL for a widget the caller may view.

    Per-view (not baked into the persisted tool result) so the token stays
    ephemeral and membership is re-checked each time the widget is opened.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        tool_call_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WidgetEmbedUrlResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            conversation_id=conversation_id,
            tool_call_id=tool_call_id,
            client=client,
        )
    ).parsed
