from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.task_progress_bean_remove_option_from_issues_result import TaskProgressBeanRemoveOptionFromIssuesResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_key: str,
    option_id: int,
    *,
    replace_with: int | Unset = UNSET,
    jql: str | Unset = UNSET,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["replaceWith"] = replace_with

    params["jql"] = jql

    params["overrideScreenSecurity"] = override_screen_security

    params["overrideEditableFlag"] = override_editable_flag


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/field/{field_key}/option/{option_id}/issue".format(field_key=quote(str(field_key), safe=""),option_id=quote(str(option_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TaskProgressBeanRemoveOptionFromIssuesResult | None:
    if response.status_code == 303:
        response_303 = TaskProgressBeanRemoveOptionFromIssuesResult.from_dict(response.json())



        return response_303

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | TaskProgressBeanRemoveOptionFromIssuesResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    replace_with: int | Unset = UNSET,
    jql: str | Unset = UNSET,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any | TaskProgressBeanRemoveOptionFromIssuesResult]:
    """ Replace issue field option

     Deselects an issue-field select-list option from all issues where it is selected. A different option
    can be selected to replace the deselected option. The update can also be limited to a smaller set of
    issues by using a JQL query.

    Connect and Forge app users with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security
    configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This is an [asynchronous operation](#async). The response object contains a link to the long-running
    task.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        replace_with (int | Unset):
        jql (str | Unset):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanRemoveOptionFromIssuesResult]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
option_id=option_id,
replace_with=replace_with,
jql=jql,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    replace_with: int | Unset = UNSET,
    jql: str | Unset = UNSET,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Any | TaskProgressBeanRemoveOptionFromIssuesResult | None:
    """ Replace issue field option

     Deselects an issue-field select-list option from all issues where it is selected. A different option
    can be selected to replace the deselected option. The update can also be limited to a smaller set of
    issues by using a JQL query.

    Connect and Forge app users with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security
    configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This is an [asynchronous operation](#async). The response object contains a link to the long-running
    task.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        replace_with (int | Unset):
        jql (str | Unset):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanRemoveOptionFromIssuesResult
     """


    return sync_detailed(
        field_key=field_key,
option_id=option_id,
client=client,
replace_with=replace_with,
jql=jql,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    ).parsed

async def asyncio_detailed(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    replace_with: int | Unset = UNSET,
    jql: str | Unset = UNSET,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Response[Any | TaskProgressBeanRemoveOptionFromIssuesResult]:
    """ Replace issue field option

     Deselects an issue-field select-list option from all issues where it is selected. A different option
    can be selected to replace the deselected option. The update can also be limited to a smaller set of
    issues by using a JQL query.

    Connect and Forge app users with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security
    configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This is an [asynchronous operation](#async). The response object contains a link to the long-running
    task.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        replace_with (int | Unset):
        jql (str | Unset):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanRemoveOptionFromIssuesResult]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
option_id=option_id,
replace_with=replace_with,
jql=jql,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    replace_with: int | Unset = UNSET,
    jql: str | Unset = UNSET,
    override_screen_security: bool | Unset = False,
    override_editable_flag: bool | Unset = False,

) -> Any | TaskProgressBeanRemoveOptionFromIssuesResult | None:
    """ Replace issue field option

     Deselects an issue-field select-list option from all issues where it is selected. A different option
    can be selected to replace the deselected option. The update can also be limited to a smaller set of
    issues by using a JQL query.

    Connect and Forge app users with *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) can override the screen security
    configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

    This is an [asynchronous operation](#async). The response object contains a link to the long-running
    task.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        replace_with (int | Unset):
        jql (str | Unset):
        override_screen_security (bool | Unset):  Default: False.
        override_editable_flag (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanRemoveOptionFromIssuesResult
     """


    return (await asyncio_detailed(
        field_key=field_key,
option_id=option_id,
client=client,
replace_with=replace_with,
jql=jql,
override_screen_security=override_screen_security,
override_editable_flag=override_editable_flag,

    )).parsed
