from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_create_records_request import BulkCreateRecordsRequest
from ...models.datastore_count_response import DatastoreCountResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    table_name: str,
    *,
    body: BulkCreateRecordsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pods/{pod_id}/datastore/tables/{table_name}/records/bulk/create".format(
            pod_id=quote(str(pod_id), safe=""),
            table_name=quote(str(table_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatastoreCountResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DatastoreCountResponse.from_dict(response.json())

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
) -> Response[DatastoreCountResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateRecordsRequest,
) -> Response[DatastoreCountResponse | ErrorResponse]:
    """Bulk Create

     Insert multiple records in one request. Returns the affected-row count.

    Args:
        pod_id (UUID):
        table_name (str):
        body (BulkCreateRecordsRequest): Schema for bulk creating records.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatastoreCountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        table_name=table_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateRecordsRequest,
) -> DatastoreCountResponse | ErrorResponse | None:
    """Bulk Create

     Insert multiple records in one request. Returns the affected-row count.

    Args:
        pod_id (UUID):
        table_name (str):
        body (BulkCreateRecordsRequest): Schema for bulk creating records.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatastoreCountResponse | ErrorResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        table_name=table_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateRecordsRequest,
) -> Response[DatastoreCountResponse | ErrorResponse]:
    """Bulk Create

     Insert multiple records in one request. Returns the affected-row count.

    Args:
        pod_id (UUID):
        table_name (str):
        body (BulkCreateRecordsRequest): Schema for bulk creating records.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatastoreCountResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        table_name=table_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkCreateRecordsRequest,
) -> DatastoreCountResponse | ErrorResponse | None:
    """Bulk Create

     Insert multiple records in one request. Returns the affected-row count.

    Args:
        pod_id (UUID):
        table_name (str):
        body (BulkCreateRecordsRequest): Schema for bulk creating records.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatastoreCountResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            table_name=table_name,
            client=client,
            body=body,
        )
    ).parsed
