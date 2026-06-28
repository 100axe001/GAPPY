from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_comments_delete_data_body import FilesCommentsDeleteDataBody
from ...models.files_comments_delete_files_comments_delete_error_schema import FilesCommentsDeleteFilesCommentsDeleteErrorSchema
from ...models.files_comments_delete_files_comments_delete_schema import FilesCommentsDeleteFilesCommentsDeleteSchema
from ...models.files_comments_delete_json_body import FilesCommentsDeleteJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesCommentsDeleteDataBody  |     FilesCommentsDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.comments.delete",
    }

    if isinstance(body, FilesCommentsDeleteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesCommentsDeleteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema:
    if response.status_code == 200:
        response_200 = FilesCommentsDeleteFilesCommentsDeleteSchema.from_dict(response.json())



        return response_200

    response_default = FilesCommentsDeleteFilesCommentsDeleteErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesCommentsDeleteDataBody  |     FilesCommentsDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema]:
    """  Deletes an existing comment on a file.

    Args:
        token (str | Unset):
        body (FilesCommentsDeleteDataBody | Unset):
        body (FilesCommentsDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    FilesCommentsDeleteDataBody  |     FilesCommentsDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema | None:
    """  Deletes an existing comment on a file.

    Args:
        token (str | Unset):
        body (FilesCommentsDeleteDataBody | Unset):
        body (FilesCommentsDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesCommentsDeleteDataBody  |     FilesCommentsDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema]:
    """  Deletes an existing comment on a file.

    Args:
        token (str | Unset):
        body (FilesCommentsDeleteDataBody | Unset):
        body (FilesCommentsDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    FilesCommentsDeleteDataBody  |     FilesCommentsDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema | None:
    """  Deletes an existing comment on a file.

    Args:
        token (str | Unset):
        body (FilesCommentsDeleteDataBody | Unset):
        body (FilesCommentsDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesCommentsDeleteFilesCommentsDeleteErrorSchema | FilesCommentsDeleteFilesCommentsDeleteSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
