from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_issue_is_watching import BulkIssueIsWatching
from ...models.issue_list import IssueList
from typing import cast



def _get_kwargs(
    *,
    body: IssueList,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/watching",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | BulkIssueIsWatching | None:
    if response.status_code == 200:
        response_200 = BulkIssueIsWatching.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | BulkIssueIsWatching]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueList,

) -> Response[Any | BulkIssueIsWatching]:
    """ Get is watching issue bulk

     Returns, for the user, details of the watched status of issues from a list. If an issue ID is
    invalid, the returned watched status is `false`.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueList): A list of issue IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkIssueIsWatching]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: IssueList,

) -> Any | BulkIssueIsWatching | None:
    """ Get is watching issue bulk

     Returns, for the user, details of the watched status of issues from a list. If an issue ID is
    invalid, the returned watched status is `false`.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueList): A list of issue IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkIssueIsWatching
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueList,

) -> Response[Any | BulkIssueIsWatching]:
    """ Get is watching issue bulk

     Returns, for the user, details of the watched status of issues from a list. If an issue ID is
    invalid, the returned watched status is `false`.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueList): A list of issue IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkIssueIsWatching]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IssueList,

) -> Any | BulkIssueIsWatching | None:
    """ Get is watching issue bulk

     Returns, for the user, details of the watched status of issues from a list. If an issue ID is
    invalid, the returned watched status is `false`.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueList): A list of issue IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkIssueIsWatching
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
