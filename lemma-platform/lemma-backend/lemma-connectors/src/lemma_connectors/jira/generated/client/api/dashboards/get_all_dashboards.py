from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_all_dashboards_filter import GetAllDashboardsFilter
from ...models.page_of_dashboards import PageOfDashboards
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    filter_: GetAllDashboardsFilter | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["filter"] = json_filter_

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | PageOfDashboards | None:
    if response.status_code == 200:
        response_200 = PageOfDashboards.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | PageOfDashboards]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_: GetAllDashboardsFilter | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Response[ErrorCollection | PageOfDashboards]:
    """ Get all dashboards

     Returns a list of dashboards owned by or shared with the user. The list may be filtered to include
    only favorite or owned dashboards.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        filter_ (GetAllDashboardsFilter | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageOfDashboards]
     """


    kwargs = _get_kwargs(
        filter_=filter_,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    filter_: GetAllDashboardsFilter | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> ErrorCollection | PageOfDashboards | None:
    """ Get all dashboards

     Returns a list of dashboards owned by or shared with the user. The list may be filtered to include
    only favorite or owned dashboards.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        filter_ (GetAllDashboardsFilter | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageOfDashboards
     """


    return sync_detailed(
        client=client,
filter_=filter_,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_: GetAllDashboardsFilter | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Response[ErrorCollection | PageOfDashboards]:
    """ Get all dashboards

     Returns a list of dashboards owned by or shared with the user. The list may be filtered to include
    only favorite or owned dashboards.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        filter_ (GetAllDashboardsFilter | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageOfDashboards]
     """


    kwargs = _get_kwargs(
        filter_=filter_,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_: GetAllDashboardsFilter | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> ErrorCollection | PageOfDashboards | None:
    """ Get all dashboards

     Returns a list of dashboards owned by or shared with the user. The list may be filtered to include
    only favorite or owned dashboards.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        filter_ (GetAllDashboardsFilter | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageOfDashboards
     """


    return (await asyncio_detailed(
        client=client,
filter_=filter_,
start_at=start_at,
max_results=max_results,

    )).parsed
