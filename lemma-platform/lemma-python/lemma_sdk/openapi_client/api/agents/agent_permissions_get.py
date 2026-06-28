from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_permissions_response import AgentPermissionsResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    agent_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/agents/{agent_name}/permissions".format(
            pod_id=quote(str(pod_id), safe=""),
            agent_name=quote(str(agent_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentPermissionsResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AgentPermissionsResponse.from_dict(response.json())

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
) -> Response[AgentPermissionsResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AgentPermissionsResponse | ErrorResponse]:
    """Get Agent Resource Permissions

     Get explicit resource grants assigned to an agent.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPermissionsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        agent_name=agent_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> AgentPermissionsResponse | ErrorResponse | None:
    """Get Agent Resource Permissions

     Get explicit resource grants assigned to an agent.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPermissionsResponse | ErrorResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        agent_name=agent_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AgentPermissionsResponse | ErrorResponse]:
    """Get Agent Resource Permissions

     Get explicit resource grants assigned to an agent.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPermissionsResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        agent_name=agent_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> AgentPermissionsResponse | ErrorResponse | None:
    """Get Agent Resource Permissions

     Get explicit resource grants assigned to an agent.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPermissionsResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            agent_name=agent_name,
            client=client,
        )
    ).parsed
