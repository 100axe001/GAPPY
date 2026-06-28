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
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/users/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[User] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = User.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | list[User]]:
    """ Get all users

     Returns a list of all users, including active users, inactive users and previously deleted users
    that have an Atlassian account.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | list[User] | None:
    """ Get all users

     Returns a list of all users, including active users, inactive users and previously deleted users
    that have an Atlassian account.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | list[User]]:
    """ Get all users

     Returns a list of all users, including active users, inactive users and previously deleted users
    that have an Atlassian account.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | list[User] | None:
    """ Get all users

     Returns a list of all users, including active users, inactive users and previously deleted users
    that have an Atlassian account.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
