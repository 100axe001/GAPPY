from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_trigger_list_response_schema import AppTriggerListResponseSchema
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    auth_config_name: str,
    *,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organizations/{organization_id}/connectors/{auth_config_name}/triggers".format(
            organization_id=quote(str(organization_id), safe=""),
            auth_config_name=quote(str(auth_config_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppTriggerListResponseSchema | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AppTriggerListResponseSchema.from_dict(response.json())

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
) -> Response[AppTriggerListResponseSchema | ErrorResponse]:
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
    search: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[AppTriggerListResponseSchema | ErrorResponse]:
    """List Connector Triggers

    Args:
        organization_id (UUID):
        auth_config_name (str):
        search (None | str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppTriggerListResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        search=search,
        limit=limit,
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
    search: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> AppTriggerListResponseSchema | ErrorResponse | None:
    """List Connector Triggers

    Args:
        organization_id (UUID):
        auth_config_name (str):
        search (None | str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppTriggerListResponseSchema | ErrorResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        client=client,
        search=search,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[AppTriggerListResponseSchema | ErrorResponse]:
    """List Connector Triggers

    Args:
        organization_id (UUID):
        auth_config_name (str):
        search (None | str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppTriggerListResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        search=search,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    auth_config_name: str,
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 100,
) -> AppTriggerListResponseSchema | ErrorResponse | None:
    """List Connector Triggers

    Args:
        organization_id (UUID):
        auth_config_name (str):
        search (None | str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppTriggerListResponseSchema | ErrorResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            auth_config_name=auth_config_name,
            client=client,
            search=search,
            limit=limit,
        )
    ).parsed
