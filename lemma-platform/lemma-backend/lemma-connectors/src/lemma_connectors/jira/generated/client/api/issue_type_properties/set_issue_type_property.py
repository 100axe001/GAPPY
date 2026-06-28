from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    issue_type_id: str,
    property_key: str,
    *,
    body: Any,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}".format(issue_type_id=quote(str(issue_type_id), safe=""),property_key=quote(str(property_key), safe=""),),
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
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set issue type property

     Creates or updates the value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against
    an issue type.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_id=issue_type_id,
property_key=property_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set issue type property

     Creates or updates the value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties). Use this resource to store and update data against
    an issue type.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_id=issue_type_id,
property_key=property_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

