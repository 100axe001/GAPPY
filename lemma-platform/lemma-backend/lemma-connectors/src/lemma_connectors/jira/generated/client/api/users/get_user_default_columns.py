from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.column_item import ColumnItem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["username"] = username


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/columns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[ColumnItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ColumnItem.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[ColumnItem]]:
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
    username: str | Unset = UNSET,

) -> Response[Any | list[ColumnItem]]:
    """ Get user default columns

     Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user.
    If `accountId` is not passed in the request, the calling user's details are returned.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the
    column details for any user.
     *  Permission to access Jira, to get the calling user's column details.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ColumnItem]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | list[ColumnItem] | None:
    """ Get user default columns

     Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user.
    If `accountId` is not passed in the request, the calling user's details are returned.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the
    column details for any user.
     *  Permission to access Jira, to get the calling user's column details.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ColumnItem]
     """


    return sync_detailed(
        client=client,
account_id=account_id,
username=username,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any | list[ColumnItem]]:
    """ Get user default columns

     Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user.
    If `accountId` is not passed in the request, the calling user's details are returned.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the
    column details for any user.
     *  Permission to access Jira, to get the calling user's column details.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ColumnItem]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | list[ColumnItem] | None:
    """ Get user default columns

     Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user.
    If `accountId` is not passed in the request, the calling user's details are returned.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the
    column details for any user.
     *  Permission to access Jira, to get the calling user's column details.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ColumnItem]
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
username=username,

    )).parsed
