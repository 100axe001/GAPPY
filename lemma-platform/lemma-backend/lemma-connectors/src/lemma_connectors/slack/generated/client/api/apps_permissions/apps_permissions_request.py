from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_permissions_request_apps_permissions_request_error_schema import AppsPermissionsRequestAppsPermissionsRequestErrorSchema
from ...models.apps_permissions_request_apps_permissions_request_schema import AppsPermissionsRequestAppsPermissionsRequestSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,
    scopes: str,
    trigger_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["scopes"] = scopes

    params["trigger_id"] = trigger_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.permissions.request",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema:
    if response.status_code == 200:
        response_200 = AppsPermissionsRequestAppsPermissionsRequestSchema.from_dict(response.json())



        return response_200

    response_default = AppsPermissionsRequestAppsPermissionsRequestErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema]:
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

) -> Response[AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema]:
    """  Allows an app to request additional scopes

    Args:
        token (str):
        scopes (str):
        trigger_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema]
     """


    kwargs = _get_kwargs(
        token=token,
scopes=scopes,
trigger_id=trigger_id,

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

) -> AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema | None:
    """  Allows an app to request additional scopes

    Args:
        token (str):
        scopes (str):
        trigger_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema
     """


    return sync_detailed(
        client=client,
token=token,
scopes=scopes,
trigger_id=trigger_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    scopes: str,
    trigger_id: str,

) -> Response[AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema]:
    """  Allows an app to request additional scopes

    Args:
        token (str):
        scopes (str):
        trigger_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema]
     """


    kwargs = _get_kwargs(
        token=token,
scopes=scopes,
trigger_id=trigger_id,

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

) -> AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema | None:
    """  Allows an app to request additional scopes

    Args:
        token (str):
        scopes (str):
        trigger_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsRequestAppsPermissionsRequestErrorSchema | AppsPermissionsRequestAppsPermissionsRequestSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
scopes=scopes,
trigger_id=trigger_id,

    )).parsed
