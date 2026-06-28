from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stars_list_stars_list_error_schema import StarsListStarsListErrorSchema
from ...models.stars_list_stars_list_schema import StarsListStarsListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["count"] = count

    params["page"] = page

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/stars.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StarsListStarsListErrorSchema | StarsListStarsListSchema:
    if response.status_code == 200:
        response_200 = StarsListStarsListSchema.from_dict(response.json())



        return response_200

    response_default = StarsListStarsListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StarsListStarsListErrorSchema | StarsListStarsListSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[StarsListStarsListErrorSchema | StarsListStarsListSchema]:
    """  Lists stars for a user.

    Args:
        token (str | Unset):
        count (str | Unset):
        page (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsListStarsListErrorSchema | StarsListStarsListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
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
    token: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> StarsListStarsListErrorSchema | StarsListStarsListSchema | None:
    """  Lists stars for a user.

    Args:
        token (str | Unset):
        count (str | Unset):
        page (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsListStarsListErrorSchema | StarsListStarsListSchema
     """


    return sync_detailed(
        client=client,
token=token,
count=count,
page=page,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[StarsListStarsListErrorSchema | StarsListStarsListSchema]:
    """  Lists stars for a user.

    Args:
        token (str | Unset):
        count (str | Unset):
        page (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsListStarsListErrorSchema | StarsListStarsListSchema]
     """


    kwargs = _get_kwargs(
        token=token,
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
    token: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> StarsListStarsListErrorSchema | StarsListStarsListSchema | None:
    """  Lists stars for a user.

    Args:
        token (str | Unset):
        count (str | Unset):
        page (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsListStarsListErrorSchema | StarsListStarsListSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
count=count,
page=page,
cursor=cursor,
limit=limit,

    )).parsed
