from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset



def _get_kwargs(
    project_id_or_key: str,
    id: int,
    *,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["user"] = user

    params["group"] = group

    params["groupId"] = group_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/project/{project_id_or_key}/role/{id}".format(project_id_or_key=quote(str(project_id_or_key), safe=""),id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete actors from project role

     Deletes actors from a project role for the project.

    To remove default actors from the project role, use [Delete default actors from project role](#api-
    rest-api-3-role-id-actors-delete).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group (str | Unset):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
id=id,
user=user,
group=group,
group_id=group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    user: str | Unset = UNSET,
    group: str | Unset = UNSET,
    group_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete actors from project role

     Deletes actors from a project role for the project.

    To remove default actors from the project role, use [Delete default actors from project role](#api-
    rest-api-3-role-id-actors-delete).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        user (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        group (str | Unset):
        group_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
id=id,
user=user,
group=group,
group_id=group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

