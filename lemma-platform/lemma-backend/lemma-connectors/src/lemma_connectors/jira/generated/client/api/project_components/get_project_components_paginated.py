from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_components_paginated_order_by import GetProjectComponentsPaginatedOrderBy
from ...models.page_bean_component_with_issue_count import PageBeanComponentWithIssueCount
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectComponentsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["query"] = query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/component".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanComponentWithIssueCount | None:
    if response.status_code == 200:
        response_200 = PageBeanComponentWithIssueCount.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanComponentWithIssueCount]:
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
    order_by: GetProjectComponentsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Response[Any | PageBeanComponentWithIssueCount]:
    """ Get project components paginated

     Returns a [paginated](#pagination) list of all components in a project. See the [Get project
    components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a
    full list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectComponentsPaginatedOrderBy | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanComponentWithIssueCount]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,

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
    order_by: GetProjectComponentsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Any | PageBeanComponentWithIssueCount | None:
    """ Get project components paginated

     Returns a [paginated](#pagination) list of all components in a project. See the [Get project
    components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a
    full list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectComponentsPaginatedOrderBy | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanComponentWithIssueCount
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: GetProjectComponentsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Response[Any | PageBeanComponentWithIssueCount]:
    """ Get project components paginated

     Returns a [paginated](#pagination) list of all components in a project. See the [Get project
    components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a
    full list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectComponentsPaginatedOrderBy | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanComponentWithIssueCount]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,

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
    order_by: GetProjectComponentsPaginatedOrderBy | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Any | PageBeanComponentWithIssueCount | None:
    """ Get project components paginated

     Returns a [paginated](#pagination) list of all components in a project. See the [Get project
    components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a
    full list of versions without pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (GetProjectComponentsPaginatedOrderBy | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanComponentWithIssueCount
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
query=query,

    )).parsed
