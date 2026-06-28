from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_update_details import IssueUpdateDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    body: IssueUpdateDetails,
    notify_users: bool | Unset = True,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["notifyUsers"] = notify_users

    params["overrideScreenSecurity"] = override_screen_security

    params["overrideEditableFlag"] = override_editable_flag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issue/{issue_id_or_key}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: IssueUpdateDetails,
    notify_users: bool | Unset = True,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any]:
    """ Edit issue

     Edits an issue. A transition may be applied and issue properties updated as part of the edit.

    The edits to the issue's fields are defined using `update` and `fields`. The fields that can be
    edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-
    get).

    The parent field may be set by key or ID. For standard issue types, the parent may be removed by
    setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and any
    `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content.
    Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format
    content.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can override
    the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        notify_users (bool | Unset):  Default: True.
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,
notify_users=notify_users,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,
    notify_users: bool | Unset = True,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any]:
    """ Edit issue

     Edits an issue. A transition may be applied and issue properties updated as part of the edit.

    The edits to the issue's fields are defined using `update` and `fields`. The fields that can be
    edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-
    get).

    The parent field may be set by key or ID. For standard issue types, the parent may be removed by
    setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and any
    `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content.
    Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format
    content.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can override
    the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        notify_users (bool | Unset):  Default: True.
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.
        body (IssueUpdateDetails): Details of an issue update request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,
notify_users=notify_users,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

