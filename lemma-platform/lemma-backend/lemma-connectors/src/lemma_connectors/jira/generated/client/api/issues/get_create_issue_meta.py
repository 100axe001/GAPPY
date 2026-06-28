from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_create_metadata import IssueCreateMetadata
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_ids: list[str] | Unset = UNSET,
    project_keys: list[str] | Unset = UNSET,
    issuetype_ids: list[str] | Unset = UNSET,
    issuetype_names: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_project_ids: list[str] | Unset = UNSET
    if not isinstance(project_ids, Unset):
        json_project_ids = project_ids


    params["projectIds"] = json_project_ids

    json_project_keys: list[str] | Unset = UNSET
    if not isinstance(project_keys, Unset):
        json_project_keys = project_keys


    params["projectKeys"] = json_project_keys

    json_issuetype_ids: list[str] | Unset = UNSET
    if not isinstance(issuetype_ids, Unset):
        json_issuetype_ids = issuetype_ids


    params["issuetypeIds"] = json_issuetype_ids

    json_issuetype_names: list[str] | Unset = UNSET
    if not isinstance(issuetype_names, Unset):
        json_issuetype_names = issuetype_names


    params["issuetypeNames"] = json_issuetype_names

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/createmeta",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueCreateMetadata | None:
    if response.status_code == 200:
        response_200 = IssueCreateMetadata.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueCreateMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: list[str] | Unset = UNSET,
    project_keys: list[str] | Unset = UNSET,
    issuetype_ids: list[str] | Unset = UNSET,
    issuetype_names: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | IssueCreateMetadata]:
    """ Get create issue metadata

     Returns details of projects, issue types within projects, and, when requested, the create screen
    fields for each issue type for the user. Use the information to populate the requests in [ Create
    issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

    The request can be restricted to specific projects or issue types using the query parameters. The
    response will contain information for the valid projects, issue types, or project and issue type
    combinations requested. Note that invalid project, issue type, or project and issue type
    combinations do not generate errors.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Create issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

    Args:
        project_ids (list[str] | Unset):
        project_keys (list[str] | Unset):
        issuetype_ids (list[str] | Unset):
        issuetype_names (list[str] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueCreateMetadata]
     """


    kwargs = _get_kwargs(
        project_ids=project_ids,
project_keys=project_keys,
issuetype_ids=issuetype_ids,
issuetype_names=issuetype_names,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    project_ids: list[str] | Unset = UNSET,
    project_keys: list[str] | Unset = UNSET,
    issuetype_ids: list[str] | Unset = UNSET,
    issuetype_names: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | IssueCreateMetadata | None:
    """ Get create issue metadata

     Returns details of projects, issue types within projects, and, when requested, the create screen
    fields for each issue type for the user. Use the information to populate the requests in [ Create
    issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

    The request can be restricted to specific projects or issue types using the query parameters. The
    response will contain information for the valid projects, issue types, or project and issue type
    combinations requested. Note that invalid project, issue type, or project and issue type
    combinations do not generate errors.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Create issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

    Args:
        project_ids (list[str] | Unset):
        project_keys (list[str] | Unset):
        issuetype_ids (list[str] | Unset):
        issuetype_names (list[str] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueCreateMetadata
     """


    return sync_detailed(
        client=client,
project_ids=project_ids,
project_keys=project_keys,
issuetype_ids=issuetype_ids,
issuetype_names=issuetype_names,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: list[str] | Unset = UNSET,
    project_keys: list[str] | Unset = UNSET,
    issuetype_ids: list[str] | Unset = UNSET,
    issuetype_names: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | IssueCreateMetadata]:
    """ Get create issue metadata

     Returns details of projects, issue types within projects, and, when requested, the create screen
    fields for each issue type for the user. Use the information to populate the requests in [ Create
    issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

    The request can be restricted to specific projects or issue types using the query parameters. The
    response will contain information for the valid projects, issue types, or project and issue type
    combinations requested. Note that invalid project, issue type, or project and issue type
    combinations do not generate errors.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Create issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

    Args:
        project_ids (list[str] | Unset):
        project_keys (list[str] | Unset):
        issuetype_ids (list[str] | Unset):
        issuetype_names (list[str] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueCreateMetadata]
     """


    kwargs = _get_kwargs(
        project_ids=project_ids,
project_keys=project_keys,
issuetype_ids=issuetype_ids,
issuetype_names=issuetype_names,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    project_ids: list[str] | Unset = UNSET,
    project_keys: list[str] | Unset = UNSET,
    issuetype_ids: list[str] | Unset = UNSET,
    issuetype_names: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | IssueCreateMetadata | None:
    """ Get create issue metadata

     Returns details of projects, issue types within projects, and, when requested, the create screen
    fields for each issue type for the user. Use the information to populate the requests in [ Create
    issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).

    The request can be restricted to specific projects or issue types using the query parameters. The
    response will contain information for the valid projects, issue types, or project and issue type
    combinations requested. Note that invalid project, issue type, or project and issue type
    combinations do not generate errors.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Create issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.

    Args:
        project_ids (list[str] | Unset):
        project_keys (list[str] | Unset):
        issuetype_ids (list[str] | Unset):
        issuetype_names (list[str] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueCreateMetadata
     """


    return (await asyncio_detailed(
        client=client,
project_ids=project_ids,
project_keys=project_keys,
issuetype_ids=issuetype_ids,
issuetype_names=issuetype_names,
expand=expand,

    )).parsed
