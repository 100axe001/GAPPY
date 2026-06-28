from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    id: str,
    move_issues_to: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/version/{id}/mergeto/{move_issues_to}".format(id=quote(str(id), safe=""),move_issues_to=quote(str(move_issues_to), safe=""),),
    }


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
    id: str,
    move_issues_to: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Merge versions

     Merges two project versions. The merge is completed by deleting the version specified in `id` and
    replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

    Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead.
    This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom
    fields.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    Args:
        id (str):
        move_issues_to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
move_issues_to=move_issues_to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    move_issues_to: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Merge versions

     Merges two project versions. The merge is completed by deleting the version specified in `id` and
    replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.

    Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead.
    This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom
    fields.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    Args:
        id (str):
        move_issues_to (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
move_issues_to=move_issues_to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

