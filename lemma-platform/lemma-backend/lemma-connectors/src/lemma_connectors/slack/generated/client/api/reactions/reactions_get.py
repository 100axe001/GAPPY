from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reactions_get_reactions_get_error_schema import ReactionsGetReactionsGetErrorSchema
from ...models.reactions_get_reactions_get_success_schema import ReactionsGetReactionsGetSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    channel: str | Unset = UNSET,
    file: str | Unset = UNSET,
    file_comment: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    timestamp: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["file"] = file

    params["file_comment"] = file_comment

    params["full"] = full

    params["timestamp"] = timestamp


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reactions.get",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema:
    if response.status_code == 200:
        response_200 = ReactionsGetReactionsGetSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ReactionsGetReactionsGetErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema]:
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
    channel: str | Unset = UNSET,
    file: str | Unset = UNSET,
    file_comment: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    timestamp: str | Unset = UNSET,

) -> Response[ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema]:
    """  Gets reactions for an item.

    Args:
        token (str):
        channel (str | Unset):
        file (str | Unset):
        file_comment (str | Unset):
        full (bool | Unset):
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
file=file,
file_comment=file_comment,
full=full,
timestamp=timestamp,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str | Unset = UNSET,
    file: str | Unset = UNSET,
    file_comment: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    timestamp: str | Unset = UNSET,

) -> ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema | None:
    """  Gets reactions for an item.

    Args:
        token (str):
        channel (str | Unset):
        file (str | Unset):
        file_comment (str | Unset):
        full (bool | Unset):
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
file=file,
file_comment=file_comment,
full=full,
timestamp=timestamp,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str | Unset = UNSET,
    file: str | Unset = UNSET,
    file_comment: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    timestamp: str | Unset = UNSET,

) -> Response[ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema]:
    """  Gets reactions for an item.

    Args:
        token (str):
        channel (str | Unset):
        file (str | Unset):
        file_comment (str | Unset):
        full (bool | Unset):
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
file=file,
file_comment=file_comment,
full=full,
timestamp=timestamp,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    channel: str | Unset = UNSET,
    file: str | Unset = UNSET,
    file_comment: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    timestamp: str | Unset = UNSET,

) -> ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema | None:
    """  Gets reactions for an item.

    Args:
        token (str):
        channel (str | Unset):
        file (str | Unset):
        file_comment (str | Unset):
        full (bool | Unset):
        timestamp (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsGetReactionsGetErrorSchema | ReactionsGetReactionsGetSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
file=file,
file_comment=file_comment,
full=full,
timestamp=timestamp,

    )).parsed
