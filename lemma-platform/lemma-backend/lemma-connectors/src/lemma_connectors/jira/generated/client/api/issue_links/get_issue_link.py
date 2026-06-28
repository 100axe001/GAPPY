from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_link import IssueLink
from typing import cast



def _get_kwargs(
    link_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issueLink/{link_id}".format(link_id=quote(str(link_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueLink | None:
    if response.status_code == 200:
        response_200 = IssueLink.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueLink]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    link_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueLink]:
    """ Get issue link

     Returns an issue link.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the linked issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission
    to view both of the issues.

    Args:
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLink]
     """


    kwargs = _get_kwargs(
        link_id=link_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    link_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueLink | None:
    """ Get issue link

     Returns an issue link.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the linked issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission
    to view both of the issues.

    Args:
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLink
     """


    return sync_detailed(
        link_id=link_id,
client=client,

    ).parsed

async def asyncio_detailed(
    link_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueLink]:
    """ Get issue link

     Returns an issue link.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the linked issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission
    to view both of the issues.

    Args:
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLink]
     """


    kwargs = _get_kwargs(
        link_id=link_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    link_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueLink | None:
    """ Get issue link

     Returns an issue link.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the
    projects containing the linked issues.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission
    to view both of the issues.

    Args:
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLink
     """


    return (await asyncio_detailed(
        link_id=link_id,
client=client,

    )).parsed
