from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_type_by_key_project_type_key import GetProjectTypeByKeyProjectTypeKey
from ...models.project_type import ProjectType
from typing import cast



def _get_kwargs(
    project_type_key: GetProjectTypeByKeyProjectTypeKey,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/type/{project_type_key}".format(project_type_key=quote(str(project_type_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectType | None:
    if response.status_code == 200:
        response_200 = ProjectType.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_type_key: GetProjectTypeByKeyProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ProjectType]:
    """ Get project type by key

     Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_type_key (GetProjectTypeByKeyProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectType]
     """


    kwargs = _get_kwargs(
        project_type_key=project_type_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_type_key: GetProjectTypeByKeyProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Any | ProjectType | None:
    """ Get project type by key

     Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_type_key (GetProjectTypeByKeyProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectType
     """


    return sync_detailed(
        project_type_key=project_type_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_type_key: GetProjectTypeByKeyProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ProjectType]:
    """ Get project type by key

     Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_type_key (GetProjectTypeByKeyProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectType]
     """


    kwargs = _get_kwargs(
        project_type_key=project_type_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_type_key: GetProjectTypeByKeyProjectTypeKey,
    *,
    client: AuthenticatedClient,

) -> Any | ProjectType | None:
    """ Get project type by key

     Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_type_key (GetProjectTypeByKeyProjectTypeKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectType
     """


    return (await asyncio_detailed(
        project_type_key=project_type_key,
client=client,

    )).parsed
