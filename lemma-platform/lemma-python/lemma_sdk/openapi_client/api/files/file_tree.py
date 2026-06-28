from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.directory_tree_response import DirectoryTreeResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    *,
    root_path: str | Unset = "/",
    files_per_directory: int | Unset = 3,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["root_path"] = root_path

    params["files_per_directory"] = files_per_directory

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/datastore/files/tree".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DirectoryTreeResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DirectoryTreeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DirectoryTreeResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    root_path: str | Unset = "/",
    files_per_directory: int | Unset = 3,
) -> Response[DirectoryTreeResponse | ErrorResponse]:
    """Get Directory Tree

    Args:
        pod_id (UUID):
        root_path (str | Unset):  Default: '/'.
        files_per_directory (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectoryTreeResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        root_path=root_path,
        files_per_directory=files_per_directory,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    root_path: str | Unset = "/",
    files_per_directory: int | Unset = 3,
) -> DirectoryTreeResponse | ErrorResponse | None:
    """Get Directory Tree

    Args:
        pod_id (UUID):
        root_path (str | Unset):  Default: '/'.
        files_per_directory (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectoryTreeResponse | ErrorResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        root_path=root_path,
        files_per_directory=files_per_directory,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    root_path: str | Unset = "/",
    files_per_directory: int | Unset = 3,
) -> Response[DirectoryTreeResponse | ErrorResponse]:
    """Get Directory Tree

    Args:
        pod_id (UUID):
        root_path (str | Unset):  Default: '/'.
        files_per_directory (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectoryTreeResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        root_path=root_path,
        files_per_directory=files_per_directory,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    root_path: str | Unset = "/",
    files_per_directory: int | Unset = 3,
) -> DirectoryTreeResponse | ErrorResponse | None:
    """Get Directory Tree

    Args:
        pod_id (UUID):
        root_path (str | Unset):  Default: '/'.
        files_per_directory (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectoryTreeResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            root_path=root_path,
            files_per_directory=files_per_directory,
        )
    ).parsed
