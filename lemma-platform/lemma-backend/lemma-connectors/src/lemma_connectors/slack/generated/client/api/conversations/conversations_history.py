from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_history_conversations_history_error_schema import ConversationsHistoryConversationsHistoryErrorSchema
from ...models.conversations_history_conversations_history_success_schema import ConversationsHistoryConversationsHistorySuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["latest"] = latest

    params["oldest"] = oldest

    params["inclusive"] = inclusive

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations.history",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsHistoryConversationsHistorySuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsHistoryConversationsHistoryErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema]:
    """  Fetches a conversation's history of messages and events.

    Args:
        token (str | Unset):
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
latest=latest,
oldest=oldest,
inclusive=inclusive,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema | None:
    """  Fetches a conversation's history of messages and events.

    Args:
        token (str | Unset):
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
latest=latest,
oldest=oldest,
inclusive=inclusive,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema]:
    """  Fetches a conversation's history of messages and events.

    Args:
        token (str | Unset):
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
latest=latest,
oldest=oldest,
inclusive=inclusive,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema | None:
    """  Fetches a conversation's history of messages and events.

    Args:
        token (str | Unset):
        channel (str | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsHistoryConversationsHistoryErrorSchema | ConversationsHistoryConversationsHistorySuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
latest=latest,
oldest=oldest,
inclusive=inclusive,
limit=limit,
cursor=cursor,

    )).parsed
