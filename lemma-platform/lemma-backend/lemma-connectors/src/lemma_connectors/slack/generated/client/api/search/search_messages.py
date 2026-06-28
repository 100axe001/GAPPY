from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_messages_default_error_template import SearchMessagesDefaultErrorTemplate
from ...models.search_messages_default_success_template import SearchMessagesDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    count: int | Unset = UNSET,
    highlight: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["count"] = count

    params["highlight"] = highlight

    params["page"] = page

    params["query"] = query

    params["sort"] = sort

    params["sort_dir"] = sort_dir


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search.messages",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = SearchMessagesDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = SearchMessagesDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate]:
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
    count: int | Unset = UNSET,
    highlight: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate]:
    """  Searches for messages matching a query.

    Args:
        token (str):
        count (int | Unset):
        highlight (bool | Unset):
        page (int | Unset):
        query (str):
        sort (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
count=count,
highlight=highlight,
page=page,
query=query,
sort=sort,
sort_dir=sort_dir,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    count: int | Unset = UNSET,
    highlight: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate | None:
    """  Searches for messages matching a query.

    Args:
        token (str):
        count (int | Unset):
        highlight (bool | Unset):
        page (int | Unset):
        query (str):
        sort (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
count=count,
highlight=highlight,
page=page,
query=query,
sort=sort,
sort_dir=sort_dir,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    count: int | Unset = UNSET,
    highlight: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> Response[SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate]:
    """  Searches for messages matching a query.

    Args:
        token (str):
        count (int | Unset):
        highlight (bool | Unset):
        page (int | Unset):
        query (str):
        sort (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
count=count,
highlight=highlight,
page=page,
query=query,
sort=sort,
sort_dir=sort_dir,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    count: int | Unset = UNSET,
    highlight: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    query: str,
    sort: str | Unset = UNSET,
    sort_dir: str | Unset = UNSET,

) -> SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate | None:
    """  Searches for messages matching a query.

    Args:
        token (str):
        count (int | Unset):
        highlight (bool | Unset):
        page (int | Unset):
        query (str):
        sort (str | Unset):
        sort_dir (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchMessagesDefaultErrorTemplate | SearchMessagesDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
count=count,
highlight=highlight,
page=page,
query=query,
sort=sort,
sort_dir=sort_dir,

    )).parsed
