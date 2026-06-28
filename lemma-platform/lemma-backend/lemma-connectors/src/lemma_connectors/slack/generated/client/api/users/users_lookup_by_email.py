from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_lookup_by_email_users_lookup_by_email_error_schema import UsersLookupByEmailUsersLookupByEmailErrorSchema
from ...models.users_lookup_by_email_users_lookup_by_email_success_schema import UsersLookupByEmailUsersLookupByEmailSuccessSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,
    email: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["email"] = email


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users.lookupByEmail",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema:
    if response.status_code == 200:
        response_200 = UsersLookupByEmailUsersLookupByEmailSuccessSchema.from_dict(response.json())



        return response_200

    response_default = UsersLookupByEmailUsersLookupByEmailErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    email: str,

) -> Response[UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema]:
    """  Find a user with an email address.

    Args:
        token (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
email=email,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    email: str,

) -> UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema | None:
    """  Find a user with an email address.

    Args:
        token (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
email=email,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    email: str,

) -> Response[UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema]:
    """  Find a user with an email address.

    Args:
        token (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
email=email,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    email: str,

) -> UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema | None:
    """  Find a user with an email address.

    Args:
        token (str):
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersLookupByEmailUsersLookupByEmailErrorSchema | UsersLookupByEmailUsersLookupByEmailSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
email=email,

    )).parsed
