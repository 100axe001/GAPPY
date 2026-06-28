from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard_gadget_update_request import DashboardGadgetUpdateRequest
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    dashboard_id: int,
    gadget_id: int,
    *,
    body: DashboardGadgetUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/dashboard/{dashboard_id}/gadget/{gadget_id}".format(dashboard_id=quote(str(dashboard_id), safe=""),gadget_id=quote(str(gadget_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | None:
    if response.status_code == 204:
        response_204 = response.json()
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: int,
    gadget_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetUpdateRequest,

) -> Response[Any | ErrorCollection]:
    """ Update gadget on dashboard

     Changes the title, position, and color of the gadget on a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        gadget_id (int):
        body (DashboardGadgetUpdateRequest): The details of the gadget to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
gadget_id=gadget_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dashboard_id: int,
    gadget_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetUpdateRequest,

) -> Any | ErrorCollection | None:
    """ Update gadget on dashboard

     Changes the title, position, and color of the gadget on a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        gadget_id (int):
        body (DashboardGadgetUpdateRequest): The details of the gadget to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return sync_detailed(
        dashboard_id=dashboard_id,
gadget_id=gadget_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dashboard_id: int,
    gadget_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetUpdateRequest,

) -> Response[Any | ErrorCollection]:
    """ Update gadget on dashboard

     Changes the title, position, and color of the gadget on a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        gadget_id (int):
        body (DashboardGadgetUpdateRequest): The details of the gadget to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
gadget_id=gadget_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dashboard_id: int,
    gadget_id: int,
    *,
    client: AuthenticatedClient,
    body: DashboardGadgetUpdateRequest,

) -> Any | ErrorCollection | None:
    """ Update gadget on dashboard

     Changes the title, position, and color of the gadget on a dashboard.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        gadget_id (int):
        body (DashboardGadgetUpdateRequest): The details of the gadget to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return (await asyncio_detailed(
        dashboard_id=dashboard_id,
gadget_id=gadget_id,
client=client,
body=body,

    )).parsed
