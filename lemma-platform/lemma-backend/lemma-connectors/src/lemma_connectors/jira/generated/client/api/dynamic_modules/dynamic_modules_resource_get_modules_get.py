from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_modules import ConnectModules
from ...models.error_message import ErrorMessage
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/atlassian-connect/1/app/module/dynamic",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectModules | ErrorMessage | None:
    if response.status_code == 200:
        response_200 = ConnectModules.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectModules | ErrorMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ConnectModules | ErrorMessage]:
    """ Get modules

     Returns all modules registered dynamically by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectModules | ErrorMessage]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ConnectModules | ErrorMessage | None:
    """ Get modules

     Returns all modules registered dynamically by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectModules | ErrorMessage
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ConnectModules | ErrorMessage]:
    """ Get modules

     Returns all modules registered dynamically by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectModules | ErrorMessage]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ConnectModules | ErrorMessage | None:
    """ Get modules

     Returns all modules registered dynamically by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectModules | ErrorMessage
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
