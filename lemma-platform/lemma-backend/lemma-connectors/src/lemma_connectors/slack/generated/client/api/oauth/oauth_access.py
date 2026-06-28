from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.oauth_access_default_error_template import OauthAccessDefaultErrorTemplate
from ...models.oauth_access_default_success_template import OauthAccessDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,
    code: str | Unset = UNSET,
    redirect_uri: str | Unset = UNSET,
    single_channel: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["client_secret"] = client_secret

    params["code"] = code

    params["redirect_uri"] = redirect_uri

    params["single_channel"] = single_channel


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth.access",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = OauthAccessDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = OauthAccessDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,
    code: str | Unset = UNSET,
    redirect_uri: str | Unset = UNSET,
    single_channel: bool | Unset = UNSET,

) -> Response[OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate]:
    """  Exchanges a temporary OAuth verifier code for an access token.

    Args:
        client_id (str | Unset):
        client_secret (str | Unset):
        code (str | Unset):
        redirect_uri (str | Unset):
        single_channel (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
client_secret=client_secret,
code=code,
redirect_uri=redirect_uri,
single_channel=single_channel,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,
    code: str | Unset = UNSET,
    redirect_uri: str | Unset = UNSET,
    single_channel: bool | Unset = UNSET,

) -> OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate | None:
    """  Exchanges a temporary OAuth verifier code for an access token.

    Args:
        client_id (str | Unset):
        client_secret (str | Unset):
        code (str | Unset):
        redirect_uri (str | Unset):
        single_channel (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
client_id=client_id,
client_secret=client_secret,
code=code,
redirect_uri=redirect_uri,
single_channel=single_channel,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,
    code: str | Unset = UNSET,
    redirect_uri: str | Unset = UNSET,
    single_channel: bool | Unset = UNSET,

) -> Response[OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate]:
    """  Exchanges a temporary OAuth verifier code for an access token.

    Args:
        client_id (str | Unset):
        client_secret (str | Unset):
        code (str | Unset):
        redirect_uri (str | Unset):
        single_channel (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
client_secret=client_secret,
code=code,
redirect_uri=redirect_uri,
single_channel=single_channel,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    client_id: str | Unset = UNSET,
    client_secret: str | Unset = UNSET,
    code: str | Unset = UNSET,
    redirect_uri: str | Unset = UNSET,
    single_channel: bool | Unset = UNSET,

) -> OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate | None:
    """  Exchanges a temporary OAuth verifier code for an access token.

    Args:
        client_id (str | Unset):
        client_secret (str | Unset):
        code (str | Unset):
        redirect_uri (str | Unset):
        single_channel (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OauthAccessDefaultErrorTemplate | OauthAccessDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
client_id=client_id,
client_secret=client_secret,
code=code,
redirect_uri=redirect_uri,
single_channel=single_channel,

    )).parsed
