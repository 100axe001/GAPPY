from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_billable_info_default_error_template import TeamBillableInfoDefaultErrorTemplate
from ...models.team_billable_info_default_success_template import TeamBillableInfoDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    user: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team.billableInfo",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = TeamBillableInfoDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = TeamBillableInfoDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate]:
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
    user: str | Unset = UNSET,

) -> Response[TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate]:
    """  Gets billable users information for the current team.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,

) -> TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate | None:
    """  Gets billable users information for the current team.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,

) -> Response[TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate]:
    """  Gets billable users information for the current team.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
user=user,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    user: str | Unset = UNSET,

) -> TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate | None:
    """  Gets billable users information for the current team.

    Args:
        token (str):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamBillableInfoDefaultErrorTemplate | TeamBillableInfoDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
user=user,

    )).parsed
