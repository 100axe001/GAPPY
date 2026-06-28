from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_all_system_avatars_type import GetAllSystemAvatarsType
from ...models.system_avatars import SystemAvatars
from typing import cast



def _get_kwargs(
    type_: GetAllSystemAvatarsType,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/avatar/{type_}/system".format(type_=quote(str(type_), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | SystemAvatars | None:
    if response.status_code == 200:
        response_200 = SystemAvatars.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | SystemAvatars]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetAllSystemAvatarsType,
    *,
    client: AuthenticatedClient,

) -> Response[Any | SystemAvatars]:
    """ Get system avatars by type

     Returns a list of system avatar details by owner type, where the owner types are issue type,
    project, or user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAllSystemAvatarsType):  Example: project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SystemAvatars]
     """


    kwargs = _get_kwargs(
        type_=type_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type_: GetAllSystemAvatarsType,
    *,
    client: AuthenticatedClient,

) -> Any | SystemAvatars | None:
    """ Get system avatars by type

     Returns a list of system avatar details by owner type, where the owner types are issue type,
    project, or user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAllSystemAvatarsType):  Example: project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SystemAvatars
     """


    return sync_detailed(
        type_=type_,
client=client,

    ).parsed

async def asyncio_detailed(
    type_: GetAllSystemAvatarsType,
    *,
    client: AuthenticatedClient,

) -> Response[Any | SystemAvatars]:
    """ Get system avatars by type

     Returns a list of system avatar details by owner type, where the owner types are issue type,
    project, or user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAllSystemAvatarsType):  Example: project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SystemAvatars]
     """


    kwargs = _get_kwargs(
        type_=type_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type_: GetAllSystemAvatarsType,
    *,
    client: AuthenticatedClient,

) -> Any | SystemAvatars | None:
    """ Get system avatars by type

     Returns a list of system avatar details by owner type, where the owner types are issue type,
    project, or user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        type_ (GetAllSystemAvatarsType):  Example: project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SystemAvatars
     """


    return (await asyncio_detailed(
        type_=type_,
client=client,

    )).parsed
