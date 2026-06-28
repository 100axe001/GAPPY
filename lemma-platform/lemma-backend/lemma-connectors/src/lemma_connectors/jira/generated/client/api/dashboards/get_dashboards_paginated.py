from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_dashboards_paginated_order_by import GetDashboardsPaginatedOrderBy
from ...models.get_dashboards_paginated_status import GetDashboardsPaginatedStatus
from ...models.page_bean_dashboard import PageBeanDashboard
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    dashboard_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    order_by: GetDashboardsPaginatedOrderBy | Unset = GetDashboardsPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    status: GetDashboardsPaginatedStatus | Unset = GetDashboardsPaginatedStatus.ACTIVE,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["dashboardName"] = dashboard_name

    params["accountId"] = account_id

    params["owner"] = owner

    params["groupname"] = groupname

    params["groupId"] = group_id

    params["projectId"] = project_id

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | PageBeanDashboard | None:
    if response.status_code == 200:
        response_200 = PageBeanDashboard.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | PageBeanDashboard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dashboard_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    order_by: GetDashboardsPaginatedOrderBy | Unset = GetDashboardsPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    status: GetDashboardsPaginatedStatus | Unset = GetDashboardsPaginatedStatus.ACTIVE,
    expand: str | Unset = UNSET,

) -> Response[ErrorCollection | PageBeanDashboard]:
    """ Search for dashboards

     Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get
    dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include
    dashboards that have specific attributes. For example, dashboards with a particular name. When
    multiple attributes are specified only filters matching all attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The following dashboards that match the query parameters
    are returned:

     *  Dashboards owned by the user. Not returned for anonymous users.
     *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
     *  Dashboards shared with a private project that the user can browse. Not returned for anonymous
    users.
     *  Dashboards shared with a public project.
     *  Dashboards shared with the public.

    Args:
        dashboard_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        order_by (GetDashboardsPaginatedOrderBy | Unset):  Default:
            GetDashboardsPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        status (GetDashboardsPaginatedStatus | Unset):  Default:
            GetDashboardsPaginatedStatus.ACTIVE.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanDashboard]
     """


    kwargs = _get_kwargs(
        dashboard_name=dashboard_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
status=status,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    dashboard_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    order_by: GetDashboardsPaginatedOrderBy | Unset = GetDashboardsPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    status: GetDashboardsPaginatedStatus | Unset = GetDashboardsPaginatedStatus.ACTIVE,
    expand: str | Unset = UNSET,

) -> ErrorCollection | PageBeanDashboard | None:
    """ Search for dashboards

     Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get
    dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include
    dashboards that have specific attributes. For example, dashboards with a particular name. When
    multiple attributes are specified only filters matching all attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The following dashboards that match the query parameters
    are returned:

     *  Dashboards owned by the user. Not returned for anonymous users.
     *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
     *  Dashboards shared with a private project that the user can browse. Not returned for anonymous
    users.
     *  Dashboards shared with a public project.
     *  Dashboards shared with the public.

    Args:
        dashboard_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        order_by (GetDashboardsPaginatedOrderBy | Unset):  Default:
            GetDashboardsPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        status (GetDashboardsPaginatedStatus | Unset):  Default:
            GetDashboardsPaginatedStatus.ACTIVE.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanDashboard
     """


    return sync_detailed(
        client=client,
dashboard_name=dashboard_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
status=status,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dashboard_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    order_by: GetDashboardsPaginatedOrderBy | Unset = GetDashboardsPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    status: GetDashboardsPaginatedStatus | Unset = GetDashboardsPaginatedStatus.ACTIVE,
    expand: str | Unset = UNSET,

) -> Response[ErrorCollection | PageBeanDashboard]:
    """ Search for dashboards

     Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get
    dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include
    dashboards that have specific attributes. For example, dashboards with a particular name. When
    multiple attributes are specified only filters matching all attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The following dashboards that match the query parameters
    are returned:

     *  Dashboards owned by the user. Not returned for anonymous users.
     *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
     *  Dashboards shared with a private project that the user can browse. Not returned for anonymous
    users.
     *  Dashboards shared with a public project.
     *  Dashboards shared with the public.

    Args:
        dashboard_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        order_by (GetDashboardsPaginatedOrderBy | Unset):  Default:
            GetDashboardsPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        status (GetDashboardsPaginatedStatus | Unset):  Default:
            GetDashboardsPaginatedStatus.ACTIVE.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanDashboard]
     """


    kwargs = _get_kwargs(
        dashboard_name=dashboard_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
status=status,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    dashboard_name: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    project_id: int | Unset = UNSET,
    order_by: GetDashboardsPaginatedOrderBy | Unset = GetDashboardsPaginatedOrderBy.NAME,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    status: GetDashboardsPaginatedStatus | Unset = GetDashboardsPaginatedStatus.ACTIVE,
    expand: str | Unset = UNSET,

) -> ErrorCollection | PageBeanDashboard | None:
    """ Search for dashboards

     Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get
    dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include
    dashboards that have specific attributes. For example, dashboards with a particular name. When
    multiple attributes are specified only filters matching all attributes are returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The following dashboards that match the query parameters
    are returned:

     *  Dashboards owned by the user. Not returned for anonymous users.
     *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.
     *  Dashboards shared with a private project that the user can browse. Not returned for anonymous
    users.
     *  Dashboards shared with a public project.
     *  Dashboards shared with the public.

    Args:
        dashboard_name (str | Unset):
        account_id (str | Unset):
        owner (str | Unset):
        groupname (str | Unset):
        group_id (str | Unset):
        project_id (int | Unset):
        order_by (GetDashboardsPaginatedOrderBy | Unset):  Default:
            GetDashboardsPaginatedOrderBy.NAME.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        status (GetDashboardsPaginatedStatus | Unset):  Default:
            GetDashboardsPaginatedStatus.ACTIVE.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanDashboard
     """


    return (await asyncio_detailed(
        client=client,
dashboard_name=dashboard_name,
account_id=account_id,
owner=owner,
groupname=groupname,
group_id=group_id,
project_id=project_id,
order_by=order_by,
start_at=start_at,
max_results=max_results,
status=status,
expand=expand,

    )).parsed
