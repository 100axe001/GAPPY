from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_revoke_auth_revoke_error_schema import AuthRevokeAuthRevokeErrorSchema
from ...models.auth_revoke_auth_revoke_schema import AuthRevokeAuthRevokeSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    test: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["test"] = test


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth.revoke",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema:
    if response.status_code == 200:
        response_200 = AuthRevokeAuthRevokeSchema.from_dict(response.json())



        return response_200

    response_default = AuthRevokeAuthRevokeErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema]:
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
    test: bool | Unset = UNSET,

) -> Response[AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema]:
    """  Revokes a token.

    Args:
        token (str):
        test (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema]
     """


    kwargs = _get_kwargs(
        token=token,
test=test,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    test: bool | Unset = UNSET,

) -> AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema | None:
    """  Revokes a token.

    Args:
        token (str):
        test (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema
     """


    return sync_detailed(
        client=client,
token=token,
test=test,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    test: bool | Unset = UNSET,

) -> Response[AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema]:
    """  Revokes a token.

    Args:
        token (str):
        test (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema]
     """


    kwargs = _get_kwargs(
        token=token,
test=test,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    test: bool | Unset = UNSET,

) -> AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema | None:
    """  Revokes a token.

    Args:
        token (str):
        test (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthRevokeAuthRevokeErrorSchema | AuthRevokeAuthRevokeSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
test=test,

    )).parsed
