from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remote_issue_link import RemoteIssueLink
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    global_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["globalId"] = global_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/remotelink".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RemoteIssueLink | None:
    if response.status_code == 200:
        response_200 = RemoteIssueLink.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RemoteIssueLink]:
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
    global_id: str | Unset = UNSET,

) -> Response[Any | RemoteIssueLink]:
    """ Get remote issue links

     Returns the remote issue links for an issue. When a remote issue link global ID is provided the
    record with that global ID is returned, otherwise all remote issue links are returned. Where a
    global ID includes reserved URL characters these must be escaped in the request. For example, pass
    `system=http://www.mycompany.com/support&id=1` as
    `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):  Example: 10000.
        global_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoteIssueLink]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
global_id=global_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    global_id: str | Unset = UNSET,

) -> Any | RemoteIssueLink | None:
    """ Get remote issue links

     Returns the remote issue links for an issue. When a remote issue link global ID is provided the
    record with that global ID is returned, otherwise all remote issue links are returned. Where a
    global ID includes reserved URL characters these must be escaped in the request. For example, pass
    `system=http://www.mycompany.com/support&id=1` as
    `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):  Example: 10000.
        global_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoteIssueLink
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
global_id=global_id,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    global_id: str | Unset = UNSET,

) -> Response[Any | RemoteIssueLink]:
    """ Get remote issue links

     Returns the remote issue links for an issue. When a remote issue link global ID is provided the
    record with that global ID is returned, otherwise all remote issue links are returned. Where a
    global ID includes reserved URL characters these must be escaped in the request. For example, pass
    `system=http://www.mycompany.com/support&id=1` as
    `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):  Example: 10000.
        global_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoteIssueLink]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
global_id=global_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    global_id: str | Unset = UNSET,

) -> Any | RemoteIssueLink | None:
    """ Get remote issue links

     Returns the remote issue links for an issue. When a remote issue link global ID is provided the
    record with that global ID is returned, otherwise all remote issue links are returned. Where a
    global ID includes reserved URL characters these must be escaped in the request. For example, pass
    `system=http://www.mycompany.com/support&id=1` as
    `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):  Example: 10000.
        global_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoteIssueLink
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
global_id=global_id,

    )).parsed
