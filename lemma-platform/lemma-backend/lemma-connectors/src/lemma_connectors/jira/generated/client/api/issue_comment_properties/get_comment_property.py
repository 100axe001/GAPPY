from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.entity_property import EntityProperty
from typing import cast



def _get_kwargs(
    comment_id: str,
    property_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/comment/{comment_id}/properties/{property_key}".format(comment_id=quote(str(comment_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EntityProperty | None:
    if response.status_code == 200:
        response_200 = EntityProperty.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | EntityProperty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get comment property

     Returns the value of a comment property.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        comment_id=comment_id,
property_key=property_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get comment property

     Returns the value of a comment property.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return sync_detailed(
        comment_id=comment_id,
property_key=property_key,
client=client,

    ).parsed

async def asyncio_detailed(
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get comment property

     Returns the value of a comment property.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        comment_id=comment_id,
property_key=property_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get comment property

     Returns the value of a comment property.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.
     *  If the comment has visibility restrictions, belongs to the group or has the role visibility is
    restricted to.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return (await asyncio_detailed(
        comment_id=comment_id,
property_key=property_key,
client=client,

    )).parsed
