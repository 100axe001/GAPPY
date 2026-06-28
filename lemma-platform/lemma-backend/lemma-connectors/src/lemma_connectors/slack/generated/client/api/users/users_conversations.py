from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_conversations_users_conversations_error_schema import UsersConversationsUsersConversationsErrorSchema
from ...models.users_conversations_users_conversations_success_schema import UsersConversationsUsersConversationsSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    types: str | Unset = UNSET,
    exclude_archived: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["user"] = user

    params["types"] = types

    params["exclude_archived"] = exclude_archived

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.conversations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema:
    if response.status_code == 200:
        response_200 = UsersConversationsUsersConversationsSuccessSchema.from_dict(response.json())



        return response_200

    response_default = UsersConversationsUsersConversationsErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema]:
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
    user: str | Unset = UNSET,
    types: str | Unset = UNSET,
    exclude_archived: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema]:
    """  List conversations the calling user may access.

    Args:
        token (str | Unset):
        user (str | Unset):
        types (str | Unset):
        exclude_archived (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
types=types,
exclude_archived=exclude_archived,
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
    user: str | Unset = UNSET,
    types: str | Unset = UNSET,
    exclude_archived: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema | None:
    """  List conversations the calling user may access.

    Args:
        token (str | Unset):
        user (str | Unset):
        types (str | Unset):
        exclude_archived (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
user=user,
types=types,
exclude_archived=exclude_archived,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    types: str | Unset = UNSET,
    exclude_archived: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema]:
    """  List conversations the calling user may access.

    Args:
        token (str | Unset):
        user (str | Unset):
        types (str | Unset):
        exclude_archived (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
types=types,
exclude_archived=exclude_archived,
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
    user: str | Unset = UNSET,
    types: str | Unset = UNSET,
    exclude_archived: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema | None:
    """  List conversations the calling user may access.

    Args:
        token (str | Unset):
        user (str | Unset):
        types (str | Unset):
        exclude_archived (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersConversationsUsersConversationsErrorSchema | UsersConversationsUsersConversationsSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
user=user,
types=types,
exclude_archived=exclude_archived,
limit=limit,
cursor=cursor,

    )).parsed
