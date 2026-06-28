from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_permissions_resources_list_apps_permissions_resources_list_error_schema import AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema
from ...models.apps_permissions_resources_list_apps_permissions_resources_list_success_schema import AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.permissions.resources.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema:
    if response.status_code == 200:
        response_200 = AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema.from_dict(response.json())



        return response_200

    response_default = AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema]:
    """  Returns list of resource grants this app has on a team.

    Args:
        token (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
cursor=cursor,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema | None:
    """  Returns list of resource grants this app has on a team.

    Args:
        token (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema]:
    """  Returns list of resource grants this app has on a team.

    Args:
        token (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
cursor=cursor,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema | None:
    """  Returns list of resource grants this app has on a team.

    Args:
        token (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsPermissionsResourcesListAppsPermissionsResourcesListErrorSchema | AppsPermissionsResourcesListAppsPermissionsResourcesListSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
cursor=cursor,
limit=limit,

    )).parsed
