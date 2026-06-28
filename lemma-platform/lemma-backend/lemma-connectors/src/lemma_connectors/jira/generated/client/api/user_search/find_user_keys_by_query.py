from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_user_key import PageBeanUserKey
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/search/query/key",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanUserKey | None:
    if response.status_code == 200:
        response_200 = PageBeanUserKey.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 408:
        response_408 = cast(Any, None)
        return response_408

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanUserKey]:
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
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanUserKey]:
    r""" Find user keys by query

     Finds users with a structured query and returns a [paginated](#pagination) list of user keys.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the structured query.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    The query statements are:

     *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project
    *PROJ*.
     *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
     *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues
    *PROJ-1* or *PROJ-2*.
     *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues
    *PROJ-1* or *PROJ-2*.
     *  `[propertyKey].entity.property.path is \"property value\"` Returns users with the entity
    property value.

    The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can
    be combined using the `AND` and `OR` operators to form more complex queries. For example:

    `is assignee of PROJ AND [propertyKey].entity.property.path is \"property value\"`

    Args:
        query (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanUserKey]
     """


    kwargs = _get_kwargs(
        query=query,
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
    query: str,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanUserKey | None:
    r""" Find user keys by query

     Finds users with a structured query and returns a [paginated](#pagination) list of user keys.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the structured query.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    The query statements are:

     *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project
    *PROJ*.
     *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
     *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues
    *PROJ-1* or *PROJ-2*.
     *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues
    *PROJ-1* or *PROJ-2*.
     *  `[propertyKey].entity.property.path is \"property value\"` Returns users with the entity
    property value.

    The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can
    be combined using the `AND` and `OR` operators to form more complex queries. For example:

    `is assignee of PROJ AND [propertyKey].entity.property.path is \"property value\"`

    Args:
        query (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanUserKey
     """


    return sync_detailed(
        client=client,
query=query,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanUserKey]:
    r""" Find user keys by query

     Finds users with a structured query and returns a [paginated](#pagination) list of user keys.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the structured query.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    The query statements are:

     *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project
    *PROJ*.
     *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
     *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues
    *PROJ-1* or *PROJ-2*.
     *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues
    *PROJ-1* or *PROJ-2*.
     *  `[propertyKey].entity.property.path is \"property value\"` Returns users with the entity
    property value.

    The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can
    be combined using the `AND` and `OR` operators to form more complex queries. For example:

    `is assignee of PROJ AND [propertyKey].entity.property.path is \"property value\"`

    Args:
        query (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanUserKey]
     """


    kwargs = _get_kwargs(
        query=query,
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
    query: str,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanUserKey | None:
    r""" Find user keys by query

     Finds users with a structured query and returns a [paginated](#pagination) list of user keys.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the structured query.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    The query statements are:

     *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project
    *PROJ*.
     *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or
    *PROJ-2*.
     *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.
     *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues
    *PROJ-1* or *PROJ-2*.
     *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues
    *PROJ-1* or *PROJ-2*.
     *  `[propertyKey].entity.property.path is \"property value\"` Returns users with the entity
    property value.

    The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can
    be combined using the `AND` and `OR` operators to form more complex queries. For example:

    `is assignee of PROJ AND [propertyKey].entity.property.path is \"property value\"`

    Args:
        query (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanUserKey
     """


    return (await asyncio_detailed(
        client=client,
query=query,
start_at=start_at,
max_results=max_results,

    )).parsed
