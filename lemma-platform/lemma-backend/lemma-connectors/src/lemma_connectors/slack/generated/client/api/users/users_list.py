from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_list_users_list_error_schema import UsersListUsersListErrorSchema
from ...models.users_list_users_list_schema import UsersListUsersListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["limit"] = limit

    params["cursor"] = cursor

    params["include_locale"] = include_locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersListUsersListErrorSchema | UsersListUsersListSchema:
    if response.status_code == 200:
        response_200 = UsersListUsersListSchema.from_dict(response.json())



        return response_200

    response_default = UsersListUsersListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersListUsersListErrorSchema | UsersListUsersListSchema]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,

) -> Response[UsersListUsersListErrorSchema | UsersListUsersListSchema]:
    """  Lists all users in a Slack team.

    Args:
        token (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        include_locale (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersListUsersListErrorSchema | UsersListUsersListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
limit=limit,
cursor=cursor,
include_locale=include_locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,

) -> UsersListUsersListErrorSchema | UsersListUsersListSchema | None:
    """  Lists all users in a Slack team.

    Args:
        token (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        include_locale (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersListUsersListErrorSchema | UsersListUsersListSchema
     """


    return sync_detailed(
        client=client,
token=token,
limit=limit,
cursor=cursor,
include_locale=include_locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,

) -> Response[UsersListUsersListErrorSchema | UsersListUsersListSchema]:
    """  Lists all users in a Slack team.

    Args:
        token (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        include_locale (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersListUsersListErrorSchema | UsersListUsersListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
limit=limit,
cursor=cursor,
include_locale=include_locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    include_locale: bool | Unset = UNSET,

) -> UsersListUsersListErrorSchema | UsersListUsersListSchema | None:
    """  Lists all users in a Slack team.

    Args:
        token (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        include_locale (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersListUsersListErrorSchema | UsersListUsersListSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
limit=limit,
cursor=cursor,
include_locale=include_locale,

    )).parsed
