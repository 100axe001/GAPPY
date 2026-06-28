from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_remove_data_body import FilesRemoteRemoveDataBody
from ...models.files_remote_remove_default_error_template import FilesRemoteRemoveDefaultErrorTemplate
from ...models.files_remote_remove_default_success_template import FilesRemoteRemoveDefaultSuccessTemplate
from ...models.files_remote_remove_json_body import FilesRemoteRemoveJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesRemoteRemoveDataBody  |     FilesRemoteRemoveJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.remote.remove",
    }

    if isinstance(body, FilesRemoteRemoveDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesRemoteRemoveJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteRemoveDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteRemoveDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteRemoveDataBody  |     FilesRemoteRemoveJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate]:
    """  Remove a remote file.

    Args:
        body (FilesRemoteRemoveDataBody | Unset):
        body (FilesRemoteRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate]
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
    body:    FilesRemoteRemoveDataBody  |     FilesRemoteRemoveJsonBody  | Unset = UNSET,

) -> FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate | None:
    """  Remove a remote file.

    Args:
        body (FilesRemoteRemoveDataBody | Unset):
        body (FilesRemoteRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteRemoveDataBody  |     FilesRemoteRemoveJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate]:
    """  Remove a remote file.

    Args:
        body (FilesRemoteRemoveDataBody | Unset):
        body (FilesRemoteRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate]
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
    body:    FilesRemoteRemoveDataBody  |     FilesRemoteRemoveJsonBody  | Unset = UNSET,

) -> FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate | None:
    """  Remove a remote file.

    Args:
        body (FilesRemoteRemoveDataBody | Unset):
        body (FilesRemoteRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteRemoveDefaultErrorTemplate | FilesRemoteRemoveDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
