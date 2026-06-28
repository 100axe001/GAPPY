from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_message_response import AgentMessageResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    agent_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/pods/{pod_id}/agents/{agent_name}".format(
            pod_id=quote(str(pod_id), safe=""),
            agent_name=quote(str(agent_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentMessageResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AgentMessageResponse.from_dict(response.json())

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
) -> Response[AgentMessageResponse | ErrorResponse]:
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
) -> Response[AgentMessageResponse | ErrorResponse]:
    """Delete Agent

     Delete a pod-owned agent definition by name.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentMessageResponse | ErrorResponse]
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
) -> AgentMessageResponse | ErrorResponse | None:
    """Delete Agent

     Delete a pod-owned agent definition by name.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentMessageResponse | ErrorResponse
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
) -> Response[AgentMessageResponse | ErrorResponse]:
    """Delete Agent

     Delete a pod-owned agent definition by name.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentMessageResponse | ErrorResponse]
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
) -> AgentMessageResponse | ErrorResponse | None:
    """Delete Agent

     Delete a pod-owned agent definition by name.

    Args:
        pod_id (UUID):
        agent_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentMessageResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            agent_name=agent_name,
            client=client,
        )
    ).parsed
