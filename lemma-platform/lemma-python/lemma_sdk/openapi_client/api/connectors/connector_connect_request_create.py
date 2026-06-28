from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect_request_initiate_schema import ConnectRequestInitiateSchema
from ...models.connect_request_response_schema import ConnectRequestResponseSchema
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    organization_id: UUID,
    *,
    body: ConnectRequestInitiateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organizations/{organization_id}/connectors/connect-requests".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectRequestResponseSchema | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ConnectRequestResponseSchema.from_dict(response.json())

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
) -> Response[ConnectRequestResponseSchema | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequestInitiateSchema,
) -> Response[ConnectRequestResponseSchema | ErrorResponse]:
    """Initiate Connect Request

     Initiate an OAuth connection request for a connector

    Args:
        organization_id (UUID):
        body (ConnectRequestInitiateSchema): Schema for initiating a connect request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRequestResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequestInitiateSchema,
) -> ConnectRequestResponseSchema | ErrorResponse | None:
    """Initiate Connect Request

     Initiate an OAuth connection request for a connector

    Args:
        organization_id (UUID):
        body (ConnectRequestInitiateSchema): Schema for initiating a connect request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRequestResponseSchema | ErrorResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequestInitiateSchema,
) -> Response[ConnectRequestResponseSchema | ErrorResponse]:
    """Initiate Connect Request

     Initiate an OAuth connection request for a connector

    Args:
        organization_id (UUID):
        body (ConnectRequestInitiateSchema): Schema for initiating a connect request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectRequestResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequestInitiateSchema,
) -> ConnectRequestResponseSchema | ErrorResponse | None:
    """Initiate Connect Request

     Initiate an OAuth connection request for a connector

    Args:
        organization_id (UUID):
        body (ConnectRequestInitiateSchema): Schema for initiating a connect request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectRequestResponseSchema | ErrorResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
