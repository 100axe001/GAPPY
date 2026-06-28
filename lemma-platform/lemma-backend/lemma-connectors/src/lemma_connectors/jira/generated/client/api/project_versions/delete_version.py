from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset



def _get_kwargs(
    id: str,
    *,
    move_fix_issues_to: str | Unset = UNSET,
    move_affected_issues_to: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["moveFixIssuesTo"] = move_fix_issues_to

    params["moveAffectedIssuesTo"] = move_affected_issues_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/version/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
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
    *,
    client: AuthenticatedClient,
    move_fix_issues_to: str | Unset = UNSET,
    move_affected_issues_to: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete version

     Deletes a project version.

    Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that
    supports swapping version values in custom fields, in addition to the swapping for `fixVersion` and
    `affectedVersion` provided in this resource.

    Alternative versions can be provided to update issues that use the deleted version in `fixVersion`
    or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and
    `affectedVersion` that contain the deleted version are cleared.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    Args:
        id (str):
        move_fix_issues_to (str | Unset):
        move_affected_issues_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
move_fix_issues_to=move_fix_issues_to,
move_affected_issues_to=move_affected_issues_to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    move_fix_issues_to: str | Unset = UNSET,
    move_affected_issues_to: str | Unset = UNSET,

) -> Response[Any]:
    """ Delete version

     Deletes a project version.

    Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that
    supports swapping version values in custom fields, in addition to the swapping for `fixVersion` and
    `affectedVersion` provided in this resource.

    Alternative versions can be provided to update issues that use the deleted version in `fixVersion`
    or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and
    `affectedVersion` that contain the deleted version are cleared.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

    Args:
        id (str):
        move_fix_issues_to (str | Unset):
        move_affected_issues_to (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
move_fix_issues_to=move_fix_issues_to,
move_affected_issues_to=move_affected_issues_to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

