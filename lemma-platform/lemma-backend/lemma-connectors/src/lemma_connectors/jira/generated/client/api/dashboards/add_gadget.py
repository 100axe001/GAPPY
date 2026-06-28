from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard_gadget import DashboardGadget
from ...models.dashboard_gadget_settings import DashboardGadgetSettings
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    dashboard_id: int,
    *,
    body: DashboardGadgetSettings,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/dashboard/{dashboard_id}/gadget".format(dashboard_id=quote(str(dashboard_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DashboardGadget | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = DashboardGadget.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DashboardGadget | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetSettings,

) -> Response[Any | DashboardGadget | ErrorCollection]:
    """ Add gadget to dashboard

     Adds a gadget to a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        body (DashboardGadgetSettings): Details of the settings for a dashboard gadget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DashboardGadget | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetSettings,

) -> Any | DashboardGadget | ErrorCollection | None:
    """ Add gadget to dashboard

     Adds a gadget to a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        body (DashboardGadgetSettings): Details of the settings for a dashboard gadget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DashboardGadget | ErrorCollection
     """


    return sync_detailed(
        dashboard_id=dashboard_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetSettings,

) -> Response[Any | DashboardGadget | ErrorCollection]:
    """ Add gadget to dashboard

     Adds a gadget to a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        body (DashboardGadgetSettings): Details of the settings for a dashboard gadget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DashboardGadget | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetSettings,

) -> Any | DashboardGadget | ErrorCollection | None:
    """ Add gadget to dashboard

     Adds a gadget to a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        body (DashboardGadgetSettings): Details of the settings for a dashboard gadget.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DashboardGadget | ErrorCollection
     """


    return (await asyncio_detailed(
        dashboard_id=dashboard_id,
client=client,
body=body,

    )).parsed
