from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_list_response_schema import AccountListResponseSchema
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: UUID,
    *,
    connector_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_connector_id: None | str | Unset
    if isinstance(connector_id, Unset):
        json_connector_id = UNSET
    else:
        json_connector_id = connector_id
    params["connector_id"] = json_connector_id

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
        "url": "/organizations/{organization_id}/connectors/accounts".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountListResponseSchema | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccountListResponseSchema.from_dict(response.json())

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
) -> Response[AccountListResponseSchema | ErrorResponse]:
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
    connector_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[AccountListResponseSchema | ErrorResponse]:
    """List Accounts

     Get all connected accounts for the current user. Optionally filter by connector_id or connector_name

    Args:
        organization_id (UUID):
        connector_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        connector_id=connector_id,
        limit=limit,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    connector_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> AccountListResponseSchema | ErrorResponse | None:
    """List Accounts

     Get all connected accounts for the current user. Optionally filter by connector_id or connector_name

    Args:
        organization_id (UUID):
        connector_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponseSchema | ErrorResponse
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        connector_id=connector_id,
        limit=limit,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    connector_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[AccountListResponseSchema | ErrorResponse]:
    """List Accounts

     Get all connected accounts for the current user. Optionally filter by connector_id or connector_name

    Args:
        organization_id (UUID):
        connector_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponseSchema | ErrorResponse]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        connector_id=connector_id,
        limit=limit,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    connector_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> AccountListResponseSchema | ErrorResponse | None:
    """List Accounts

     Get all connected accounts for the current user. Optionally filter by connector_id or connector_name

    Args:
        organization_id (UUID):
        connector_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponseSchema | ErrorResponse
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            connector_id=connector_id,
            limit=limit,
            page_token=page_token,
        )
    ).parsed
