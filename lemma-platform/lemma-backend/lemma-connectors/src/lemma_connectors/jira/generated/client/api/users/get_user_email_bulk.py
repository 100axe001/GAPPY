from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.unrestricted_user_email import UnrestrictedUserEmail
from typing import cast



def _get_kwargs(
    *,
    account_id: list[str],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_account_id = account_id


    params["accountId"] = json_account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/email/bulk",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | UnrestrictedUserEmail | None:
    if response.status_code == 200:
        response_200 = UnrestrictedUserEmail.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | UnrestrictedUserEmail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: list[str],

) -> Response[Any | UnrestrictedUserEmail]:
    """ Get user email bulk

     Returns a user's email address. This API is only available to apps approved by Atlassian, according
    to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-
    to-email-address/27603).

    Args:
        account_id (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UnrestrictedUserEmail]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    account_id: list[str],

) -> Any | UnrestrictedUserEmail | None:
    """ Get user email bulk

     Returns a user's email address. This API is only available to apps approved by Atlassian, according
    to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-
    to-email-address/27603).

    Args:
        account_id (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UnrestrictedUserEmail
     """


    return sync_detailed(
        client=client,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: list[str],

) -> Response[Any | UnrestrictedUserEmail]:
    """ Get user email bulk

     Returns a user's email address. This API is only available to apps approved by Atlassian, according
    to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-
    to-email-address/27603).

    Args:
        account_id (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UnrestrictedUserEmail]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: list[str],

) -> Any | UnrestrictedUserEmail | None:
    """ Get user email bulk

     Returns a user's email address. This API is only available to apps approved by Atlassian, according
    to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-
    to-email-address/27603).

    Args:
        account_id (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UnrestrictedUserEmail
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,

    )).parsed
