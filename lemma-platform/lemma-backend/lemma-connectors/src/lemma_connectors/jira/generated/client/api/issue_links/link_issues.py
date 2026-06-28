from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.link_issue_request_json_bean import LinkIssueRequestJsonBean
from typing import cast



def _get_kwargs(
    *,
    body: LinkIssueRequestJsonBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issueLink",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 201:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LinkIssueRequestJsonBean,

) -> Response[Any]:
    """ Create issue link

     Creates a link between two issues. Use this operation to indicate a relationship between two issues
    and optionally add a comment to the from (outward) issue. To use this resource the site must have
    [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

    This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link,
    use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

    If the link request duplicates a link, the response indicates that the issue link was created. If
    the request included a comment, the comment is added.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the issues to be linked,
     *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project
    containing the from (outward) issue,
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        body (LinkIssueRequestJsonBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LinkIssueRequestJsonBean,

) -> Response[Any]:
    """ Create issue link

     Creates a link between two issues. Use this operation to indicate a relationship between two issues
    and optionally add a comment to the from (outward) issue. To use this resource the site must have
    [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled.

    This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link,
    use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`.

    If the link request duplicates a link, the response indicates that the issue link was created. If
    the request included a comment, the comment is added.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the issues to be linked,
     *  *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project
    containing the from (outward) issue,
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        body (LinkIssueRequestJsonBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

