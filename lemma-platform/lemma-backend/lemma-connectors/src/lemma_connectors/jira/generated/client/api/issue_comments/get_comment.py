from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.comment import Comment
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    id: str,
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/comment/{id}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Comment | None:
    if response.status_code == 200:
        response_200 = Comment.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Comment]:
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
    expand: str | Unset = UNSET,

) -> Response[Any | Comment]:
    """ Get comment

     Returns a comment.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, the user belongs to the group or has the role
    visibility is restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Comment]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
expand=expand,

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
    expand: str | Unset = UNSET,

) -> Any | Comment | None:
    """ Get comment

     Returns a comment.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, the user belongs to the group or has the role
    visibility is restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Comment
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
id=id,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    id: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | Comment]:
    """ Get comment

     Returns a comment.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, the user belongs to the group or has the role
    visibility is restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Comment]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
id=id,
expand=expand,

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
    expand: str | Unset = UNSET,

) -> Any | Comment | None:
    """ Get comment

     Returns a comment.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, the user belongs to the group or has the role
    visibility is restricted to.

    Args:
        issue_id_or_key (str):
        id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Comment
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
id=id,
client=client,
expand=expand,

    )).parsed
