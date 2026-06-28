from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_delete_data_body import FilesDeleteDataBody
from ...models.files_delete_files_delete_error_schema import FilesDeleteFilesDeleteErrorSchema
from ...models.files_delete_files_delete_schema import FilesDeleteFilesDeleteSchema
from ...models.files_delete_json_body import FilesDeleteJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesDeleteDataBody  |     FilesDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.delete",
    }

    if isinstance(body, FilesDeleteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesDeleteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema:
    if response.status_code == 200:
        response_200 = FilesDeleteFilesDeleteSchema.from_dict(response.json())



        return response_200

    response_default = FilesDeleteFilesDeleteErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesDeleteDataBody  |     FilesDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema]:
    """  Deletes a file.

    Args:
        token (str | Unset):
        body (FilesDeleteDataBody | Unset):
        body (FilesDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema]
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
    body:    FilesDeleteDataBody  |     FilesDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema | None:
    """  Deletes a file.

    Args:
        token (str | Unset):
        body (FilesDeleteDataBody | Unset):
        body (FilesDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesDeleteDataBody  |     FilesDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema]:
    """  Deletes a file.

    Args:
        token (str | Unset):
        body (FilesDeleteDataBody | Unset):
        body (FilesDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema]
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
    body:    FilesDeleteDataBody  |     FilesDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema | None:
    """  Deletes a file.

    Args:
        token (str | Unset):
        body (FilesDeleteDataBody | Unset):
        body (FilesDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesDeleteFilesDeleteErrorSchema | FilesDeleteFilesDeleteSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
