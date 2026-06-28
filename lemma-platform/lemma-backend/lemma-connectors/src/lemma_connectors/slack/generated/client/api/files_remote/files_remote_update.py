from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_update_data_body import FilesRemoteUpdateDataBody
from ...models.files_remote_update_default_error_template import FilesRemoteUpdateDefaultErrorTemplate
from ...models.files_remote_update_default_success_template import FilesRemoteUpdateDefaultSuccessTemplate
from ...models.files_remote_update_json_body import FilesRemoteUpdateJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesRemoteUpdateDataBody  |     FilesRemoteUpdateJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.remote.update",
    }

    if isinstance(body, FilesRemoteUpdateDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesRemoteUpdateJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteUpdateDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteUpdateDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteUpdateDataBody  |     FilesRemoteUpdateJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate]:
    """  Updates an existing remote file.

    Args:
        body (FilesRemoteUpdateDataBody | Unset):
        body (FilesRemoteUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate]
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
    body:    FilesRemoteUpdateDataBody  |     FilesRemoteUpdateJsonBody  | Unset = UNSET,

) -> FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate | None:
    """  Updates an existing remote file.

    Args:
        body (FilesRemoteUpdateDataBody | Unset):
        body (FilesRemoteUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteUpdateDataBody  |     FilesRemoteUpdateJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate]:
    """  Updates an existing remote file.

    Args:
        body (FilesRemoteUpdateDataBody | Unset):
        body (FilesRemoteUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate]
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
    body:    FilesRemoteUpdateDataBody  |     FilesRemoteUpdateJsonBody  | Unset = UNSET,

) -> FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate | None:
    """  Updates an existing remote file.

    Args:
        body (FilesRemoteUpdateDataBody | Unset):
        body (FilesRemoteUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteUpdateDefaultErrorTemplate | FilesRemoteUpdateDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
