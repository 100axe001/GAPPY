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
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    property_: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["username"] = username

    params["accountId"] = account_id

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["property"] = property_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/search",
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
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    property_: str | Unset = UNSET,

) -> Response[Any | list[User]]:
    """ Find users

     Returns a list of users that match the search string and property.

    This operation first applies a filter to match the search string and property, and then takes the
    filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get
    all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-
    search-get) and filter the records in your code.

    This operation can be accessed anonymously.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without
    the required permission return empty search results.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        property_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
username=username,
account_id=account_id,
start_at=start_at,
max_results=max_results,
property_=property_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    property_: str | Unset = UNSET,

) -> Any | list[User] | None:
    """ Find users

     Returns a list of users that match the search string and property.

    This operation first applies a filter to match the search string and property, and then takes the
    filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get
    all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-
    search-get) and filter the records in your code.

    This operation can be accessed anonymously.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without
    the required permission return empty search results.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        property_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return sync_detailed(
        client=client,
query=query,
username=username,
account_id=account_id,
start_at=start_at,
max_results=max_results,
property_=property_,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    property_: str | Unset = UNSET,

) -> Response[Any | list[User]]:
    """ Find users

     Returns a list of users that match the search string and property.

    This operation first applies a filter to match the search string and property, and then takes the
    filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get
    all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-
    search-get) and filter the records in your code.

    This operation can be accessed anonymously.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without
    the required permission return empty search results.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        property_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
username=username,
account_id=account_id,
start_at=start_at,
max_results=max_results,
property_=property_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    property_: str | Unset = UNSET,

) -> Any | list[User] | None:
    """ Find users

     Returns a list of users that match the search string and property.

    This operation first applies a filter to match the search string and property, and then takes the
    filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get
    all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-
    search-get) and filter the records in your code.

    This operation can be accessed anonymously.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without
    the required permission return empty search results.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        property_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return (await asyncio_detailed(
        client=client,
query=query,
username=username,
account_id=account_id,
start_at=start_at,
max_results=max_results,
property_=property_,

    )).parsed
