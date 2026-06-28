from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.views_open_default_error_template import ViewsOpenDefaultErrorTemplate
from ...models.views_open_default_success_template import ViewsOpenDefaultSuccessTemplate
from typing import cast



def _get_kwargs(
    *,
    trigger_id: str,
    view: str,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["trigger_id"] = trigger_id

    params["view"] = view


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/views.open",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = ViewsOpenDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = ViewsOpenDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    trigger_id: str,
    view: str,
    token: str,

) -> Response[ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate]:
    """  Open a view for a user.

    Args:
        trigger_id (str):
        view (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
view=view,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    trigger_id: str,
    view: str,
    token: str,

) -> ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate | None:
    """  Open a view for a user.

    Args:
        trigger_id (str):
        view (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
trigger_id=trigger_id,
view=view,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    trigger_id: str,
    view: str,
    token: str,

) -> Response[ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate]:
    """  Open a view for a user.

    Args:
        trigger_id (str):
        view (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        trigger_id=trigger_id,
view=view,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    trigger_id: str,
    view: str,
    token: str,

) -> ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate | None:
    """  Open a view for a user.

    Args:
        trigger_id (str):
        view (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ViewsOpenDefaultErrorTemplate | ViewsOpenDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
trigger_id=trigger_id,
view=view,
token=token,

    )).parsed
