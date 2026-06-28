from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_upload_data_body import FilesUploadDataBody
from ...models.files_upload_files_upload_error_schema import FilesUploadFilesUploadErrorSchema
from ...models.files_upload_files_upload_schema import FilesUploadFilesUploadSchema
from ...models.files_upload_json_body import FilesUploadJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesUploadDataBody  |     FilesUploadJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.upload",
    }

    if isinstance(body, FilesUploadDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesUploadJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema:
    if response.status_code == 200:
        response_200 = FilesUploadFilesUploadSchema.from_dict(response.json())



        return response_200

    response_default = FilesUploadFilesUploadErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesUploadDataBody  |     FilesUploadJsonBody  | Unset = UNSET,

) -> Response[FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema]:
    """  Uploads or creates a file.

    Args:
        body (FilesUploadDataBody | Unset):
        body (FilesUploadJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    FilesUploadDataBody  |     FilesUploadJsonBody  | Unset = UNSET,

) -> FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema | None:
    """  Uploads or creates a file.

    Args:
        body (FilesUploadDataBody | Unset):
        body (FilesUploadJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesUploadDataBody  |     FilesUploadJsonBody  | Unset = UNSET,

) -> Response[FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema]:
    """  Uploads or creates a file.

    Args:
        body (FilesUploadDataBody | Unset):
        body (FilesUploadJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    FilesUploadDataBody  |     FilesUploadJsonBody  | Unset = UNSET,

) -> FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema | None:
    """  Uploads or creates a file.

    Args:
        body (FilesUploadDataBody | Unset):
        body (FilesUploadJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesUploadFilesUploadErrorSchema | FilesUploadFilesUploadSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
