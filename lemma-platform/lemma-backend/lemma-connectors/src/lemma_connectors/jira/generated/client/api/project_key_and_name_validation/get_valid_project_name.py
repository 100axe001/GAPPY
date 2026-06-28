from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    *,
    name: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/projectvalidate/validProjectName",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str,

) -> Response[Any | str]:
    """ Get valid project name

     Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If
    the name is in use, this operation attempts to generate a valid project name based on the one
    supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404
    response is returned.

    **[Permissions](#permissions) required:** None.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    name: str,

) -> Any | str | None:
    """ Get valid project name

     Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If
    the name is in use, this operation attempts to generate a valid project name based on the one
    supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404
    response is returned.

    **[Permissions](#permissions) required:** None.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
     """


    return sync_detailed(
        client=client,
name=name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str,

) -> Response[Any | str]:
    """ Get valid project name

     Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If
    the name is in use, this operation attempts to generate a valid project name based on the one
    supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404
    response is returned.

    **[Permissions](#permissions) required:** None.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str,

) -> Any | str | None:
    """ Get valid project name

     Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If
    the name is in use, this operation attempts to generate a valid project name based on the one
    supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404
    response is returned.

    **[Permissions](#permissions) required:** None.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
     """


    return (await asyncio_detailed(
        client=client,
name=name,

    )).parsed
