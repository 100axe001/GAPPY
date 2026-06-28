from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user_migration_bean import UserMigrationBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/bulk/migration",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[UserMigrationBean] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = UserMigrationBean.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[UserMigrationBean]]:
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

) -> Response[Any | list[UserMigrationBean]]:
    """ Get account IDs for users

     Returns the account IDs for the users specified in the `key` or `username` parameters. Note that
    multiple `key` or `username` parameters can be specified.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[UserMigrationBean]]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
username=username,
key=key,

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

) -> Any | list[UserMigrationBean] | None:
    """ Get account IDs for users

     Returns the account IDs for the users specified in the `key` or `username` parameters. Note that
    multiple `key` or `username` parameters can be specified.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[UserMigrationBean]
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
username=username,
key=key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    username: list[str] | Unset = UNSET,
    key: list[str] | Unset = UNSET,

) -> Response[Any | list[UserMigrationBean]]:
    """ Get account IDs for users

     Returns the account IDs for the users specified in the `key` or `username` parameters. Note that
    multiple `key` or `username` parameters can be specified.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[UserMigrationBean]]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
username=username,
key=key,

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

) -> Any | list[UserMigrationBean] | None:
    """ Get account IDs for users

     Returns the account IDs for the users specified in the `key` or `username` parameters. Note that
    multiple `key` or `username` parameters can be specified.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        username (list[str] | Unset):
        key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[UserMigrationBean]
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
username=username,
key=key,

    )).parsed
