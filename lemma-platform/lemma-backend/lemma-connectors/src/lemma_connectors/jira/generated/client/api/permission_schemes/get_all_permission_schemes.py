from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permission_schemes import PermissionSchemes
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/permissionscheme",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PermissionSchemes | None:
    if response.status_code == 200:
        response_200 = PermissionSchemes.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PermissionSchemes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionSchemes]:
    r""" Get all permission schemes

     Returns all permission schemes.

    ### About permission schemes and grants ###

    A permission scheme is a collection of permission grants. A permission grant consists of a `holder`
    and a `permission`.

    #### Holder object ####

    The `holder` object contains information about the user or group being granted the permission. For
    example, the *Administer projects* permission is granted to a group named *Teams in space
    administrators*. In this case, the type is `\"type\": \"group\"`, and the parameter is the group
    name, `\"parameter\": \"Teams in space administrators\"` and the value is group ID, `\"value\":
    \"ca85fac0-d974-40ca-a615-7af99c48d24f\"`. The `holder` object is defined by the following
    properties:

     *  `type` Identifies the user or group (see the list of types below).
     *  `parameter` As a group's name can change, use of `value` is recommended. The value of this
    property depends on the `type`. For example, if the `type` is a group, then you need to specify the
    group name.
     *  `value` The value of this property depends on the `type`. If the `type` is a group, then you
    need to specify the group ID. For other `type` it has the same value as `parameter`

    The following `types` are available. The expected values for `parameter` and `value` are given in
    parentheses (some types may not have a `parameter` or `value`):

     *  `anyone` Grant for anonymous users.
     *  `applicationRole` Grant for users with access to the specified application (application name,
    application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL)
    for more information.
     *  `assignee` Grant for the user currently assigned to an issue.
     *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
     *  `groupCustomField` Grant for a user in the group selected in the specified custom field
    (`parameter` : custom field ID, `value` : custom field ID).
     *  `projectLead` Grant for a project lead.
     *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` :
    project role ID).
     *  `reporter` Grant for the user who reported the issue.
     *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the
    customer portal but not Jira. See [Customizing Jira Service Desk
    permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
     *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey
    but that is deprecated and the account ID should be used, `value` : user ID).
     *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom
    field ID, `value` : custom field ID).

    #### Built-in permissions ####

    The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps
    can also define custom permissions. See the [project
    permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and
    [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/)
    module documentation for more information.

    **Project permissions**

     *  `ADMINISTER_PROJECTS`
     *  `BROWSE_PROJECTS`
     *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
     *  `SERVICEDESK_AGENT` (Jira Service Desk only)
     *  `VIEW_DEV_TOOLS` (Jira Software only)
     *  `VIEW_READONLY_WORKFLOW`

    **Issue permissions**

     *  `ASSIGNABLE_USER`
     *  `ASSIGN_ISSUES`
     *  `CLOSE_ISSUES`
     *  `CREATE_ISSUES`
     *  `DELETE_ISSUES`
     *  `EDIT_ISSUES`
     *  `LINK_ISSUES`
     *  `MODIFY_REPORTER`
     *  `MOVE_ISSUES`
     *  `RESOLVE_ISSUES`
     *  `SCHEDULE_ISSUES`
     *  `SET_ISSUE_SECURITY`
     *  `TRANSITION_ISSUES`

    **Voters and watchers permissions**

     *  `MANAGE_WATCHERS`
     *  `VIEW_VOTERS_AND_WATCHERS`

    **Comments permissions**

     *  `ADD_COMMENTS`
     *  `DELETE_ALL_COMMENTS`
     *  `DELETE_OWN_COMMENTS`
     *  `EDIT_ALL_COMMENTS`
     *  `EDIT_OWN_COMMENTS`

    **Attachments permissions**

     *  `CREATE_ATTACHMENTS`
     *  `DELETE_ALL_ATTACHMENTS`
     *  `DELETE_OWN_ATTACHMENTS`

    **Time tracking permissions**

     *  `DELETE_ALL_WORKLOGS`
     *  `DELETE_OWN_WORKLOGS`
     *  `EDIT_ALL_WORKLOGS`
     *  `EDIT_OWN_WORKLOGS`
     *  `WORK_ON_ISSUES`

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionSchemes]
     """


    kwargs = _get_kwargs(
        expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | PermissionSchemes | None:
    r""" Get all permission schemes

     Returns all permission schemes.

    ### About permission schemes and grants ###

    A permission scheme is a collection of permission grants. A permission grant consists of a `holder`
    and a `permission`.

    #### Holder object ####

    The `holder` object contains information about the user or group being granted the permission. For
    example, the *Administer projects* permission is granted to a group named *Teams in space
    administrators*. In this case, the type is `\"type\": \"group\"`, and the parameter is the group
    name, `\"parameter\": \"Teams in space administrators\"` and the value is group ID, `\"value\":
    \"ca85fac0-d974-40ca-a615-7af99c48d24f\"`. The `holder` object is defined by the following
    properties:

     *  `type` Identifies the user or group (see the list of types below).
     *  `parameter` As a group's name can change, use of `value` is recommended. The value of this
    property depends on the `type`. For example, if the `type` is a group, then you need to specify the
    group name.
     *  `value` The value of this property depends on the `type`. If the `type` is a group, then you
    need to specify the group ID. For other `type` it has the same value as `parameter`

    The following `types` are available. The expected values for `parameter` and `value` are given in
    parentheses (some types may not have a `parameter` or `value`):

     *  `anyone` Grant for anonymous users.
     *  `applicationRole` Grant for users with access to the specified application (application name,
    application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL)
    for more information.
     *  `assignee` Grant for the user currently assigned to an issue.
     *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
     *  `groupCustomField` Grant for a user in the group selected in the specified custom field
    (`parameter` : custom field ID, `value` : custom field ID).
     *  `projectLead` Grant for a project lead.
     *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` :
    project role ID).
     *  `reporter` Grant for the user who reported the issue.
     *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the
    customer portal but not Jira. See [Customizing Jira Service Desk
    permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
     *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey
    but that is deprecated and the account ID should be used, `value` : user ID).
     *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom
    field ID, `value` : custom field ID).

    #### Built-in permissions ####

    The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps
    can also define custom permissions. See the [project
    permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and
    [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/)
    module documentation for more information.

    **Project permissions**

     *  `ADMINISTER_PROJECTS`
     *  `BROWSE_PROJECTS`
     *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
     *  `SERVICEDESK_AGENT` (Jira Service Desk only)
     *  `VIEW_DEV_TOOLS` (Jira Software only)
     *  `VIEW_READONLY_WORKFLOW`

    **Issue permissions**

     *  `ASSIGNABLE_USER`
     *  `ASSIGN_ISSUES`
     *  `CLOSE_ISSUES`
     *  `CREATE_ISSUES`
     *  `DELETE_ISSUES`
     *  `EDIT_ISSUES`
     *  `LINK_ISSUES`
     *  `MODIFY_REPORTER`
     *  `MOVE_ISSUES`
     *  `RESOLVE_ISSUES`
     *  `SCHEDULE_ISSUES`
     *  `SET_ISSUE_SECURITY`
     *  `TRANSITION_ISSUES`

    **Voters and watchers permissions**

     *  `MANAGE_WATCHERS`
     *  `VIEW_VOTERS_AND_WATCHERS`

    **Comments permissions**

     *  `ADD_COMMENTS`
     *  `DELETE_ALL_COMMENTS`
     *  `DELETE_OWN_COMMENTS`
     *  `EDIT_ALL_COMMENTS`
     *  `EDIT_OWN_COMMENTS`

    **Attachments permissions**

     *  `CREATE_ATTACHMENTS`
     *  `DELETE_ALL_ATTACHMENTS`
     *  `DELETE_OWN_ATTACHMENTS`

    **Time tracking permissions**

     *  `DELETE_ALL_WORKLOGS`
     *  `DELETE_OWN_WORKLOGS`
     *  `EDIT_ALL_WORKLOGS`
     *  `EDIT_OWN_WORKLOGS`
     *  `WORK_ON_ISSUES`

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionSchemes
     """


    return sync_detailed(
        client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | PermissionSchemes]:
    r""" Get all permission schemes

     Returns all permission schemes.

    ### About permission schemes and grants ###

    A permission scheme is a collection of permission grants. A permission grant consists of a `holder`
    and a `permission`.

    #### Holder object ####

    The `holder` object contains information about the user or group being granted the permission. For
    example, the *Administer projects* permission is granted to a group named *Teams in space
    administrators*. In this case, the type is `\"type\": \"group\"`, and the parameter is the group
    name, `\"parameter\": \"Teams in space administrators\"` and the value is group ID, `\"value\":
    \"ca85fac0-d974-40ca-a615-7af99c48d24f\"`. The `holder` object is defined by the following
    properties:

     *  `type` Identifies the user or group (see the list of types below).
     *  `parameter` As a group's name can change, use of `value` is recommended. The value of this
    property depends on the `type`. For example, if the `type` is a group, then you need to specify the
    group name.
     *  `value` The value of this property depends on the `type`. If the `type` is a group, then you
    need to specify the group ID. For other `type` it has the same value as `parameter`

    The following `types` are available. The expected values for `parameter` and `value` are given in
    parentheses (some types may not have a `parameter` or `value`):

     *  `anyone` Grant for anonymous users.
     *  `applicationRole` Grant for users with access to the specified application (application name,
    application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL)
    for more information.
     *  `assignee` Grant for the user currently assigned to an issue.
     *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
     *  `groupCustomField` Grant for a user in the group selected in the specified custom field
    (`parameter` : custom field ID, `value` : custom field ID).
     *  `projectLead` Grant for a project lead.
     *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` :
    project role ID).
     *  `reporter` Grant for the user who reported the issue.
     *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the
    customer portal but not Jira. See [Customizing Jira Service Desk
    permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
     *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey
    but that is deprecated and the account ID should be used, `value` : user ID).
     *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom
    field ID, `value` : custom field ID).

    #### Built-in permissions ####

    The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps
    can also define custom permissions. See the [project
    permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and
    [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/)
    module documentation for more information.

    **Project permissions**

     *  `ADMINISTER_PROJECTS`
     *  `BROWSE_PROJECTS`
     *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
     *  `SERVICEDESK_AGENT` (Jira Service Desk only)
     *  `VIEW_DEV_TOOLS` (Jira Software only)
     *  `VIEW_READONLY_WORKFLOW`

    **Issue permissions**

     *  `ASSIGNABLE_USER`
     *  `ASSIGN_ISSUES`
     *  `CLOSE_ISSUES`
     *  `CREATE_ISSUES`
     *  `DELETE_ISSUES`
     *  `EDIT_ISSUES`
     *  `LINK_ISSUES`
     *  `MODIFY_REPORTER`
     *  `MOVE_ISSUES`
     *  `RESOLVE_ISSUES`
     *  `SCHEDULE_ISSUES`
     *  `SET_ISSUE_SECURITY`
     *  `TRANSITION_ISSUES`

    **Voters and watchers permissions**

     *  `MANAGE_WATCHERS`
     *  `VIEW_VOTERS_AND_WATCHERS`

    **Comments permissions**

     *  `ADD_COMMENTS`
     *  `DELETE_ALL_COMMENTS`
     *  `DELETE_OWN_COMMENTS`
     *  `EDIT_ALL_COMMENTS`
     *  `EDIT_OWN_COMMENTS`

    **Attachments permissions**

     *  `CREATE_ATTACHMENTS`
     *  `DELETE_ALL_ATTACHMENTS`
     *  `DELETE_OWN_ATTACHMENTS`

    **Time tracking permissions**

     *  `DELETE_ALL_WORKLOGS`
     *  `DELETE_OWN_WORKLOGS`
     *  `EDIT_ALL_WORKLOGS`
     *  `EDIT_OWN_WORKLOGS`
     *  `WORK_ON_ISSUES`

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PermissionSchemes]
     """


    kwargs = _get_kwargs(
        expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | PermissionSchemes | None:
    r""" Get all permission schemes

     Returns all permission schemes.

    ### About permission schemes and grants ###

    A permission scheme is a collection of permission grants. A permission grant consists of a `holder`
    and a `permission`.

    #### Holder object ####

    The `holder` object contains information about the user or group being granted the permission. For
    example, the *Administer projects* permission is granted to a group named *Teams in space
    administrators*. In this case, the type is `\"type\": \"group\"`, and the parameter is the group
    name, `\"parameter\": \"Teams in space administrators\"` and the value is group ID, `\"value\":
    \"ca85fac0-d974-40ca-a615-7af99c48d24f\"`. The `holder` object is defined by the following
    properties:

     *  `type` Identifies the user or group (see the list of types below).
     *  `parameter` As a group's name can change, use of `value` is recommended. The value of this
    property depends on the `type`. For example, if the `type` is a group, then you need to specify the
    group name.
     *  `value` The value of this property depends on the `type`. If the `type` is a group, then you
    need to specify the group ID. For other `type` it has the same value as `parameter`

    The following `types` are available. The expected values for `parameter` and `value` are given in
    parentheses (some types may not have a `parameter` or `value`):

     *  `anyone` Grant for anonymous users.
     *  `applicationRole` Grant for users with access to the specified application (application name,
    application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL)
    for more information.
     *  `assignee` Grant for the user currently assigned to an issue.
     *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).
     *  `groupCustomField` Grant for a user in the group selected in the specified custom field
    (`parameter` : custom field ID, `value` : custom field ID).
     *  `projectLead` Grant for a project lead.
     *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` :
    project role ID).
     *  `reporter` Grant for the user who reported the issue.
     *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the
    customer portal but not Jira. See [Customizing Jira Service Desk
    permissions](https://confluence.atlassian.com/x/24dKLg) for more information.
     *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey
    but that is deprecated and the account ID should be used, `value` : user ID).
     *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom
    field ID, `value` : custom field ID).

    #### Built-in permissions ####

    The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps
    can also define custom permissions. See the [project
    permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and
    [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/)
    module documentation for more information.

    **Project permissions**

     *  `ADMINISTER_PROJECTS`
     *  `BROWSE_PROJECTS`
     *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)
     *  `SERVICEDESK_AGENT` (Jira Service Desk only)
     *  `VIEW_DEV_TOOLS` (Jira Software only)
     *  `VIEW_READONLY_WORKFLOW`

    **Issue permissions**

     *  `ASSIGNABLE_USER`
     *  `ASSIGN_ISSUES`
     *  `CLOSE_ISSUES`
     *  `CREATE_ISSUES`
     *  `DELETE_ISSUES`
     *  `EDIT_ISSUES`
     *  `LINK_ISSUES`
     *  `MODIFY_REPORTER`
     *  `MOVE_ISSUES`
     *  `RESOLVE_ISSUES`
     *  `SCHEDULE_ISSUES`
     *  `SET_ISSUE_SECURITY`
     *  `TRANSITION_ISSUES`

    **Voters and watchers permissions**

     *  `MANAGE_WATCHERS`
     *  `VIEW_VOTERS_AND_WATCHERS`

    **Comments permissions**

     *  `ADD_COMMENTS`
     *  `DELETE_ALL_COMMENTS`
     *  `DELETE_OWN_COMMENTS`
     *  `EDIT_ALL_COMMENTS`
     *  `EDIT_OWN_COMMENTS`

    **Attachments permissions**

     *  `CREATE_ATTACHMENTS`
     *  `DELETE_ALL_ATTACHMENTS`
     *  `DELETE_OWN_ATTACHMENTS`

    **Time tracking permissions**

     *  `DELETE_ALL_WORKLOGS`
     *  `DELETE_OWN_WORKLOGS`
     *  `EDIT_ALL_WORKLOGS`
     *  `EDIT_OWN_WORKLOGS`
     *  `WORK_ON_ISSUES`

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PermissionSchemes
     """


    return (await asyncio_detailed(
        client=client,
expand=expand,

    )).parsed
