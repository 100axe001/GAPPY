from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_access_logs_team_access_logs_error_schema import TeamAccessLogsTeamAccessLogsErrorSchema
from ...models.team_access_logs_team_access_logs_schema import TeamAccessLogsTeamAccessLogsSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    before: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["before"] = before

    params["count"] = count

    params["page"] = page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team.accessLogs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema:
    if response.status_code == 200:
        response_200 = TeamAccessLogsTeamAccessLogsSchema.from_dict(response.json())



        return response_200

    response_default = TeamAccessLogsTeamAccessLogsErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema]:
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
    before: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,

) -> Response[TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema]:
    """  Gets the access logs for the current team.

    Args:
        token (str):
        before (str | Unset):
        count (str | Unset):
        page (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema]
     """


    kwargs = _get_kwargs(
        token=token,
before=before,
count=count,
page=page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    before: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,

) -> TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema | None:
    """  Gets the access logs for the current team.

    Args:
        token (str):
        before (str | Unset):
        count (str | Unset):
        page (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema
     """


    return sync_detailed(
        client=client,
token=token,
before=before,
count=count,
page=page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    before: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,

) -> Response[TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema]:
    """  Gets the access logs for the current team.

    Args:
        token (str):
        before (str | Unset):
        count (str | Unset):
        page (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema]
     """


    kwargs = _get_kwargs(
        token=token,
before=before,
count=count,
page=page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    before: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,

) -> TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema | None:
    """  Gets the access logs for the current team.

    Args:
        token (str):
        before (str | Unset):
        count (str | Unset):
        page (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamAccessLogsTeamAccessLogsErrorSchema | TeamAccessLogsTeamAccessLogsSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
before=before,
count=count,
page=page,

    )).parsed
