from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permission_grants import PermissionGrants
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    scheme_id: int,
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/permissionscheme/{scheme_id}/permission".format(scheme_id=quote(str(scheme_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PermissionGrants | None:
    if response.status_code == 200:
        response_200 = PermissionGrants.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PermissionGrants]:
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
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionGrants]:
    """ Get permission scheme grants

     Returns all permission grants for a permission scheme.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        scheme_id (int):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionGrants]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
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
    expand: str | Unset = UNSET,

) -> Any | PermissionGrants | None:
    """ Get permission scheme grants

     Returns all permission grants for a permission scheme.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        scheme_id (int):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionGrants
     """


    return sync_detailed(
        scheme_id=scheme_id,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    scheme_id: int,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionGrants]:
    """ Get permission scheme grants

     Returns all permission grants for a permission scheme.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        scheme_id (int):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionGrants]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
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
    expand: str | Unset = UNSET,

) -> Any | PermissionGrants | None:
    """ Get permission scheme grants

     Returns all permission grants for a permission scheme.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        scheme_id (int):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionGrants
     """


    return (await asyncio_detailed(
        scheme_id=scheme_id,
client=client,
expand=expand,

    )).parsed
