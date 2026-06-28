from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_user import PageBeanUser
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,
    account_id: list[str],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_username: list[str] | Unset = UNSET
    if not isinstance(username, Unset):
        json_username = username


    params["username"] = json_username

    json_key: list[str] | Unset = UNSET
    if not isinstance(key, Unset):
        json_key = key


    params["key"] = json_key

    json_account_id = account_id


    params["accountId"] = json_account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/bulk",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanUser | None:
    if response.status_code == 200:
        response_200 = PageBeanUser.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,
    account_id: list[str],

) -> Response[Any | PageBeanUser]:
    """ Bulk get users

     Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):
        account_id (list[str]):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanUser]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
username=username,
key=key,
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,
    account_id: list[str],

) -> Any | PageBeanUser | None:
    """ Bulk get users

     Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):
        account_id (list[str]):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanUser
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
username=username,
key=key,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,
    account_id: list[str],

) -> Response[Any | PageBeanUser]:
    """ Bulk get users

     Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):
        account_id (list[str]):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanUser]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
username=username,
key=key,
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,
    account_id: list[str],

) -> Any | PageBeanUser | None:
    """ Bulk get users

     Returns a [paginated](#pagination) list of the users specified by one or more account IDs.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):
        account_id (list[str]):  Example: 5b10ac8d82e05b22cc7d4ef5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanUser
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
username=username,
key=key,
account_id=account_id,

    )).parsed
