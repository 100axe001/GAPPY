from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_profile_get_users_profile_get_error_schema import UsersProfileGetUsersProfileGetErrorSchema
from ...models.users_profile_get_users_profile_get_schema import UsersProfileGetUsersProfileGetSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    include_labels: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["include_labels"] = include_labels

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.profile.get",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema:
    if response.status_code == 200:
        response_200 = UsersProfileGetUsersProfileGetSchema.from_dict(response.json())



        return response_200

    response_default = UsersProfileGetUsersProfileGetErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema]:
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
    include_labels: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema]:
    """  Retrieves a user's profile information.

    Args:
        token (str):
        include_labels (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema]
     """


    kwargs = _get_kwargs(
        token=token,
include_labels=include_labels,
user=user,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    include_labels: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema | None:
    """  Retrieves a user's profile information.

    Args:
        token (str):
        include_labels (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema
     """


    return sync_detailed(
        client=client,
token=token,
include_labels=include_labels,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    include_labels: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema]:
    """  Retrieves a user's profile information.

    Args:
        token (str):
        include_labels (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema]
     """


    kwargs = _get_kwargs(
        token=token,
include_labels=include_labels,
user=user,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    include_labels: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema | None:
    """  Retrieves a user's profile information.

    Args:
        token (str):
        include_labels (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersProfileGetUsersProfileGetErrorSchema | UsersProfileGetUsersProfileGetSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
include_labels=include_labels,
user=user,

    )).parsed
