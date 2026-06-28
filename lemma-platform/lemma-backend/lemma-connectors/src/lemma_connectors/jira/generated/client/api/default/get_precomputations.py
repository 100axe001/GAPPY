from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_jql_function_precomputation_bean import PageBeanJqlFunctionPrecomputationBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    function_key: list[str] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_function_key: list[str] | Unset = UNSET
    if not isinstance(function_key, Unset):
        json_function_key = function_key


    params["functionKey"] = json_function_key

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["orderBy"] = order_by

    params["filter"] = filter_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/jql/function/computation",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageBeanJqlFunctionPrecomputationBean | None:
    if response.status_code == 200:
        response_200 = PageBeanJqlFunctionPrecomputationBean.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageBeanJqlFunctionPrecomputationBean]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    function_key: list[str] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,

) -> Response[PageBeanJqlFunctionPrecomputationBean]:
    """ Get precomputation

    Args:
        function_key (list[str] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBeanJqlFunctionPrecomputationBean]
     """


    kwargs = _get_kwargs(
        function_key=function_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
filter_=filter_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    function_key: list[str] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,

) -> PageBeanJqlFunctionPrecomputationBean | None:
    """ Get precomputation

    Args:
        function_key (list[str] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBeanJqlFunctionPrecomputationBean
     """


    return sync_detailed(
        client=client,
function_key=function_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
filter_=filter_,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    function_key: list[str] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,

) -> Response[PageBeanJqlFunctionPrecomputationBean]:
    """ Get precomputation

    Args:
        function_key (list[str] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBeanJqlFunctionPrecomputationBean]
     """


    kwargs = _get_kwargs(
        function_key=function_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
filter_=filter_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    function_key: list[str] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 5000,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,

) -> PageBeanJqlFunctionPrecomputationBean | None:
    """ Get precomputation

    Args:
        function_key (list[str] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 5000.
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBeanJqlFunctionPrecomputationBean
     """


    return (await asyncio_detailed(
        client=client,
function_key=function_key,
start_at=start_at,
max_results=max_results,
order_by=order_by,
filter_=filter_,

    )).parsed
