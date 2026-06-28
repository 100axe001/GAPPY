from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_statuses import PageOfStatuses
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    expand: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 200,
    search_string: str | Unset = UNSET,
    status_category: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand

    params["projectId"] = project_id

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["searchString"] = search_string

    params["statusCategory"] = status_category


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/statuses/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageOfStatuses | None:
    if response.status_code == 200:
        response_200 = PageOfStatuses.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageOfStatuses]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 200,
    search_string: str | Unset = UNSET,
    status_category: str | Unset = UNSET,

) -> Response[Any | PageOfStatuses]:
    """ Search statuses paginated

     Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination)
    list of statuses that match a search on name or project.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        expand (str | Unset):
        project_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 200.
        search_string (str | Unset):
        status_category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfStatuses]
     """


    kwargs = _get_kwargs(
        expand=expand,
project_id=project_id,
start_at=start_at,
max_results=max_results,
search_string=search_string,
status_category=status_category,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 200,
    search_string: str | Unset = UNSET,
    status_category: str | Unset = UNSET,

) -> Any | PageOfStatuses | None:
    """ Search statuses paginated

     Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination)
    list of statuses that match a search on name or project.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        expand (str | Unset):
        project_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 200.
        search_string (str | Unset):
        status_category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfStatuses
     """


    return sync_detailed(
        client=client,
expand=expand,
project_id=project_id,
start_at=start_at,
max_results=max_results,
search_string=search_string,
status_category=status_category,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 200,
    search_string: str | Unset = UNSET,
    status_category: str | Unset = UNSET,

) -> Response[Any | PageOfStatuses]:
    """ Search statuses paginated

     Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination)
    list of statuses that match a search on name or project.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        expand (str | Unset):
        project_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 200.
        search_string (str | Unset):
        status_category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfStatuses]
     """


    kwargs = _get_kwargs(
        expand=expand,
project_id=project_id,
start_at=start_at,
max_results=max_results,
search_string=search_string,
status_category=status_category,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 200,
    search_string: str | Unset = UNSET,
    status_category: str | Unset = UNSET,

) -> Any | PageOfStatuses | None:
    """ Search statuses paginated

     Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination)
    list of statuses that match a search on name or project.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        expand (str | Unset):
        project_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 200.
        search_string (str | Unset):
        status_category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfStatuses
     """


    return (await asyncio_detailed(
        client=client,
expand=expand,
project_id=project_id,
start_at=start_at,
max_results=max_results,
search_string=search_string,
status_category=status_category,

    )).parsed
