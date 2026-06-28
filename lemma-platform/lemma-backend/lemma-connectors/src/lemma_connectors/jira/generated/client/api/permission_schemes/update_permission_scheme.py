from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permission_scheme import PermissionScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    scheme_id: int,
    *,
    body: PermissionScheme,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/permissionscheme/{scheme_id}".format(scheme_id=quote(str(scheme_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PermissionScheme | None:
    if response.status_code == 200:
        response_200 = PermissionScheme.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PermissionScheme]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: PermissionScheme,
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionScheme]:
    """ Update permission scheme

     Updates a permission scheme. Below are some important things to note when using this resource:

     *  If a permissions list is present in the request, then it is set in the permission scheme,
    overwriting *all existing* grants.
     *  If you want to update only the name and description, then do not send a permissions list in the
    request.
     *  Sending an empty list will remove all permission grants from the permission scheme.

    If you want to add or delete a permission grant instead of updating the whole list, see [Create
    permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission
    scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

    See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-
    and-grants) for more details.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        scheme_id (int):
        expand (str | Unset):
        body (PermissionScheme): Details of a permission scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionScheme]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
body=body,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: PermissionScheme,
    expand: str | Unset = UNSET,

) -> Any | PermissionScheme | None:
    """ Update permission scheme

     Updates a permission scheme. Below are some important things to note when using this resource:

     *  If a permissions list is present in the request, then it is set in the permission scheme,
    overwriting *all existing* grants.
     *  If you want to update only the name and description, then do not send a permissions list in the
    request.
     *  Sending an empty list will remove all permission grants from the permission scheme.

    If you want to add or delete a permission grant instead of updating the whole list, see [Create
    permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission
    scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

    See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-
    and-grants) for more details.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        scheme_id (int):
        expand (str | Unset):
        body (PermissionScheme): Details of a permission scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionScheme
     """


    return sync_detailed(
        scheme_id=scheme_id,
client=client,
body=body,
expand=expand,

    ).parsed

async def asyncio_detailed(
    scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: PermissionScheme,
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionScheme]:
    """ Update permission scheme

     Updates a permission scheme. Below are some important things to note when using this resource:

     *  If a permissions list is present in the request, then it is set in the permission scheme,
    overwriting *all existing* grants.
     *  If you want to update only the name and description, then do not send a permissions list in the
    request.
     *  Sending an empty list will remove all permission grants from the permission scheme.

    If you want to add or delete a permission grant instead of updating the whole list, see [Create
    permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission
    scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

    See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-
    and-grants) for more details.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        scheme_id (int):
        expand (str | Unset):
        body (PermissionScheme): Details of a permission scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionScheme]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
body=body,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: PermissionScheme,
    expand: str | Unset = UNSET,

) -> Any | PermissionScheme | None:
    """ Update permission scheme

     Updates a permission scheme. Below are some important things to note when using this resource:

     *  If a permissions list is present in the request, then it is set in the permission scheme,
    overwriting *all existing* grants.
     *  If you want to update only the name and description, then do not send a permissions list in the
    request.
     *  Sending an empty list will remove all permission grants from the permission scheme.

    If you want to add or delete a permission grant instead of updating the whole list, see [Create
    permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission
    scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).

    See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-
    and-grants) for more details.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        scheme_id (int):
        expand (str | Unset):
        body (PermissionScheme): Details of a permission scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionScheme
     """


    return (await asyncio_detailed(
        scheme_id=scheme_id,
client=client,
body=body,
expand=expand,

    )).parsed
