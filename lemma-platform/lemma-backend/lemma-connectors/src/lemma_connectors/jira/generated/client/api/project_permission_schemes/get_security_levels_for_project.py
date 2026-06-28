from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_issue_security_levels import ProjectIssueSecurityLevels
from typing import cast



def _get_kwargs(
    project_key_or_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_key_or_id}/securitylevel".format(project_key_or_id=quote(str(project_key_or_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectIssueSecurityLevels | None:
    if response.status_code == 200:
        response_200 = ProjectIssueSecurityLevels.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectIssueSecurityLevels]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ProjectIssueSecurityLevels]:
    """ Get project issue security levels

     Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that
    the user has access to.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security
    levels are only returned for authenticated user with *Set Issue Security* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

    Args:
        project_key_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectIssueSecurityLevels]
     """


    kwargs = _get_kwargs(
        project_key_or_id=project_key_or_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | ProjectIssueSecurityLevels | None:
    """ Get project issue security levels

     Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that
    the user has access to.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security
    levels are only returned for authenticated user with *Set Issue Security* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

    Args:
        project_key_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectIssueSecurityLevels
     """


    return sync_detailed(
        project_key_or_id=project_key_or_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ProjectIssueSecurityLevels]:
    """ Get project issue security levels

     Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that
    the user has access to.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security
    levels are only returned for authenticated user with *Set Issue Security* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

    Args:
        project_key_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectIssueSecurityLevels]
     """


    kwargs = _get_kwargs(
        project_key_or_id=project_key_or_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | ProjectIssueSecurityLevels | None:
    """ Get project issue security levels

     Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that
    the user has access to.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security
    levels are only returned for authenticated user with *Set Issue Security* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

    Args:
        project_key_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectIssueSecurityLevels
     """


    return (await asyncio_detailed(
        project_key_or_id=project_key_or_id,
client=client,

    )).parsed
