from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_revoke_public_url_data_body import FilesRevokePublicURLDataBody
from ...models.files_revoke_public_url_files_revoke_public_url_error_schema import FilesRevokePublicURLFilesRevokePublicURLErrorSchema
from ...models.files_revoke_public_url_files_revoke_public_url_schema import FilesRevokePublicURLFilesRevokePublicURLSchema
from ...models.files_revoke_public_url_json_body import FilesRevokePublicURLJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesRevokePublicURLDataBody  |     FilesRevokePublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.revokePublicURL",
    }

    if isinstance(body, FilesRevokePublicURLDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesRevokePublicURLJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema:
    if response.status_code == 200:
        response_200 = FilesRevokePublicURLFilesRevokePublicURLSchema.from_dict(response.json())



        return response_200

    response_default = FilesRevokePublicURLFilesRevokePublicURLErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRevokePublicURLDataBody  |     FilesRevokePublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema]:
    """  Revokes public/external sharing access for a file

    Args:
        token (str | Unset):
        body (FilesRevokePublicURLDataBody | Unset):
        body (FilesRevokePublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema]
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
    body:    FilesRevokePublicURLDataBody  |     FilesRevokePublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema | None:
    """  Revokes public/external sharing access for a file

    Args:
        token (str | Unset):
        body (FilesRevokePublicURLDataBody | Unset):
        body (FilesRevokePublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRevokePublicURLDataBody  |     FilesRevokePublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema]:
    """  Revokes public/external sharing access for a file

    Args:
        token (str | Unset):
        body (FilesRevokePublicURLDataBody | Unset):
        body (FilesRevokePublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema]
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
    body:    FilesRevokePublicURLDataBody  |     FilesRevokePublicURLJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema | None:
    """  Revokes public/external sharing access for a file

    Args:
        token (str | Unset):
        body (FilesRevokePublicURLDataBody | Unset):
        body (FilesRevokePublicURLJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRevokePublicURLFilesRevokePublicURLErrorSchema | FilesRevokePublicURLFilesRevokePublicURLSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
