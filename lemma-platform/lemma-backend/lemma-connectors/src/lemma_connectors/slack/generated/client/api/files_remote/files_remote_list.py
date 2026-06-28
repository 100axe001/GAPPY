from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_list_default_error_template import FilesRemoteListDefaultErrorTemplate
from ...models.files_remote_list_default_success_template import FilesRemoteListDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["channel"] = channel

    params["ts_from"] = ts_from

    params["ts_to"] = ts_to

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files.remote.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteListDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteListDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate]:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate | None:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate]:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate | None:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteListDefaultErrorTemplate | FilesRemoteListDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
limit=limit,
cursor=cursor,

    )).parsed
