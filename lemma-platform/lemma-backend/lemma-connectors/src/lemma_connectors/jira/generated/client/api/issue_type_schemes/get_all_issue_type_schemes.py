from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_all_issue_type_schemes_order_by import GetAllIssueTypeSchemesOrderBy
from ...models.page_bean_issue_type_scheme import PageBeanIssueTypeScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    order_by: GetAllIssueTypeSchemesOrderBy | Unset = GetAllIssueTypeSchemesOrderBy.ID,
    expand: str | Unset = '',
    query_string: str | Unset = '',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["expand"] = expand

    params["queryString"] = query_string


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetypescheme",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueTypeScheme | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueTypeScheme.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueTypeScheme]:
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
    id: list[int] | Unset = UNSET,
    order_by: GetAllIssueTypeSchemesOrderBy | Unset = GetAllIssueTypeSchemesOrderBy.ID,
    expand: str | Unset = '',
    query_string: str | Unset = '',

) -> Response[Any | PageBeanIssueTypeScheme]:
    """ Get all issue type schemes

     Returns a [paginated](#pagination) list of issue type schemes.

    Only issue type schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        order_by (GetAllIssueTypeSchemesOrderBy | Unset):  Default:
            GetAllIssueTypeSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.
        query_string (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
order_by=order_by,
expand=expand,
query_string=query_string,

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
    id: list[int] | Unset = UNSET,
    order_by: GetAllIssueTypeSchemesOrderBy | Unset = GetAllIssueTypeSchemesOrderBy.ID,
    expand: str | Unset = '',
    query_string: str | Unset = '',

) -> Any | PageBeanIssueTypeScheme | None:
    """ Get all issue type schemes

     Returns a [paginated](#pagination) list of issue type schemes.

    Only issue type schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        order_by (GetAllIssueTypeSchemesOrderBy | Unset):  Default:
            GetAllIssueTypeSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.
        query_string (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScheme
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
order_by=order_by,
expand=expand,
query_string=query_string,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    order_by: GetAllIssueTypeSchemesOrderBy | Unset = GetAllIssueTypeSchemesOrderBy.ID,
    expand: str | Unset = '',
    query_string: str | Unset = '',

) -> Response[Any | PageBeanIssueTypeScheme]:
    """ Get all issue type schemes

     Returns a [paginated](#pagination) list of issue type schemes.

    Only issue type schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        order_by (GetAllIssueTypeSchemesOrderBy | Unset):  Default:
            GetAllIssueTypeSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.
        query_string (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
order_by=order_by,
expand=expand,
query_string=query_string,

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
    id: list[int] | Unset = UNSET,
    order_by: GetAllIssueTypeSchemesOrderBy | Unset = GetAllIssueTypeSchemesOrderBy.ID,
    expand: str | Unset = '',
    query_string: str | Unset = '',

) -> Any | PageBeanIssueTypeScheme | None:
    """ Get all issue type schemes

     Returns a [paginated](#pagination) list of issue type schemes.

    Only issue type schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        order_by (GetAllIssueTypeSchemesOrderBy | Unset):  Default:
            GetAllIssueTypeSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.
        query_string (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScheme
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
order_by=order_by,
expand=expand,
query_string=query_string,

    )).parsed
