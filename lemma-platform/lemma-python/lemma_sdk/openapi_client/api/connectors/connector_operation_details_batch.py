from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.operation_details_batch_request import OperationDetailsBatchRequest
from ...models.operation_details_batch_response import OperationDetailsBatchResponse
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    auth_config_name: str,
    *,
    body: OperationDetailsBatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations/{organization_id}/connectors/{auth_config_name}/operations/details".format(
            organization_id=quote(str(organization_id), safe=""),
            auth_config_name=quote(str(auth_config_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | OperationDetailsBatchResponse | None:
    if response.status_code == 200:
        response_200 = OperationDetailsBatchResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | OperationDetailsBatchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: OperationDetailsBatchRequest,
) -> Response[ErrorResponse | OperationDetailsBatchResponse]:
    """Get Connector Operation Details In Batch

    Args:
        organization_id (UUID):
        auth_config_name (str):
        body (OperationDetailsBatchRequest): Request multiple operation details in a single call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OperationDetailsBatchResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: OperationDetailsBatchRequest,
) -> ErrorResponse | OperationDetailsBatchResponse | None:
    """Get Connector Operation Details In Batch

    Args:
        organization_id (UUID):
        auth_config_name (str):
        body (OperationDetailsBatchRequest): Request multiple operation details in a single call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OperationDetailsBatchResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: OperationDetailsBatchRequest,
) -> Response[ErrorResponse | OperationDetailsBatchResponse]:
    """Get Connector Operation Details In Batch

    Args:
        organization_id (UUID):
        auth_config_name (str):
        body (OperationDetailsBatchRequest): Request multiple operation details in a single call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | OperationDetailsBatchResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: OperationDetailsBatchRequest,
) -> ErrorResponse | OperationDetailsBatchResponse | None:
    """Get Connector Operation Details In Batch

    Args:
        organization_id (UUID):
        auth_config_name (str):
        body (OperationDetailsBatchRequest): Request multiple operation details in a single call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | OperationDetailsBatchResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            auth_config_name=auth_config_name,
            client=client,
            body=body,
        )
    ).parsed
