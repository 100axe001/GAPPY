from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.pins_add_data_body import PinsAddDataBody
from ...models.pins_add_json_body import PinsAddJsonBody
from ...models.pins_add_pins_add_error_schema import PinsAddPinsAddErrorSchema
from ...models.pins_add_pins_add_schema import PinsAddPinsAddSchema
from typing import cast



def _get_kwargs(
    *,
    body:    PinsAddDataBody  |     PinsAddJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pins.add",
    }

    if isinstance(body, PinsAddDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PinsAddJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema:
    if response.status_code == 200:
        response_200 = PinsAddPinsAddSchema.from_dict(response.json())



        return response_200

    response_default = PinsAddPinsAddErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    PinsAddDataBody  |     PinsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema]:
    """  Pins an item to a channel.

    Args:
        token (str):
        body (PinsAddDataBody):
        body (PinsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema]
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
    body:    PinsAddDataBody  |     PinsAddJsonBody  | Unset = UNSET,
    token: str,

) -> PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema | None:
    """  Pins an item to a channel.

    Args:
        token (str):
        body (PinsAddDataBody):
        body (PinsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    PinsAddDataBody  |     PinsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema]:
    """  Pins an item to a channel.

    Args:
        token (str):
        body (PinsAddDataBody):
        body (PinsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema]
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
    body:    PinsAddDataBody  |     PinsAddJsonBody  | Unset = UNSET,
    token: str,

) -> PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema | None:
    """  Pins an item to a channel.

    Args:
        token (str):
        body (PinsAddDataBody):
        body (PinsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PinsAddPinsAddErrorSchema | PinsAddPinsAddSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
