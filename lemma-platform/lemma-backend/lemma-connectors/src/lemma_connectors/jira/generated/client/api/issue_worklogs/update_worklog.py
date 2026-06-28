from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_worklog_adjust_estimate import UpdateWorklogAdjustEstimate
from ...models.worklog import Worklog
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    id: str,
    *,
    body: Worklog,
    notify_users: bool | Unset = True,
    adjust_estimate: UpdateWorklogAdjustEstimate | Unset = UpdateWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    expand: str | Unset = '',
    override_editable_flag: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["notifyUsers"] = notify_users

    json_adjust_estimate: str | Unset = UNSET
    if not isinstance(adjust_estimate, Unset):
        json_adjust_estimate = adjust_estimate.value

    params["adjustEstimate"] = json_adjust_estimate

    params["newEstimate"] = new_estimate

    params["expand"] = expand

    params["overrideEditableFlag"] = override_editable_flag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issue/{issue_id_or_key}/worklog/{id}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Worklog | None:
    if response.status_code == 200:
        response_200 = Worklog.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Worklog]:
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
    body: Worklog,
    notify_users: bool | Unset = True,
    adjust_estimate: UpdateWorklogAdjustEstimate | Unset = UpdateWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    expand: str | Unset = '',
    override_editable_flag: bool | Unset = False,

) -> Response[Any | Worklog]:
    """ Update worklog

     Updates a worklog.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (UpdateWorklogAdjustEstimate | Unset):  Default:
            UpdateWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        expand (str | Unset):  Default: ''.
        override_editable_flag (bool | Unset):  Default: False.
        body (Worklog): Details of a worklog.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Worklog]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
body=body,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
expand=expand,
override_editable_flag=override_editable_flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Worklog,
    notify_users: bool | Unset = True,
    adjust_estimate: UpdateWorklogAdjustEstimate | Unset = UpdateWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    expand: str | Unset = '',
    override_editable_flag: bool | Unset = False,

) -> Any | Worklog | None:
    """ Update worklog

     Updates a worklog.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (UpdateWorklogAdjustEstimate | Unset):  Default:
            UpdateWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        expand (str | Unset):  Default: ''.
        override_editable_flag (bool | Unset):  Default: False.
        body (Worklog): Details of a worklog.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Worklog
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
id=id,
client=client,
body=body,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
expand=expand,
override_editable_flag=override_editable_flag,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Worklog,
    notify_users: bool | Unset = True,
    adjust_estimate: UpdateWorklogAdjustEstimate | Unset = UpdateWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    expand: str | Unset = '',
    override_editable_flag: bool | Unset = False,

) -> Response[Any | Worklog]:
    """ Update worklog

     Updates a worklog.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (UpdateWorklogAdjustEstimate | Unset):  Default:
            UpdateWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        expand (str | Unset):  Default: ''.
        override_editable_flag (bool | Unset):  Default: False.
        body (Worklog): Details of a worklog.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Worklog]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
body=body,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
expand=expand,
override_editable_flag=override_editable_flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: Worklog,
    notify_users: bool | Unset = True,
    adjust_estimate: UpdateWorklogAdjustEstimate | Unset = UpdateWorklogAdjustEstimate.AUTO,
    new_estimate: str | Unset = UNSET,
    expand: str | Unset = '',
    override_editable_flag: bool | Unset = False,

) -> Any | Worklog | None:
    """ Update worklog

     Updates a worklog.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        notify_users (bool | Unset):  Default: True.
        adjust_estimate (UpdateWorklogAdjustEstimate | Unset):  Default:
            UpdateWorklogAdjustEstimate.AUTO.
        new_estimate (str | Unset):
        expand (str | Unset):  Default: ''.
        override_editable_flag (bool | Unset):  Default: False.
        body (Worklog): Details of a worklog.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Worklog
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
id=id,
client=client,
body=body,
notify_users=notify_users,
adjust_estimate=adjust_estimate,
new_estimate=new_estimate,
expand=expand,
override_editable_flag=override_editable_flag,

    )).parsed
