from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bots_info_bots_info_error_schema import BotsInfoBotsInfoErrorSchema
from ...models.bots_info_bots_info_schema import BotsInfoBotsInfoSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str,
    bot: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["bot"] = bot


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/bots.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema:
    if response.status_code == 200:
        response_200 = BotsInfoBotsInfoSchema.from_dict(response.json())



        return response_200

    response_default = BotsInfoBotsInfoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema]:
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
    bot: str | Unset = UNSET,

) -> Response[BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema]:
    """  Gets information about a bot user.

    Args:
        token (str):
        bot (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
bot=bot,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str,
    bot: str | Unset = UNSET,

) -> BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema | None:
    """  Gets information about a bot user.

    Args:
        token (str):
        bot (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema
     """


    return sync_detailed(
        client=client,
token=token,
bot=bot,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    bot: str | Unset = UNSET,

) -> Response[BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema]:
    """  Gets information about a bot user.

    Args:
        token (str):
        bot (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
bot=bot,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    bot: str | Unset = UNSET,

) -> BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema | None:
    """  Gets information about a bot user.

    Args:
        token (str):
        bot (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsInfoBotsInfoErrorSchema | BotsInfoBotsInfoSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
bot=bot,

    )).parsed
