from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.version import Version
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/versions".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Version] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Version.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Version]]:
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

) -> Response[Any | list[Version]]:
    """ Get project versions

     Returns all versions in a project. The response is not paginated. Use [Get project versions
    paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a
    project with pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Version]]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
expand=expand,

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

) -> Any | list[Version] | None:
    """ Get project versions

     Returns all versions in a project. The response is not paginated. Use [Get project versions
    paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a
    project with pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Version]
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | list[Version]]:
    """ Get project versions

     Returns all versions in a project. The response is not paginated. Use [Get project versions
    paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a
    project with pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Version]]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
expand=expand,

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

) -> Any | list[Version] | None:
    """ Get project versions

     Returns all versions in a project. The response is not paginated. Use [Get project versions
    paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a
    project with pagination.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Version]
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
expand=expand,

    )).parsed
