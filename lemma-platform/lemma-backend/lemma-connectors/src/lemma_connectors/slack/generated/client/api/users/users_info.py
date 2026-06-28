from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_info_users_info_error_schema import UsersInfoUsersInfoErrorSchema
from ...models.users_info_users_info_success_schema import UsersInfoUsersInfoSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    include_locale: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["include_locale"] = include_locale

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema:
    if response.status_code == 200:
        response_200 = UsersInfoUsersInfoSuccessSchema.from_dict(response.json())



        return response_200

    response_default = UsersInfoUsersInfoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema]:
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
    include_locale: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema]:
    """  Gets information about a user.

    Args:
        token (str):
        include_locale (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
include_locale=include_locale,
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
    include_locale: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema | None:
    """  Gets information about a user.

    Args:
        token (str):
        include_locale (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
include_locale=include_locale,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    include_locale: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema]:
    """  Gets information about a user.

    Args:
        token (str):
        include_locale (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
include_locale=include_locale,
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
    include_locale: bool | Unset = UNSET,
    user: str | Unset = UNSET,

) -> UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema | None:
    """  Gets information about a user.

    Args:
        token (str):
        include_locale (bool | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersInfoUsersInfoErrorSchema | UsersInfoUsersInfoSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
include_locale=include_locale,
user=user,

    )).parsed
