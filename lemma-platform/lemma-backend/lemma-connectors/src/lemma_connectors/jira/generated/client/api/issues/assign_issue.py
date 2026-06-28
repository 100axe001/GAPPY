from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    body: User,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issue/{issue_id_or_key}/assignee".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
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
    body: User,

) -> Response[Any]:
    r""" Assign issue

     Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues*
    permission but has the *Assign issue* permission for the project that the issue is in.

    If `name` or `accountId` is set to:

     *  `\"-1\"`, the issue is assigned to the default assignee for the project.
     *  `null`, the issue is set to unassigned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Assign Issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (User): A user with details as permitted by the user's Atlassian Account privacy
            settings. However, be aware of these exceptions:

             *  User record deleted from Atlassian: This occurs as the result of a right to be
            forgotten request. In this case, `displayName` provides an indication and other parameters
            have default values or are blank (for example, email is blank).
             *  User record corrupted: This occurs as a results of events such as a server import and
            can only happen to deleted users. In this case, `accountId` returns *unknown* and all
            other parameters have fallback values.
             *  User record unavailable: This usually occurs due to an internal service outage. In
            this case, all parameters have fallback values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: User,

) -> Response[Any]:
    r""" Assign issue

     Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues*
    permission but has the *Assign issue* permission for the project that the issue is in.

    If `name` or `accountId` is set to:

     *  `\"-1\"`, the issue is assigned to the default assignee for the project.
     *  `null`, the issue is set to unassigned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse Projects* and *Assign Issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (User): A user with details as permitted by the user's Atlassian Account privacy
            settings. However, be aware of these exceptions:

             *  User record deleted from Atlassian: This occurs as the result of a right to be
            forgotten request. In this case, `displayName` provides an indication and other parameters
            have default values or are blank (for example, email is blank).
             *  User record corrupted: This occurs as a results of events such as a server import and
            can only happen to deleted users. In this case, `accountId` returns *unknown* and all
            other parameters have fallback values.
             *  User record unavailable: This usually occurs due to an internal service outage. In
            this case, all parameters have fallback values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

