from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_permission_grants import BulkPermissionGrants
from ...models.bulk_permissions_request_bean import BulkPermissionsRequestBean
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    *,
    body: BulkPermissionsRequestBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/permissions/check",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkPermissionGrants | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = BulkPermissionGrants.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkPermissionGrants | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPermissionsRequestBean,

) -> Response[BulkPermissionGrants | ErrorCollection]:
    """ Get bulk permissions

     Returns:

     *  for a list of global permissions, the global permissions granted to a user.
     *  for a list of project permissions and lists of projects and issues, for each project permission
    a list of the projects and issues a user can access or manipulate.

    If no account ID is provided, the operation returns details for the logged in user.

    Note that:

     *  Invalid project and issue IDs are ignored.
     *  A maximum of 1000 projects and 1000 issues can be checked.
     *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and
    `projectPermissions.issues` are ignored.
     *  Empty strings in `projectPermissions.permissions` are ignored.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users,
    otherwise none. However, Connect apps can make a call from the app server to the product to obtain
    permission details for any user, without admin permission. This Connect app ability doesn't apply to
    calls made using AP.request() in a browser.

    Args:
        body (BulkPermissionsRequestBean): Details of global permissions to look up and project
            permissions with associated projects and issues to look up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkPermissionGrants | ErrorCollection]
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
    body: BulkPermissionsRequestBean,

) -> BulkPermissionGrants | ErrorCollection | None:
    """ Get bulk permissions

     Returns:

     *  for a list of global permissions, the global permissions granted to a user.
     *  for a list of project permissions and lists of projects and issues, for each project permission
    a list of the projects and issues a user can access or manipulate.

    If no account ID is provided, the operation returns details for the logged in user.

    Note that:

     *  Invalid project and issue IDs are ignored.
     *  A maximum of 1000 projects and 1000 issues can be checked.
     *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and
    `projectPermissions.issues` are ignored.
     *  Empty strings in `projectPermissions.permissions` are ignored.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users,
    otherwise none. However, Connect apps can make a call from the app server to the product to obtain
    permission details for any user, without admin permission. This Connect app ability doesn't apply to
    calls made using AP.request() in a browser.

    Args:
        body (BulkPermissionsRequestBean): Details of global permissions to look up and project
            permissions with associated projects and issues to look up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkPermissionGrants | ErrorCollection
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPermissionsRequestBean,

) -> Response[BulkPermissionGrants | ErrorCollection]:
    """ Get bulk permissions

     Returns:

     *  for a list of global permissions, the global permissions granted to a user.
     *  for a list of project permissions and lists of projects and issues, for each project permission
    a list of the projects and issues a user can access or manipulate.

    If no account ID is provided, the operation returns details for the logged in user.

    Note that:

     *  Invalid project and issue IDs are ignored.
     *  A maximum of 1000 projects and 1000 issues can be checked.
     *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and
    `projectPermissions.issues` are ignored.
     *  Empty strings in `projectPermissions.permissions` are ignored.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users,
    otherwise none. However, Connect apps can make a call from the app server to the product to obtain
    permission details for any user, without admin permission. This Connect app ability doesn't apply to
    calls made using AP.request() in a browser.

    Args:
        body (BulkPermissionsRequestBean): Details of global permissions to look up and project
            permissions with associated projects and issues to look up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkPermissionGrants | ErrorCollection]
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
    body: BulkPermissionsRequestBean,

) -> BulkPermissionGrants | ErrorCollection | None:
    """ Get bulk permissions

     Returns:

     *  for a list of global permissions, the global permissions granted to a user.
     *  for a list of project permissions and lists of projects and issues, for each project permission
    a list of the projects and issues a user can access or manipulate.

    If no account ID is provided, the operation returns details for the logged in user.

    Note that:

     *  Invalid project and issue IDs are ignored.
     *  A maximum of 1000 projects and 1000 issues can be checked.
     *  Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and
    `projectPermissions.issues` are ignored.
     *  Empty strings in `projectPermissions.permissions` are ignored.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users,
    otherwise none. However, Connect apps can make a call from the app server to the product to obtain
    permission details for any user, without admin permission. This Connect app ability doesn't apply to
    calls made using AP.request() in a browser.

    Args:
        body (BulkPermissionsRequestBean): Details of global permissions to look up and project
            permissions with associated projects and issues to look up.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkPermissionGrants | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
