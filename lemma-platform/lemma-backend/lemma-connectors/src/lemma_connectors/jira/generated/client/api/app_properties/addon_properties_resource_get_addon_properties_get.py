from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.operation_message import OperationMessage
from ...models.property_keys import PropertyKeys
from typing import cast



def _get_kwargs(
    addon_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/atlassian-connect/1/addons/{addon_key}/properties".format(addon_key=quote(str(addon_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OperationMessage | PropertyKeys | None:
    if response.status_code == 200:
        response_200 = PropertyKeys.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = OperationMessage.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OperationMessage | PropertyKeys]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    addon_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[OperationMessage | PropertyKeys]:
    """ Get app properties

     Gets all the properties of an app.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.
    Additionally, Forge apps published on the Marketplace can access properties of Connect apps they
    were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    Args:
        addon_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationMessage | PropertyKeys]
     """


    kwargs = _get_kwargs(
        addon_key=addon_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    addon_key: str,
    *,
    client: AuthenticatedClient,

) -> OperationMessage | PropertyKeys | None:
    """ Get app properties

     Gets all the properties of an app.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.
    Additionally, Forge apps published on the Marketplace can access properties of Connect apps they
    were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    Args:
        addon_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationMessage | PropertyKeys
     """


    return sync_detailed(
        addon_key=addon_key,
client=client,

    ).parsed

async def asyncio_detailed(
    addon_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[OperationMessage | PropertyKeys]:
    """ Get app properties

     Gets all the properties of an app.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.
    Additionally, Forge apps published on the Marketplace can access properties of Connect apps they
    were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    Args:
        addon_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationMessage | PropertyKeys]
     """


    kwargs = _get_kwargs(
        addon_key=addon_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    addon_key: str,
    *,
    client: AuthenticatedClient,

) -> OperationMessage | PropertyKeys | None:
    """ Get app properties

     Gets all the properties of an app.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.
    Additionally, Forge apps published on the Marketplace can access properties of Connect apps they
    were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    Args:
        addon_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationMessage | PropertyKeys
     """


    return (await asyncio_detailed(
        addon_key=addon_key,
client=client,

    )).parsed
