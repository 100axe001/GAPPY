from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_avatar_image_by_type_format import GetAvatarImageByTypeFormat
from ...models.get_avatar_image_by_type_response_200 import GetAvatarImageByTypeResponse200
from ...models.get_avatar_image_by_type_size import GetAvatarImageByTypeSize
from ...models.get_avatar_image_by_type_type import GetAvatarImageByTypeType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    type_: GetAvatarImageByTypeType,
    *,
    size: GetAvatarImageByTypeSize | Unset = UNSET,
    format_: GetAvatarImageByTypeFormat | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_size: str | Unset = UNSET
    if not isinstance(size, Unset):
        json_size = size.value

    params["size"] = json_size

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/universal_avatar/view/type/{type_}".format(type_=quote(str(type_), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | GetAvatarImageByTypeResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAvatarImageByTypeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | GetAvatarImageByTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetAvatarImageByTypeType,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByTypeSize | Unset = UNSET,
    format_: GetAvatarImageByTypeFormat | Unset = UNSET,

) -> Response[ErrorCollection | GetAvatarImageByTypeResponse200]:
    """ Get avatar image by type

     Returns the default project or issue type avatar image.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAvatarImageByTypeType):
        size (GetAvatarImageByTypeSize | Unset):
        format_ (GetAvatarImageByTypeFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | GetAvatarImageByTypeResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
size=size,
format_=format_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type_: GetAvatarImageByTypeType,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByTypeSize | Unset = UNSET,
    format_: GetAvatarImageByTypeFormat | Unset = UNSET,

) -> ErrorCollection | GetAvatarImageByTypeResponse200 | None:
    """ Get avatar image by type

     Returns the default project or issue type avatar image.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAvatarImageByTypeType):
        size (GetAvatarImageByTypeSize | Unset):
        format_ (GetAvatarImageByTypeFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | GetAvatarImageByTypeResponse200
     """


    return sync_detailed(
        type_=type_,
client=client,
size=size,
format_=format_,

    ).parsed

async def asyncio_detailed(
    type_: GetAvatarImageByTypeType,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByTypeSize | Unset = UNSET,
    format_: GetAvatarImageByTypeFormat | Unset = UNSET,

) -> Response[ErrorCollection | GetAvatarImageByTypeResponse200]:
    """ Get avatar image by type

     Returns the default project or issue type avatar image.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAvatarImageByTypeType):
        size (GetAvatarImageByTypeSize | Unset):
        format_ (GetAvatarImageByTypeFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | GetAvatarImageByTypeResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
size=size,
format_=format_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type_: GetAvatarImageByTypeType,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByTypeSize | Unset = UNSET,
    format_: GetAvatarImageByTypeFormat | Unset = UNSET,

) -> ErrorCollection | GetAvatarImageByTypeResponse200 | None:
    """ Get avatar image by type

     Returns the default project or issue type avatar image.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAvatarImageByTypeType):
        size (GetAvatarImageByTypeSize | Unset):
        format_ (GetAvatarImageByTypeFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | GetAvatarImageByTypeResponse200
     """


    return (await asyncio_detailed(
        type_=type_,
client=client,
size=size,
format_=format_,

    )).parsed
