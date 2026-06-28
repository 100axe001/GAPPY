from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_shared_public_url_data_body import FilesSharedPublicURLDataBody
from ...models.files_shared_public_url_files_shared_public_url_error_schema import FilesSharedPublicURLFilesSharedPublicURLErrorSchema
from ...models.files_shared_public_url_files_shared_public_url_schema import FilesSharedPublicURLFilesSharedPublicURLSchema
from ...models.files_shared_public_url_json_body import FilesSharedPublicURLJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesSharedPublicURLDataBody  |     FilesSharedPublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.sharedPublicURL",
    }

    if isinstance(body, FilesSharedPublicURLDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesSharedPublicURLJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema:
    if response.status_code == 200:
        response_200 = FilesSharedPublicURLFilesSharedPublicURLSchema.from_dict(response.json())



        return response_200

    response_default = FilesSharedPublicURLFilesSharedPublicURLErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesSharedPublicURLDataBody  |     FilesSharedPublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema]:
    """  Enables a file for public/external sharing.

    Args:
        token (str | Unset):
        body (FilesSharedPublicURLDataBody | Unset):
        body (FilesSharedPublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema]
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
    body:    FilesSharedPublicURLDataBody  |     FilesSharedPublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema | None:
    """  Enables a file for public/external sharing.

    Args:
        token (str | Unset):
        body (FilesSharedPublicURLDataBody | Unset):
        body (FilesSharedPublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesSharedPublicURLDataBody  |     FilesSharedPublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema]:
    """  Enables a file for public/external sharing.

    Args:
        token (str | Unset):
        body (FilesSharedPublicURLDataBody | Unset):
        body (FilesSharedPublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema]
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
    body:    FilesSharedPublicURLDataBody  |     FilesSharedPublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema | None:
    """  Enables a file for public/external sharing.

    Args:
        token (str | Unset):
        body (FilesSharedPublicURLDataBody | Unset):
        body (FilesSharedPublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesSharedPublicURLFilesSharedPublicURLErrorSchema | FilesSharedPublicURLFilesSharedPublicURLSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
