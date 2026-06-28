from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset



def _get_kwargs(
    issue_id_or_key: str,
    *,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["username"] = username

    params["accountId"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/issue/{issue_id_or_key}/watchers".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
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
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete watcher

     Deletes a user as a watcher of an issue.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  To remove users other than themselves from the watchlist, *Manage watcher list* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

    Args:
        issue_id_or_key (str):
        username (str | Unset):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
username=username,
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete watcher

     Deletes a user as a watcher of an issue.

    This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in
    General configuration for Jira. See [Configuring Jira application
    options](https://confluence.atlassian.com/x/uYXKM) for details.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  To remove users other than themselves from the watchlist, *Manage watcher list* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

    Args:
        issue_id_or_key (str):
        username (str | Unset):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
username=username,
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

