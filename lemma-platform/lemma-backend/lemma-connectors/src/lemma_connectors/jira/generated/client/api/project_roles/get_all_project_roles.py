from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_role import ProjectRole
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/role",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[ProjectRole] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProjectRole.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[ProjectRole]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[ProjectRole]]:
    """ Get all project roles

     Gets a list of all project roles, complete with project role details and default actors.

    ### About project roles ###

    [Project roles](https://confluence.atlassian.com/x/3odKLg) are a flexible way to to associate users
    and groups with projects. In Jira Cloud, the list of project roles is shared globally with all
    projects, but each project can have a different set of actors associated with it (unlike groups,
    which have the same membership throughout all Jira applications).

    Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email
    notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-
    api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and
    workflow conditions.

    #### Members and actors ####

    In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user
    associated with a project role.

    Actors may be set as [default
    members](https://confluence.atlassian.com/x/3odKLg#Managingprojectroles-
    Specifying'defaultmembers'foraprojectrole) of the project role or set at the project level:

     *  Default actors: Users and groups that are assigned to the project role for all newly created
    projects. The default actors can be removed at the project level later if desired.
     *  Actors: Users and groups that are associated with a project role for a project, which may differ
    from the default actors. This enables you to assign a user to different roles in different projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ProjectRole]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Any | list[ProjectRole] | None:
    """ Get all project roles

     Gets a list of all project roles, complete with project role details and default actors.

    ### About project roles ###

    [Project roles](https://confluence.atlassian.com/x/3odKLg) are a flexible way to to associate users
    and groups with projects. In Jira Cloud, the list of project roles is shared globally with all
    projects, but each project can have a different set of actors associated with it (unlike groups,
    which have the same membership throughout all Jira applications).

    Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email
    notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-
    api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and
    workflow conditions.

    #### Members and actors ####

    In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user
    associated with a project role.

    Actors may be set as [default
    members](https://confluence.atlassian.com/x/3odKLg#Managingprojectroles-
    Specifying'defaultmembers'foraprojectrole) of the project role or set at the project level:

     *  Default actors: Users and groups that are assigned to the project role for all newly created
    projects. The default actors can be removed at the project level later if desired.
     *  Actors: Users and groups that are associated with a project role for a project, which may differ
    from the default actors. This enables you to assign a user to different roles in different projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ProjectRole]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[ProjectRole]]:
    """ Get all project roles

     Gets a list of all project roles, complete with project role details and default actors.

    ### About project roles ###

    [Project roles](https://confluence.atlassian.com/x/3odKLg) are a flexible way to to associate users
    and groups with projects. In Jira Cloud, the list of project roles is shared globally with all
    projects, but each project can have a different set of actors associated with it (unlike groups,
    which have the same membership throughout all Jira applications).

    Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email
    notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-
    api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and
    workflow conditions.

    #### Members and actors ####

    In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user
    associated with a project role.

    Actors may be set as [default
    members](https://confluence.atlassian.com/x/3odKLg#Managingprojectroles-
    Specifying'defaultmembers'foraprojectrole) of the project role or set at the project level:

     *  Default actors: Users and groups that are assigned to the project role for all newly created
    projects. The default actors can be removed at the project level later if desired.
     *  Actors: Users and groups that are associated with a project role for a project, which may differ
    from the default actors. This enables you to assign a user to different roles in different projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ProjectRole]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Any | list[ProjectRole] | None:
    """ Get all project roles

     Gets a list of all project roles, complete with project role details and default actors.

    ### About project roles ###

    [Project roles](https://confluence.atlassian.com/x/3odKLg) are a flexible way to to associate users
    and groups with projects. In Jira Cloud, the list of project roles is shared globally with all
    projects, but each project can have a different set of actors associated with it (unlike groups,
    which have the same membership throughout all Jira applications).

    Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email
    notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-
    api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and
    workflow conditions.

    #### Members and actors ####

    In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user
    associated with a project role.

    Actors may be set as [default
    members](https://confluence.atlassian.com/x/3odKLg#Managingprojectroles-
    Specifying'defaultmembers'foraprojectrole) of the project role or set at the project level:

     *  Default actors: Users and groups that are assigned to the project role for all newly created
    projects. The default actors can be removed at the project level later if desired.
     *  Actors: Users and groups that are associated with a project role for a project, which may differ
    from the default actors. This enables you to assign a user to different roles in different projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ProjectRole]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
