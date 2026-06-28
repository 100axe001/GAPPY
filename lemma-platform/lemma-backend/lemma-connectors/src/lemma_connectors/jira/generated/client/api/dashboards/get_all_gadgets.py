from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard_gadget_response import DashboardGadgetResponse
from ...models.error_collection import ErrorCollection
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    dashboard_id: int,
    *,
    module_key: list[str] | Unset = UNSET,
    uri: list[str] | Unset = UNSET,
    gadget_id: list[int] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_module_key: list[str] | Unset = UNSET
    if not isinstance(module_key, Unset):
        json_module_key = module_key


    params["moduleKey"] = json_module_key

    json_uri: list[str] | Unset = UNSET
    if not isinstance(uri, Unset):
        json_uri = uri


    params["uri"] = json_uri

    json_gadget_id: list[int] | Unset = UNSET
    if not isinstance(gadget_id, Unset):
        json_gadget_id = gadget_id


    params["gadgetId"] = json_gadget_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/{dashboard_id}/gadget".format(dashboard_id=quote(str(dashboard_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DashboardGadgetResponse | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = DashboardGadgetResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DashboardGadgetResponse | ErrorCollection]:
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
    module_key: list[str] | Unset = UNSET,
    uri: list[str] | Unset = UNSET,
    gadget_id: list[int] | Unset = UNSET,

) -> Response[Any | DashboardGadgetResponse | ErrorCollection]:
    """ Get gadgets

     Returns a list of dashboard gadgets on a dashboard.

    This operation returns:

     *  Gadgets from a list of IDs, when `id` is set.
     *  Gadgets with a module key, when `moduleKey` is set.
     *  Gadgets from a list of URIs, when `uri` is set.
     *  All gadgets, when no other parameters are set.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        module_key (list[str] | Unset):
        uri (list[str] | Unset):
        gadget_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DashboardGadgetResponse | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
module_key=module_key,
uri=uri,
gadget_id=gadget_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    module_key: list[str] | Unset = UNSET,
    uri: list[str] | Unset = UNSET,
    gadget_id: list[int] | Unset = UNSET,

) -> Any | DashboardGadgetResponse | ErrorCollection | None:
    """ Get gadgets

     Returns a list of dashboard gadgets on a dashboard.

    This operation returns:

     *  Gadgets from a list of IDs, when `id` is set.
     *  Gadgets with a module key, when `moduleKey` is set.
     *  Gadgets from a list of URIs, when `uri` is set.
     *  All gadgets, when no other parameters are set.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        module_key (list[str] | Unset):
        uri (list[str] | Unset):
        gadget_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DashboardGadgetResponse | ErrorCollection
     """


    return sync_detailed(
        dashboard_id=dashboard_id,
client=client,
module_key=module_key,
uri=uri,
gadget_id=gadget_id,

    ).parsed

async def asyncio_detailed(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    module_key: list[str] | Unset = UNSET,
    uri: list[str] | Unset = UNSET,
    gadget_id: list[int] | Unset = UNSET,

) -> Response[Any | DashboardGadgetResponse | ErrorCollection]:
    """ Get gadgets

     Returns a list of dashboard gadgets on a dashboard.

    This operation returns:

     *  Gadgets from a list of IDs, when `id` is set.
     *  Gadgets with a module key, when `moduleKey` is set.
     *  Gadgets from a list of URIs, when `uri` is set.
     *  All gadgets, when no other parameters are set.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        module_key (list[str] | Unset):
        uri (list[str] | Unset):
        gadget_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DashboardGadgetResponse | ErrorCollection]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
module_key=module_key,
uri=uri,
gadget_id=gadget_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dashboard_id: int,
    *,
    client: AuthenticatedClient,
    module_key: list[str] | Unset = UNSET,
    uri: list[str] | Unset = UNSET,
    gadget_id: list[int] | Unset = UNSET,

) -> Any | DashboardGadgetResponse | ErrorCollection | None:
    """ Get gadgets

     Returns a list of dashboard gadgets on a dashboard.

    This operation returns:

     *  Gadgets from a list of IDs, when `id` is set.
     *  Gadgets with a module key, when `moduleKey` is set.
     *  Gadgets from a list of URIs, when `uri` is set.
     *  All gadgets, when no other parameters are set.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        dashboard_id (int):
        module_key (list[str] | Unset):
        uri (list[str] | Unset):
        gadget_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DashboardGadgetResponse | ErrorCollection
     """


    return (await asyncio_detailed(
        dashboard_id=dashboard_id,
client=client,
module_key=module_key,
uri=uri,
gadget_id=gadget_id,

    )).parsed
