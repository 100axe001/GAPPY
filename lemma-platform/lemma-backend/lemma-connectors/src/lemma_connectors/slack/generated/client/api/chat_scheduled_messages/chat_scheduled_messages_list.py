from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_scheduled_messages_list_chat_scheduled_messages_list_error_schema import ChatScheduledMessagesListChatScheduledMessagesListErrorSchema
from ...models.chat_scheduled_messages_list_chat_scheduled_messages_list_schema import ChatScheduledMessagesListChatScheduledMessagesListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    params: dict[str, Any] = {}

    params["channel"] = channel

    params["latest"] = latest

    params["oldest"] = oldest

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat.scheduledMessages.list",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema:
    if response.status_code == 200:
        response_200 = ChatScheduledMessagesListChatScheduledMessagesListSchema.from_dict(response.json())



        return response_200

    response_default = ChatScheduledMessagesListChatScheduledMessagesListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema]:
    """  Returns a list of scheduled messages.

    Args:
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema]
     """


    kwargs = _get_kwargs(
        channel=channel,
latest=latest,
oldest=oldest,
limit=limit,
cursor=cursor,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema | None:
    """  Returns a list of scheduled messages.

    Args:
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema
     """


    return sync_detailed(
        client=client,
channel=channel,
latest=latest,
oldest=oldest,
limit=limit,
cursor=cursor,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema]:
    """  Returns a list of scheduled messages.

    Args:
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema]
     """


    kwargs = _get_kwargs(
        channel=channel,
latest=latest,
oldest=oldest,
limit=limit,
cursor=cursor,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema | None:
    """  Returns a list of scheduled messages.

    Args:
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatScheduledMessagesListChatScheduledMessagesListErrorSchema | ChatScheduledMessagesListChatScheduledMessagesListSchema
     """


    return (await asyncio_detailed(
        client=client,
channel=channel,
latest=latest,
oldest=oldest,
limit=limit,
cursor=cursor,
token=token,

    )).parsed
