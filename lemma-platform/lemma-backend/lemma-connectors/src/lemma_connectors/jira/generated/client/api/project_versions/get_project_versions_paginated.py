from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_versions_paginated_order_by import GetProjectVersionsPaginatedOrderBy
from ...models.page_bean_version import PageBeanVersion
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectVersionsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,
    status: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["query"] = query

    params["status"] = status

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/version".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanVersion | None:
    if response.status_code == 200:
        response_200 = PageBeanVersion.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectVersionsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,
    status: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanVersion]:
    """ Get project versions paginated

     Returns a [paginated](#pagination) list of all versions in a project. See the [Get project
    versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full
    list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectVersionsPaginatedOrderBy | Unset):
        query (str | Unset):
        status (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanVersion]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,
status=status,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectVersionsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,
    status: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageBeanVersion | None:
    """ Get project versions paginated

     Returns a [paginated](#pagination) list of all versions in a project. See the [Get project
    versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full
    list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectVersionsPaginatedOrderBy | Unset):
        query (str | Unset):
        status (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanVersion
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,
status=status,
expand=expand,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectVersionsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,
    status: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanVersion]:
    """ Get project versions paginated

     Returns a [paginated](#pagination) list of all versions in a project. See the [Get project
    versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full
    list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectVersionsPaginatedOrderBy | Unset):
        query (str | Unset):
        status (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanVersion]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,
status=status,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectVersionsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,
    status: str | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageBeanVersion | None:
    """ Get project versions paginated

     Returns a [paginated](#pagination) list of all versions in a project. See the [Get project
    versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full
    list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectVersionsPaginatedOrderBy | Unset):
        query (str | Unset):
        status (str | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanVersion
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,
status=status,
expand=expand,

    )).parsed
