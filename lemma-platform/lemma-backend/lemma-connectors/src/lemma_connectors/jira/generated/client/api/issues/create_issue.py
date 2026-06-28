from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.created_issue import CreatedIssue
from ...models.error_collection import ErrorCollection
from ...models.issue_update_details import IssueUpdateDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: IssueUpdateDetails,
    update_history: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["updateHistory"] = update_history


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatedIssue | ErrorCollection | None:
    if response.status_code == 201:
        response_201 = CreatedIssue.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatedIssue | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,
    update_history: bool | Unset = False,

) -> Response[CreatedIssue | ErrorCollection]:
    """ Create issue

     Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition
    may be applied, to move the issue or subtask to a workflow step other than the default start step,
    and issue properties set.

    The content of the issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` must contain the ID or key of the parent issue.

    In a next-gen project any issue may be made a child providing that the parent and child are members
    of the same project.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or
    subtask is created.

    Args:
        update_history (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedIssue | ErrorCollection]
     """


    kwargs = _get_kwargs(
        body=body,
update_history=update_history,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,
    update_history: bool | Unset = False,

) -> CreatedIssue | ErrorCollection | None:
    """ Create issue

     Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition
    may be applied, to move the issue or subtask to a workflow step other than the default start step,
    and issue properties set.

    The content of the issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` must contain the ID or key of the parent issue.

    In a next-gen project any issue may be made a child providing that the parent and child are members
    of the same project.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or
    subtask is created.

    Args:
        update_history (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedIssue | ErrorCollection
     """


    return sync_detailed(
        client=client,
body=body,
update_history=update_history,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,
    update_history: bool | Unset = False,

) -> Response[CreatedIssue | ErrorCollection]:
    """ Create issue

     Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition
    may be applied, to move the issue or subtask to a workflow step other than the default start step,
    and issue properties set.

    The content of the issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` must contain the ID or key of the parent issue.

    In a next-gen project any issue may be made a child providing that the parent and child are members
    of the same project.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or
    subtask is created.

    Args:
        update_history (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedIssue | ErrorCollection]
     """


    kwargs = _get_kwargs(
        body=body,
update_history=update_history,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,
    update_history: bool | Unset = False,

) -> CreatedIssue | ErrorCollection | None:
    """ Create issue

     Creates an issue or, where the option to create subtasks is enabled in Jira, a subtask. A transition
    may be applied, to move the issue or subtask to a workflow step other than the default start step,
    and issue properties set.

    The content of the issue or subtask is defined using `update` and `fields`. The fields that can be
    set in the issue or subtask are determined using the [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get). These are the same fields that appear on the issue's create screen.
    Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text
    fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a
    string and don't handle Atlassian Document Format content.

    Creating a subtask differs from creating an issue as follows:

     *  `issueType` must be set to a subtask issue type (use [ Get create issue metadata](#api-rest-
    api-3-issue-createmeta-get) to find subtask issue types).
     *  `parent` must contain the ID or key of the parent issue.

    In a next-gen project any issue may be made a child providing that the parent and child are members
    of the same project.

    **[Permissions](#permissions) required:** *Browse projects* and *Create issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project in which the issue or
    subtask is created.

    Args:
        update_history (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedIssue | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,
body=body,
update_history=update_history,

    )).parsed
