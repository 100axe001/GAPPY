from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.found_groups import FoundGroups
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    exclude: list[str] | Unset = UNSET,
    exclude_id: list[str] | Unset = UNSET,
    max_results: int | Unset = UNSET,
    case_insensitive: bool | Unset = False,
    user_name: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["query"] = query

    json_exclude: list[str] | Unset = UNSET
    if not isinstance(exclude, Unset):
        json_exclude = exclude


    params["exclude"] = json_exclude

    json_exclude_id: list[str] | Unset = UNSET
    if not isinstance(exclude_id, Unset):
        json_exclude_id = exclude_id


    params["excludeId"] = json_exclude_id

    params["maxResults"] = max_results

    params["caseInsensitive"] = case_insensitive

    params["userName"] = user_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/groups/picker",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FoundGroups | None:
    if response.status_code == 200:
        response_200 = FoundGroups.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FoundGroups]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    exclude: list[str] | Unset = UNSET,
    exclude_id: list[str] | Unset = UNSET,
    max_results: int | Unset = UNSET,
    case_insensitive: bool | Unset = False,
    user_name: str | Unset = UNSET,

) -> Response[FoundGroups]:
    """ Find groups

     Returns a list of groups whose names contain a query string. A list of group names can be provided
    to exclude groups from the results.

    The primary use case for this resource is to populate a group picker suggestions list. To this end,
    the returned object includes the `html` field where the matched query term is highlighted in the
    group name with the HTML strong tag. Also, the groups list is wrapped in a response object that
    contains a header for use in the picker, specifically *Showing X of Y matching groups*.

    The list returns with the groups sorted. If no groups match the list criteria, an empty list is
    returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without
    the required permission return an empty list.

    *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without
    this permission, calls where query is not an exact match to an existing group will return an empty
    list.

    Args:
        account_id (str | Unset):
        query (str | Unset):  Example: query.
        exclude (list[str] | Unset):
        exclude_id (list[str] | Unset):
        max_results (int | Unset):
        case_insensitive (bool | Unset):  Default: False.
        user_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FoundGroups]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
query=query,
exclude=exclude,
exclude_id=exclude_id,
max_results=max_results,
case_insensitive=case_insensitive,
user_name=user_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    exclude: list[str] | Unset = UNSET,
    exclude_id: list[str] | Unset = UNSET,
    max_results: int | Unset = UNSET,
    case_insensitive: bool | Unset = False,
    user_name: str | Unset = UNSET,

) -> FoundGroups | None:
    """ Find groups

     Returns a list of groups whose names contain a query string. A list of group names can be provided
    to exclude groups from the results.

    The primary use case for this resource is to populate a group picker suggestions list. To this end,
    the returned object includes the `html` field where the matched query term is highlighted in the
    group name with the HTML strong tag. Also, the groups list is wrapped in a response object that
    contains a header for use in the picker, specifically *Showing X of Y matching groups*.

    The list returns with the groups sorted. If no groups match the list criteria, an empty list is
    returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without
    the required permission return an empty list.

    *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without
    this permission, calls where query is not an exact match to an existing group will return an empty
    list.

    Args:
        account_id (str | Unset):
        query (str | Unset):  Example: query.
        exclude (list[str] | Unset):
        exclude_id (list[str] | Unset):
        max_results (int | Unset):
        case_insensitive (bool | Unset):  Default: False.
        user_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FoundGroups
     """


    return sync_detailed(
        client=client,
account_id=account_id,
query=query,
exclude=exclude,
exclude_id=exclude_id,
max_results=max_results,
case_insensitive=case_insensitive,
user_name=user_name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    exclude: list[str] | Unset = UNSET,
    exclude_id: list[str] | Unset = UNSET,
    max_results: int | Unset = UNSET,
    case_insensitive: bool | Unset = False,
    user_name: str | Unset = UNSET,

) -> Response[FoundGroups]:
    """ Find groups

     Returns a list of groups whose names contain a query string. A list of group names can be provided
    to exclude groups from the results.

    The primary use case for this resource is to populate a group picker suggestions list. To this end,
    the returned object includes the `html` field where the matched query term is highlighted in the
    group name with the HTML strong tag. Also, the groups list is wrapped in a response object that
    contains a header for use in the picker, specifically *Showing X of Y matching groups*.

    The list returns with the groups sorted. If no groups match the list criteria, an empty list is
    returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without
    the required permission return an empty list.

    *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without
    this permission, calls where query is not an exact match to an existing group will return an empty
    list.

    Args:
        account_id (str | Unset):
        query (str | Unset):  Example: query.
        exclude (list[str] | Unset):
        exclude_id (list[str] | Unset):
        max_results (int | Unset):
        case_insensitive (bool | Unset):  Default: False.
        user_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FoundGroups]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
query=query,
exclude=exclude,
exclude_id=exclude_id,
max_results=max_results,
case_insensitive=case_insensitive,
user_name=user_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    exclude: list[str] | Unset = UNSET,
    exclude_id: list[str] | Unset = UNSET,
    max_results: int | Unset = UNSET,
    case_insensitive: bool | Unset = False,
    user_name: str | Unset = UNSET,

) -> FoundGroups | None:
    """ Find groups

     Returns a list of groups whose names contain a query string. A list of group names can be provided
    to exclude groups from the results.

    The primary use case for this resource is to populate a group picker suggestions list. To this end,
    the returned object includes the `html` field where the matched query term is highlighted in the
    group name with the HTML strong tag. Also, the groups list is wrapped in a response object that
    contains a header for use in the picker, specifically *Showing X of Y matching groups*.

    The list returns with the groups sorted. If no groups match the list criteria, an empty list is
    returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without
    the required permission return an empty list.

    *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without
    this permission, calls where query is not an exact match to an existing group will return an empty
    list.

    Args:
        account_id (str | Unset):
        query (str | Unset):  Example: query.
        exclude (list[str] | Unset):
        exclude_id (list[str] | Unset):
        max_results (int | Unset):
        case_insensitive (bool | Unset):  Default: False.
        user_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FoundGroups
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
query=query,
exclude=exclude,
exclude_id=exclude_id,
max_results=max_results,
case_insensitive=case_insensitive,
user_name=user_name,

    )).parsed
