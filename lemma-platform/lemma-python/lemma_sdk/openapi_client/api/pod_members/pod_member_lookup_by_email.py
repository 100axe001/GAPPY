from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pod_member_detail_response import PodMemberDetailResponse
from ...types import UNSET, Response


def _get_kwargs(
    pod_id: UUID,
    *,
    email: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/members/lookup/by-email".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PodMemberDetailResponse | None:
    if response.status_code == 200:
        response_200 = PodMemberDetailResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PodMemberDetailResponse]:
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
    email: str,
) -> Response[ErrorResponse | PodMemberDetailResponse]:
    """Lookup Pod Member By Email

     Resolve a pod member by email

    Args:
        pod_id (UUID):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodMemberDetailResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        email=email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    email: str,
) -> ErrorResponse | PodMemberDetailResponse | None:
    """Lookup Pod Member By Email

     Resolve a pod member by email

    Args:
        pod_id (UUID):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodMemberDetailResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        email=email,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    email: str,
) -> Response[ErrorResponse | PodMemberDetailResponse]:
    """Lookup Pod Member By Email

     Resolve a pod member by email

    Args:
        pod_id (UUID):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodMemberDetailResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        email=email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    email: str,
) -> ErrorResponse | PodMemberDetailResponse | None:
    """Lookup Pod Member By Email

     Resolve a pod member by email

    Args:
        pod_id (UUID):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodMemberDetailResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            email=email,
        )
    ).parsed
