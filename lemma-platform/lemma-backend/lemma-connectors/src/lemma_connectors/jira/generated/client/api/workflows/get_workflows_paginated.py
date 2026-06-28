from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_workflows_paginated_order_by import GetWorkflowsPaginatedOrderBy
from ...models.page_bean_workflow import PageBeanWorkflow
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    workflow_name: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    query_string: str | Unset = UNSET,
    order_by: GetWorkflowsPaginatedOrderBy | Unset = UNSET,
    is_active: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_workflow_name: list[str] | Unset = UNSET
    if not isinstance(workflow_name, Unset):
        json_workflow_name = workflow_name


    params["workflowName"] = json_workflow_name

    params["expand"] = expand

    params["queryString"] = query_string

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["isActive"] = is_active


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/workflow/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | PageBeanWorkflow | None:
    if response.status_code == 200:
        response_200 = PageBeanWorkflow.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | PageBeanWorkflow]:
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
    workflow_name: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    query_string: str | Unset = UNSET,
    order_by: GetWorkflowsPaginatedOrderBy | Unset = UNSET,
    is_active: bool | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanWorkflow]:
    """ Get workflows paginated

     Returns a [paginated](#pagination) list of published classic workflows. When workflow names are
    specified, details of those workflows are returned. Otherwise, all published classic workflows are
    returned.

    This operation does not return next-gen workflows.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        workflow_name (list[str] | Unset):
        expand (str | Unset):
        query_string (str | Unset):
        order_by (GetWorkflowsPaginatedOrderBy | Unset):
        is_active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanWorkflow]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
workflow_name=workflow_name,
expand=expand,
query_string=query_string,
order_by=order_by,
is_active=is_active,

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
    workflow_name: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    query_string: str | Unset = UNSET,
    order_by: GetWorkflowsPaginatedOrderBy | Unset = UNSET,
    is_active: bool | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanWorkflow | None:
    """ Get workflows paginated

     Returns a [paginated](#pagination) list of published classic workflows. When workflow names are
    specified, details of those workflows are returned. Otherwise, all published classic workflows are
    returned.

    This operation does not return next-gen workflows.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        workflow_name (list[str] | Unset):
        expand (str | Unset):
        query_string (str | Unset):
        order_by (GetWorkflowsPaginatedOrderBy | Unset):
        is_active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanWorkflow
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
workflow_name=workflow_name,
expand=expand,
query_string=query_string,
order_by=order_by,
is_active=is_active,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    workflow_name: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    query_string: str | Unset = UNSET,
    order_by: GetWorkflowsPaginatedOrderBy | Unset = UNSET,
    is_active: bool | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanWorkflow]:
    """ Get workflows paginated

     Returns a [paginated](#pagination) list of published classic workflows. When workflow names are
    specified, details of those workflows are returned. Otherwise, all published classic workflows are
    returned.

    This operation does not return next-gen workflows.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        workflow_name (list[str] | Unset):
        expand (str | Unset):
        query_string (str | Unset):
        order_by (GetWorkflowsPaginatedOrderBy | Unset):
        is_active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanWorkflow]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
workflow_name=workflow_name,
expand=expand,
query_string=query_string,
order_by=order_by,
is_active=is_active,

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
    workflow_name: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    query_string: str | Unset = UNSET,
    order_by: GetWorkflowsPaginatedOrderBy | Unset = UNSET,
    is_active: bool | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanWorkflow | None:
    """ Get workflows paginated

     Returns a [paginated](#pagination) list of published classic workflows. When workflow names are
    specified, details of those workflows are returned. Otherwise, all published classic workflows are
    returned.

    This operation does not return next-gen workflows.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        workflow_name (list[str] | Unset):
        expand (str | Unset):
        query_string (str | Unset):
        order_by (GetWorkflowsPaginatedOrderBy | Unset):
        is_active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanWorkflow
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
workflow_name=workflow_name,
expand=expand,
query_string=query_string,
order_by=order_by,
is_active=is_active,

    )).parsed
