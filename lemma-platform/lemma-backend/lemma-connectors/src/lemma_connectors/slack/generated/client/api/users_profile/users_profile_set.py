from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_profile_set_data_body import UsersProfileSetDataBody
from ...models.users_profile_set_json_body import UsersProfileSetJsonBody
from ...models.users_profile_set_users_profile_set_error_schema import UsersProfileSetUsersProfileSetErrorSchema
from ...models.users_profile_set_users_profile_set_schema import UsersProfileSetUsersProfileSetSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    UsersProfileSetDataBody  |     UsersProfileSetJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users.profile.set",
    }

    if isinstance(body, UsersProfileSetDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsersProfileSetJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema:
    if response.status_code == 200:
        response_200 = UsersProfileSetUsersProfileSetSchema.from_dict(response.json())



        return response_200

    response_default = UsersProfileSetUsersProfileSetErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersProfileSetDataBody  |     UsersProfileSetJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema]:
    """  Set the profile information for a user.

    Args:
        token (str):
        body (UsersProfileSetDataBody | Unset):
        body (UsersProfileSetJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema]
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
    body:    UsersProfileSetDataBody  |     UsersProfileSetJsonBody  | Unset = UNSET,
    token: str,

) -> UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema | None:
    """  Set the profile information for a user.

    Args:
        token (str):
        body (UsersProfileSetDataBody | Unset):
        body (UsersProfileSetJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersProfileSetDataBody  |     UsersProfileSetJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema]:
    """  Set the profile information for a user.

    Args:
        token (str):
        body (UsersProfileSetDataBody | Unset):
        body (UsersProfileSetJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema]
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
    body:    UsersProfileSetDataBody  |     UsersProfileSetJsonBody  | Unset = UNSET,
    token: str,

) -> UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema | None:
    """  Set the profile information for a user.

    Args:
        token (str):
        body (UsersProfileSetDataBody | Unset):
        body (UsersProfileSetJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersProfileSetUsersProfileSetErrorSchema | UsersProfileSetUsersProfileSetSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
