from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.operation_message import OperationMessage
from typing import cast



def _get_kwargs(
    addon_key: str,
    property_key: str,
    *,
    body: Any,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/atlassian-connect/1/addons/{addon_key}/properties/{property_key}".format(addon_key=quote(str(addon_key), safe=""),property_key=quote(str(property_key), safe=""),),
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OperationMessage | None:
    if response.status_code == 200:
        response_200 = OperationMessage.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = OperationMessage.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = OperationMessage.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = OperationMessage.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OperationMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    addon_key: str,
    property_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any,

) -> Response[OperationMessage]:
    """ Set app property

     Sets the value of an app's property. Use this resource to store custom data for your app.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.

    Args:
        addon_key (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationMessage]
     """


    kwargs = _get_kwargs(
        addon_key=addon_key,
property_key=property_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    addon_key: str,
    property_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any,

) -> OperationMessage | None:
    """ Set app property

     Sets the value of an app's property. Use this resource to store custom data for your app.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.

    Args:
        addon_key (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationMessage
     """


    return sync_detailed(
        addon_key=addon_key,
property_key=property_key,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    addon_key: str,
    property_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any,

) -> Response[OperationMessage]:
    """ Set app property

     Sets the value of an app's property. Use this resource to store custom data for your app.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.

    Args:
        addon_key (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OperationMessage]
     """


    kwargs = _get_kwargs(
        addon_key=addon_key,
property_key=property_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    addon_key: str,
    property_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any,

) -> OperationMessage | None:
    """ Set app property

     Sets the value of an app's property. Use this resource to store custom data for your app.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make
    this request.

    Args:
        addon_key (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OperationMessage
     """


    return (await asyncio_detailed(
        addon_key=addon_key,
property_key=property_key,
client=client,
body=body,

    )).parsed
