from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apps_event_authorizations_list_default_error_template import AppsEventAuthorizationsListDefaultErrorTemplate
from ...models.apps_event_authorizations_list_default_success_template import AppsEventAuthorizationsListDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    event_context: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["event_context"] = event_context

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/apps.event.authorizations.list",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = AppsEventAuthorizationsListDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = AppsEventAuthorizationsListDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    event_context: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    token: str,

) -> Response[AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate]:
    """  Get a list of authorizations for the given event context. Each authorization represents an app
    installation that the event is visible to.

    Args:
        event_context (str):
        cursor (str | Unset):
        limit (int | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        event_context=event_context,
cursor=cursor,
limit=limit,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    event_context: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    token: str,

) -> AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate | None:
    """  Get a list of authorizations for the given event context. Each authorization represents an app
    installation that the event is visible to.

    Args:
        event_context (str):
        cursor (str | Unset):
        limit (int | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
event_context=event_context,
cursor=cursor,
limit=limit,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    event_context: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    token: str,

) -> Response[AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate]:
    """  Get a list of authorizations for the given event context. Each authorization represents an app
    installation that the event is visible to.

    Args:
        event_context (str):
        cursor (str | Unset):
        limit (int | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        event_context=event_context,
cursor=cursor,
limit=limit,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    event_context: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    token: str,

) -> AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate | None:
    """  Get a list of authorizations for the given event context. Each authorization represents an app
    installation that the event is visible to.

    Args:
        event_context (str):
        cursor (str | Unset):
        limit (int | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppsEventAuthorizationsListDefaultErrorTemplate | AppsEventAuthorizationsListDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
event_context=event_context,
cursor=cursor,
limit=limit,
token=token,

    )).parsed
