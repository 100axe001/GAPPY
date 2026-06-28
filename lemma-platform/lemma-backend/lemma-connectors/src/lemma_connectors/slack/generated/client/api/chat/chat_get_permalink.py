from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_get_permalink_chat_get_permalink_error_schema import ChatGetPermalinkChatGetPermalinkErrorSchema
from ...models.chat_get_permalink_chat_get_permalink_success_schema import ChatGetPermalinkChatGetPermalinkSuccessSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,
    channel: str,
    message_ts: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["message_ts"] = message_ts


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat.getPermalink",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatGetPermalinkChatGetPermalinkSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatGetPermalinkChatGetPermalinkErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str,
    message_ts: str,

) -> Response[ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema]:
    """  Retrieve a permalink URL for a specific extant message

    Args:
        token (str):
        channel (str):
        message_ts (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
message_ts=message_ts,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str,
    message_ts: str,

) -> ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema | None:
    """  Retrieve a permalink URL for a specific extant message

    Args:
        token (str):
        channel (str):
        message_ts (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
message_ts=message_ts,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str,
    message_ts: str,

) -> Response[ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema]:
    """  Retrieve a permalink URL for a specific extant message

    Args:
        token (str):
        channel (str):
        message_ts (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
message_ts=message_ts,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str,
    message_ts: str,

) -> ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema | None:
    """  Retrieve a permalink URL for a specific extant message

    Args:
        token (str):
        channel (str):
        message_ts (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatGetPermalinkChatGetPermalinkErrorSchema | ChatGetPermalinkChatGetPermalinkSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
message_ts=message_ts,

    )).parsed
