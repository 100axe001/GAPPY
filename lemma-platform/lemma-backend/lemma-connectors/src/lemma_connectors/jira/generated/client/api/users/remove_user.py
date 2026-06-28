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
    account_id: str,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["username"] = username

    params["key"] = key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/user",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
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
    account_id: str,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete user

     Deletes a user. If the operation completes successfully then the user is removed from Jira's user
    base. This operation does not delete the user's Atlassian account.

    **[Permissions](#permissions) required:** Site administration (that is, membership of the *site-
    admin* [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        account_id (str):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,
key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete user

     Deletes a user. If the operation completes successfully then the user is removed from Jira's user
    base. This operation does not delete the user's Atlassian account.

    **[Permissions](#permissions) required:** Site administration (that is, membership of the *site-
    admin* [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        account_id (str):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,
key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

