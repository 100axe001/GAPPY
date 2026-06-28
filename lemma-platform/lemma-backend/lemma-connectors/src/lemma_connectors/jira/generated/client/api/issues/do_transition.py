from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_update_details import IssueUpdateDetails
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    body: IssueUpdateDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/{issue_id_or_key}/transitions".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
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
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: IssueUpdateDetails,

) -> Response[Any]:
    """ Transition issue

     Performs an issue transition and, if the transition has a screen, updates the fields from the
    transition screen.

    sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or
    `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-
    rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Transition issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (IssueUpdateDetails): Details of an issue update request.

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
    body: IssueUpdateDetails,

) -> Response[Any]:
    """ Transition issue

     Performs an issue transition and, if the transition has a screen, updates the fields from the
    transition screen.

    sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or
    `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-
    rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Transition issues* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        body (IssueUpdateDetails): Details of an issue update request.

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

