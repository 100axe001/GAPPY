from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permissions_keys_bean import PermissionsKeysBean
from ...models.permitted_projects import PermittedProjects
from typing import cast



def _get_kwargs(
    *,
    body: PermissionsKeysBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/permissions/project",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PermittedProjects | None:
    if response.status_code == 200:
        response_200 = PermittedProjects.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PermittedProjects]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PermissionsKeysBean,

) -> Response[Any | PermittedProjects]:
    """ Get permitted projects

     Returns all the projects where the user is granted a list of project permissions.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        body (PermissionsKeysBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermittedProjects]
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
    body: PermissionsKeysBean,

) -> Any | PermittedProjects | None:
    """ Get permitted projects

     Returns all the projects where the user is granted a list of project permissions.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        body (PermissionsKeysBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermittedProjects
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PermissionsKeysBean,

) -> Response[Any | PermittedProjects]:
    """ Get permitted projects

     Returns all the projects where the user is granted a list of project permissions.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        body (PermissionsKeysBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermittedProjects]
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
    body: PermissionsKeysBean,

) -> Any | PermittedProjects | None:
    """ Get permitted projects

     Returns all the projects where the user is granted a list of project permissions.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        body (PermissionsKeysBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermittedProjects
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
