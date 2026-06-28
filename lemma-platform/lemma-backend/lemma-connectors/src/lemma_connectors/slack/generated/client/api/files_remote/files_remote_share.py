from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_share_default_error_template import FilesRemoteShareDefaultErrorTemplate
from ...models.files_remote_share_default_success_template import FilesRemoteShareDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    channels: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["file"] = file

    params["external_id"] = external_id

    params["channels"] = channels


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files.remote.share",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteShareDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteShareDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate]:
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
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    channels: str | Unset = UNSET,

) -> Response[FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate]:
    """  Share a remote file into a channel.

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):
        channels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
external_id=external_id,
channels=channels,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    channels: str | Unset = UNSET,

) -> FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate | None:
    """  Share a remote file into a channel.

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):
        channels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
file=file,
external_id=external_id,
channels=channels,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    channels: str | Unset = UNSET,

) -> Response[FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate]:
    """  Share a remote file into a channel.

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):
        channels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
external_id=external_id,
channels=channels,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    channels: str | Unset = UNSET,

) -> FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate | None:
    """  Share a remote file into a channel.

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):
        channels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteShareDefaultErrorTemplate | FilesRemoteShareDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
file=file,
external_id=external_id,
channels=channels,

    )).parsed
