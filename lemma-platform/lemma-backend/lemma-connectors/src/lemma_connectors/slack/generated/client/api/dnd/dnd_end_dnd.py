from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dnd_end_dnd_dnd_end_dnd_error_schema import DndEndDndDndEndDndErrorSchema
from ...models.dnd_end_dnd_dnd_end_dnd_schema import DndEndDndDndEndDndSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dnd.endDnd",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema:
    if response.status_code == 200:
        response_200 = DndEndDndDndEndDndSchema.from_dict(response.json())



        return response_200

    response_default = DndEndDndDndEndDndErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema]:
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

) -> Response[DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema]:
    """  Ends the current user's Do Not Disturb session immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema]
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

) -> DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema | None:
    """  Ends the current user's Do Not Disturb session immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema
     """


    return sync_detailed(
        client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,

) -> Response[DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema]:
    """  Ends the current user's Do Not Disturb session immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema]
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

) -> DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema | None:
    """  Ends the current user's Do Not Disturb session immediately.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndEndDndDndEndDndErrorSchema | DndEndDndDndEndDndSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,

    )).parsed
