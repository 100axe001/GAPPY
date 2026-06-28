from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reactions_add_data_body import ReactionsAddDataBody
from ...models.reactions_add_json_body import ReactionsAddJsonBody
from ...models.reactions_add_reactions_add_error_schema import ReactionsAddReactionsAddErrorSchema
from ...models.reactions_add_reactions_add_schema import ReactionsAddReactionsAddSchema
from typing import cast



def _get_kwargs(
    *,
    body:    ReactionsAddDataBody  |     ReactionsAddJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reactions.add",
    }

    if isinstance(body, ReactionsAddDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ReactionsAddJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema:
    if response.status_code == 200:
        response_200 = ReactionsAddReactionsAddSchema.from_dict(response.json())



        return response_200

    response_default = ReactionsAddReactionsAddErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ReactionsAddDataBody  |     ReactionsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema]:
    """  Adds a reaction to an item.

    Args:
        token (str):
        body (ReactionsAddDataBody):
        body (ReactionsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema]
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
    body:    ReactionsAddDataBody  |     ReactionsAddJsonBody  | Unset = UNSET,
    token: str,

) -> ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema | None:
    """  Adds a reaction to an item.

    Args:
        token (str):
        body (ReactionsAddDataBody):
        body (ReactionsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ReactionsAddDataBody  |     ReactionsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema]:
    """  Adds a reaction to an item.

    Args:
        token (str):
        body (ReactionsAddDataBody):
        body (ReactionsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema]
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
    body:    ReactionsAddDataBody  |     ReactionsAddJsonBody  | Unset = UNSET,
    token: str,

) -> ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema | None:
    """  Adds a reaction to an item.

    Args:
        token (str):
        body (ReactionsAddDataBody):
        body (ReactionsAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsAddReactionsAddErrorSchema | ReactionsAddReactionsAddSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
