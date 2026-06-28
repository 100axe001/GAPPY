from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reactions_list_reactions_list_error_schema import ReactionsListReactionsListErrorSchema
from ...models.reactions_list_reactions_list_schema import ReactionsListReactionsListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    user: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    count: int | Unset = UNSET,
    page: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["user"] = user

    params["full"] = full

    params["count"] = count

    params["page"] = page

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reactions.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema:
    if response.status_code == 200:
        response_200 = ReactionsListReactionsListSchema.from_dict(response.json())



        return response_200

    response_default = ReactionsListReactionsListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema]:
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
    user: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    count: int | Unset = UNSET,
    page: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema]:
    """  Lists reactions made by a user.

    Args:
        token (str):
        user (str | Unset):
        full (bool | Unset):
        count (int | Unset):
        page (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
full=full,
count=count,
page=page,
cursor=cursor,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    count: int | Unset = UNSET,
    page: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema | None:
    """  Lists reactions made by a user.

    Args:
        token (str):
        user (str | Unset):
        full (bool | Unset):
        count (int | Unset):
        page (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema
     """


    return sync_detailed(
        client=client,
token=token,
user=user,
full=full,
count=count,
page=page,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    count: int | Unset = UNSET,
    page: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema]:
    """  Lists reactions made by a user.

    Args:
        token (str):
        user (str | Unset):
        full (bool | Unset):
        count (int | Unset):
        page (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,
full=full,
count=count,
page=page,
cursor=cursor,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,
    full: bool | Unset = UNSET,
    count: int | Unset = UNSET,
    page: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema | None:
    """  Lists reactions made by a user.

    Args:
        token (str):
        user (str | Unset):
        full (bool | Unset):
        count (int | Unset):
        page (int | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReactionsListReactionsListErrorSchema | ReactionsListReactionsListSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
user=user,
full=full,
count=count,
page=page,
cursor=cursor,
limit=limit,

    )).parsed
