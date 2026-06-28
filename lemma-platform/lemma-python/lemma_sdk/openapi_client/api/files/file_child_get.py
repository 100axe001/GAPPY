from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    *,
    path: str,
    page_start: int | None | Unset = UNSET,
    page_end: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    json_page_start: int | None | Unset
    if isinstance(page_start, Unset):
        json_page_start = UNSET
    else:
        json_page_start = page_start
    params["page_start"] = json_page_start

    json_page_end: int | None | Unset
    if isinstance(page_end, Unset):
        json_page_end = UNSET
    else:
        json_page_end = page_end
    params["page_end"] = json_page_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/datastore/files/children/content".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[ErrorResponse | File]:
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
    path: str,
    page_start: int | None | Unset = UNSET,
    page_end: int | None | Unset = UNSET,
) -> Response[ErrorResponse | File]:
    """Fetch a document's child artifact by path

    Args:
        pod_id (UUID):
        path (str): Child path, e.g. /folder/report.pdf/document.md,
            /folder/report.pdf/image_0.png, or /folder/report.pdf/pages/page_0001.jpg
        page_start (int | None | Unset):
        page_end (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        path=path,
        page_start=page_start,
        page_end=page_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    page_start: int | None | Unset = UNSET,
    page_end: int | None | Unset = UNSET,
) -> ErrorResponse | File | None:
    """Fetch a document's child artifact by path

    Args:
        pod_id (UUID):
        path (str): Child path, e.g. /folder/report.pdf/document.md,
            /folder/report.pdf/image_0.png, or /folder/report.pdf/pages/page_0001.jpg
        page_start (int | None | Unset):
        page_end (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        path=path,
        page_start=page_start,
        page_end=page_end,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    page_start: int | None | Unset = UNSET,
    page_end: int | None | Unset = UNSET,
) -> Response[ErrorResponse | File]:
    """Fetch a document's child artifact by path

    Args:
        pod_id (UUID):
        path (str): Child path, e.g. /folder/report.pdf/document.md,
            /folder/report.pdf/image_0.png, or /folder/report.pdf/pages/page_0001.jpg
        page_start (int | None | Unset):
        page_end (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        path=path,
        page_start=page_start,
        page_end=page_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    page_start: int | None | Unset = UNSET,
    page_end: int | None | Unset = UNSET,
) -> ErrorResponse | File | None:
    """Fetch a document's child artifact by path

    Args:
        pod_id (UUID):
        path (str): Child path, e.g. /folder/report.pdf/document.md,
            /folder/report.pdf/image_0.png, or /folder/report.pdf/pages/page_0001.jpg
        page_start (int | None | Unset):
        page_end (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            path=path,
            page_start=page_start,
            page_end=page_end,
        )
    ).parsed
