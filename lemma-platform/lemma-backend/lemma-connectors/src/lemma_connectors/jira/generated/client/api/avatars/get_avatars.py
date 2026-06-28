from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.avatars import Avatars
from ...models.get_avatars_type import GetAvatarsType
from typing import cast



def _get_kwargs(
    type_: GetAvatarsType,
    entity_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/universal_avatar/type/{type_}/owner/{entity_id}".format(type_=quote(str(type_), safe=""),entity_id=quote(str(entity_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Avatars | None:
    if response.status_code == 200:
        response_200 = Avatars.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Avatars]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetAvatarsType,
    entity_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Avatars]:
    """ Get avatars

     Returns the system and custom avatars for a project or issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  for custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  for custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.
     *  for system avatars, none.

    Args:
        type_ (GetAvatarsType):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Avatars]
     """


    kwargs = _get_kwargs(
        type_=type_,
entity_id=entity_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type_: GetAvatarsType,
    entity_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Avatars | None:
    """ Get avatars

     Returns the system and custom avatars for a project or issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  for custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  for custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.
     *  for system avatars, none.

    Args:
        type_ (GetAvatarsType):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Avatars
     """


    return sync_detailed(
        type_=type_,
entity_id=entity_id,
client=client,

    ).parsed

async def asyncio_detailed(
    type_: GetAvatarsType,
    entity_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Avatars]:
    """ Get avatars

     Returns the system and custom avatars for a project or issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  for custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  for custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.
     *  for system avatars, none.

    Args:
        type_ (GetAvatarsType):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Avatars]
     """


    kwargs = _get_kwargs(
        type_=type_,
entity_id=entity_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type_: GetAvatarsType,
    entity_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Avatars | None:
    """ Get avatars

     Returns the system and custom avatars for a project or issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  for custom project avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.
     *  for custom issue type avatars, *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is
    used in.
     *  for system avatars, none.

    Args:
        type_ (GetAvatarsType):
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Avatars
     """


    return (await asyncio_detailed(
        type_=type_,
entity_id=entity_id,
client=client,

    )).parsed
