from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reactions_remove_data_body import ReactionsRemoveDataBody
from ...models.reactions_remove_json_body import ReactionsRemoveJsonBody
from ...models.reactions_remove_reactions_remove_error_schema import ReactionsRemoveReactionsRemoveErrorSchema
from ...models.reactions_remove_reactions_remove_schema import ReactionsRemoveReactionsRemoveSchema
from typing import cast



def _get_kwargs(
    *,
    body:    ReactionsRemoveDataBody  |     ReactionsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reactions.remove",
    }

    if isinstance(body, ReactionsRemoveDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ReactionsRemoveJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema:
    if response.status_code == 200:
        response_200 = ReactionsRemoveReactionsRemoveSchema.from_dict(response.json())



        return response_200

    response_default = ReactionsRemoveReactionsRemoveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ReactionsRemoveDataBody  |     ReactionsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema]:
    """  Removes a reaction from an item.

    Args:
        token (str):
        body (ReactionsRemoveDataBody):
        body (ReactionsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    ReactionsRemoveDataBody  |     ReactionsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema | None:
    """  Removes a reaction from an item.

    Args:
        token (str):
        body (ReactionsRemoveDataBody):
        body (ReactionsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ReactionsRemoveDataBody  |     ReactionsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema]:
    """  Removes a reaction from an item.

    Args:
        token (str):
        body (ReactionsRemoveDataBody):
        body (ReactionsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    ReactionsRemoveDataBody  |     ReactionsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema | None:
    """  Removes a reaction from an item.

    Args:
        token (str):
        body (ReactionsRemoveDataBody):
        body (ReactionsRemoveJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsRemoveReactionsRemoveErrorSchema | ReactionsRemoveReactionsRemoveSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
