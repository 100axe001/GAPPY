from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.migration_exchange_migration_exchange_error_schema import MigrationExchangeMigrationExchangeErrorSchema
from ...models.migration_exchange_migration_exchange_success_schema import MigrationExchangeMigrationExchangeSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    users: str,
    team_id: str | Unset = UNSET,
    to_old: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["users"] = users

    params["team_id"] = team_id

    params["to_old"] = to_old


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/migration.exchange",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema:
    if response.status_code == 200:
        response_200 = MigrationExchangeMigrationExchangeSuccessSchema.from_dict(response.json())



        return response_200

    response_default = MigrationExchangeMigrationExchangeErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema]:
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
    users: str,
    team_id: str | Unset = UNSET,
    to_old: bool | Unset = UNSET,

) -> Response[MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema]:
    """  For Enterprise Grid workspaces, map local user IDs to global user IDs

    Args:
        token (str):
        users (str):
        team_id (str | Unset):
        to_old (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
users=users,
team_id=team_id,
to_old=to_old,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    users: str,
    team_id: str | Unset = UNSET,
    to_old: bool | Unset = UNSET,

) -> MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema | None:
    """  For Enterprise Grid workspaces, map local user IDs to global user IDs

    Args:
        token (str):
        users (str):
        team_id (str | Unset):
        to_old (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
users=users,
team_id=team_id,
to_old=to_old,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    users: str,
    team_id: str | Unset = UNSET,
    to_old: bool | Unset = UNSET,

) -> Response[MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema]:
    """  For Enterprise Grid workspaces, map local user IDs to global user IDs

    Args:
        token (str):
        users (str):
        team_id (str | Unset):
        to_old (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
users=users,
team_id=team_id,
to_old=to_old,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    users: str,
    team_id: str | Unset = UNSET,
    to_old: bool | Unset = UNSET,

) -> MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema | None:
    """  For Enterprise Grid workspaces, map local user IDs to global user IDs

    Args:
        token (str):
        users (str):
        team_id (str | Unset):
        to_old (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MigrationExchangeMigrationExchangeErrorSchema | MigrationExchangeMigrationExchangeSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
users=users,
team_id=team_id,
to_old=to_old,

    )).parsed
