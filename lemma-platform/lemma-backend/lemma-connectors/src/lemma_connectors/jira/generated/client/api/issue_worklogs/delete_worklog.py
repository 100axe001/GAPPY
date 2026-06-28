from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_worklog_adjust_estimate import DeleteWorklogAdjustEstimate
from ...types import UNSET, Unset



def _get_kwargs(
    issue_id_or_key: str,
    id: str,
    *,
    notify_users: bool | Unset = True,
    adjust_estimate: DeleteWorklogAdjustEstimate | Unset = DeleteWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    increase_by: str | Unset = UNSET,
    override_editable_flag: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["notifyUsers"] = notify_users

    json_adjust_estimate: str | Unset = UNSET
    if not isinstance(adjust_estimate, Unset):
        json_adjust_estimate = adjust_estimate.value

    params["adjustEstimate"] = json_adjust_estimate

    params["newEstimate"] = new_estimate

    params["increaseBy"] = increase_by

    params["overrideEditableFlag"] = override_editable_flag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/issue/{issue_id_or_key}/worklog/{id}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),id=quote(str(id), safe=""),),
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
    id: str,
    *,
    client: AuthenticatedClient,
    notify_users: bool | Unset = True,
    adjust_estimate: DeleteWorklogAdjustEstimate | Unset = DeleteWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    increase_by: str | Unset = UNSET,
    override_editable_flag: bool | Unset = False,

) -> Response[Any]:
    """ Delete worklog

     Deletes a worklog from an issue.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete
    any worklog or *Delete own worklogs* to delete worklogs created by the user,
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (DeleteWorklogAdjustEstimate | Unset):  Default:
            DeleteWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        increase_by (str | Unset):
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
increase_by=increase_by,
override_editable_flag=override_editable_flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    id: str,
    *,
    client: AuthenticatedClient,
    notify_users: bool | Unset = True,
    adjust_estimate: DeleteWorklogAdjustEstimate | Unset = DeleteWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    increase_by: str | Unset = UNSET,
    override_editable_flag: bool | Unset = False,

) -> Response[Any]:
    """ Delete worklog

     Deletes a worklog from an issue.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Delete all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to delete
    any worklog or *Delete own worklogs* to delete worklogs created by the user,
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (DeleteWorklogAdjustEstimate | Unset):  Default:
            DeleteWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        increase_by (str | Unset):
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
increase_by=increase_by,
override_editable_flag=override_editable_flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

