from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.order_of_issue_types import OrderOfIssueTypes
from typing import cast



def _get_kwargs(
    issue_type_scheme_id: int,
    *,
    body: OrderOfIssueTypes,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move".format(issue_type_scheme_id=quote(str(issue_type_scheme_id), safe=""),),
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
    issue_type_scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: OrderOfIssueTypes,

) -> Response[Any]:
    """ Change order of issue types

     Changes the order of issue types in an issue type scheme.

    The request body parameters must meet the following requirements:

     *  all of the issue types must belong to the issue type scheme.
     *  either `after` or `position` must be provided.
     *  the issue type in `after` must not be in the issue type list.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_scheme_id (int):
        body (OrderOfIssueTypes): An ordered list of issue type IDs and information about where to
            move them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_scheme_id=issue_type_scheme_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_type_scheme_id: int,
    *,
    client: AuthenticatedClient,
    body: OrderOfIssueTypes,

) -> Response[Any]:
    """ Change order of issue types

     Changes the order of issue types in an issue type scheme.

    The request body parameters must meet the following requirements:

     *  all of the issue types must belong to the issue type scheme.
     *  either `after` or `position` must be provided.
     *  the issue type in `after` must not be in the issue type list.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_scheme_id (int):
        body (OrderOfIssueTypes): An ordered list of issue type IDs and information about where to
            move them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_scheme_id=issue_type_scheme_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

