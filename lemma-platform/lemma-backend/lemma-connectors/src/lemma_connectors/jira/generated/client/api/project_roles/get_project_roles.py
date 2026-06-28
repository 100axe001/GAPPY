from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_roles_response_200 import GetProjectRolesResponse200
from typing import cast



def _get_kwargs(
    project_id_or_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/role".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GetProjectRolesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetProjectRolesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | GetProjectRolesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | GetProjectRolesResponse200]:
    """ Get project roles for project

     Returns a list of [project roles](https://confluence.atlassian.com/x/3odKLg) for the project
    returning the name and self URL for each role.

    Note that all project roles are shared with all projects in Jira Cloud. See [Get all project
    roles](#api-rest-api-3-role-get) for more information.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer
    Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectRolesResponse200]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | GetProjectRolesResponse200 | None:
    """ Get project roles for project

     Returns a list of [project roles](https://confluence.atlassian.com/x/3odKLg) for the project
    returning the name and self URL for each role.

    Note that all project roles are shared with all projects in Jira Cloud. See [Get all project
    roles](#api-rest-api-3-role-get) for more information.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer
    Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectRolesResponse200
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | GetProjectRolesResponse200]:
    """ Get project roles for project

     Returns a list of [project roles](https://confluence.atlassian.com/x/3odKLg) for the project
    returning the name and self URL for each role.

    Note that all project roles are shared with all projects in Jira Cloud. See [Get all project
    roles](#api-rest-api-3-role-get) for more information.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer
    Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectRolesResponse200]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | GetProjectRolesResponse200 | None:
    """ Get project roles for project

     Returns a list of [project roles](https://confluence.atlassian.com/x/3odKLg) for the project
    returning the name and self URL for each role.

    Note that all project roles are shared with all projects in Jira Cloud. See [Get all project
    roles](#api-rest-api-3-role-get) for more information.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer
    Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectRolesResponse200
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    )).parsed
