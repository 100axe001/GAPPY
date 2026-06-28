from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.message_list_response import MessageListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    conversation_id: UUID,
    *,
    page_token: None | str | Unset = UNSET,
    before_sequence: int | None | Unset = UNSET,
    after_sequence: int | None | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_page_token: None | str | Unset
    if isinstance(page_token, Unset):
        json_page_token = UNSET
    else:
        json_page_token = page_token
    params["page_token"] = json_page_token

    json_before_sequence: int | None | Unset
    if isinstance(before_sequence, Unset):
        json_before_sequence = UNSET
    else:
        json_before_sequence = before_sequence
    params["before_sequence"] = json_before_sequence

    json_after_sequence: int | None | Unset
    if isinstance(after_sequence, Unset):
        json_after_sequence = UNSET
    else:
        json_after_sequence = after_sequence
    params["after_sequence"] = json_after_sequence

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/conversations/{conversation_id}/messages".format(
            pod_id=quote(str(pod_id), safe=""),
            conversation_id=quote(str(conversation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | MessageListResponse | None:
    if response.status_code == 200:
        response_200 = MessageListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | MessageListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page_token: None | str | Unset = UNSET,
    before_sequence: int | None | Unset = UNSET,
    after_sequence: int | None | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ErrorResponse | MessageListResponse]:
    """List Pod Conversation Messages

     List the latest persisted messages in chronological order. Pass next_page_token as page_token to
    fetch the next older page above the current page.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        page_token (None | str | Unset):
        before_sequence (int | None | Unset):
        after_sequence (int | None | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MessageListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        conversation_id=conversation_id,
        page_token=page_token,
        before_sequence=before_sequence,
        after_sequence=after_sequence,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page_token: None | str | Unset = UNSET,
    before_sequence: int | None | Unset = UNSET,
    after_sequence: int | None | Unset = UNSET,
    limit: int | Unset = 100,
) -> ErrorResponse | MessageListResponse | None:
    """List Pod Conversation Messages

     List the latest persisted messages in chronological order. Pass next_page_token as page_token to
    fetch the next older page above the current page.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        page_token (None | str | Unset):
        before_sequence (int | None | Unset):
        after_sequence (int | None | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MessageListResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        conversation_id=conversation_id,
        client=client,
        page_token=page_token,
        before_sequence=before_sequence,
        after_sequence=after_sequence,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page_token: None | str | Unset = UNSET,
    before_sequence: int | None | Unset = UNSET,
    after_sequence: int | None | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[ErrorResponse | MessageListResponse]:
    """List Pod Conversation Messages

     List the latest persisted messages in chronological order. Pass next_page_token as page_token to
    fetch the next older page above the current page.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        page_token (None | str | Unset):
        before_sequence (int | None | Unset):
        after_sequence (int | None | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | MessageListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        conversation_id=conversation_id,
        page_token=page_token,
        before_sequence=before_sequence,
        after_sequence=after_sequence,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page_token: None | str | Unset = UNSET,
    before_sequence: int | None | Unset = UNSET,
    after_sequence: int | None | Unset = UNSET,
    limit: int | Unset = 100,
) -> ErrorResponse | MessageListResponse | None:
    """List Pod Conversation Messages

     List the latest persisted messages in chronological order. Pass next_page_token as page_token to
    fetch the next older page above the current page.

    Args:
        pod_id (UUID):
        conversation_id (UUID):
        page_token (None | str | Unset):
        before_sequence (int | None | Unset):
        after_sequence (int | None | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | MessageListResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            conversation_id=conversation_id,
            client=client,
            page_token=page_token,
            before_sequence=before_sequence,
            after_sequence=after_sequence,
            limit=limit,
        )
    ).parsed
