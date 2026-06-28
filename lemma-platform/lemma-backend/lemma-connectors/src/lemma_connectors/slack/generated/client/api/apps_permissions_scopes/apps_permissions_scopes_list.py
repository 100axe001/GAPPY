from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_permissions_scopes_list_api_permissions_scopes_list_success_schema import AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema
from ...models.apps_permissions_scopes_list_apps_permissions_scopes_list_error_schema import AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.permissions.scopes.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema:
    if response.status_code == 200:
        response_200 = AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema.from_dict(response.json())



        return response_200

    response_default = AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema]:
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

) -> Response[AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema]:
    """  Returns list of scopes this app has on a team.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,

) -> AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema | None:
    """  Returns list of scopes this app has on a team.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema
     """


    return sync_detailed(
        client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,

) -> Response[AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema]:
    """  Returns list of scopes this app has on a team.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,

) -> AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema | None:
    """  Returns list of scopes this app has on a team.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsScopesListApiPermissionsScopesListSuccessSchema | AppsPermissionsScopesListAppsPermissionsScopesListErrorSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,

    )).parsed
