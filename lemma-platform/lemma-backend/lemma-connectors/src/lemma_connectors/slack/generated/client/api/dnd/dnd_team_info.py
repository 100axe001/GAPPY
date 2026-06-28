from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dnd_team_info_default_error_template import DndTeamInfoDefaultErrorTemplate
from ...models.dnd_team_info_default_success_template import DndTeamInfoDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    users: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["users"] = users


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dnd.teamInfo",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = DndTeamInfoDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = DndTeamInfoDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    users: str | Unset = UNSET,

) -> Response[DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate]:
    """  Retrieves the Do Not Disturb status for up to 50 users on a team.

    Args:
        token (str | Unset):
        users (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
users=users,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    users: str | Unset = UNSET,

) -> DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate | None:
    """  Retrieves the Do Not Disturb status for up to 50 users on a team.

    Args:
        token (str | Unset):
        users (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
token=token,
users=users,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    users: str | Unset = UNSET,

) -> Response[DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate]:
    """  Retrieves the Do Not Disturb status for up to 50 users on a team.

    Args:
        token (str | Unset):
        users (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        token=token,
users=users,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    users: str | Unset = UNSET,

) -> DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate | None:
    """  Retrieves the Do Not Disturb status for up to 50 users on a team.

    Args:
        token (str | Unset):
        users (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DndTeamInfoDefaultErrorTemplate | DndTeamInfoDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
token=token,
users=users,

    )).parsed
