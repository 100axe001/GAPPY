from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_fields_paginated_order_by import GetFieldsPaginatedOrderBy
from ...models.get_fields_paginated_type_item import GetFieldsPaginatedTypeItem
from ...models.page_bean_field import PageBeanField
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    type_: list[GetFieldsPaginatedTypeItem] | Unset = UNSET,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    order_by: GetFieldsPaginatedOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)


    params["type"] = json_type_

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["query"] = query

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/search",
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
    type_: list[GetFieldsPaginatedTypeItem] | Unset = UNSET,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    order_by: GetFieldsPaginatedOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanField]:
    """ Get fields paginated

     Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

     *  all fields
     *  specific fields, by defining `id`
     *  fields that contain a string in the field name or description, by defining `query`
     *  specific fields that contain a string in the field name or description, by defining `id` and
    `query`

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        type_ (list[GetFieldsPaginatedTypeItem] | Unset):
        id (list[str] | Unset):
        query (str | Unset):
        order_by (GetFieldsPaginatedOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanField]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
type_=type_,
id=id,
query=query,
order_by=order_by,
expand=expand,

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
    type_: list[GetFieldsPaginatedTypeItem] | Unset = UNSET,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    order_by: GetFieldsPaginatedOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanField | None:
    """ Get fields paginated

     Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

     *  all fields
     *  specific fields, by defining `id`
     *  fields that contain a string in the field name or description, by defining `query`
     *  specific fields that contain a string in the field name or description, by defining `id` and
    `query`

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        type_ (list[GetFieldsPaginatedTypeItem] | Unset):
        id (list[str] | Unset):
        query (str | Unset):
        order_by (GetFieldsPaginatedOrderBy | Unset):
        expand (str | Unset):

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
type_=type_,
id=id,
query=query,
order_by=order_by,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    type_: list[GetFieldsPaginatedTypeItem] | Unset = UNSET,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    order_by: GetFieldsPaginatedOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanField]:
    """ Get fields paginated

     Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

     *  all fields
     *  specific fields, by defining `id`
     *  fields that contain a string in the field name or description, by defining `query`
     *  specific fields that contain a string in the field name or description, by defining `id` and
    `query`

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        type_ (list[GetFieldsPaginatedTypeItem] | Unset):
        id (list[str] | Unset):
        query (str | Unset):
        order_by (GetFieldsPaginatedOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanField]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
type_=type_,
id=id,
query=query,
order_by=order_by,
expand=expand,

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
    type_: list[GetFieldsPaginatedTypeItem] | Unset = UNSET,
    id: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    order_by: GetFieldsPaginatedOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanField | None:
    """ Get fields paginated

     Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:

     *  all fields
     *  specific fields, by defining `id`
     *  fields that contain a string in the field name or description, by defining `query`
     *  specific fields that contain a string in the field name or description, by defining `id` and
    `query`

    Only custom fields can be queried, `type` must be set to `custom`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        type_ (list[GetFieldsPaginatedTypeItem] | Unset):
        id (list[str] | Unset):
        query (str | Unset):
        order_by (GetFieldsPaginatedOrderBy | Unset):
        expand (str | Unset):

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
type_=type_,
id=id,
query=query,
order_by=order_by,
expand=expand,

    )).parsed
