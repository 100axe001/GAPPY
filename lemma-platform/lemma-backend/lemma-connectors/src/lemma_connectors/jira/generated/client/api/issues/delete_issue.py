from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_issue_delete_subtasks import DeleteIssueDeleteSubtasks
from ...types import UNSET, Unset



def _get_kwargs(
    issue_id_or_key: str,
    *,
    delete_subtasks: DeleteIssueDeleteSubtasks | Unset = DeleteIssueDeleteSubtasks.FALSE,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_delete_subtasks: str | Unset = UNSET
    if not isinstance(delete_subtasks, Unset):
        json_delete_subtasks = delete_subtasks.value

    params["deleteSubtasks"] = json_delete_subtasks


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/issue/{issue_id_or_key}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    delete_subtasks: DeleteIssueDeleteSubtasks | Unset = DeleteIssueDeleteSubtasks.FALSE,

) -> Response[Any]:
    """ Delete issue

     Deletes an issue.

    An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set
    `deleteSubtasks`. This causes the issue's subtasks to be deleted with the issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Delete issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        delete_subtasks (DeleteIssueDeleteSubtasks | Unset):  Default:
            DeleteIssueDeleteSubtasks.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
delete_subtasks=delete_subtasks,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    delete_subtasks: DeleteIssueDeleteSubtasks | Unset = DeleteIssueDeleteSubtasks.FALSE,

) -> Response[Any]:
    """ Delete issue

     Deletes an issue.

    An issue cannot be deleted if it has one or more subtasks. To delete an issue with subtasks, set
    `deleteSubtasks`. This causes the issue's subtasks to be deleted with the issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Delete issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        delete_subtasks (DeleteIssueDeleteSubtasks | Unset):  Default:
            DeleteIssueDeleteSubtasks.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
delete_subtasks=delete_subtasks,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

