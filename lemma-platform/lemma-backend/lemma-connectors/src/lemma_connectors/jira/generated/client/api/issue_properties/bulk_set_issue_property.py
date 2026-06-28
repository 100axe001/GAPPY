from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_issue_property_update_request import BulkIssuePropertyUpdateRequest
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    property_key: str,
    *,
    body: BulkIssuePropertyUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issue/properties/{property_key}".format(property_key=quote(str(property_key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: BulkIssuePropertyUpdateRequest,

) -> Response[Any | ErrorCollection]:
    r""" Bulk set issue property

     Sets a property value on multiple issues.

    The value set can be a constant or determined by a [Jira
    expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must
    be computable with constant complexity when applied to a set of issues. Expressions must also comply
    with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions/#restrictions) that apply to all Jira expressions.

    The issues to be updated can be specified by a filter.

    The filter identifies issues eligible for update using these criteria:

     *  `entityIds` Only issues from this list are eligible.
     *  `currentValue` Only issues with the property set to this value are eligible.
     *  `hasProperty`:

         *  If *true*, only issues with the property are eligible.
         *  If *false*, only issues without the property are eligible.

    If more than one criteria is specified, they are joined with the logical *AND*: only issues that
    satisfy all criteria are eligible.

    If an invalid combination of criteria is provided, an error is returned. For example, specifying a
    `currentValue` and `hasProperty` as *false* would not match any issues (because without the property
    the property cannot have a value).

    The filter is optional. Without the filter all the issues visible to the user and where the user has
    the EDIT\_ISSUES permission for the issue are considered eligible.

    This operation is:

     *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each
    project containing issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    Args:
        property_key (str):
        body (BulkIssuePropertyUpdateRequest): Bulk issue property update request details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: BulkIssuePropertyUpdateRequest,

) -> Any | ErrorCollection | None:
    r""" Bulk set issue property

     Sets a property value on multiple issues.

    The value set can be a constant or determined by a [Jira
    expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must
    be computable with constant complexity when applied to a set of issues. Expressions must also comply
    with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions/#restrictions) that apply to all Jira expressions.

    The issues to be updated can be specified by a filter.

    The filter identifies issues eligible for update using these criteria:

     *  `entityIds` Only issues from this list are eligible.
     *  `currentValue` Only issues with the property set to this value are eligible.
     *  `hasProperty`:

         *  If *true*, only issues with the property are eligible.
         *  If *false*, only issues without the property are eligible.

    If more than one criteria is specified, they are joined with the logical *AND*: only issues that
    satisfy all criteria are eligible.

    If an invalid combination of criteria is provided, an error is returned. For example, specifying a
    `currentValue` and `hasProperty` as *false* would not match any issues (because without the property
    the property cannot have a value).

    The filter is optional. Without the filter all the issues visible to the user and where the user has
    the EDIT\_ISSUES permission for the issue are considered eligible.

    This operation is:

     *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each
    project containing issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    Args:
        property_key (str):
        body (BulkIssuePropertyUpdateRequest): Bulk issue property update request details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return sync_detailed(
        property_key=property_key,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: BulkIssuePropertyUpdateRequest,

) -> Response[Any | ErrorCollection]:
    r""" Bulk set issue property

     Sets a property value on multiple issues.

    The value set can be a constant or determined by a [Jira
    expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must
    be computable with constant complexity when applied to a set of issues. Expressions must also comply
    with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions/#restrictions) that apply to all Jira expressions.

    The issues to be updated can be specified by a filter.

    The filter identifies issues eligible for update using these criteria:

     *  `entityIds` Only issues from this list are eligible.
     *  `currentValue` Only issues with the property set to this value are eligible.
     *  `hasProperty`:

         *  If *true*, only issues with the property are eligible.
         *  If *false*, only issues without the property are eligible.

    If more than one criteria is specified, they are joined with the logical *AND*: only issues that
    satisfy all criteria are eligible.

    If an invalid combination of criteria is provided, an error is returned. For example, specifying a
    `currentValue` and `hasProperty` as *false* would not match any issues (because without the property
    the property cannot have a value).

    The filter is optional. Without the filter all the issues visible to the user and where the user has
    the EDIT\_ISSUES permission for the issue are considered eligible.

    This operation is:

     *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each
    project containing issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    Args:
        property_key (str):
        body (BulkIssuePropertyUpdateRequest): Bulk issue property update request details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: BulkIssuePropertyUpdateRequest,

) -> Any | ErrorCollection | None:
    r""" Bulk set issue property

     Sets a property value on multiple issues.

    The value set can be a constant or determined by a [Jira
    expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must
    be computable with constant complexity when applied to a set of issues. Expressions must also comply
    with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions/#restrictions) that apply to all Jira expressions.

    The issues to be updated can be specified by a filter.

    The filter identifies issues eligible for update using these criteria:

     *  `entityIds` Only issues from this list are eligible.
     *  `currentValue` Only issues with the property set to this value are eligible.
     *  `hasProperty`:

         *  If *true*, only issues with the property are eligible.
         *  If *false*, only issues without the property are eligible.

    If more than one criteria is specified, they are joined with the logical *AND*: only issues that
    satisfy all criteria are eligible.

    If an invalid combination of criteria is provided, an error is returned. For example, specifying a
    `currentValue` and `hasProperty` as *false* would not match any issues (because without the property
    the property cannot have a value).

    The filter is optional. Without the filter all the issues visible to the user and where the user has
    the EDIT\_ISSUES permission for the issue are considered eligible.

    This operation is:

     *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each
    project containing issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.

    Args:
        property_key (str):
        body (BulkIssuePropertyUpdateRequest): Bulk issue property update request details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return (await asyncio_detailed(
        property_key=property_key,
client=client,
body=body,

    )).parsed
