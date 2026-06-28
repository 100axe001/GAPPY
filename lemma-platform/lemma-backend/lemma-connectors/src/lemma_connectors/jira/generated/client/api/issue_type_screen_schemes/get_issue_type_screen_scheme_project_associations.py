from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_issue_type_screen_schemes_projects import PageBeanIssueTypeScreenSchemesProjects
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_project_id = project_id


    params["projectId"] = json_project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetypescreenscheme/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueTypeScreenSchemesProjects | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueTypeScreenSchemesProjects.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueTypeScreenSchemesProjects]:
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
    project_id: list[int],

) -> Response[Any | PageBeanIssueTypeScreenSchemesProjects]:
    """ Get issue type screen schemes for projects

     Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen
    scheme, a list of the projects that use it.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScreenSchemesProjects]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
project_id=project_id,

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
    project_id: list[int],

) -> Any | PageBeanIssueTypeScreenSchemesProjects | None:
    """ Get issue type screen schemes for projects

     Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen
    scheme, a list of the projects that use it.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScreenSchemesProjects
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> Response[Any | PageBeanIssueTypeScreenSchemesProjects]:
    """ Get issue type screen schemes for projects

     Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen
    scheme, a list of the projects that use it.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScreenSchemesProjects]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
project_id=project_id,

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
    project_id: list[int],

) -> Any | PageBeanIssueTypeScreenSchemesProjects | None:
    """ Get issue type screen schemes for projects

     Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen
    scheme, a list of the projects that use it.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScreenSchemesProjects
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    )).parsed
