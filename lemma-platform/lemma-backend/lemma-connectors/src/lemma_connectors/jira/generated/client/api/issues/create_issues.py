from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.created_issues import CreatedIssues
from ...models.issues_update_bean import IssuesUpdateBean
from typing import cast



def _get_kwargs(
    *,
    body: IssuesUpdateBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/bulk",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreatedIssues | None:
    if response.status_code == 201:
        response_201 = CreatedIssues.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = CreatedIssues.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreatedIssues]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssuesUpdateBean,

) -> Response[Any | CreatedIssues]:
    """ Bulk create issue

     Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks.
    Transitions may be applied, to move the issues or subtasks to a workflow step other than the default
    start step, and issue properties set.

    The content of each issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` the must contain the ID or key of the parent issue.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or
    subtask is created.

    Args:
        body (IssuesUpdateBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatedIssues]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: IssuesUpdateBean,

) -> Any | CreatedIssues | None:
    """ Bulk create issue

     Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks.
    Transitions may be applied, to move the issues or subtasks to a workflow step other than the default
    start step, and issue properties set.

    The content of each issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` the must contain the ID or key of the parent issue.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or
    subtask is created.

    Args:
        body (IssuesUpdateBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatedIssues
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssuesUpdateBean,

) -> Response[Any | CreatedIssues]:
    """ Bulk create issue

     Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks.
    Transitions may be applied, to move the issues or subtasks to a workflow step other than the default
    start step, and issue properties set.

    The content of each issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` the must contain the ID or key of the parent issue.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or
    subtask is created.

    Args:
        body (IssuesUpdateBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreatedIssues]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IssuesUpdateBean,

) -> Any | CreatedIssues | None:
    """ Bulk create issue

     Creates upto **50** issues and, where the option to create subtasks is enabled in Jira, subtasks.
    Transitions may be applied, to move the issues or subtasks to a workflow step other than the default
    start step, and issue properties set.

    The content of each issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issues' create screens.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` the must contain the ID or key of the parent issue.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which each issue or
    subtask is created.

    Args:
        body (IssuesUpdateBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreatedIssues
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
