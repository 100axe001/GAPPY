from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset



def _get_kwargs(
    *,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["groupname"] = groupname

    params["groupId"] = group_id

    params["username"] = username

    params["accountId"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/group/user",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str,

) -> Response[Any]:
    """ Remove user from group

     Removes a user from a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        username (str | Unset):
        account_id (str):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        groupname=groupname,
group_id=group_id,
username=username,
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str,

) -> Response[Any]:
    """ Remove user from group

     Removes a user from a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        username (str | Unset):
        account_id (str):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        groupname=groupname,
group_id=group_id,
username=username,
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

