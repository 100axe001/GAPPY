from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.rtm_connect_rtm_connect_error_schema import RtmConnectRtmConnectErrorSchema
from ...models.rtm_connect_rtm_connect_schema import RtmConnectRtmConnectSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    batch_presence_aware: bool | Unset = UNSET,
    presence_sub: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["batch_presence_aware"] = batch_presence_aware

    params["presence_sub"] = presence_sub


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rtm.connect",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema:
    if response.status_code == 200:
        response_200 = RtmConnectRtmConnectSchema.from_dict(response.json())



        return response_200

    response_default = RtmConnectRtmConnectErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    batch_presence_aware: bool | Unset = UNSET,
    presence_sub: bool | Unset = UNSET,

) -> Response[RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema]:
    """  Starts a Real Time Messaging session.

    Args:
        token (str):
        batch_presence_aware (bool | Unset):
        presence_sub (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema]
     """


    kwargs = _get_kwargs(
        token=token,
batch_presence_aware=batch_presence_aware,
presence_sub=presence_sub,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    batch_presence_aware: bool | Unset = UNSET,
    presence_sub: bool | Unset = UNSET,

) -> RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema | None:
    """  Starts a Real Time Messaging session.

    Args:
        token (str):
        batch_presence_aware (bool | Unset):
        presence_sub (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema
     """


    return sync_detailed(
        client=client,
token=token,
batch_presence_aware=batch_presence_aware,
presence_sub=presence_sub,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    batch_presence_aware: bool | Unset = UNSET,
    presence_sub: bool | Unset = UNSET,

) -> Response[RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema]:
    """  Starts a Real Time Messaging session.

    Args:
        token (str):
        batch_presence_aware (bool | Unset):
        presence_sub (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema]
     """


    kwargs = _get_kwargs(
        token=token,
batch_presence_aware=batch_presence_aware,
presence_sub=presence_sub,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    batch_presence_aware: bool | Unset = UNSET,
    presence_sub: bool | Unset = UNSET,

) -> RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema | None:
    """  Starts a Real Time Messaging session.

    Args:
        token (str):
        batch_presence_aware (bool | Unset):
        presence_sub (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RtmConnectRtmConnectErrorSchema | RtmConnectRtmConnectSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
batch_presence_aware=batch_presence_aware,
presence_sub=presence_sub,

    )).parsed
