from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_details import IssueTypeDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_id: int,
    level: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["level"] = level


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetype/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[IssueTypeDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IssueTypeDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[IssueTypeDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: int,
    level: int | Unset = UNSET,

) -> Response[Any | list[IssueTypeDetails]]:
    """ Get issue types for project

     Returns issue types for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira*
    [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (int):
        level (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeDetails]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
level=level,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    project_id: int,
    level: int | Unset = UNSET,

) -> Any | list[IssueTypeDetails] | None:
    """ Get issue types for project

     Returns issue types for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira*
    [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (int):
        level (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeDetails]
     """


    return sync_detailed(
        client=client,
project_id=project_id,
level=level,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: int,
    level: int | Unset = UNSET,

) -> Response[Any | list[IssueTypeDetails]]:
    """ Get issue types for project

     Returns issue types for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira*
    [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (int):
        level (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeDetails]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
level=level,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: int,
    level: int | Unset = UNSET,

) -> Any | list[IssueTypeDetails] | None:
    """ Get issue types for project

     Returns issue types for a project.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira*
    [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id (int):
        level (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeDetails]
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
level=level,

    )).parsed
