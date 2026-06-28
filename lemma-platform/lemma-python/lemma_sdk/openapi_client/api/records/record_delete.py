from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.record_access_mode import RecordAccessMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    table_name: str,
    record_id: str,
    *,
    mode: None | RecordAccessMode | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_mode: None | str | Unset
    if isinstance(mode, Unset):
        json_mode = UNSET
    elif isinstance(mode, RecordAccessMode):
        json_mode = mode.value
    else:
        json_mode = mode
    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/pods/{pod_id}/datastore/tables/{table_name}/records/{record_id}".format(
            pod_id=quote(str(pod_id), safe=""),
            table_name=quote(str(table_name), safe=""),
            record_id=quote(str(record_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    table_name: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: None | RecordAccessMode | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Delete Record

     Delete a record by primary key.

    Args:
        pod_id (UUID):
        table_name (str):
        record_id (str):
        mode (None | RecordAccessMode | Unset): Row-visibility mode for RLS-enabled tables.
            Omitted/`USER` (default) scopes rows to the signed-in user's own records — the per-user
            semantics an app app expects. `ADMIN` returns/operates on every member's rows and requires
            permission to administer the table; a caller without it gets a 403. Ignored for non-RLS
            tables, whose rows are shared by all members.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        table_name=table_name,
        record_id=record_id,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    table_name: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: None | RecordAccessMode | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Delete Record

     Delete a record by primary key.

    Args:
        pod_id (UUID):
        table_name (str):
        record_id (str):
        mode (None | RecordAccessMode | Unset): Row-visibility mode for RLS-enabled tables.
            Omitted/`USER` (default) scopes rows to the signed-in user's own records — the per-user
            semantics an app app expects. `ADMIN` returns/operates on every member's rows and requires
            permission to administer the table; a caller without it gets a 403. Ignored for non-RLS
            tables, whose rows are shared by all members.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        table_name=table_name,
        record_id=record_id,
        client=client,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    table_name: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: None | RecordAccessMode | Unset = UNSET,
) -> Response[Any | ErrorResponse]:
    """Delete Record

     Delete a record by primary key.

    Args:
        pod_id (UUID):
        table_name (str):
        record_id (str):
        mode (None | RecordAccessMode | Unset): Row-visibility mode for RLS-enabled tables.
            Omitted/`USER` (default) scopes rows to the signed-in user's own records — the per-user
            semantics an app app expects. `ADMIN` returns/operates on every member's rows and requires
            permission to administer the table; a caller without it gets a 403. Ignored for non-RLS
            tables, whose rows are shared by all members.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        table_name=table_name,
        record_id=record_id,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    table_name: str,
    record_id: str,
    *,
    client: AuthenticatedClient | Client,
    mode: None | RecordAccessMode | Unset = UNSET,
) -> Any | ErrorResponse | None:
    """Delete Record

     Delete a record by primary key.

    Args:
        pod_id (UUID):
        table_name (str):
        record_id (str):
        mode (None | RecordAccessMode | Unset): Row-visibility mode for RLS-enabled tables.
            Omitted/`USER` (default) scopes rows to the signed-in user's own records — the per-user
            semantics an app app expects. `ADMIN` returns/operates on every member's rows and requires
            permission to administer the table; a caller without it gets a 403. Ignored for non-RLS
            tables, whose rows are shared by all members.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            table_name=table_name,
            record_id=record_id,
            client=client,
            mode=mode,
        )
    ).parsed
