from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    comment_id: str,
    property_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/comment/{comment_id}/properties/{property_key}".format(comment_id=quote(str(comment_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }


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
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Delete comment property

     Deletes a comment property.

    **[Permissions](#permissions) required:** either of:

     *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a
    property from any comment.
     *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a
    property from a comment created by the user.

    Also, when the visibility of a comment is restricted to a role or group the user must be a member of
    that role or group.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        comment_id=comment_id,
property_key=property_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    comment_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Delete comment property

     Deletes a comment property.

    **[Permissions](#permissions) required:** either of:

     *  *Edit All Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a
    property from any comment.
     *  *Edit Own Comments* [project permission](https://confluence.atlassian.com/x/yodKLg) to delete a
    property from a comment created by the user.

    Also, when the visibility of a comment is restricted to a role or group the user must be a member of
    that role or group.

    Args:
        comment_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        comment_id=comment_id,
property_key=property_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

