from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project import Project
from typing import cast



def _get_kwargs(
    project_id_or_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/project/{project_id_or_key}/restore".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
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
    *,
    client: AuthenticatedClient,

) -> Response[Any | Project]:
    """ Restore deleted or archived project

     Restores a project that has been archived or placed in the Jira recycle bin.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
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

) -> Any | Project | None:
    """ Restore deleted or archived project

     Restores a project that has been archived or placed in the Jira recycle bin.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Project]:
    """ Restore deleted or archived project

     Restores a project that has been archived or placed in the Jira recycle bin.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Project]
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

) -> Any | Project | None:
    """ Restore deleted or archived project

     Restores a project that has been archived or placed in the Jira recycle bin.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Project
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    )).parsed
