from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_integration_logs_team_integration_logs_error_schema import TeamIntegrationLogsTeamIntegrationLogsErrorSchema
from ...models.team_integration_logs_team_integration_logs_schema import TeamIntegrationLogsTeamIntegrationLogsSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    app_id: str | Unset = UNSET,
    change_type: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    user: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["app_id"] = app_id

    params["change_type"] = change_type

    params["count"] = count

    params["page"] = page

    params["service_id"] = service_id

    params["user"] = user


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team.integrationLogs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema:
    if response.status_code == 200:
        response_200 = TeamIntegrationLogsTeamIntegrationLogsSchema.from_dict(response.json())



        return response_200

    response_default = TeamIntegrationLogsTeamIntegrationLogsErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema]:
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
    app_id: str | Unset = UNSET,
    change_type: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema]:
    """  Gets the integration logs for the current team.

    Args:
        token (str):
        app_id (str | Unset):
        change_type (str | Unset):
        count (str | Unset):
        page (str | Unset):
        service_id (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema]
     """


    kwargs = _get_kwargs(
        token=token,
app_id=app_id,
change_type=change_type,
count=count,
page=page,
service_id=service_id,
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
    app_id: str | Unset = UNSET,
    change_type: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    user: str | Unset = UNSET,

) -> TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema | None:
    """  Gets the integration logs for the current team.

    Args:
        token (str):
        app_id (str | Unset):
        change_type (str | Unset):
        count (str | Unset):
        page (str | Unset):
        service_id (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema
     """


    return sync_detailed(
        client=client,
token=token,
app_id=app_id,
change_type=change_type,
count=count,
page=page,
service_id=service_id,
user=user,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    app_id: str | Unset = UNSET,
    change_type: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    user: str | Unset = UNSET,

) -> Response[TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema]:
    """  Gets the integration logs for the current team.

    Args:
        token (str):
        app_id (str | Unset):
        change_type (str | Unset):
        count (str | Unset):
        page (str | Unset):
        service_id (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema]
     """


    kwargs = _get_kwargs(
        token=token,
app_id=app_id,
change_type=change_type,
count=count,
page=page,
service_id=service_id,
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
    app_id: str | Unset = UNSET,
    change_type: str | Unset = UNSET,
    count: str | Unset = UNSET,
    page: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    user: str | Unset = UNSET,

) -> TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema | None:
    """  Gets the integration logs for the current team.

    Args:
        token (str):
        app_id (str | Unset):
        change_type (str | Unset):
        count (str | Unset):
        page (str | Unset):
        service_id (str | Unset):
        user (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIntegrationLogsTeamIntegrationLogsErrorSchema | TeamIntegrationLogsTeamIntegrationLogsSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
app_id=app_id,
change_type=change_type,
count=count,
page=page,
service_id=service_id,
user=user,

    )).parsed
