from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.container_of_workflow_scheme_associations import ContainerOfWorkflowSchemeAssociations
from typing import cast



def _get_kwargs(
    *,
    project_id: list[int],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_project_id = project_id


    params["projectId"] = json_project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/workflowscheme/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ContainerOfWorkflowSchemeAssociations | None:
    if response.status_code == 200:
        response_200 = ContainerOfWorkflowSchemeAssociations.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ContainerOfWorkflowSchemeAssociations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: list[int],

) -> Response[Any | ContainerOfWorkflowSchemeAssociations]:
    """ Get workflow scheme project associations

     Returns a list of the workflow schemes associated with a list of projects. Each returned workflow
    scheme includes a list of the requested projects associated with it. Any team-managed or non-
    existent projects in the request are ignored and no errors are returned.

    If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because
    the way the `Default Workflow Scheme` is stored means it has no ID.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContainerOfWorkflowSchemeAssociations]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    project_id: list[int],

) -> Any | ContainerOfWorkflowSchemeAssociations | None:
    """ Get workflow scheme project associations

     Returns a list of the workflow schemes associated with a list of projects. Each returned workflow
    scheme includes a list of the requested projects associated with it. Any team-managed or non-
    existent projects in the request are ignored and no errors are returned.

    If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because
    the way the `Default Workflow Scheme` is stored means it has no ID.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContainerOfWorkflowSchemeAssociations
     """


    return sync_detailed(
        client=client,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: list[int],

) -> Response[Any | ContainerOfWorkflowSchemeAssociations]:
    """ Get workflow scheme project associations

     Returns a list of the workflow schemes associated with a list of projects. Each returned workflow
    scheme includes a list of the requested projects associated with it. Any team-managed or non-
    existent projects in the request are ignored and no errors are returned.

    If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because
    the way the `Default Workflow Scheme` is stored means it has no ID.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContainerOfWorkflowSchemeAssociations]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: list[int],

) -> Any | ContainerOfWorkflowSchemeAssociations | None:
    """ Get workflow scheme project associations

     Returns a list of the workflow schemes associated with a list of projects. Each returned workflow
    scheme includes a list of the requested projects associated with it. Any team-managed or non-
    existent projects in the request are ignored and no errors are returned.

    If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because
    the way the `Default Workflow Scheme` is stored means it has no ID.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContainerOfWorkflowSchemeAssociations
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,

    )).parsed
