from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dnd_end_snooze_dnd_end_snooze_error_schema import DndEndSnoozeDndEndSnoozeErrorSchema
from ...models.dnd_end_snooze_dnd_end_snooze_schema import DndEndSnoozeDndEndSnoozeSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dnd.endSnooze",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema:
    if response.status_code == 200:
        response_200 = DndEndSnoozeDndEndSnoozeSchema.from_dict(response.json())



        return response_200

    response_default = DndEndSnoozeDndEndSnoozeErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema]:
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

) -> Response[DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema]:
    """  Ends the current user's snooze mode immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,

) -> DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema | None:
    """  Ends the current user's snooze mode immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema
     """


    return sync_detailed(
        client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,

) -> Response[DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema]:
    """  Ends the current user's snooze mode immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,

) -> DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema | None:
    """  Ends the current user's snooze mode immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndEndSnoozeDndEndSnoozeErrorSchema | DndEndSnoozeDndEndSnoozeSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,

    )).parsed
