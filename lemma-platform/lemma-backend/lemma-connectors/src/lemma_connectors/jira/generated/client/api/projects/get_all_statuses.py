from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_with_status import IssueTypeWithStatus
from typing import cast



def _get_kwargs(
    project_id_or_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/statuses".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[IssueTypeWithStatus] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IssueTypeWithStatus.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[IssueTypeWithStatus]]:
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

) -> Response[Any | list[IssueTypeWithStatus]]:
    """ Get all statuses for project

     Returns the valid statuses for a project. The statuses are grouped by issue type, as each project
    has a set of valid issue types and each issue type has a set of valid statuses.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeWithStatus]]
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

) -> Any | list[IssueTypeWithStatus] | None:
    """ Get all statuses for project

     Returns the valid statuses for a project. The statuses are grouped by issue type, as each project
    has a set of valid issue types and each issue type has a set of valid statuses.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeWithStatus]
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[IssueTypeWithStatus]]:
    """ Get all statuses for project

     Returns the valid statuses for a project. The statuses are grouped by issue type, as each project
    has a set of valid issue types and each issue type has a set of valid statuses.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeWithStatus]]
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

) -> Any | list[IssueTypeWithStatus] | None:
    """ Get all statuses for project

     Returns the valid statuses for a project. The statuses are grouped by issue type, as each project
    has a set of valid issue types and each issue type has a set of valid statuses.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeWithStatus]
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    )).parsed
