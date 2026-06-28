from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_permissions_users_request_default_error_template import AppsPermissionsUsersRequestDefaultErrorTemplate
from ...models.apps_permissions_users_request_default_success_template import AppsPermissionsUsersRequestDefaultSuccessTemplate
from typing import cast



def _get_kwargs(
    *,
    token: str,
    scopes: str,
    trigger_id: str,
    user: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["scopes"] = scopes

    params["trigger_id"] = trigger_id

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.permissions.users.request",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = AppsPermissionsUsersRequestDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = AppsPermissionsUsersRequestDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    scopes: str,
    trigger_id: str,
    user: str,

) -> Response[AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate]:
    """  Enables an app to trigger a permissions modal to grant an app access to a user access scope.

    Args:
        token (str):
        scopes (str):
        trigger_id (str):
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
scopes=scopes,
trigger_id=trigger_id,
user=user,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    scopes: str,
    trigger_id: str,
    user: str,

) -> AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate | None:
    """  Enables an app to trigger a permissions modal to grant an app access to a user access scope.

    Args:
        token (str):
        scopes (str):
        trigger_id (str):
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
scopes=scopes,
trigger_id=trigger_id,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    scopes: str,
    trigger_id: str,
    user: str,

) -> Response[AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate]:
    """  Enables an app to trigger a permissions modal to grant an app access to a user access scope.

    Args:
        token (str):
        scopes (str):
        trigger_id (str):
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
scopes=scopes,
trigger_id=trigger_id,
user=user,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    scopes: str,
    trigger_id: str,
    user: str,

) -> AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate | None:
    """  Enables an app to trigger a permissions modal to grant an app access to a user access scope.

    Args:
        token (str):
        scopes (str):
        trigger_id (str):
        user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsUsersRequestDefaultErrorTemplate | AppsPermissionsUsersRequestDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
scopes=scopes,
trigger_id=trigger_id,
user=user,

    )).parsed
