from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_string import PageBeanString
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 1000,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/label",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageBeanString | None:
    if response.status_code == 200:
        response_200 = PageBeanString.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageBeanString]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 1000,

) -> Response[PageBeanString]:
    """ Get all labels

     Returns a [paginated](#pagination) list of labels.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBeanString]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 1000,

) -> PageBeanString | None:
    """ Get all labels

     Returns a [paginated](#pagination) list of labels.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBeanString
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 1000,

) -> Response[PageBeanString]:
    """ Get all labels

     Returns a [paginated](#pagination) list of labels.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBeanString]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 1000,

) -> PageBeanString | None:
    """ Get all labels

     Returns a [paginated](#pagination) list of labels.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBeanString
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
