from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project import Project
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand

    json_properties: list[str] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties


    params["properties"] = json_properties


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Project]:
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
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Response[Any | Project]:
    """ Get project

     Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
expand=expand,
properties=properties,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Any | Project | None:
    """ Get project

     Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
expand=expand,
properties=properties,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Response[Any | Project]:
    """ Get project

     Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
expand=expand,
properties=properties,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Any | Project | None:
    """ Get project

     Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
expand=expand,
properties=properties,

    )).parsed
