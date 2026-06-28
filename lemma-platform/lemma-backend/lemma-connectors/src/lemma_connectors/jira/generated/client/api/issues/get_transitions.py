from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.transitions import Transitions
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    expand: str | Unset = UNSET,
    transition_id: str | Unset = UNSET,
    skip_remote_only_condition: bool | Unset = False,
    include_unavailable_transitions: bool | Unset = False,
    sort_by_ops_bar_and_status: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand

    params["transitionId"] = transition_id

    params["skipRemoteOnlyCondition"] = skip_remote_only_condition

    params["includeUnavailableTransitions"] = include_unavailable_transitions

    params["sortByOpsBarAndStatus"] = sort_by_ops_bar_and_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}/transitions".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Transitions | None:
    if response.status_code == 200:
        response_200 = Transitions.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Transitions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    transition_id: str | Unset = UNSET,
    skip_remote_only_condition: bool | Unset = False,
    include_unavailable_transitions: bool | Unset = False,
    sort_by_ops_bar_and_status: bool | Unset = False,

) -> Response[Any | Transitions]:
    """ Get transitions

     Returns either all transitions or a transition that can be performed by the user on an issue, based
    on the issue's status.

    Note, if a request is made for a transition that does not exist or cannot be performed on the issue,
    given its status, the response will return any empty transitions list.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required: A list or transition is returned only when the user has:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    However, if the user does not have the *Transition issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

    Args:
        issue_id_or_key (str):
        expand (str | Unset):
        transition_id (str | Unset):
        skip_remote_only_condition (bool | Unset):  Default: False.
        include_unavailable_transitions (bool | Unset):  Default: False.
        sort_by_ops_bar_and_status (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Transitions]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
expand=expand,
transition_id=transition_id,
skip_remote_only_condition=skip_remote_only_condition,
include_unavailable_transitions=include_unavailable_transitions,
sort_by_ops_bar_and_status=sort_by_ops_bar_and_status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    transition_id: str | Unset = UNSET,
    skip_remote_only_condition: bool | Unset = False,
    include_unavailable_transitions: bool | Unset = False,
    sort_by_ops_bar_and_status: bool | Unset = False,

) -> Any | Transitions | None:
    """ Get transitions

     Returns either all transitions or a transition that can be performed by the user on an issue, based
    on the issue's status.

    Note, if a request is made for a transition that does not exist or cannot be performed on the issue,
    given its status, the response will return any empty transitions list.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required: A list or transition is returned only when the user has:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    However, if the user does not have the *Transition issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

    Args:
        issue_id_or_key (str):
        expand (str | Unset):
        transition_id (str | Unset):
        skip_remote_only_condition (bool | Unset):  Default: False.
        include_unavailable_transitions (bool | Unset):  Default: False.
        sort_by_ops_bar_and_status (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Transitions
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
expand=expand,
transition_id=transition_id,
skip_remote_only_condition=skip_remote_only_condition,
include_unavailable_transitions=include_unavailable_transitions,
sort_by_ops_bar_and_status=sort_by_ops_bar_and_status,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    transition_id: str | Unset = UNSET,
    skip_remote_only_condition: bool | Unset = False,
    include_unavailable_transitions: bool | Unset = False,
    sort_by_ops_bar_and_status: bool | Unset = False,

) -> Response[Any | Transitions]:
    """ Get transitions

     Returns either all transitions or a transition that can be performed by the user on an issue, based
    on the issue's status.

    Note, if a request is made for a transition that does not exist or cannot be performed on the issue,
    given its status, the response will return any empty transitions list.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required: A list or transition is returned only when the user has:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    However, if the user does not have the *Transition issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

    Args:
        issue_id_or_key (str):
        expand (str | Unset):
        transition_id (str | Unset):
        skip_remote_only_condition (bool | Unset):  Default: False.
        include_unavailable_transitions (bool | Unset):  Default: False.
        sort_by_ops_bar_and_status (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Transitions]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
expand=expand,
transition_id=transition_id,
skip_remote_only_condition=skip_remote_only_condition,
include_unavailable_transitions=include_unavailable_transitions,
sort_by_ops_bar_and_status=sort_by_ops_bar_and_status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    transition_id: str | Unset = UNSET,
    skip_remote_only_condition: bool | Unset = False,
    include_unavailable_transitions: bool | Unset = False,
    sort_by_ops_bar_and_status: bool | Unset = False,

) -> Any | Transitions | None:
    """ Get transitions

     Returns either all transitions or a transition that can be performed by the user on an issue, based
    on the issue's status.

    Note, if a request is made for a transition that does not exist or cannot be performed on the issue,
    given its status, the response will return any empty transitions list.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required: A list or transition is returned only when the user has:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    However, if the user does not have the *Transition issues* [ project
    permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

    Args:
        issue_id_or_key (str):
        expand (str | Unset):
        transition_id (str | Unset):
        skip_remote_only_condition (bool | Unset):  Default: False.
        include_unavailable_transitions (bool | Unset):  Default: False.
        sort_by_ops_bar_and_status (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Transitions
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
expand=expand,
transition_id=transition_id,
skip_remote_only_condition=skip_remote_only_condition,
include_unavailable_transitions=include_unavailable_transitions,
sort_by_ops_bar_and_status=sort_by_ops_bar_and_status,

    )).parsed
