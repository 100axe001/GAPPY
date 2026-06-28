from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_screens_order_by import GetScreensOrderBy
from ...models.get_screens_scope_item import GetScreensScopeItem
from ...models.page_bean_screen import PageBeanScreen
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    scope: list[GetScreensScopeItem] | Unset = UNSET,
    order_by: GetScreensOrderBy | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["queryString"] = query_string

    json_scope: list[str] | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = []
        for scope_item_data in scope:
            scope_item = scope_item_data.value
            json_scope.append(scope_item)


    params["scope"] = json_scope

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/screens",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanScreen | None:
    if response.status_code == 200:
        response_200 = PageBeanScreen.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanScreen]:
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
    max_results: int | Unset = 100,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    scope: list[GetScreensScopeItem] | Unset = UNSET,
    order_by: GetScreensOrderBy | Unset = UNSET,

) -> Response[Any | PageBeanScreen]:
    """ Get screens

     Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        scope (list[GetScreensScopeItem] | Unset):
        order_by (GetScreensOrderBy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanScreen]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
scope=scope,
order_by=order_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    scope: list[GetScreensScopeItem] | Unset = UNSET,
    order_by: GetScreensOrderBy | Unset = UNSET,

) -> Any | PageBeanScreen | None:
    """ Get screens

     Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        scope (list[GetScreensScopeItem] | Unset):
        order_by (GetScreensOrderBy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanScreen
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
scope=scope,
order_by=order_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    scope: list[GetScreensScopeItem] | Unset = UNSET,
    order_by: GetScreensOrderBy | Unset = UNSET,

) -> Response[Any | PageBeanScreen]:
    """ Get screens

     Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        scope (list[GetScreensScopeItem] | Unset):
        order_by (GetScreensOrderBy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanScreen]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
scope=scope,
order_by=order_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    scope: list[GetScreensScopeItem] | Unset = UNSET,
    order_by: GetScreensOrderBy | Unset = UNSET,

) -> Any | PageBeanScreen | None:
    """ Get screens

     Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        scope (list[GetScreensScopeItem] | Unset):
        order_by (GetScreensOrderBy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanScreen
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
scope=scope,
order_by=order_by,

    )).parsed
