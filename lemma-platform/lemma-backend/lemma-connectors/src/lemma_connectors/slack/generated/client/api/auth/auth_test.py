from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_test_auth_test_error_schema import AuthTestAuthTestErrorSchema
from ...models.auth_test_auth_test_success_schema import AuthTestAuthTestSuccessSchema
from typing import cast



def _get_kwargs(
    *,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth.test",
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema:
    if response.status_code == 200:
        response_200 = AuthTestAuthTestSuccessSchema.from_dict(response.json())



        return response_200

    response_default = AuthTestAuthTestErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema]:
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

) -> Response[AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema]:
    """  Checks authentication & identity.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,

) -> AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema | None:
    """  Checks authentication & identity.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,

) -> Response[AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema]:
    """  Checks authentication & identity.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,

) -> AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema | None:
    """  Checks authentication & identity.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTestAuthTestErrorSchema | AuthTestAuthTestSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,

    )).parsed
