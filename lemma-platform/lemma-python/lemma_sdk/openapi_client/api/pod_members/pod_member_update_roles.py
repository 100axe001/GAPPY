from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pod_member_response import PodMemberResponse
from ...models.pod_member_update_role_request import PodMemberUpdateRoleRequest
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    pod_member_id: UUID,
    *,
    body: PodMemberUpdateRoleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/pods/{pod_id}/members/{pod_member_id}/roles".format(
            pod_id=quote(str(pod_id), safe=""),
            pod_member_id=quote(str(pod_member_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PodMemberResponse | None:
    if response.status_code == 200:
        response_200 = PodMemberResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PodMemberResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    pod_member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PodMemberUpdateRoleRequest,
) -> Response[ErrorResponse | PodMemberResponse]:
    """Update Member Roles

     Update a pod member's roles

    Args:
        pod_id (UUID):
        pod_member_id (UUID):
        body (PodMemberUpdateRoleRequest): Pod member role update request schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodMemberResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        pod_member_id=pod_member_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    pod_member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PodMemberUpdateRoleRequest,
) -> ErrorResponse | PodMemberResponse | None:
    """Update Member Roles

     Update a pod member's roles

    Args:
        pod_id (UUID):
        pod_member_id (UUID):
        body (PodMemberUpdateRoleRequest): Pod member role update request schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodMemberResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        pod_member_id=pod_member_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    pod_member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PodMemberUpdateRoleRequest,
) -> Response[ErrorResponse | PodMemberResponse]:
    """Update Member Roles

     Update a pod member's roles

    Args:
        pod_id (UUID):
        pod_member_id (UUID):
        body (PodMemberUpdateRoleRequest): Pod member role update request schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodMemberResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        pod_member_id=pod_member_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    pod_member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PodMemberUpdateRoleRequest,
) -> ErrorResponse | PodMemberResponse | None:
    """Update Member Roles

     Update a pod member's roles

    Args:
        pod_id (UUID):
        pod_member_id (UUID):
        body (PodMemberUpdateRoleRequest): Pod member role update request schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodMemberResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            pod_member_id=pod_member_id,
            client=client,
            body=body,
        )
    ).parsed
