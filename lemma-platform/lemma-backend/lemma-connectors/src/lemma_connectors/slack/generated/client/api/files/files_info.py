from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_info_files_info_error_schema import FilesInfoFilesInfoErrorSchema
from ...models.files_info_files_info_schema import FilesInfoFilesInfoSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["file"] = file

    params["count"] = count

    params["page"] = page

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema:
    if response.status_code == 200:
        response_200 = FilesInfoFilesInfoSchema.from_dict(response.json())



        return response_200

    response_default = FilesInfoFilesInfoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema]:
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
    file: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema]:
    """  Gets information about a file.

    Args:
        token (str | Unset):
        file (str | Unset):
        count (str | Unset):
        page (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
count=count,
page=page,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema | None:
    """  Gets information about a file.

    Args:
        token (str | Unset):
        file (str | Unset):
        count (str | Unset):
        page (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema
     """


    return sync_detailed(
        client=client,
token=token,
file=file,
count=count,
page=page,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema]:
    """  Gets information about a file.

    Args:
        token (str | Unset):
        file (str | Unset):
        count (str | Unset):
        page (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
file=file,
count=count,
page=page,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    file: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema | None:
    """  Gets information about a file.

    Args:
        token (str | Unset):
        file (str | Unset):
        count (str | Unset):
        page (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesInfoFilesInfoErrorSchema | FilesInfoFilesInfoSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
file=file,
count=count,
page=page,
limit=limit,
cursor=cursor,

    )).parsed
