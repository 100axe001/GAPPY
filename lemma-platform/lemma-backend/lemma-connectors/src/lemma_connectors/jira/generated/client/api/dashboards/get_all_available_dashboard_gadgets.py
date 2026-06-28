from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.available_dashboard_gadgets_response import AvailableDashboardGadgetsResponse
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/gadgets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AvailableDashboardGadgetsResponse | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = AvailableDashboardGadgetsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AvailableDashboardGadgetsResponse | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AvailableDashboardGadgetsResponse | ErrorCollection]:
    """ Get available gadgets

     Gets a list of all available gadgets that can be added to all dashboards.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableDashboardGadgetsResponse | ErrorCollection]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> AvailableDashboardGadgetsResponse | ErrorCollection | None:
    """ Get available gadgets

     Gets a list of all available gadgets that can be added to all dashboards.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableDashboardGadgetsResponse | ErrorCollection
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AvailableDashboardGadgetsResponse | ErrorCollection]:
    """ Get available gadgets

     Gets a list of all available gadgets that can be added to all dashboards.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableDashboardGadgetsResponse | ErrorCollection]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> AvailableDashboardGadgetsResponse | ErrorCollection | None:
    """ Get available gadgets

     Gets a list of all available gadgets that can be added to all dashboards.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableDashboardGadgetsResponse | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
