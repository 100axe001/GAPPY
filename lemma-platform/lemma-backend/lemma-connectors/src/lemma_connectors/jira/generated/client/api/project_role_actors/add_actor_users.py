from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.actors_map import ActorsMap
from ...models.project_role import ProjectRole
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    id: int,
    *,
    body: ActorsMap,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/project/{project_id_or_key}/role/{id}".format(project_id_or_key=quote(str(project_id_or_key), safe=""),id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ActorsMap,

) -> Response[Any | ProjectRole]:
    """ Add actors to project role

     Adds actors to a project role for the project.

    To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-
    projectIdOrKey-role-id-put).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        body (ActorsMap):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ActorsMap,

) -> Any | ProjectRole | None:
    """ Add actors to project role

     Adds actors to a project role for the project.

    To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-
    projectIdOrKey-role-id-put).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        body (ActorsMap):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ActorsMap,

) -> Response[Any | ProjectRole]:
    """ Add actors to project role

     Adds actors to a project role for the project.

    To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-
    projectIdOrKey-role-id-put).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        body (ActorsMap):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    id: int,
    *,
    client: AuthenticatedClient,
    body: ActorsMap,

) -> Any | ProjectRole | None:
    """ Add actors to project role

     Adds actors to a project role for the project.

    To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-
    projectIdOrKey-role-id-put).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        id (int):
        body (ActorsMap):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
id=id,
client=client,
body=body,

    )).parsed
