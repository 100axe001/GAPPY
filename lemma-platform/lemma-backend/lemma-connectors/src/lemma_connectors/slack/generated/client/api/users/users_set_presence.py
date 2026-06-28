from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_set_presence_data_body import UsersSetPresenceDataBody
from ...models.users_set_presence_json_body import UsersSetPresenceJsonBody
from ...models.users_set_presence_users_set_presence_error_schema import UsersSetPresenceUsersSetPresenceErrorSchema
from ...models.users_set_presence_users_set_presence_schema import UsersSetPresenceUsersSetPresenceSchema
from typing import cast



def _get_kwargs(
    *,
    body:    UsersSetPresenceDataBody  |     UsersSetPresenceJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users.setPresence",
    }

    if isinstance(body, UsersSetPresenceDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsersSetPresenceJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema:
    if response.status_code == 200:
        response_200 = UsersSetPresenceUsersSetPresenceSchema.from_dict(response.json())



        return response_200

    response_default = UsersSetPresenceUsersSetPresenceErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPresenceDataBody  |     UsersSetPresenceJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema]:
    """  Manually sets user presence.

    Args:
        token (str):
        body (UsersSetPresenceDataBody):
        body (UsersSetPresenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPresenceDataBody  |     UsersSetPresenceJsonBody  | Unset = UNSET,
    token: str,

) -> UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema | None:
    """  Manually sets user presence.

    Args:
        token (str):
        body (UsersSetPresenceDataBody):
        body (UsersSetPresenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPresenceDataBody  |     UsersSetPresenceJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema]:
    """  Manually sets user presence.

    Args:
        token (str):
        body (UsersSetPresenceDataBody):
        body (UsersSetPresenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPresenceDataBody  |     UsersSetPresenceJsonBody  | Unset = UNSET,
    token: str,

) -> UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema | None:
    """  Manually sets user presence.

    Args:
        token (str):
        body (UsersSetPresenceDataBody):
        body (UsersSetPresenceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersSetPresenceUsersSetPresenceErrorSchema | UsersSetPresenceUsersSetPresenceSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
