from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_info_conversations_info_error_schema import ConversationsInfoConversationsInfoErrorSchema
from ...models.conversations_info_conversations_info_success_schema import ConversationsInfoConversationsInfoSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,
    include_num_members: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["include_locale"] = include_locale

    params["include_num_members"] = include_num_members


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsInfoConversationsInfoSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsInfoConversationsInfoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema]:
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
    include_locale: bool | Unset = UNSET,
    include_num_members: bool | Unset = UNSET,

) -> Response[ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema]:
    """  Retrieve information about a conversation.

    Args:
        token (str | Unset):
        channel (str | Unset):
        include_locale (bool | Unset):
        include_num_members (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
include_locale=include_locale,
include_num_members=include_num_members,

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
    include_locale: bool | Unset = UNSET,
    include_num_members: bool | Unset = UNSET,

) -> ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema | None:
    """  Retrieve information about a conversation.

    Args:
        token (str | Unset):
        channel (str | Unset):
        include_locale (bool | Unset):
        include_num_members (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
include_locale=include_locale,
include_num_members=include_num_members,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,
    include_num_members: bool | Unset = UNSET,

) -> Response[ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema]:
    """  Retrieve information about a conversation.

    Args:
        token (str | Unset):
        channel (str | Unset):
        include_locale (bool | Unset):
        include_num_members (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
include_locale=include_locale,
include_num_members=include_num_members,

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
    include_locale: bool | Unset = UNSET,
    include_num_members: bool | Unset = UNSET,

) -> ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema | None:
    """  Retrieve information about a conversation.

    Args:
        token (str | Unset):
        channel (str | Unset):
        include_locale (bool | Unset):
        include_num_members (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsInfoConversationsInfoErrorSchema | ConversationsInfoConversationsInfoSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
include_locale=include_locale,
include_num_members=include_num_members,

    )).parsed
