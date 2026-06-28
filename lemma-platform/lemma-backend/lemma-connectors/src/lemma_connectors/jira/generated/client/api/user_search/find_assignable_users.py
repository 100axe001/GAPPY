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
    session_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    project: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    action_descriptor_id: int | Unset = UNSET,
    recommend: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["sessionId"] = session_id

    params["username"] = username

    params["accountId"] = account_id

    params["project"] = project

    params["issueKey"] = issue_key

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["actionDescriptorId"] = action_descriptor_id

    params["recommend"] = recommend


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/assignable/search",
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
    session_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    project: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    action_descriptor_id: int | Unset = UNSET,
    recommend: bool | Unset = False,

) -> Response[Any | list[User]]:
    """ Find users assignable to issues

     Returns a list of users that can be assigned to an issue. Use this operation to find the list of
    users who can be assigned to:

     *  a new issue, by providing the `projectKeyOrId`.
     *  an updated issue, by providing the `issueKey`.
     *  to an issue during a transition (workflow action), by providing the `issueKey` and the
    transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using
    the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-
    issueIdOrKey-get).

    In all these cases, you can pass an account ID to determine if a user can be assigned to an issue.
    The user is returned in the response if they can be assigned to the issue or issue transition.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that can be assigned the issue.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        query (str | Unset):  Example: query.
        session_id (str | Unset):
        username (str | Unset):
        account_id (str | Unset):
        project (str | Unset):
        issue_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        action_descriptor_id (int | Unset):
        recommend (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
session_id=session_id,
username=username,
account_id=account_id,
project=project,
issue_key=issue_key,
start_at=start_at,
max_results=max_results,
action_descriptor_id=action_descriptor_id,
recommend=recommend,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    project: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    action_descriptor_id: int | Unset = UNSET,
    recommend: bool | Unset = False,

) -> Any | list[User] | None:
    """ Find users assignable to issues

     Returns a list of users that can be assigned to an issue. Use this operation to find the list of
    users who can be assigned to:

     *  a new issue, by providing the `projectKeyOrId`.
     *  an updated issue, by providing the `issueKey`.
     *  to an issue during a transition (workflow action), by providing the `issueKey` and the
    transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using
    the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-
    issueIdOrKey-get).

    In all these cases, you can pass an account ID to determine if a user can be assigned to an issue.
    The user is returned in the response if they can be assigned to the issue or issue transition.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that can be assigned the issue.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        query (str | Unset):  Example: query.
        session_id (str | Unset):
        username (str | Unset):
        account_id (str | Unset):
        project (str | Unset):
        issue_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        action_descriptor_id (int | Unset):
        recommend (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return sync_detailed(
        client=client,
query=query,
session_id=session_id,
username=username,
account_id=account_id,
project=project,
issue_key=issue_key,
start_at=start_at,
max_results=max_results,
action_descriptor_id=action_descriptor_id,
recommend=recommend,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    project: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    action_descriptor_id: int | Unset = UNSET,
    recommend: bool | Unset = False,

) -> Response[Any | list[User]]:
    """ Find users assignable to issues

     Returns a list of users that can be assigned to an issue. Use this operation to find the list of
    users who can be assigned to:

     *  a new issue, by providing the `projectKeyOrId`.
     *  an updated issue, by providing the `issueKey`.
     *  to an issue during a transition (workflow action), by providing the `issueKey` and the
    transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using
    the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-
    issueIdOrKey-get).

    In all these cases, you can pass an account ID to determine if a user can be assigned to an issue.
    The user is returned in the response if they can be assigned to the issue or issue transition.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that can be assigned the issue.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        query (str | Unset):  Example: query.
        session_id (str | Unset):
        username (str | Unset):
        account_id (str | Unset):
        project (str | Unset):
        issue_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        action_descriptor_id (int | Unset):
        recommend (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[User]]
     """


    kwargs = _get_kwargs(
        query=query,
session_id=session_id,
username=username,
account_id=account_id,
project=project,
issue_key=issue_key,
start_at=start_at,
max_results=max_results,
action_descriptor_id=action_descriptor_id,
recommend=recommend,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    username: str | Unset = UNSET,
    account_id: str | Unset = UNSET,
    project: str | Unset = UNSET,
    issue_key: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    action_descriptor_id: int | Unset = UNSET,
    recommend: bool | Unset = False,

) -> Any | list[User] | None:
    """ Find users assignable to issues

     Returns a list of users that can be assigned to an issue. Use this operation to find the list of
    users who can be assigned to:

     *  a new issue, by providing the `projectKeyOrId`.
     *  an updated issue, by providing the `issueKey`.
     *  to an issue during a transition (workflow action), by providing the `issueKey` and the
    transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using
    the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-
    issueIdOrKey-get).

    In all these cases, you can pass an account ID to determine if a user can be assigned to an issue.
    The user is returned in the response if they can be assigned to the issue or issue transition.

    This operation takes the users in the range defined by `startAt` and `maxResults`, up to the
    thousandth user, and then returns only the users from that range that can be assigned the issue.
    This means the operation usually returns fewer users than specified in `maxResults`. To get all the
    users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and
    filter the records in your code.

    Privacy controls are applied to the response based on the users' preferences. This could mean, for
    example, that the user's email address is hidden. See the [Profile visibility
    overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        query (str | Unset):  Example: query.
        session_id (str | Unset):
        username (str | Unset):
        account_id (str | Unset):
        project (str | Unset):
        issue_key (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        action_descriptor_id (int | Unset):
        recommend (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[User]
     """


    return (await asyncio_detailed(
        client=client,
query=query,
session_id=session_id,
username=username,
account_id=account_id,
project=project,
issue_key=issue_key,
start_at=start_at,
max_results=max_results,
action_descriptor_id=action_descriptor_id,
recommend=recommend,

    )).parsed
