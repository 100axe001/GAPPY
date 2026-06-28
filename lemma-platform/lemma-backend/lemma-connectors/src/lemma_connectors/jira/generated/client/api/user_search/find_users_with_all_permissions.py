from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user import User
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    permissions: str,
    issue_key: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["username"] = username

    params["accountId"] = account_id

    params["permissions"] = permissions

    params["issueKey"] = issue_key

    params["projectKey"] = project_key

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/permission/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[User] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = User.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    permissions: str,
    issue_key: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | list[User]]:
    """ Find users with permissions

     Returns a list of users who fulfill these criteria:

     *  their user attributes match a search string.
     *  they have a set of permissions for a project or issue.

    If no search string is provided, a list of all users with the permissions is returned.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the search string and
    have permission for the project or issue. This means the operation usually returns fewer users than
    specified in `maxResults`. To get all the users who match the search string and have permission for
    the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records
    in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users
    for any project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a
    project, to get users for that project.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        permissions (str):
        issue_key (str | Unset):
        project_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
username=username,
account_id=account_id,
permissions=permissions,
issue_key=issue_key,
project_key=project_key,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    permissions: str,
    issue_key: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | list[User] | None:
    """ Find users with permissions

     Returns a list of users who fulfill these criteria:

     *  their user attributes match a search string.
     *  they have a set of permissions for a project or issue.

    If no search string is provided, a list of all users with the permissions is returned.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the search string and
    have permission for the project or issue. This means the operation usually returns fewer users than
    specified in `maxResults`. To get all the users who match the search string and have permission for
    the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records
    in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users
    for any project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a
    project, to get users for that project.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        permissions (str):
        issue_key (str | Unset):
        project_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return sync_detailed(
        client=client,
query=query,
username=username,
account_id=account_id,
permissions=permissions,
issue_key=issue_key,
project_key=project_key,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    permissions: str,
    issue_key: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | list[User]]:
    """ Find users with permissions

     Returns a list of users who fulfill these criteria:

     *  their user attributes match a search string.
     *  they have a set of permissions for a project or issue.

    If no search string is provided, a list of all users with the permissions is returned.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the search string and
    have permission for the project or issue. This means the operation usually returns fewer users than
    specified in `maxResults`. To get all the users who match the search string and have permission for
    the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records
    in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users
    for any project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a
    project, to get users for that project.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        permissions (str):
        issue_key (str | Unset):
        project_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
username=username,
account_id=account_id,
permissions=permissions,
issue_key=issue_key,
project_key=project_key,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    permissions: str,
    issue_key: str | Unset = UNSET,
    project_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | list[User] | None:
    """ Find users with permissions

     Returns a list of users who fulfill these criteria:

     *  their user attributes match a search string.
     *  they have a set of permissions for a project or issue.

    If no search string is provided, a list of all users with the permissions is returned.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that match the search string and
    have permission for the project or issue. This means the operation usually returns fewer users than
    specified in `maxResults`. To get all the users who match the search string and have permission for
    the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records
    in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users
    for any project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a
    project, to get users for that project.

    Args:
        query (str | Unset):  Example: query.
        username (str | Unset):
        account_id (str | Unset):
        permissions (str):
        issue_key (str | Unset):
        project_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return (await asyncio_detailed(
        client=client,
query=query,
username=username,
account_id=account_id,
permissions=permissions,
issue_key=issue_key,
project_key=project_key,
start_at=start_at,
max_results=max_results,

    )).parsed
