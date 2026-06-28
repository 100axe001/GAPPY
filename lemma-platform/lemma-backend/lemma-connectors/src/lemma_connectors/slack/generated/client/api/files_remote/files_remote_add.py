from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.files_remote_add_data_body import FilesRemoteAddDataBody
from ...models.files_remote_add_default_error_template import FilesRemoteAddDefaultErrorTemplate
from ...models.files_remote_add_default_success_template import FilesRemoteAddDefaultSuccessTemplate
from ...models.files_remote_add_json_body import FilesRemoteAddJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    FilesRemoteAddDataBody  |     FilesRemoteAddJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files.remote.add",
    }

    if isinstance(body, FilesRemoteAddDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, FilesRemoteAddJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = FilesRemoteAddDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = FilesRemoteAddDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteAddDataBody  |     FilesRemoteAddJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate]:
    """  Adds a file from a remote service

    Args:
        body (FilesRemoteAddDataBody | Unset):
        body (FilesRemoteAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate]
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
    body:    FilesRemoteAddDataBody  |     FilesRemoteAddJsonBody  | Unset = UNSET,

) -> FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate | None:
    """  Adds a file from a remote service

    Args:
        body (FilesRemoteAddDataBody | Unset):
        body (FilesRemoteAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    FilesRemoteAddDataBody  |     FilesRemoteAddJsonBody  | Unset = UNSET,

) -> Response[FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate]:
    """  Adds a file from a remote service

    Args:
        body (FilesRemoteAddDataBody | Unset):
        body (FilesRemoteAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate]
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
    body:    FilesRemoteAddDataBody  |     FilesRemoteAddJsonBody  | Unset = UNSET,

) -> FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate | None:
    """  Adds a file from a remote service

    Args:
        body (FilesRemoteAddDataBody | Unset):
        body (FilesRemoteAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesRemoteAddDefaultErrorTemplate | FilesRemoteAddDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
