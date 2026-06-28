from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calls_info_default_error_template import CallsInfoDefaultErrorTemplate
from ...models.calls_info_default_success_template import CallsInfoDefaultSuccessTemplate
from typing import cast



def _get_kwargs(
    *,
    id: str,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["id"] = id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/calls.info",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = CallsInfoDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = CallsInfoDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    token: str,

) -> Response[CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate]:
    """  Returns information about a Call.

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        id=id,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    token: str,

) -> CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate | None:
    """  Returns information about a Call.

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
id=id,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    token: str,

) -> Response[CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate]:
    """  Returns information about a Call.

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        id=id,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    token: str,

) -> CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate | None:
    """  Returns information about a Call.

    Args:
        id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallsInfoDefaultErrorTemplate | CallsInfoDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
id=id,
token=token,

    )).parsed
