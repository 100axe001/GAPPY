from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_list_files_list_error_schema import FilesListFilesListErrorSchema
from ...models.files_list_files_list_schema import FilesListFilesListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    types: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    show_files_hidden_by_limit: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["user"] = user

    params["channel"] = channel

    params["ts_from"] = ts_from

    params["ts_to"] = ts_to

    params["types"] = types

    params["count"] = count

    params["page"] = page

    params["show_files_hidden_by_limit"] = show_files_hidden_by_limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesListFilesListErrorSchema | FilesListFilesListSchema:
    if response.status_code == 200:
        response_200 = FilesListFilesListSchema.from_dict(response.json())



        return response_200

    response_default = FilesListFilesListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesListFilesListErrorSchema | FilesListFilesListSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    types: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    show_files_hidden_by_limit: bool | Unset = UNSET,

) -> Response[FilesListFilesListErrorSchema | FilesListFilesListSchema]:
    """  List for a team, in a channel, or from a user with applied filters.

    Args:
        token (str | Unset):
        user (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        types (str | Unset):
        count (str | Unset):
        page (str | Unset):
        show_files_hidden_by_limit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesListFilesListErrorSchema | FilesListFilesListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
types=types,
count=count,
page=page,
show_files_hidden_by_limit=show_files_hidden_by_limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    types: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    show_files_hidden_by_limit: bool | Unset = UNSET,

) -> FilesListFilesListErrorSchema | FilesListFilesListSchema | None:
    """  List for a team, in a channel, or from a user with applied filters.

    Args:
        token (str | Unset):
        user (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        types (str | Unset):
        count (str | Unset):
        page (str | Unset):
        show_files_hidden_by_limit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesListFilesListErrorSchema | FilesListFilesListSchema
     """


    return sync_detailed(
        client=client,
token=token,
user=user,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
types=types,
count=count,
page=page,
show_files_hidden_by_limit=show_files_hidden_by_limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    types: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    show_files_hidden_by_limit: bool | Unset = UNSET,

) -> Response[FilesListFilesListErrorSchema | FilesListFilesListSchema]:
    """  List for a team, in a channel, or from a user with applied filters.

    Args:
        token (str | Unset):
        user (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        types (str | Unset):
        count (str | Unset):
        page (str | Unset):
        show_files_hidden_by_limit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesListFilesListErrorSchema | FilesListFilesListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
types=types,
count=count,
page=page,
show_files_hidden_by_limit=show_files_hidden_by_limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    user: str | Unset = UNSET,
    channel: str | Unset = UNSET,
    ts_from: float | Unset = UNSET,
    ts_to: float | Unset = UNSET,
    types: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    show_files_hidden_by_limit: bool | Unset = UNSET,

) -> FilesListFilesListErrorSchema | FilesListFilesListSchema | None:
    """  List for a team, in a channel, or from a user with applied filters.

    Args:
        token (str | Unset):
        user (str | Unset):
        channel (str | Unset):
        ts_from (float | Unset):
        ts_to (float | Unset):
        types (str | Unset):
        count (str | Unset):
        page (str | Unset):
        show_files_hidden_by_limit (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesListFilesListErrorSchema | FilesListFilesListSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
user=user,
channel=channel,
ts_from=ts_from,
ts_to=ts_to,
types=types,
count=count,
page=page,
show_files_hidden_by_limit=show_files_hidden_by_limit,

    )).parsed
