from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pod_join_request_list_response import PodJoinRequestListResponse
from ...models.pod_join_request_status import PodJoinRequestStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    *,
    status_filter: None | PodJoinRequestStatus | Unset = PodJoinRequestStatus.PENDING,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status_filter: None | str | Unset
    if isinstance(status_filter, Unset):
        json_status_filter = UNSET
    elif isinstance(status_filter, PodJoinRequestStatus):
        json_status_filter = status_filter.value
    else:
        json_status_filter = status_filter
    params["status_filter"] = json_status_filter

    params["limit"] = limit

    json_page_token: None | str | Unset
    if isinstance(page_token, Unset):
        json_page_token = UNSET
    else:
        json_page_token = page_token
    params["page_token"] = json_page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/join-requests".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PodJoinRequestListResponse | None:
    if response.status_code == 200:
        response_200 = PodJoinRequestListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | PodJoinRequestListResponse]:
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
    status_filter: None | PodJoinRequestStatus | Unset = PodJoinRequestStatus.PENDING,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[ErrorResponse | PodJoinRequestListResponse]:
    """List Pod Join Requests

     List join requests for a pod

    Args:
        pod_id (UUID):
        status_filter (None | PodJoinRequestStatus | Unset):  Default:
            PodJoinRequestStatus.PENDING.
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodJoinRequestListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        status_filter=status_filter,
        limit=limit,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status_filter: None | PodJoinRequestStatus | Unset = PodJoinRequestStatus.PENDING,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> ErrorResponse | PodJoinRequestListResponse | None:
    """List Pod Join Requests

     List join requests for a pod

    Args:
        pod_id (UUID):
        status_filter (None | PodJoinRequestStatus | Unset):  Default:
            PodJoinRequestStatus.PENDING.
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodJoinRequestListResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        status_filter=status_filter,
        limit=limit,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status_filter: None | PodJoinRequestStatus | Unset = PodJoinRequestStatus.PENDING,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[ErrorResponse | PodJoinRequestListResponse]:
    """List Pod Join Requests

     List join requests for a pod

    Args:
        pod_id (UUID):
        status_filter (None | PodJoinRequestStatus | Unset):  Default:
            PodJoinRequestStatus.PENDING.
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PodJoinRequestListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        status_filter=status_filter,
        limit=limit,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status_filter: None | PodJoinRequestStatus | Unset = PodJoinRequestStatus.PENDING,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> ErrorResponse | PodJoinRequestListResponse | None:
    """List Pod Join Requests

     List join requests for a pod

    Args:
        pod_id (UUID):
        status_filter (None | PodJoinRequestStatus | Unset):  Default:
            PodJoinRequestStatus.PENDING.
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PodJoinRequestListResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            status_filter=status_filter,
            limit=limit,
            page_token=page_token,
        )
    ).parsed
