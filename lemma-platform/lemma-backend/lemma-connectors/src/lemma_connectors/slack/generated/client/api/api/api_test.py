from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_test_api_test_error_schema import ApiTestApiTestErrorSchema
from ...models.api_test_api_test_success_schema import ApiTestApiTestSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    error: str | Unset = UNSET,
    foo: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["error"] = error

    params["foo"] = foo


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api.test",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema:
    if response.status_code == 200:
        response_200 = ApiTestApiTestSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ApiTestApiTestErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    foo: str | Unset = UNSET,

) -> Response[ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema]:
    """  Checks API calling code.

    Args:
        error (str | Unset):
        foo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema]
     """


    kwargs = _get_kwargs(
        error=error,
foo=foo,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    foo: str | Unset = UNSET,

) -> ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema | None:
    """  Checks API calling code.

    Args:
        error (str | Unset):
        foo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema
     """


    return sync_detailed(
        client=client,
error=error,
foo=foo,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    foo: str | Unset = UNSET,

) -> Response[ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema]:
    """  Checks API calling code.

    Args:
        error (str | Unset):
        foo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema]
     """


    kwargs = _get_kwargs(
        error=error,
foo=foo,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    error: str | Unset = UNSET,
    foo: str | Unset = UNSET,

) -> ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema | None:
    """  Checks API calling code.

    Args:
        error (str | Unset):
        foo (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTestApiTestErrorSchema | ApiTestApiTestSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
error=error,
foo=foo,

    )).parsed
