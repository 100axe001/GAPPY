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
    *,
    expand: str | Unset = UNSET,
    recent: int | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand

    params["recent"] = recent

    json_properties: list[str] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties


    params["properties"] = json_properties


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Project] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Project.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Project]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    recent: int | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Response[Any | list[Project]]:
    """ Get all projects

     Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-
    api-3-project-search-get) that supports search and pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse
    Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
    for the project.

    Args:
        expand (str | Unset):
        recent (int | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Project]]
     """


    kwargs = _get_kwargs(
        expand=expand,
recent=recent,
properties=properties,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    recent: int | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Any | list[Project] | None:
    """ Get all projects

     Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-
    api-3-project-search-get) that supports search and pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse
    Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
    for the project.

    Args:
        expand (str | Unset):
        recent (int | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Project]
     """


    return sync_detailed(
        client=client,
expand=expand,
recent=recent,
properties=properties,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    recent: int | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Response[Any | list[Project]]:
    """ Get all projects

     Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-
    api-3-project-search-get) that supports search and pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse
    Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
    for the project.

    Args:
        expand (str | Unset):
        recent (int | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Project]]
     """


    kwargs = _get_kwargs(
        expand=expand,
recent=recent,
properties=properties,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    recent: int | Unset = UNSET,
    properties: list[str] | Unset = UNSET,

) -> Any | list[Project] | None:
    """ Get all projects

     Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-
    api-3-project-search-get) that supports search and pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse
    Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg)
    for the project.

    Args:
        expand (str | Unset):
        recent (int | Unset):
        properties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Project]
     """


    return (await asyncio_detailed(
        client=client,
expand=expand,
recent=recent,
properties=properties,

    )).parsed
