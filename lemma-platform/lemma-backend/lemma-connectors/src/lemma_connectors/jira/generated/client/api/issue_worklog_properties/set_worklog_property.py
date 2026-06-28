from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    issue_id_or_key: str,
    worklog_id: str,
    property_key: str,
    *,
    body: Any,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issue/{issue_id_or_key}/worklog/{worklog_id}/properties/{property_key}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),worklog_id=quote(str(worklog_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 201:
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
    worklog_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set worklog property

     Sets the value of a worklog property. Use this operation to store custom data against the worklog.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        worklog_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
worklog_id=worklog_id,
property_key=property_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_id_or_key: str,
    worklog_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set worklog property

     Sets the value of a worklog property. Use this operation to store custom data against the worklog.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update
    any worklog or *Edit own worklogs* to update worklogs created by the user.
     *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        issue_id_or_key (str):
        worklog_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
worklog_id=worklog_id,
property_key=property_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

