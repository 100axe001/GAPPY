from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project import Project
from ...models.update_project_type_new_project_type_key import UpdateProjectTypeNewProjectTypeKey
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    new_project_type_key: UpdateProjectTypeNewProjectTypeKey,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/project/{project_id_or_key}/type/{new_project_type_key}".format(project_id_or_key=quote(str(project_id_or_key), safe=""),new_project_type_key=quote(str(new_project_type_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    new_project_type_key: UpdateProjectTypeNewProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Project]:
    """ Update project type

     Deprecated, this feature is no longer supported and no alternatives are available, see [Convert
    project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a
    [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for
    classic projects only, project type cannot be updated for next-gen projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        new_project_type_key (UpdateProjectTypeNewProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
new_project_type_key=new_project_type_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    new_project_type_key: UpdateProjectTypeNewProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Any | Project | None:
    """ Update project type

     Deprecated, this feature is no longer supported and no alternatives are available, see [Convert
    project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a
    [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for
    classic projects only, project type cannot be updated for next-gen projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        new_project_type_key (UpdateProjectTypeNewProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
new_project_type_key=new_project_type_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    new_project_type_key: UpdateProjectTypeNewProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Project]:
    """ Update project type

     Deprecated, this feature is no longer supported and no alternatives are available, see [Convert
    project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a
    [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for
    classic projects only, project type cannot be updated for next-gen projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        new_project_type_key (UpdateProjectTypeNewProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
new_project_type_key=new_project_type_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    new_project_type_key: UpdateProjectTypeNewProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Any | Project | None:
    """ Update project type

     Deprecated, this feature is no longer supported and no alternatives are available, see [Convert
    project to a different template or type](https://confluence.atlassian.com/x/yEKeOQ). Updates a
    [project type](https://confluence.atlassian.com/x/GwiiLQ). The project type can be updated for
    classic projects only, project type cannot be updated for next-gen projects.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):
        new_project_type_key (UpdateProjectTypeNewProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
new_project_type_key=new_project_type_key,
client=client,

    )).parsed
