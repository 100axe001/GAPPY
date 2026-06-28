from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_link_type import IssueLinkType
from typing import cast



def _get_kwargs(
    issue_link_type_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issueLinkType/{issue_link_type_id}".format(issue_link_type_id=quote(str(issue_link_type_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueLinkType | None:
    if response.status_code == 200:
        response_200 = IssueLinkType.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueLinkType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueLinkType]:
    """ Get issue link type

     Returns an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

    Args:
        issue_link_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLinkType]
     """


    kwargs = _get_kwargs(
        issue_link_type_id=issue_link_type_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueLinkType | None:
    """ Get issue link type

     Returns an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

    Args:
        issue_link_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLinkType
     """


    return sync_detailed(
        issue_link_type_id=issue_link_type_id,
client=client,

    ).parsed

async def asyncio_detailed(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueLinkType]:
    """ Get issue link type

     Returns an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

    Args:
        issue_link_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLinkType]
     """


    kwargs = _get_kwargs(
        issue_link_type_id=issue_link_type_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueLinkType | None:
    """ Get issue link type

     Returns an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

    Args:
        issue_link_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLinkType
     """


    return (await asyncio_detailed(
        issue_link_type_id=issue_link_type_id,
client=client,

    )).parsed
