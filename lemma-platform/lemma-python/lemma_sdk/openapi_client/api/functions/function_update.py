from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.function_action_response import FunctionActionResponse
from ...models.update_function_request import UpdateFunctionRequest
from ...types import Response


def _get_kwargs(
    pod_id: UUID,
    function_name: str,
    *,
    body: UpdateFunctionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/pods/{pod_id}/functions/{function_name}".format(
            pod_id=quote(str(pod_id), safe=""),
            function_name=quote(str(function_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | FunctionActionResponse | None:
    if response.status_code == 200:
        response_200 = FunctionActionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | FunctionActionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    function_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFunctionRequest,
) -> Response[ErrorResponse | FunctionActionResponse]:
    """Update Function

     Update a function. When code is supplied, the platform re-derives the function input_schema and
    output_schema and returns the refreshed function.

    Args:
        pod_id (UUID):
        function_name (str):
        body (UpdateFunctionRequest): Request to update a function.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FunctionActionResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        function_name=function_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    function_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFunctionRequest,
) -> ErrorResponse | FunctionActionResponse | None:
    """Update Function

     Update a function. When code is supplied, the platform re-derives the function input_schema and
    output_schema and returns the refreshed function.

    Args:
        pod_id (UUID):
        function_name (str):
        body (UpdateFunctionRequest): Request to update a function.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FunctionActionResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        function_name=function_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    function_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFunctionRequest,
) -> Response[ErrorResponse | FunctionActionResponse]:
    """Update Function

     Update a function. When code is supplied, the platform re-derives the function input_schema and
    output_schema and returns the refreshed function.

    Args:
        pod_id (UUID):
        function_name (str):
        body (UpdateFunctionRequest): Request to update a function.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FunctionActionResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        function_name=function_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    function_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFunctionRequest,
) -> ErrorResponse | FunctionActionResponse | None:
    """Update Function

     Update a function. When code is supplied, the platform re-derives the function input_schema and
    output_schema and returns the refreshed function.

    Args:
        pod_id (UUID):
        function_name (str):
        body (UpdateFunctionRequest): Request to update a function.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FunctionActionResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            function_name=function_name,
            client=client,
            body=body,
        )
    ).parsed
