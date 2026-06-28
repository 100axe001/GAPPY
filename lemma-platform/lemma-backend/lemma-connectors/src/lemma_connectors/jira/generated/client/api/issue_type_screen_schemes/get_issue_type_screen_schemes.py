from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_issue_type_screen_schemes_order_by import GetIssueTypeScreenSchemesOrderBy
from ...models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    order_by: GetIssueTypeScreenSchemesOrderBy | Unset = GetIssueTypeScreenSchemesOrderBy.ID,
    expand: str | Unset = '',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["queryString"] = query_string

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetypescreenscheme",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueTypeScreenScheme | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueTypeScreenScheme.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueTypeScreenScheme]:
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
    query_string: str | Unset = '',
    order_by: GetIssueTypeScreenSchemesOrderBy | Unset = GetIssueTypeScreenSchemesOrderBy.ID,
    expand: str | Unset = '',

) -> Response[Any | PageBeanIssueTypeScreenScheme]:
    """ Get issue type screen schemes

     Returns a [paginated](#pagination) list of issue type screen schemes.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        order_by (GetIssueTypeScreenSchemesOrderBy | Unset):  Default:
            GetIssueTypeScreenSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScreenScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
order_by=order_by,
expand=expand,

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
    query_string: str | Unset = '',
    order_by: GetIssueTypeScreenSchemesOrderBy | Unset = GetIssueTypeScreenSchemesOrderBy.ID,
    expand: str | Unset = '',

) -> Any | PageBeanIssueTypeScreenScheme | None:
    """ Get issue type screen schemes

     Returns a [paginated](#pagination) list of issue type screen schemes.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        order_by (GetIssueTypeScreenSchemesOrderBy | Unset):  Default:
            GetIssueTypeScreenSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScreenScheme
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
order_by=order_by,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    query_string: str | Unset = '',
    order_by: GetIssueTypeScreenSchemesOrderBy | Unset = GetIssueTypeScreenSchemesOrderBy.ID,
    expand: str | Unset = '',

) -> Response[Any | PageBeanIssueTypeScreenScheme]:
    """ Get issue type screen schemes

     Returns a [paginated](#pagination) list of issue type screen schemes.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        order_by (GetIssueTypeScreenSchemesOrderBy | Unset):  Default:
            GetIssueTypeScreenSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueTypeScreenScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
order_by=order_by,
expand=expand,

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
    query_string: str | Unset = '',
    order_by: GetIssueTypeScreenSchemesOrderBy | Unset = GetIssueTypeScreenSchemesOrderBy.ID,
    expand: str | Unset = '',

) -> Any | PageBeanIssueTypeScreenScheme | None:
    """ Get issue type screen schemes

     Returns a [paginated](#pagination) list of issue type screen schemes.

    Only issue type screen schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        query_string (str | Unset):  Default: ''.
        order_by (GetIssueTypeScreenSchemesOrderBy | Unset):  Default:
            GetIssueTypeScreenSchemesOrderBy.ID.
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueTypeScreenScheme
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
query_string=query_string,
order_by=order_by,
expand=expand,

    )).parsed
