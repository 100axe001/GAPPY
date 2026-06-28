from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_signed_url_request import FileSignedUrlRequest
from ...models.file_signed_url_response import FileSignedUrlResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    *,
    body: FileSignedUrlRequest | None | Unset = UNSET,
    path: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pods/{pod_id}/datastore/files/signed-url".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, FileSignedUrlRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FileSignedUrlResponse | None:
    if response.status_code == 201:
        response_201 = FileSignedUrlResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | FileSignedUrlResponse]:
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
    body: FileSignedUrlRequest | None | Unset = UNSET,
    path: str,
) -> Response[ErrorResponse | FileSignedUrlResponse]:
    """Create a public, hit-capped signed URL for a file

    Args:
        pod_id (UUID):
        path (str):
        body (FileSignedUrlRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FileSignedUrlResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        body=body,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileSignedUrlRequest | None | Unset = UNSET,
    path: str,
) -> ErrorResponse | FileSignedUrlResponse | None:
    """Create a public, hit-capped signed URL for a file

    Args:
        pod_id (UUID):
        path (str):
        body (FileSignedUrlRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FileSignedUrlResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        body=body,
        path=path,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileSignedUrlRequest | None | Unset = UNSET,
    path: str,
) -> Response[ErrorResponse | FileSignedUrlResponse]:
    """Create a public, hit-capped signed URL for a file

    Args:
        pod_id (UUID):
        path (str):
        body (FileSignedUrlRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FileSignedUrlResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        body=body,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: FileSignedUrlRequest | None | Unset = UNSET,
    path: str,
) -> ErrorResponse | FileSignedUrlResponse | None:
    """Create a public, hit-capped signed URL for a file

    Args:
        pod_id (UUID):
        path (str):
        body (FileSignedUrlRequest | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FileSignedUrlResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            body=body,
            path=path,
        )
    ).parsed
