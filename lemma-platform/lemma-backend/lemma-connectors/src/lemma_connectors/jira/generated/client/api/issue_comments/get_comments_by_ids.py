from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_comment_list_request_bean import IssueCommentListRequestBean
from ...models.page_bean_comment import PageBeanComment
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: IssueCommentListRequestBean,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/comment/list",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanComment | None:
    if response.status_code == 200:
        response_200 = PageBeanComment.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanComment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueCommentListRequestBean,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanComment]:
    """ Get comments by IDs

     Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are returned where the user:

     *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        expand (str | Unset):
        body (IssueCommentListRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanComment]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: IssueCommentListRequestBean,
    expand: str | Unset = UNSET,

) -> Any | PageBeanComment | None:
    """ Get comments by IDs

     Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are returned where the user:

     *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        expand (str | Unset):
        body (IssueCommentListRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanComment
     """


    return sync_detailed(
        client=client,
body=body,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueCommentListRequestBean,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanComment]:
    """ Get comments by IDs

     Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are returned where the user:

     *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        expand (str | Unset):
        body (IssueCommentListRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanComment]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IssueCommentListRequestBean,
    expand: str | Unset = UNSET,

) -> Any | PageBeanComment | None:
    """ Get comments by IDs

     Returns a [paginated](#pagination) list of comments specified by a list of comment IDs.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Comments are returned where the user:

     *  has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the comment.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        expand (str | Unset):
        body (IssueCommentListRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanComment
     """


    return (await asyncio_detailed(
        client=client,
body=body,
expand=expand,

    )).parsed
