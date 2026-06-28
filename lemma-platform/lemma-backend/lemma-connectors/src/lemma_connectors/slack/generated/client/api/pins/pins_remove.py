from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.pins_remove_data_body import PinsRemoveDataBody
from ...models.pins_remove_json_body import PinsRemoveJsonBody
from ...models.pins_remove_pins_remove_error_schema import PinsRemovePinsRemoveErrorSchema
from ...models.pins_remove_pins_remove_schema import PinsRemovePinsRemoveSchema
from typing import cast



def _get_kwargs(
    *,
    body:    PinsRemoveDataBody  |     PinsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pins.remove",
    }

    if isinstance(body, PinsRemoveDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PinsRemoveJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema:
    if response.status_code == 200:
        response_200 = PinsRemovePinsRemoveSchema.from_dict(response.json())



        return response_200

    response_default = PinsRemovePinsRemoveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    PinsRemoveDataBody  |     PinsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema]:
    """  Un-pins an item from a channel.

    Args:
        token (str):
        body (PinsRemoveDataBody):
        body (PinsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    PinsRemoveDataBody  |     PinsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema | None:
    """  Un-pins an item from a channel.

    Args:
        token (str):
        body (PinsRemoveDataBody):
        body (PinsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    PinsRemoveDataBody  |     PinsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema]:
    """  Un-pins an item from a channel.

    Args:
        token (str):
        body (PinsRemoveDataBody):
        body (PinsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    PinsRemoveDataBody  |     PinsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema | None:
    """  Un-pins an item from a channel.

    Args:
        token (str):
        body (PinsRemoveDataBody):
        body (PinsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinsRemovePinsRemoveErrorSchema | PinsRemovePinsRemoveSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
