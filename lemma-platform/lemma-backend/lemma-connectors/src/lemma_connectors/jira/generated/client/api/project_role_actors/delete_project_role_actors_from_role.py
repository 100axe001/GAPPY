from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_role import ProjectRole
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    user: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["user"] = user

    params["groupId"] = group_id

    params["group"] = group


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/role/{id}/actors".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectRole | None:
    if response.status_code == 200:
        response_200 = ProjectRole.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectRole]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Response[Any | ProjectRole]:
    """ Delete default actors from project role

     Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a
    group or user, but you cannot delete a group and a user in the same request.

    Changing a project role's default actors does not affect project role members for projects already
    created.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group_id (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
     """


    kwargs = _get_kwargs(
        id=id,
user=user,
group_id=group_id,
group=group,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Any | ProjectRole | None:
    """ Delete default actors from project role

     Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a
    group or user, but you cannot delete a group and a user in the same request.

    Changing a project role's default actors does not affect project role members for projects already
    created.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group_id (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return sync_detailed(
        id=id,
client=client,
user=user,
group_id=group_id,
group=group,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Response[Any | ProjectRole]:
    """ Delete default actors from project role

     Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a
    group or user, but you cannot delete a group and a user in the same request.

    Changing a project role's default actors does not affect project role members for projects already
    created.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group_id (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
     """


    kwargs = _get_kwargs(
        id=id,
user=user,
group_id=group_id,
group=group,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Any | ProjectRole | None:
    """ Delete default actors from project role

     Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a
    group or user, but you cannot delete a group and a user in the same request.

    Changing a project role's default actors does not affect project role members for projects already
    created.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group_id (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return (await asyncio_detailed(
        id=id,
client=client,
user=user,
group_id=group_id,
group=group,

    )).parsed
