from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_uninstall_apps_uninstall_error_schema import AppsUninstallAppsUninstallErrorSchema
from ...models.apps_uninstall_apps_uninstall_schema import AppsUninstallAppsUninstallSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["client_id"] = client_id

    params["client_secret"] = client_secret


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.uninstall",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema:
    if response.status_code == 200:
        response_200 = AppsUninstallAppsUninstallSchema.from_dict(response.json())



        return response_200

    response_default = AppsUninstallAppsUninstallErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,

) -> Response[AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema]:
    """  Uninstalls your app from a workspace.

    Args:
        token (str | Unset):
        client_id (str | Unset):
        client_secret (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema]
     """


    kwargs = _get_kwargs(
        token=token,
client_id=client_id,
client_secret=client_secret,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,

) -> AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema | None:
    """  Uninstalls your app from a workspace.

    Args:
        token (str | Unset):
        client_id (str | Unset):
        client_secret (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema
     """


    return sync_detailed(
        client=client,
token=token,
client_id=client_id,
client_secret=client_secret,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,

) -> Response[AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema]:
    """  Uninstalls your app from a workspace.

    Args:
        token (str | Unset):
        client_id (str | Unset):
        client_secret (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema]
     """


    kwargs = _get_kwargs(
        token=token,
client_id=client_id,
client_secret=client_secret,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,

) -> AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema | None:
    """  Uninstalls your app from a workspace.

    Args:
        token (str | Unset):
        client_id (str | Unset):
        client_secret (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsUninstallAppsUninstallErrorSchema | AppsUninstallAppsUninstallSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
client_id=client_id,
client_secret=client_secret,

    )).parsed
