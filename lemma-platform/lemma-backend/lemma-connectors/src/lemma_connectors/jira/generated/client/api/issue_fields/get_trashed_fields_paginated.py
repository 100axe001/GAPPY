from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_trashed_fields_paginated_expand import GetTrashedFieldsPaginatedExpand
from ...models.page_bean_field import PageBeanField
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    expand: GetTrashedFieldsPaginatedExpand | Unset = UNSET,
    order_by: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["query"] = query

    json_expand: str | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand.value

    params["expand"] = json_expand

    params["orderBy"] = order_by


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/search/trashed",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | PageBeanField | None:
    if response.status_code == 200:
        response_200 = PageBeanField.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | PageBeanField]:
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
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    expand: GetTrashedFieldsPaginatedExpand | Unset = UNSET,
    order_by: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanField]:
    """ Get fields in trash paginated

     Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields
    whose field name or description partially match a string.

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[str] | Unset):
        query (str | Unset):
        expand (GetTrashedFieldsPaginatedExpand | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanField]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query=query,
expand=expand,
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
    max_results: int | Unset = 50,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    expand: GetTrashedFieldsPaginatedExpand | Unset = UNSET,
    order_by: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanField | None:
    """ Get fields in trash paginated

     Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields
    whose field name or description partially match a string.

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[str] | Unset):
        query (str | Unset):
        expand (GetTrashedFieldsPaginatedExpand | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanField
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query=query,
expand=expand,
order_by=order_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    expand: GetTrashedFieldsPaginatedExpand | Unset = UNSET,
    order_by: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanField]:
    """ Get fields in trash paginated

     Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields
    whose field name or description partially match a string.

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[str] | Unset):
        query (str | Unset):
        expand (GetTrashedFieldsPaginatedExpand | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanField]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query=query,
expand=expand,
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
    max_results: int | Unset = 50,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    expand: GetTrashedFieldsPaginatedExpand | Unset = UNSET,
    order_by: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanField | None:
    """ Get fields in trash paginated

     Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields
    whose field name or description partially match a string.

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[str] | Unset):
        query (str | Unset):
        expand (GetTrashedFieldsPaginatedExpand | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanField
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query=query,
expand=expand,
order_by=order_by,

    )).parsed
