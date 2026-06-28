from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.filter_ import Filter
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: Filter,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand

    params["overrideSharePermissions"] = override_share_permissions


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/filter",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Filter | None:
    if response.status_code == 200:
        response_200 = Filter.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Filter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Filter,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Response[Any | Filter]:
    """ Create filter

     Creates a filter. The filter is shared according to the [default share scope](#api-rest-
    api-3-filter-post). The filter is not selected as a favorite.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.
        body (Filter): Details about a filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Filter]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,
override_share_permissions=override_share_permissions,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: Filter,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Any | Filter | None:
    """ Create filter

     Creates a filter. The filter is shared according to the [default share scope](#api-rest-
    api-3-filter-post). The filter is not selected as a favorite.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.
        body (Filter): Details about a filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Filter
     """


    return sync_detailed(
        client=client,
body=body,
expand=expand,
override_share_permissions=override_share_permissions,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Filter,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Response[Any | Filter]:
    """ Create filter

     Creates a filter. The filter is shared according to the [default share scope](#api-rest-
    api-3-filter-post). The filter is not selected as a favorite.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.
        body (Filter): Details about a filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Filter]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,
override_share_permissions=override_share_permissions,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Filter,
    expand: str | Unset = UNSET,
    override_share_permissions: bool | Unset = False,

) -> Any | Filter | None:
    """ Create filter

     Creates a filter. The filter is shared according to the [default share scope](#api-rest-
    api-3-filter-post). The filter is not selected as a favorite.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        expand (str | Unset):
        override_share_permissions (bool | Unset):  Default: False.
        body (Filter): Details about a filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Filter
     """


    return (await asyncio_detailed(
        client=client,
body=body,
expand=expand,
override_share_permissions=override_share_permissions,

    )).parsed
