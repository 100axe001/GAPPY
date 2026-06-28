from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard import Dashboard
from ...models.dashboard_details import DashboardDetails
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: DashboardDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/dashboard/{id}/copy".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dashboard | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dashboard | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DashboardDetails,

) -> Response[Dashboard | ErrorCollection]:
    """ Copy dashboard

     Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied
    dashboard.

    **[Permissions](#permissions) required:** None

    The dashboard to be copied must be owned by or shared with the user.

    Args:
        id (str):
        body (DashboardDetails): Details of a dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | ErrorCollection]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DashboardDetails,

) -> Dashboard | ErrorCollection | None:
    """ Copy dashboard

     Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied
    dashboard.

    **[Permissions](#permissions) required:** None

    The dashboard to be copied must be owned by or shared with the user.

    Args:
        id (str):
        body (DashboardDetails): Details of a dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | ErrorCollection
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DashboardDetails,

) -> Response[Dashboard | ErrorCollection]:
    """ Copy dashboard

     Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied
    dashboard.

    **[Permissions](#permissions) required:** None

    The dashboard to be copied must be owned by or shared with the user.

    Args:
        id (str):
        body (DashboardDetails): Details of a dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | ErrorCollection]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: DashboardDetails,

) -> Dashboard | ErrorCollection | None:
    """ Copy dashboard

     Copies a dashboard. Any values provided in the `dashboard` parameter replace those in the copied
    dashboard.

    **[Permissions](#permissions) required:** None

    The dashboard to be copied must be owned by or shared with the user.

    Args:
        id (str):
        body (DashboardDetails): Details of a dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | ErrorCollection
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
