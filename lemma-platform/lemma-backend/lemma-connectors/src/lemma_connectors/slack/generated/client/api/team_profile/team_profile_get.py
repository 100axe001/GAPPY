from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_profile_get_team_profile_get_error_schema import TeamProfileGetTeamProfileGetErrorSchema
from ...models.team_profile_get_team_profile_get_success_schema import TeamProfileGetTeamProfileGetSuccessSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    visibility: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["visibility"] = visibility


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team.profile.get",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema:
    if response.status_code == 200:
        response_200 = TeamProfileGetTeamProfileGetSuccessSchema.from_dict(response.json())



        return response_200

    response_default = TeamProfileGetTeamProfileGetErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema]:
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
    visibility: str | Unset = UNSET,

) -> Response[TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema]:
    """  Retrieve a team's profile.

    Args:
        token (str):
        visibility (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
visibility=visibility,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    visibility: str | Unset = UNSET,

) -> TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema | None:
    """  Retrieve a team's profile.

    Args:
        token (str):
        visibility (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema
     """


    return sync_detailed(
        client=client,
token=token,
visibility=visibility,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    visibility: str | Unset = UNSET,

) -> Response[TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema]:
    """  Retrieve a team's profile.

    Args:
        token (str):
        visibility (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema]
     """


    kwargs = _get_kwargs(
        token=token,
visibility=visibility,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    visibility: str | Unset = UNSET,

) -> TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema | None:
    """  Retrieve a team's profile.

    Args:
        token (str):
        visibility (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamProfileGetTeamProfileGetErrorSchema | TeamProfileGetTeamProfileGetSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
visibility=visibility,

    )).parsed
