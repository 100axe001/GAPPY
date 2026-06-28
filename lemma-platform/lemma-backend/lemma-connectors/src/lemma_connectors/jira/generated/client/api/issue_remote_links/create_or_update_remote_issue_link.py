from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remote_issue_link_identifies import RemoteIssueLinkIdentifies
from ...models.remote_issue_link_request import RemoteIssueLinkRequest
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    body: RemoteIssueLinkRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/{issue_id_or_key}/remotelink".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | RemoteIssueLinkIdentifies | None:
    if response.status_code == 200:
        response_200 = RemoteIssueLinkIdentifies.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = RemoteIssueLinkIdentifies.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | RemoteIssueLinkIdentifies]:
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
    body: RemoteIssueLinkRequest,

) -> Response[Any | RemoteIssueLinkIdentifies]:
    """ Create or update remote issue link

     Creates or updates a remote issue link for an issue.

    If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any
    fields without values in the request are set to null. Otherwise, the remote issue link is created.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Link issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (RemoteIssueLinkRequest): Details of a remote issue link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoteIssueLinkIdentifies]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: RemoteIssueLinkRequest,

) -> Any | RemoteIssueLinkIdentifies | None:
    """ Create or update remote issue link

     Creates or updates a remote issue link for an issue.

    If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any
    fields without values in the request are set to null. Otherwise, the remote issue link is created.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Link issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (RemoteIssueLinkRequest): Details of a remote issue link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoteIssueLinkIdentifies
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: RemoteIssueLinkRequest,

) -> Response[Any | RemoteIssueLinkIdentifies]:
    """ Create or update remote issue link

     Creates or updates a remote issue link for an issue.

    If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any
    fields without values in the request are set to null. Otherwise, the remote issue link is created.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Link issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (RemoteIssueLinkRequest): Details of a remote issue link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoteIssueLinkIdentifies]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: RemoteIssueLinkRequest,

) -> Any | RemoteIssueLinkIdentifies | None:
    """ Create or update remote issue link

     Creates or updates a remote issue link for an issue.

    If a `globalId` is provided and a remote issue link with that global ID is found it is updated. Any
    fields without values in the request are set to null. Otherwise, the remote issue link is created.

    This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Link issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (RemoteIssueLinkRequest): Details of a remote issue link.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoteIssueLinkIdentifies
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
body=body,

    )).parsed
