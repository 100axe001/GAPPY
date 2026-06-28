from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_get_presence_api_method_users_get_presence import UsersGetPresenceAPIMethodUsersGetPresence
from ...models.users_get_presence_users_counts_error_schema import UsersGetPresenceUsersCountsErrorSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    user: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.getPresence",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema:
    if response.status_code == 200:
        response_200 = UsersGetPresenceAPIMethodUsersGetPresence.from_dict(response.json())



        return response_200

    response_default = UsersGetPresenceUsersCountsErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema]:
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
    user: str | Unset = UNSET,

) -> Response[UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema]:
    """  Gets user presence information.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema]
     """


    kwargs = _get_kwargs(
        token=token,
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
    user: str | Unset = UNSET,

) -> UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema | None:
    """  Gets user presence information.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema
     """


    return sync_detailed(
        client=client,
token=token,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,

) -> Response[UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema]:
    """  Gets user presence information.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema]
     """


    kwargs = _get_kwargs(
        token=token,
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
    user: str | Unset = UNSET,

) -> UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema | None:
    """  Gets user presence information.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersGetPresenceAPIMethodUsersGetPresence | UsersGetPresenceUsersCountsErrorSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
user=user,

    )).parsed
