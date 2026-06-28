from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_update_metadata import IssueUpdateMetadata
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["overrideScreenSecurity"] = override_screen_security

    params["overrideEditableFlag"] = override_editable_flag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/editmeta".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueUpdateMetadata | None:
    if response.status_code == 200:
        response_200 = IssueUpdateMetadata.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueUpdateMetadata]:
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
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any | IssueUpdateMetadata]:
    """ Get edit issue metadata

     Returns the edit screen fields for an issue that are visible to and editable by the user. Use the
    information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).

    This endpoint will check for these conditions:

    1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme,
    and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.
    2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-
    administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this
    condition.
    3.  Field is shown on the issue: each field has different conditions here. For example: Attachment
    field only shows if attachments are enabled. Assignee only shows if user has permissions to assign
    the issue.
    4.  If a field is custom then it must have valid custom field context, applicable for its project
    and issue type. All system fields are assumed to have context in all projects and all issue types.
    5.  Issue has a project, issue type, and status defined.
    6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step.
    `overrideEditableFlag=true` skips this condition.
    7.  The current workflow step is editable. This is true by default, but [can be disabled by
    setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the
    `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition.
    8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-
    administration/docs/permissions-for-company-managed-projects/).
    9.  Workflow permissions allow editing a field. This is true by default but [can be
    modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/)
    using `jira.permission.*` workflow properties.

    Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-
    cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return
    additional details using:

     *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields
    are available through screens, and field configuration (conditions 1. and 2. from the list above).
     *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow
    is present and if the current step is editable (conditions 6. and 7. from the list above).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note: For any fields to be editable the user must have the *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the issue.

    Args:
        issue_id_or_key (str):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueUpdateMetadata]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Any | IssueUpdateMetadata | None:
    """ Get edit issue metadata

     Returns the edit screen fields for an issue that are visible to and editable by the user. Use the
    information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).

    This endpoint will check for these conditions:

    1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme,
    and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.
    2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-
    administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this
    condition.
    3.  Field is shown on the issue: each field has different conditions here. For example: Attachment
    field only shows if attachments are enabled. Assignee only shows if user has permissions to assign
    the issue.
    4.  If a field is custom then it must have valid custom field context, applicable for its project
    and issue type. All system fields are assumed to have context in all projects and all issue types.
    5.  Issue has a project, issue type, and status defined.
    6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step.
    `overrideEditableFlag=true` skips this condition.
    7.  The current workflow step is editable. This is true by default, but [can be disabled by
    setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the
    `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition.
    8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-
    administration/docs/permissions-for-company-managed-projects/).
    9.  Workflow permissions allow editing a field. This is true by default but [can be
    modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/)
    using `jira.permission.*` workflow properties.

    Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-
    cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return
    additional details using:

     *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields
    are available through screens, and field configuration (conditions 1. and 2. from the list above).
     *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow
    is present and if the current step is editable (conditions 6. and 7. from the list above).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note: For any fields to be editable the user must have the *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the issue.

    Args:
        issue_id_or_key (str):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueUpdateMetadata
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any | IssueUpdateMetadata]:
    """ Get edit issue metadata

     Returns the edit screen fields for an issue that are visible to and editable by the user. Use the
    information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).

    This endpoint will check for these conditions:

    1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme,
    and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.
    2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-
    administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this
    condition.
    3.  Field is shown on the issue: each field has different conditions here. For example: Attachment
    field only shows if attachments are enabled. Assignee only shows if user has permissions to assign
    the issue.
    4.  If a field is custom then it must have valid custom field context, applicable for its project
    and issue type. All system fields are assumed to have context in all projects and all issue types.
    5.  Issue has a project, issue type, and status defined.
    6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step.
    `overrideEditableFlag=true` skips this condition.
    7.  The current workflow step is editable. This is true by default, but [can be disabled by
    setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the
    `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition.
    8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-
    administration/docs/permissions-for-company-managed-projects/).
    9.  Workflow permissions allow editing a field. This is true by default but [can be
    modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/)
    using `jira.permission.*` workflow properties.

    Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-
    cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return
    additional details using:

     *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields
    are available through screens, and field configuration (conditions 1. and 2. from the list above).
     *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow
    is present and if the current step is editable (conditions 6. and 7. from the list above).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note: For any fields to be editable the user must have the *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the issue.

    Args:
        issue_id_or_key (str):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueUpdateMetadata]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Any | IssueUpdateMetadata | None:
    """ Get edit issue metadata

     Returns the edit screen fields for an issue that are visible to and editable by the user. Use the
    information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).

    This endpoint will check for these conditions:

    1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme,
    and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition.
    2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-
    administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this
    condition.
    3.  Field is shown on the issue: each field has different conditions here. For example: Attachment
    field only shows if attachments are enabled. Assignee only shows if user has permissions to assign
    the issue.
    4.  If a field is custom then it must have valid custom field context, applicable for its project
    and issue type. All system fields are assumed to have context in all projects and all issue types.
    5.  Issue has a project, issue type, and status defined.
    6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step.
    `overrideEditableFlag=true` skips this condition.
    7.  The current workflow step is editable. This is true by default, but [can be disabled by
    setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the
    `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition.
    8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-
    administration/docs/permissions-for-company-managed-projects/).
    9.  Workflow permissions allow editing a field. This is true by default but [can be
    modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/)
    using `jira.permission.*` workflow properties.

    Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-
    cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.

    Connect apps having an app user with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users
    with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return
    additional details using:

     *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields
    are available through screens, and field configuration (conditions 1. and 2. from the list above).
     *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow
    is present and if the current step is editable (conditions 6. and 7. from the list above).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note: For any fields to be editable the user must have the *Edit issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the issue.

    Args:
        issue_id_or_key (str):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueUpdateMetadata
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )).parsed
