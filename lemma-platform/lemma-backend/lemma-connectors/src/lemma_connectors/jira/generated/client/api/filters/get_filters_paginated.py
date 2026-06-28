from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_filters_paginated_order_by import GetFiltersPaginatedOrderBy
from ...models.page_bean_filter_details import PageBeanFilterDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    filter_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    order_by: GetFiltersPaginatedOrderBy | Unset = GetFiltersPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["filterName"] = filter_name

    params["accountId"] = account_id

    params["owner"] = owner

    params["groupname"] = groupname

    params["groupId"] = group_id

    params["projectId"] = project_id

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["expand"] = expand

    params["overrideSharePermissions"] = override_share_permissions


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/filter/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | PageBeanFilterDetails | None:
    if response.status_code == 200:
        response_200 = PageBeanFilterDetails.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | PageBeanFilterDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    order_by: GetFiltersPaginatedOrderBy | Unset = GetFiltersPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Response[Any | ErrorCollection | PageBeanFilterDetails]:
    """ Search for filters

     Returns a [paginated](#pagination) list of filters. Use this operation to get:

     *  specific filters, by defining `id` only.
     *  filters that match all of the specified attributes. For example, all filters for a user with a
    particular word in their name. When multiple attributes are specified only filters matching all
    attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, only the following filters that match the
    query parameters are returned:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        filter_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        id (list[int] | Unset):
        order_by (GetFiltersPaginatedOrderBy | Unset):  Default: GetFiltersPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanFilterDetails]
     """


    kwargs = _get_kwargs(
        filter_name=filter_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
id=id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
expand=expand,
override_share_permissions=override_share_permissions,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    filter_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    order_by: GetFiltersPaginatedOrderBy | Unset = GetFiltersPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Any | ErrorCollection | PageBeanFilterDetails | None:
    """ Search for filters

     Returns a [paginated](#pagination) list of filters. Use this operation to get:

     *  specific filters, by defining `id` only.
     *  filters that match all of the specified attributes. For example, all filters for a user with a
    particular word in their name. When multiple attributes are specified only filters matching all
    attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, only the following filters that match the
    query parameters are returned:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        filter_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        id (list[int] | Unset):
        order_by (GetFiltersPaginatedOrderBy | Unset):  Default: GetFiltersPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanFilterDetails
     """


    return sync_detailed(
        client=client,
filter_name=filter_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
id=id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
expand=expand,
override_share_permissions=override_share_permissions,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    order_by: GetFiltersPaginatedOrderBy | Unset = GetFiltersPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Response[Any | ErrorCollection | PageBeanFilterDetails]:
    """ Search for filters

     Returns a [paginated](#pagination) list of filters. Use this operation to get:

     *  specific filters, by defining `id` only.
     *  filters that match all of the specified attributes. For example, all filters for a user with a
    particular word in their name. When multiple attributes are specified only filters matching all
    attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, only the following filters that match the
    query parameters are returned:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        filter_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        id (list[int] | Unset):
        order_by (GetFiltersPaginatedOrderBy | Unset):  Default: GetFiltersPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanFilterDetails]
     """


    kwargs = _get_kwargs(
        filter_name=filter_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
id=id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
expand=expand,
override_share_permissions=override_share_permissions,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    id: list[int] | Unset = UNSET,
    order_by: GetFiltersPaginatedOrderBy | Unset = GetFiltersPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Any | ErrorCollection | PageBeanFilterDetails | None:
    """ Search for filters

     Returns a [paginated](#pagination) list of filters. Use this operation to get:

     *  specific filters, by defining `id` only.
     *  filters that match all of the specified attributes. For example, all filters for a user with a
    particular word in their name. When multiple attributes are specified only filters matching all
    attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, only the following filters that match the
    query parameters are returned:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        filter_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        id (list[int] | Unset):
        order_by (GetFiltersPaginatedOrderBy | Unset):  Default: GetFiltersPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanFilterDetails
     """


    return (await asyncio_detailed(
        client=client,
filter_name=filter_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
id=id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
expand=expand,
override_share_permissions=override_share_permissions,

    )).parsed
