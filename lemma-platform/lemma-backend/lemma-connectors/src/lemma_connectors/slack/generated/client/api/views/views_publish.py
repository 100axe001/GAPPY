from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.views_publish_default_error_template import ViewsPublishDefaultErrorTemplate
from ...models.views_publish_default_success_template import ViewsPublishDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    user_id: str,
    view: str,
    hash_: str | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["view"] = view

    params["hash"] = hash_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/views.publish",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = ViewsPublishDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = ViewsPublishDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    view: str,
    hash_: str | Unset = UNSET,
    token: str,

) -> Response[ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate]:
    """  Publish a static view for a User.

    Args:
        user_id (str):
        view (str):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: str,
    view: str,
    hash_: str | Unset = UNSET,
    token: str,

) -> ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate | None:
    """  Publish a static view for a User.

    Args:
        user_id (str):
        view (str):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
user_id=user_id,
view=view,
hash_=hash_,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    view: str,
    hash_: str | Unset = UNSET,
    token: str,

) -> Response[ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate]:
    """  Publish a static view for a User.

    Args:
        user_id (str):
        view (str):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: str,
    view: str,
    hash_: str | Unset = UNSET,
    token: str,

) -> ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate | None:
    """  Publish a static view for a User.

    Args:
        user_id (str):
        view (str):
        hash_ (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsPublishDefaultErrorTemplate | ViewsPublishDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
user_id=user_id,
view=view,
hash_=hash_,
token=token,

    )).parsed
