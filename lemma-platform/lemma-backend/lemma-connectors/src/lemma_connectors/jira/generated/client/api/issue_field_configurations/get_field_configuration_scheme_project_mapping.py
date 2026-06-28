from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_field_configuration_scheme_projects import PageBeanFieldConfigurationSchemeProjects
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_project_id = project_id


    params["projectId"] = json_project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/fieldconfigurationscheme/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanFieldConfigurationSchemeProjects | None:
    if response.status_code == 200:
        response_200 = PageBeanFieldConfigurationSchemeProjects.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanFieldConfigurationSchemeProjects]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> Response[Any | PageBeanFieldConfigurationSchemeProjects]:
    """ Get field configuration schemes for projects

     Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list
    of the projects that use it.

    The list is sorted by field configuration scheme ID. The first item contains the list of project IDs
    assigned to the default field configuration scheme.

    Only field configuration schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationSchemeProjects]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> Any | PageBeanFieldConfigurationSchemeProjects | None:
    """ Get field configuration schemes for projects

     Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list
    of the projects that use it.

    The list is sorted by field configuration scheme ID. The first item contains the list of project IDs
    assigned to the default field configuration scheme.

    Only field configuration schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationSchemeProjects
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> Response[Any | PageBeanFieldConfigurationSchemeProjects]:
    """ Get field configuration schemes for projects

     Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list
    of the projects that use it.

    The list is sorted by field configuration scheme ID. The first item contains the list of project IDs
    assigned to the default field configuration scheme.

    Only field configuration schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationSchemeProjects]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    project_id: list[int],

) -> Any | PageBeanFieldConfigurationSchemeProjects | None:
    """ Get field configuration schemes for projects

     Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list
    of the projects that use it.

    The list is sorted by field configuration scheme ID. The first item contains the list of project IDs
    assigned to the default field configuration scheme.

    Only field configuration schemes used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        project_id (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationSchemeProjects
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    )).parsed
