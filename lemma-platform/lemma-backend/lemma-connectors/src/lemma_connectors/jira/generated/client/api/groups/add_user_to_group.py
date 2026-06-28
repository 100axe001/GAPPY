from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.group import Group
from ...models.update_user_to_group_bean import UpdateUserToGroupBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UpdateUserToGroupBean,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["groupname"] = groupname

    params["groupId"] = group_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/group/user",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Group | None:
    if response.status_code == 201:
        response_201 = Group.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Group]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserToGroupBean,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Response[Any | Group]:
    """ Add user to group

     Adds a user to a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        body (UpdateUserToGroupBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Group]
     """


    kwargs = _get_kwargs(
        body=body,
groupname=groupname,
group_id=group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateUserToGroupBean,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Any | Group | None:
    """ Add user to group

     Adds a user to a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        body (UpdateUserToGroupBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Group
     """


    return sync_detailed(
        client=client,
body=body,
groupname=groupname,
group_id=group_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateUserToGroupBean,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Response[Any | Group]:
    """ Add user to group

     Adds a user to a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        body (UpdateUserToGroupBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Group]
     """


    kwargs = _get_kwargs(
        body=body,
groupname=groupname,
group_id=group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateUserToGroupBean,
    groupname: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Any | Group | None:
    """ Add user to group

     Adds a user to a group.

    **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin*
    [group](https://confluence.atlassian.com/x/24xjL)).

    Args:
        groupname (str | Unset):
        group_id (str | Unset):
        body (UpdateUserToGroupBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Group
     """


    return (await asyncio_detailed(
        client=client,
body=body,
groupname=groupname,
group_id=group_id,

    )).parsed
