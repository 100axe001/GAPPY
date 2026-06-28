from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.views_update_default_error_template import ViewsUpdateDefaultErrorTemplate
from ...models.views_update_default_success_template import ViewsUpdateDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    view_id: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    view: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["view_id"] = view_id

    params["external_id"] = external_id

    params["view"] = view

    params["hash"] = hash_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/views.update",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = ViewsUpdateDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = ViewsUpdateDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    view_id: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    view: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    token: str,

) -> Response[ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate]:
    """  Update an existing view.

    Args:
        view_id (str | Unset):
        external_id (str | Unset):
        view (str | Unset):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        view_id=view_id,
external_id=external_id,
view=view,
hash_=hash_,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    view_id: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    view: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    token: str,

) -> ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate | None:
    """  Update an existing view.

    Args:
        view_id (str | Unset):
        external_id (str | Unset):
        view (str | Unset):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
view_id=view_id,
external_id=external_id,
view=view,
hash_=hash_,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    view_id: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    view: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    token: str,

) -> Response[ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate]:
    """  Update an existing view.

    Args:
        view_id (str | Unset):
        external_id (str | Unset):
        view (str | Unset):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        view_id=view_id,
external_id=external_id,
view=view,
hash_=hash_,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    view_id: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    view: str | Unset = UNSET,
    hash_: str | Unset = UNSET,
    token: str,

) -> ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate | None:
    """  Update an existing view.

    Args:
        view_id (str | Unset):
        external_id (str | Unset):
        view (str | Unset):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsUpdateDefaultErrorTemplate | ViewsUpdateDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
view_id=view_id,
external_id=external_id,
view=view,
hash_=hash_,
token=token,

    )).parsed
