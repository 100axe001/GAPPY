from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["username"] = username

    params["key"] = key

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | User | None:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | User]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | User]:
    """ Get user

     Returns a user.

    Privacy controls are applied to the response based on the user's preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,
key=key,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | User | None:
    """ Get user

     Returns a user.

    Privacy controls are applied to the response based on the user's preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
     """


    return sync_detailed(
        client=client,
account_id=account_id,
username=username,
key=key,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | User]:
    """ Get user

     Returns a user.

    Privacy controls are applied to the response based on the user's preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,
key=key,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    key: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | User | None:
    """ Get user

     Returns a user.

    Privacy controls are applied to the response based on the user's preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):
        key (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
username=username,
key=key,
expand=expand,

    )).parsed
