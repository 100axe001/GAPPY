from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_context import PageBeanContext
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/{field_id}/contexts".format(field_id=quote(str(field_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanContext | None:
    if response.status_code == 200:
        response_200 = PageBeanContext.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanContext]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Response[Any | PageBeanContext]:
    """ Get contexts for a field

     Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get
    custom field contexts](#api-rest-api-3-field-fieldId-context-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContext]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Any | PageBeanContext | None:
    """ Get contexts for a field

     Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get
    custom field contexts](#api-rest-api-3-field-fieldId-context-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContext
     """


    return sync_detailed(
        field_id=field_id,
client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Response[Any | PageBeanContext]:
    """ Get contexts for a field

     Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get
    custom field contexts](#api-rest-api-3-field-fieldId-context-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContext]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 20,

) -> Any | PageBeanContext | None:
    """ Get contexts for a field

     Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get
    custom field contexts](#api-rest-api-3-field-fieldId-context-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContext
     """


    return (await asyncio_detailed(
        field_id=field_id,
client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
