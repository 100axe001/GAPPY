from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_invite_conversations_invite_error_schema import ConversationsInviteConversationsInviteErrorSchema
from ...models.conversations_invite_data_body import ConversationsInviteDataBody
from ...models.conversations_invite_json_body import ConversationsInviteJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsInviteDataBody  |     ConversationsInviteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.invite",
    }

    if isinstance(body, ConversationsInviteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsInviteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsInviteConversationsInviteErrorSchema | None:
    if response.status_code == 200:
        response_200 = ConversationsInviteConversationsInviteErrorSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsInviteConversationsInviteErrorSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsInviteDataBody  |     ConversationsInviteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsInviteConversationsInviteErrorSchema]:
    """  Invites users to a channel.

    Args:
        token (str | Unset):
        body (ConversationsInviteDataBody | Unset):
        body (ConversationsInviteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsInviteConversationsInviteErrorSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    ConversationsInviteDataBody  |     ConversationsInviteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsInviteConversationsInviteErrorSchema | None:
    """  Invites users to a channel.

    Args:
        token (str | Unset):
        body (ConversationsInviteDataBody | Unset):
        body (ConversationsInviteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsInviteConversationsInviteErrorSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsInviteDataBody  |     ConversationsInviteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsInviteConversationsInviteErrorSchema]:
    """  Invites users to a channel.

    Args:
        token (str | Unset):
        body (ConversationsInviteDataBody | Unset):
        body (ConversationsInviteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsInviteConversationsInviteErrorSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    ConversationsInviteDataBody  |     ConversationsInviteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsInviteConversationsInviteErrorSchema | None:
    """  Invites users to a channel.

    Args:
        token (str | Unset):
        body (ConversationsInviteDataBody | Unset):
        body (ConversationsInviteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsInviteConversationsInviteErrorSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
