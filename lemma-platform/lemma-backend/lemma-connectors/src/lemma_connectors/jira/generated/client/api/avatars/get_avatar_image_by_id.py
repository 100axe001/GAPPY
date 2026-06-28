from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_avatar_image_by_id_format import GetAvatarImageByIDFormat
from ...models.get_avatar_image_by_id_response_200 import GetAvatarImageByIDResponse200
from ...models.get_avatar_image_by_id_size import GetAvatarImageByIDSize
from ...models.get_avatar_image_by_id_type import GetAvatarImageByIDType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    type_: GetAvatarImageByIDType,
    id: int,
    *,
    size: GetAvatarImageByIDSize | Unset = UNSET,
    format_: GetAvatarImageByIDFormat | Unset = UNSET,

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
        "url": "/rest/api/3/universal_avatar/view/type/{type_}/avatar/{id}".format(type_=quote(str(type_), safe=""),id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | GetAvatarImageByIDResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAvatarImageByIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | GetAvatarImageByIDResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetAvatarImageByIDType,
    id: int,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByIDSize | Unset = UNSET,
    format_: GetAvatarImageByIDFormat | Unset = UNSET,

) -> Response[ErrorCollection | GetAvatarImageByIDResponse200]:
    """ Get avatar image by ID

     Returns a project or issue type avatar image by ID.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  For system avatars, none.
     *  For custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  For custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.

    Args:
        type_ (GetAvatarImageByIDType):
        id (int):
        size (GetAvatarImageByIDSize | Unset):
        format_ (GetAvatarImageByIDFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | GetAvatarImageByIDResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
id=id,
size=size,
format_=format_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type_: GetAvatarImageByIDType,
    id: int,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByIDSize | Unset = UNSET,
    format_: GetAvatarImageByIDFormat | Unset = UNSET,

) -> ErrorCollection | GetAvatarImageByIDResponse200 | None:
    """ Get avatar image by ID

     Returns a project or issue type avatar image by ID.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  For system avatars, none.
     *  For custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  For custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.

    Args:
        type_ (GetAvatarImageByIDType):
        id (int):
        size (GetAvatarImageByIDSize | Unset):
        format_ (GetAvatarImageByIDFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | GetAvatarImageByIDResponse200
     """


    return sync_detailed(
        type_=type_,
id=id,
client=client,
size=size,
format_=format_,

    ).parsed

async def asyncio_detailed(
    type_: GetAvatarImageByIDType,
    id: int,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByIDSize | Unset = UNSET,
    format_: GetAvatarImageByIDFormat | Unset = UNSET,

) -> Response[ErrorCollection | GetAvatarImageByIDResponse200]:
    """ Get avatar image by ID

     Returns a project or issue type avatar image by ID.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  For system avatars, none.
     *  For custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  For custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.

    Args:
        type_ (GetAvatarImageByIDType):
        id (int):
        size (GetAvatarImageByIDSize | Unset):
        format_ (GetAvatarImageByIDFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | GetAvatarImageByIDResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
id=id,
size=size,
format_=format_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type_: GetAvatarImageByIDType,
    id: int,
    *,
    client: AuthenticatedClient,
    size: GetAvatarImageByIDSize | Unset = UNSET,
    format_: GetAvatarImageByIDFormat | Unset = UNSET,

) -> ErrorCollection | GetAvatarImageByIDResponse200 | None:
    """ Get avatar image by ID

     Returns a project or issue type avatar image by ID.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  For system avatars, none.
     *  For custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  For custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.

    Args:
        type_ (GetAvatarImageByIDType):
        id (int):
        size (GetAvatarImageByIDSize | Unset):
        format_ (GetAvatarImageByIDFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | GetAvatarImageByIDResponse200
     """


    return (await asyncio_detailed(
        type_=type_,
id=id,
client=client,
size=size,
format_=format_,

    )).parsed
