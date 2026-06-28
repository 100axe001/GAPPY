from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_info_default_error_template import FilesRemoteInfoDefaultErrorTemplate
from ...models.files_remote_info_default_success_template import FilesRemoteInfoDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["file"] = file

    params["external_id"] = external_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files.remote.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteInfoDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteInfoDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate]:
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

) -> Response[FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate]:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
external_id=external_id,

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

) -> FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate | None:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
file=file,
external_id=external_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    external_id: str | Unset = UNSET,

) -> Response[FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate]:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
external_id=external_id,

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

) -> FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate | None:
    """  Retrieve information about a remote file added to Slack

    Args:
        token (str | Unset):
        file (str | Unset):
        external_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteInfoDefaultErrorTemplate | FilesRemoteInfoDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
file=file,
external_id=external_id,

    )).parsed
