from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.share_permission import SharePermission
from typing import cast



def _get_kwargs(
    id: int,
    permission_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/filter/{id}/permission/{permission_id}".format(id=quote(str(id), safe=""),permission_id=quote(str(permission_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | SharePermission | None:
    if response.status_code == 200:
        response_200 = SharePermission.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | SharePermission]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    permission_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | SharePermission]:
    """ Get share permission

     Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in
    users, or the public. Sharing with all logged-in users or the public is known as a global share
    permission.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, a share permission is only returned for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        permission_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SharePermission]
     """


    kwargs = _get_kwargs(
        id=id,
permission_id=permission_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    permission_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | SharePermission | None:
    """ Get share permission

     Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in
    users, or the public. Sharing with all logged-in users or the public is known as a global share
    permission.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, a share permission is only returned for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        permission_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SharePermission
     """


    return sync_detailed(
        id=id,
permission_id=permission_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    permission_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | SharePermission]:
    """ Get share permission

     Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in
    users, or the public. Sharing with all logged-in users or the public is known as a global share
    permission.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, a share permission is only returned for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        permission_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SharePermission]
     """


    kwargs = _get_kwargs(
        id=id,
permission_id=permission_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    permission_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | SharePermission | None:
    """ Get share permission

     Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in
    users, or the public. Sharing with all logged-in users or the public is known as a global share
    permission.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None, however, a share permission is only returned for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        permission_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SharePermission
     """


    return (await asyncio_detailed(
        id=id,
permission_id=permission_id,
client=client,

    )).parsed
