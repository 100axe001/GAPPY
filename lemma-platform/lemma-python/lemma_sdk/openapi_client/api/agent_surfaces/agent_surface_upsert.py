from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.surface_upsert_request import SurfaceUpsertRequest
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    platform: str,
    *,
    body: SurfaceUpsertRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/pods/{pod_id}/surfaces/{platform}".format(
            pod_id=quote(str(pod_id), safe=""),
            platform=quote(str(platform), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    platform: str,
    *,
    client: AuthenticatedClient | Client,
    body: SurfaceUpsertRequest,
) -> Response[Any | ErrorResponse]:
    """Upsert Surface

     Create the surface for a platform, or merge updates into the existing one.

    A surface is unique per ``pod_id + platform``, so this single idempotent
    write covers create, config edits, channel routing, account/credential
    changes, and enable/disable. Only fields present in the request are applied
    on update.

    Args:
        pod_id (UUID):
        platform (str):
        body (SurfaceUpsertRequest): The single create-or-update body for `PUT
            /surfaces/{platform}`.

            A surface is uniquely identified by `pod_id + platform`, so this one
            request handles both creation and partial update. Only the fields present
            in the request are applied on update (merge semantics); `is_enabled`
            defaults to True on create and is only changed on update when sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        platform=platform,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    platform: str,
    *,
    client: AuthenticatedClient | Client,
    body: SurfaceUpsertRequest,
) -> Any | ErrorResponse | None:
    """Upsert Surface

     Create the surface for a platform, or merge updates into the existing one.

    A surface is unique per ``pod_id + platform``, so this single idempotent
    write covers create, config edits, channel routing, account/credential
    changes, and enable/disable. Only fields present in the request are applied
    on update.

    Args:
        pod_id (UUID):
        platform (str):
        body (SurfaceUpsertRequest): The single create-or-update body for `PUT
            /surfaces/{platform}`.

            A surface is uniquely identified by `pod_id + platform`, so this one
            request handles both creation and partial update. Only the fields present
            in the request are applied on update (merge semantics); `is_enabled`
            defaults to True on create and is only changed on update when sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        platform=platform,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    platform: str,
    *,
    client: AuthenticatedClient | Client,
    body: SurfaceUpsertRequest,
) -> Response[Any | ErrorResponse]:
    """Upsert Surface

     Create the surface for a platform, or merge updates into the existing one.

    A surface is unique per ``pod_id + platform``, so this single idempotent
    write covers create, config edits, channel routing, account/credential
    changes, and enable/disable. Only fields present in the request are applied
    on update.

    Args:
        pod_id (UUID):
        platform (str):
        body (SurfaceUpsertRequest): The single create-or-update body for `PUT
            /surfaces/{platform}`.

            A surface is uniquely identified by `pod_id + platform`, so this one
            request handles both creation and partial update. Only the fields present
            in the request are applied on update (merge semantics); `is_enabled`
            defaults to True on create and is only changed on update when sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        platform=platform,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    platform: str,
    *,
    client: AuthenticatedClient | Client,
    body: SurfaceUpsertRequest,
) -> Any | ErrorResponse | None:
    """Upsert Surface

     Create the surface for a platform, or merge updates into the existing one.

    A surface is unique per ``pod_id + platform``, so this single idempotent
    write covers create, config edits, channel routing, account/credential
    changes, and enable/disable. Only fields present in the request are applied
    on update.

    Args:
        pod_id (UUID):
        platform (str):
        body (SurfaceUpsertRequest): The single create-or-update body for `PUT
            /surfaces/{platform}`.

            A surface is uniquely identified by `pod_id + platform`, so this one
            request handles both creation and partial update. Only the fields present
            in the request are applied on update (merge semantics); `is_enabled`
            defaults to True on create and is only changed on update when sent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            platform=platform,
            client=client,
            body=body,
        )
    ).parsed
