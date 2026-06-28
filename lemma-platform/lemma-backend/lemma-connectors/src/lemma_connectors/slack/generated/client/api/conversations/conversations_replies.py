from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_replies_conversations_replies_error_schema import ConversationsRepliesConversationsRepliesErrorSchema
from ...models.conversations_replies_conversations_replies_success_schema import ConversationsRepliesConversationsRepliesSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts: float | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["ts"] = ts

    params["latest"] = latest

    params["oldest"] = oldest

    params["inclusive"] = inclusive

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations.replies",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsRepliesConversationsRepliesSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsRepliesConversationsRepliesErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema]:
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
    ts: float | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema]:
    """  Retrieve a thread of messages posted to a conversation

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts (float | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
ts=ts,
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
    ts: float | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema | None:
    """  Retrieve a thread of messages posted to a conversation

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts (float | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
ts=ts,
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
    ts: float | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema]:
    """  Retrieve a thread of messages posted to a conversation

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts (float | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
ts=ts,
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
    ts: float | Unset = UNSET,
    latest: float | Unset = UNSET,
    oldest: float | Unset = UNSET,
    inclusive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema | None:
    """  Retrieve a thread of messages posted to a conversation

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts (float | Unset):
        latest (float | Unset):
        oldest (float | Unset):
        inclusive (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsRepliesConversationsRepliesErrorSchema | ConversationsRepliesConversationsRepliesSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
ts=ts,
latest=latest,
oldest=oldest,
inclusive=inclusive,
limit=limit,
cursor=cursor,

    )).parsed
