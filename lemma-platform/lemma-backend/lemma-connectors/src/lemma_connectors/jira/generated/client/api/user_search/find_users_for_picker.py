from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.found_users import FoundUsers
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    exclude: list[str] | Unset = UNSET,
    exclude_account_ids: list[str] | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    exclude_connect_users: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["maxResults"] = max_results

    params["showAvatar"] = show_avatar

    json_exclude: list[str] | Unset = UNSET
    if not isinstance(exclude, Unset):
        json_exclude = exclude


    params["exclude"] = json_exclude

    json_exclude_account_ids: list[str] | Unset = UNSET
    if not isinstance(exclude_account_ids, Unset):
        json_exclude_account_ids = exclude_account_ids


    params["excludeAccountIds"] = json_exclude_account_ids

    params["avatarSize"] = avatar_size

    params["excludeConnectUsers"] = exclude_connect_users


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/picker",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | FoundUsers | None:
    if response.status_code == 200:
        response_200 = FoundUsers.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | FoundUsers]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    exclude: list[str] | Unset = UNSET,
    exclude_account_ids: list[str] | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    exclude_connect_users: bool | Unset = False,

) -> Response[Any | FoundUsers]:
    """ Find users for picker

     Returns a list of users whose attributes match the query term. The returned object includes the
    `html` field where the matched query term is highlighted with the HTML strong tag. A list of account
    IDs can be provided to exclude users from the results.

    This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and
    then returns only the users from that range that match the query term. This means the operation
    usually returns fewer users than specified in `maxResults`. To get all the users who match the query
    term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without
    the required permission return search results for an exact name match only.

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        exclude (list[str] | Unset):
        exclude_account_ids (list[str] | Unset):
        avatar_size (str | Unset):
        exclude_connect_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FoundUsers]
     """


    kwargs = _get_kwargs(
        query=query,
max_results=max_results,
show_avatar=show_avatar,
exclude=exclude,
exclude_account_ids=exclude_account_ids,
avatar_size=avatar_size,
exclude_connect_users=exclude_connect_users,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    exclude: list[str] | Unset = UNSET,
    exclude_account_ids: list[str] | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    exclude_connect_users: bool | Unset = False,

) -> Any | FoundUsers | None:
    """ Find users for picker

     Returns a list of users whose attributes match the query term. The returned object includes the
    `html` field where the matched query term is highlighted with the HTML strong tag. A list of account
    IDs can be provided to exclude users from the results.

    This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and
    then returns only the users from that range that match the query term. This means the operation
    usually returns fewer users than specified in `maxResults`. To get all the users who match the query
    term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without
    the required permission return search results for an exact name match only.

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        exclude (list[str] | Unset):
        exclude_account_ids (list[str] | Unset):
        avatar_size (str | Unset):
        exclude_connect_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FoundUsers
     """


    return sync_detailed(
        client=client,
query=query,
max_results=max_results,
show_avatar=show_avatar,
exclude=exclude,
exclude_account_ids=exclude_account_ids,
avatar_size=avatar_size,
exclude_connect_users=exclude_connect_users,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    exclude: list[str] | Unset = UNSET,
    exclude_account_ids: list[str] | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    exclude_connect_users: bool | Unset = False,

) -> Response[Any | FoundUsers]:
    """ Find users for picker

     Returns a list of users whose attributes match the query term. The returned object includes the
    `html` field where the matched query term is highlighted with the HTML strong tag. A list of account
    IDs can be provided to exclude users from the results.

    This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and
    then returns only the users from that range that match the query term. This means the operation
    usually returns fewer users than specified in `maxResults`. To get all the users who match the query
    term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without
    the required permission return search results for an exact name match only.

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        exclude (list[str] | Unset):
        exclude_account_ids (list[str] | Unset):
        avatar_size (str | Unset):
        exclude_connect_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FoundUsers]
     """


    kwargs = _get_kwargs(
        query=query,
max_results=max_results,
show_avatar=show_avatar,
exclude=exclude,
exclude_account_ids=exclude_account_ids,
avatar_size=avatar_size,
exclude_connect_users=exclude_connect_users,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    exclude: list[str] | Unset = UNSET,
    exclude_account_ids: list[str] | Unset = UNSET,
    avatar_size: str | Unset = UNSET,
    exclude_connect_users: bool | Unset = False,

) -> Any | FoundUsers | None:
    """ Find users for picker

     Returns a list of users whose attributes match the query term. The returned object includes the
    `html` field where the matched query term is highlighted with the HTML strong tag. A list of account
    IDs can be provided to exclude users from the results.

    This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and
    then returns only the users from that range that match the query term. This means the operation
    usually returns fewer users than specified in `maxResults`. To get all the users who match the query
    term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without
    the required permission return search results for an exact name match only.

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        exclude (list[str] | Unset):
        exclude_account_ids (list[str] | Unset):
        avatar_size (str | Unset):
        exclude_connect_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FoundUsers
     """


    return (await asyncio_detailed(
        client=client,
query=query,
max_results=max_results,
show_avatar=show_avatar,
exclude=exclude,
exclude_account_ids=exclude_account_ids,
avatar_size=avatar_size,
exclude_connect_users=exclude_connect_users,

    )).parsed
