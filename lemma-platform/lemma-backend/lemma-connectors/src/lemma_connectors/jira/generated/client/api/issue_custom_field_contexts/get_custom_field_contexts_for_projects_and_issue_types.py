from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_context_for_project_and_issue_type import PageBeanContextForProjectAndIssueType
from ...models.project_issue_type_mappings import ProjectIssueTypeMappings
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id: str,
    *,
    body: ProjectIssueTypeMappings,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/field/{field_id}/context/mapping".format(field_id=quote(str(field_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanContextForProjectAndIssueType | None:
    if response.status_code == 200:
        response_200 = PageBeanContextForProjectAndIssueType.from_dict(response.json())



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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanContextForProjectAndIssueType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectIssueTypeMappings,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanContextForProjectAndIssueType]:
    """ Get custom field contexts for projects and issue types

     Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping,
    the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the
    project and issue type.

    If there is no custom field context assigned to the project then, if present, the custom field
    context that applies to all projects is returned if it also applies to the issue type or all issue
    types. If a custom field context is not found, the returned custom field context ID is `null`.

    Duplicate project and issue type mappings cannot be provided in the request.

    The order of the returned values is the same as provided in the request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        body (ProjectIssueTypeMappings): The project and issue type mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContextForProjectAndIssueType]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
body=body,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectIssueTypeMappings,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanContextForProjectAndIssueType | None:
    """ Get custom field contexts for projects and issue types

     Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping,
    the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the
    project and issue type.

    If there is no custom field context assigned to the project then, if present, the custom field
    context that applies to all projects is returned if it also applies to the issue type or all issue
    types. If a custom field context is not found, the returned custom field context ID is `null`.

    Duplicate project and issue type mappings cannot be provided in the request.

    The order of the returned values is the same as provided in the request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        body (ProjectIssueTypeMappings): The project and issue type mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContextForProjectAndIssueType
     """


    return sync_detailed(
        field_id=field_id,
client=client,
body=body,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectIssueTypeMappings,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanContextForProjectAndIssueType]:
    """ Get custom field contexts for projects and issue types

     Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping,
    the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the
    project and issue type.

    If there is no custom field context assigned to the project then, if present, the custom field
    context that applies to all projects is returned if it also applies to the issue type or all issue
    types. If a custom field context is not found, the returned custom field context ID is `null`.

    Duplicate project and issue type mappings cannot be provided in the request.

    The order of the returned values is the same as provided in the request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        body (ProjectIssueTypeMappings): The project and issue type mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContextForProjectAndIssueType]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
body=body,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectIssueTypeMappings,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanContextForProjectAndIssueType | None:
    """ Get custom field contexts for projects and issue types

     Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping,
    the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the
    project and issue type.

    If there is no custom field context assigned to the project then, if present, the custom field
    context that applies to all projects is returned if it also applies to the issue type or all issue
    types. If a custom field context is not found, the returned custom field context ID is `null`.

    Duplicate project and issue type mappings cannot be provided in the request.

    The order of the returned values is the same as provided in the request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        body (ProjectIssueTypeMappings): The project and issue type mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContextForProjectAndIssueType
     """


    return (await asyncio_detailed(
        field_id=field_id,
client=client,
body=body,
start_at=start_at,
max_results=max_results,

    )).parsed
