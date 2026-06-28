from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.permissions import Permissions
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_key: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    issue_id: str | Unset = UNSET,
    permissions: str | Unset = UNSET,
    project_uuid: str | Unset = UNSET,
    project_configuration_uuid: str | Unset = UNSET,
    comment_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["projectKey"] = project_key

    params["projectId"] = project_id

    params["issueKey"] = issue_key

    params["issueId"] = issue_id

    params["permissions"] = permissions

    params["projectUuid"] = project_uuid

    params["projectConfigurationUuid"] = project_configuration_uuid

    params["commentId"] = comment_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/mypermissions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | Permissions | None:
    if response.status_code == 200:
        response_200 = Permissions.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | Permissions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    issue_id: str | Unset = UNSET,
    permissions: str | Unset = UNSET,
    project_uuid: str | Unset = UNSET,
    project_configuration_uuid: str | Unset = UNSET,
    comment_id: str | Unset = UNSET,

) -> Response[ErrorCollection | Permissions]:
    r""" Get my permissions

     Returns a list of permissions indicating which permissions the user has. Details of the user's
    permissions can be obtained in a global, project, issue or comment context.

    The user is reported as having a project permission:

     *  in the global context, if the user has the project permission in any project.
     *  for a project, where the project permission is determined using issue data, if the user meets
    the permission's criteria for any issue in the project. Otherwise, if the user has the project
    permission in the project.
     *  for an issue, where a project permission is determined using issue data, if the user has the
    permission in the issue. Otherwise, if the user has the project permission in the project containing
    the issue.
     *  for a comment, where the user has both the permission to browse the comment and the project
    permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a
    `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be
    returned.

    This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the
    global context or a project context but may not have the permission for any or all issues. For
    example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this
    permission in the global context or the context of a project, because any user can be a reporter.
    However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES
    permission for that issue.

    Global permissions are unaffected by context.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_key (str | Unset):
        project_id (str | Unset):
        issue_key (str | Unset):
        issue_id (str | Unset):
        permissions (str | Unset):  Example: BROWSE_PROJECTS,EDIT_ISSUES.
        project_uuid (str | Unset):
        project_configuration_uuid (str | Unset):
        comment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | Permissions]
     """


    kwargs = _get_kwargs(
        project_key=project_key,
project_id=project_id,
issue_key=issue_key,
issue_id=issue_id,
permissions=permissions,
project_uuid=project_uuid,
project_configuration_uuid=project_configuration_uuid,
comment_id=comment_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    issue_id: str | Unset = UNSET,
    permissions: str | Unset = UNSET,
    project_uuid: str | Unset = UNSET,
    project_configuration_uuid: str | Unset = UNSET,
    comment_id: str | Unset = UNSET,

) -> ErrorCollection | Permissions | None:
    r""" Get my permissions

     Returns a list of permissions indicating which permissions the user has. Details of the user's
    permissions can be obtained in a global, project, issue or comment context.

    The user is reported as having a project permission:

     *  in the global context, if the user has the project permission in any project.
     *  for a project, where the project permission is determined using issue data, if the user meets
    the permission's criteria for any issue in the project. Otherwise, if the user has the project
    permission in the project.
     *  for an issue, where a project permission is determined using issue data, if the user has the
    permission in the issue. Otherwise, if the user has the project permission in the project containing
    the issue.
     *  for a comment, where the user has both the permission to browse the comment and the project
    permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a
    `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be
    returned.

    This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the
    global context or a project context but may not have the permission for any or all issues. For
    example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this
    permission in the global context or the context of a project, because any user can be a reporter.
    However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES
    permission for that issue.

    Global permissions are unaffected by context.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_key (str | Unset):
        project_id (str | Unset):
        issue_key (str | Unset):
        issue_id (str | Unset):
        permissions (str | Unset):  Example: BROWSE_PROJECTS,EDIT_ISSUES.
        project_uuid (str | Unset):
        project_configuration_uuid (str | Unset):
        comment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | Permissions
     """


    return sync_detailed(
        client=client,
project_key=project_key,
project_id=project_id,
issue_key=issue_key,
issue_id=issue_id,
permissions=permissions,
project_uuid=project_uuid,
project_configuration_uuid=project_configuration_uuid,
comment_id=comment_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    issue_id: str | Unset = UNSET,
    permissions: str | Unset = UNSET,
    project_uuid: str | Unset = UNSET,
    project_configuration_uuid: str | Unset = UNSET,
    comment_id: str | Unset = UNSET,

) -> Response[ErrorCollection | Permissions]:
    r""" Get my permissions

     Returns a list of permissions indicating which permissions the user has. Details of the user's
    permissions can be obtained in a global, project, issue or comment context.

    The user is reported as having a project permission:

     *  in the global context, if the user has the project permission in any project.
     *  for a project, where the project permission is determined using issue data, if the user meets
    the permission's criteria for any issue in the project. Otherwise, if the user has the project
    permission in the project.
     *  for an issue, where a project permission is determined using issue data, if the user has the
    permission in the issue. Otherwise, if the user has the project permission in the project containing
    the issue.
     *  for a comment, where the user has both the permission to browse the comment and the project
    permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a
    `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be
    returned.

    This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the
    global context or a project context but may not have the permission for any or all issues. For
    example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this
    permission in the global context or the context of a project, because any user can be a reporter.
    However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES
    permission for that issue.

    Global permissions are unaffected by context.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_key (str | Unset):
        project_id (str | Unset):
        issue_key (str | Unset):
        issue_id (str | Unset):
        permissions (str | Unset):  Example: BROWSE_PROJECTS,EDIT_ISSUES.
        project_uuid (str | Unset):
        project_configuration_uuid (str | Unset):
        comment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | Permissions]
     """


    kwargs = _get_kwargs(
        project_key=project_key,
project_id=project_id,
issue_key=issue_key,
issue_id=issue_id,
permissions=permissions,
project_uuid=project_uuid,
project_configuration_uuid=project_configuration_uuid,
comment_id=comment_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    issue_id: str | Unset = UNSET,
    permissions: str | Unset = UNSET,
    project_uuid: str | Unset = UNSET,
    project_configuration_uuid: str | Unset = UNSET,
    comment_id: str | Unset = UNSET,

) -> ErrorCollection | Permissions | None:
    r""" Get my permissions

     Returns a list of permissions indicating which permissions the user has. Details of the user's
    permissions can be obtained in a global, project, issue or comment context.

    The user is reported as having a project permission:

     *  in the global context, if the user has the project permission in any project.
     *  for a project, where the project permission is determined using issue data, if the user meets
    the permission's criteria for any issue in the project. Otherwise, if the user has the project
    permission in the project.
     *  for an issue, where a project permission is determined using issue data, if the user has the
    permission in the issue. Otherwise, if the user has the project permission in the project containing
    the issue.
     *  for a comment, where the user has both the permission to browse the comment and the project
    permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a
    `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be
    returned.

    This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the
    global context or a project context but may not have the permission for any or all issues. For
    example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this
    permission in the global context or the context of a project, because any user can be a reporter.
    However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES
    permission for that issue.

    Global permissions are unaffected by context.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        project_key (str | Unset):
        project_id (str | Unset):
        issue_key (str | Unset):
        issue_id (str | Unset):
        permissions (str | Unset):  Example: BROWSE_PROJECTS,EDIT_ISSUES.
        project_uuid (str | Unset):
        project_configuration_uuid (str | Unset):
        comment_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | Permissions
     """


    return (await asyncio_detailed(
        client=client,
project_key=project_key,
project_id=project_id,
issue_key=issue_key,
issue_id=issue_id,
permissions=permissions,
project_uuid=project_uuid,
project_configuration_uuid=project_configuration_uuid,
comment_id=comment_id,

    )).parsed
