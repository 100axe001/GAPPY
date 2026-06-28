from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dnd_set_snooze_data_body import DndSetSnoozeDataBody
from ...models.dnd_set_snooze_dnd_set_snooze_error_schema import DndSetSnoozeDndSetSnoozeErrorSchema
from ...models.dnd_set_snooze_dnd_set_snooze_schema import DndSetSnoozeDndSetSnoozeSchema
from ...models.dnd_set_snooze_json_body import DndSetSnoozeJsonBody
from typing import cast



def _get_kwargs(
    *,
    body:    DndSetSnoozeDataBody  |     DndSetSnoozeJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dnd.setSnooze",
    }

    if isinstance(body, DndSetSnoozeDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DndSetSnoozeJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema:
    if response.status_code == 200:
        response_200 = DndSetSnoozeDndSetSnoozeSchema.from_dict(response.json())



        return response_200

    response_default = DndSetSnoozeDndSetSnoozeErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    DndSetSnoozeDataBody  |     DndSetSnoozeJsonBody  | Unset = UNSET,

) -> Response[DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema]:
    """  Turns on Do Not Disturb mode for the current user, or changes its duration.

    Args:
        body (DndSetSnoozeDataBody):
        body (DndSetSnoozeJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    DndSetSnoozeDataBody  |     DndSetSnoozeJsonBody  | Unset = UNSET,

) -> DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema | None:
    """  Turns on Do Not Disturb mode for the current user, or changes its duration.

    Args:
        body (DndSetSnoozeDataBody):
        body (DndSetSnoozeJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    DndSetSnoozeDataBody  |     DndSetSnoozeJsonBody  | Unset = UNSET,

) -> Response[DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema]:
    """  Turns on Do Not Disturb mode for the current user, or changes its duration.

    Args:
        body (DndSetSnoozeDataBody):
        body (DndSetSnoozeJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    DndSetSnoozeDataBody  |     DndSetSnoozeJsonBody  | Unset = UNSET,

) -> DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema | None:
    """  Turns on Do Not Disturb mode for the current user, or changes its duration.

    Args:
        body (DndSetSnoozeDataBody):
        body (DndSetSnoozeJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndSetSnoozeDndSetSnoozeErrorSchema | DndSetSnoozeDndSetSnoozeSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
