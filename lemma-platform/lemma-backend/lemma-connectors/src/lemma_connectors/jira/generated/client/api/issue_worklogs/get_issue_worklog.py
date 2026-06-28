from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_of_worklogs import PageOfWorklogs
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    started_after: int | Unset = UNSET,
    started_before: int | Unset = UNSET,
    expand: str | Unset = '',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["startedAfter"] = started_after

    params["startedBefore"] = started_before

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/worklog".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageOfWorklogs | None:
    if response.status_code == 200:
        response_200 = PageOfWorklogs.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageOfWorklogs]:
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
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    started_after: int | Unset = UNSET,
    started_before: int | Unset = UNSET,
    expand: str | Unset = '',

) -> Response[Any | PageOfWorklogs]:
    """ Get issue worklogs

     Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or
    after a date and time.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Workloads are only returned where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        started_after (int | Unset):
        started_before (int | Unset):
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfWorklogs]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
start_at=start_at,
max_results=max_results,
started_after=started_after,
started_before=started_before,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    started_after: int | Unset = UNSET,
    started_before: int | Unset = UNSET,
    expand: str | Unset = '',

) -> Any | PageOfWorklogs | None:
    """ Get issue worklogs

     Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or
    after a date and time.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Workloads are only returned where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        started_after (int | Unset):
        started_before (int | Unset):
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfWorklogs
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
started_after=started_after,
started_before=started_before,
expand=expand,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    started_after: int | Unset = UNSET,
    started_before: int | Unset = UNSET,
    expand: str | Unset = '',

) -> Response[Any | PageOfWorklogs]:
    """ Get issue worklogs

     Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or
    after a date and time.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Workloads are only returned where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        started_after (int | Unset):
        started_before (int | Unset):
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfWorklogs]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
start_at=start_at,
max_results=max_results,
started_after=started_after,
started_before=started_before,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    started_after: int | Unset = UNSET,
    started_before: int | Unset = UNSET,
    expand: str | Unset = '',

) -> Any | PageOfWorklogs | None:
    """ Get issue worklogs

     Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or
    after a date and time.

    Time tracking must be enabled in Jira, otherwise this operation returns an error. For more
    information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Workloads are only returned where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        started_after (int | Unset):
        started_before (int | Unset):
        expand (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfWorklogs
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
started_after=started_after,
started_before=started_before,
expand=expand,

    )).parsed
