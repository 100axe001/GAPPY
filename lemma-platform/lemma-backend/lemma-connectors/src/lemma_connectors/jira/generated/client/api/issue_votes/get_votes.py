from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.votes import Votes
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/votes".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Votes | None:
    if response.status_code == 200:
        response_200 = Votes.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Votes]:
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

) -> Response[Any | Votes]:
    """ Get votes

     Returns details about the votes on an issue.

    This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set
    in General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is ini
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note that users with the necessary permissions for this operation but without the *View voters and
    watchers* project permissions are not returned details in the `voters` field.

    Args:
        issue_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Votes]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | Votes | None:
    """ Get votes

     Returns details about the votes on an issue.

    This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set
    in General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is ini
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note that users with the necessary permissions for this operation but without the *View voters and
    watchers* project permissions are not returned details in the `voters` field.

    Args:
        issue_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Votes
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Votes]:
    """ Get votes

     Returns details about the votes on an issue.

    This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set
    in General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is ini
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note that users with the necessary permissions for this operation but without the *View voters and
    watchers* project permissions are not returned details in the `voters` field.

    Args:
        issue_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Votes]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | Votes | None:
    """ Get votes

     Returns details about the votes on an issue.

    This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set
    in General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is ini
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Note that users with the necessary permissions for this operation but without the *View voters and
    watchers* project permissions are not returned details in the `voters` field.

    Args:
        issue_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Votes
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,

    )).parsed
