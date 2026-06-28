from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_comments_order_by import GetCommentsOrderBy
from ...models.page_of_comments import PageOfComments
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: GetCommentsOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/comment".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageOfComments | None:
    if response.status_code == 200:
        response_200 = PageOfComments.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageOfComments]:
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
    order_by: GetCommentsOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageOfComments]:
    """ Get comments

     Returns all comments for an issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    role visibility is restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (GetCommentsOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfComments]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
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
    order_by: GetCommentsOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageOfComments | None:
    """ Get comments

     Returns all comments for an issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    role visibility is restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (GetCommentsOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfComments
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
expand=expand,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: GetCommentsOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageOfComments]:
    """ Get comments

     Returns all comments for an issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    role visibility is restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (GetCommentsOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageOfComments]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
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
    order_by: GetCommentsOrderBy | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageOfComments | None:
    """ Get comments

     Returns all comments for an issue.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    role visibility is restricted to.

    Args:
        issue_id_or_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (GetCommentsOrderBy | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageOfComments
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
expand=expand,

    )).parsed
