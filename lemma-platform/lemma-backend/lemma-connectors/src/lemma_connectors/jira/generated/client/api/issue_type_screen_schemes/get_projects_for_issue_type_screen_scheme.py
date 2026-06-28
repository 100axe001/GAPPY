from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_project_details import PageBeanProjectDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_type_screen_scheme_id: int,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    query: str | Unset = '',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["query"] = query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/project".format(issue_type_screen_scheme_id=quote(str(issue_type_screen_scheme_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanProjectDetails | None:
    if response.status_code == 200:
        response_200 = PageBeanProjectDetails.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanProjectDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_type_screen_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    query: str | Unset = '',

) -> Response[Any | PageBeanProjectDetails]:
    """ Get issue type screen scheme projects

     Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

    Only company-managed projects associated with an issue type screen scheme are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanProjectDetails]
     """


    kwargs = _get_kwargs(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
start_at=start_at,
max_results=max_results,
query=query,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_type_screen_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    query: str | Unset = '',

) -> Any | PageBeanProjectDetails | None:
    """ Get issue type screen scheme projects

     Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

    Only company-managed projects associated with an issue type screen scheme are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanProjectDetails
     """


    return sync_detailed(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
client=client,
start_at=start_at,
max_results=max_results,
query=query,

    ).parsed

async def asyncio_detailed(
    issue_type_screen_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    query: str | Unset = '',

) -> Response[Any | PageBeanProjectDetails]:
    """ Get issue type screen scheme projects

     Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

    Only company-managed projects associated with an issue type screen scheme are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanProjectDetails]
     """


    kwargs = _get_kwargs(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
start_at=start_at,
max_results=max_results,
query=query,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_type_screen_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    query: str | Unset = '',

) -> Any | PageBeanProjectDetails | None:
    """ Get issue type screen scheme projects

     Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.

    Only company-managed projects associated with an issue type screen scheme are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanProjectDetails
     """


    return (await asyncio_detailed(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
client=client,
start_at=start_at,
max_results=max_results,
query=query,

    )).parsed
