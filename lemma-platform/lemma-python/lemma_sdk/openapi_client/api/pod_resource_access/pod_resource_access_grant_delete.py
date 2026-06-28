from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.resource_access_response import ResourceAccessResponse
from ...models.resource_type import ResourceType
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    resource_type: ResourceType,
    resource_name: str,
    grantee_type: str,
    grantee_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/pods/{pod_id}/resources/{resource_type}/{resource_name}/access/grantees/{grantee_type}/{grantee_id}".format(
            pod_id=quote(str(pod_id), safe=""),
            resource_type=quote(str(resource_type), safe=""),
            resource_name=quote(str(resource_name), safe=""),
            grantee_type=quote(str(grantee_type), safe=""),
            grantee_id=quote(str(grantee_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ResourceAccessResponse | None:
    if response.status_code == 200:
        response_200 = ResourceAccessResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | ResourceAccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    resource_type: ResourceType,
    resource_name: str,
    grantee_type: str,
    grantee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ResourceAccessResponse]:
    """Delete Resource Access Grant

    Args:
        pod_id (UUID):
        resource_type (ResourceType):
        resource_name (str):
        grantee_type (str):
        grantee_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceAccessResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        resource_type=resource_type,
        resource_name=resource_name,
        grantee_type=grantee_type,
        grantee_id=grantee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    resource_type: ResourceType,
    resource_name: str,
    grantee_type: str,
    grantee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | ResourceAccessResponse | None:
    """Delete Resource Access Grant

    Args:
        pod_id (UUID):
        resource_type (ResourceType):
        resource_name (str):
        grantee_type (str):
        grantee_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceAccessResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        resource_type=resource_type,
        resource_name=resource_name,
        grantee_type=grantee_type,
        grantee_id=grantee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    resource_type: ResourceType,
    resource_name: str,
    grantee_type: str,
    grantee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | ResourceAccessResponse]:
    """Delete Resource Access Grant

    Args:
        pod_id (UUID):
        resource_type (ResourceType):
        resource_name (str):
        grantee_type (str):
        grantee_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResourceAccessResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        resource_type=resource_type,
        resource_name=resource_name,
        grantee_type=grantee_type,
        grantee_id=grantee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    resource_type: ResourceType,
    resource_name: str,
    grantee_type: str,
    grantee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | ResourceAccessResponse | None:
    """Delete Resource Access Grant

    Args:
        pod_id (UUID):
        resource_type (ResourceType):
        resource_name (str):
        grantee_type (str):
        grantee_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResourceAccessResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            resource_type=resource_type,
            resource_name=resource_name,
            grantee_type=grantee_type,
            grantee_id=grantee_id,
            client=client,
        )
    ).parsed
