from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_set_photo_data_body import UsersSetPhotoDataBody
from ...models.users_set_photo_json_body import UsersSetPhotoJsonBody
from ...models.users_set_photo_users_set_photo_error_schema import UsersSetPhotoUsersSetPhotoErrorSchema
from ...models.users_set_photo_users_set_photo_schema import UsersSetPhotoUsersSetPhotoSchema
from typing import cast



def _get_kwargs(
    *,
    body:    UsersSetPhotoDataBody  |     UsersSetPhotoJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users.setPhoto",
    }

    if isinstance(body, UsersSetPhotoDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsersSetPhotoJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema:
    if response.status_code == 200:
        response_200 = UsersSetPhotoUsersSetPhotoSchema.from_dict(response.json())



        return response_200

    response_default = UsersSetPhotoUsersSetPhotoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPhotoDataBody  |     UsersSetPhotoJsonBody  | Unset = UNSET,

) -> Response[UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema]:
    """  Set the user profile photo

    Args:
        body (UsersSetPhotoDataBody):
        body (UsersSetPhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPhotoDataBody  |     UsersSetPhotoJsonBody  | Unset = UNSET,

) -> UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema | None:
    """  Set the user profile photo

    Args:
        body (UsersSetPhotoDataBody):
        body (UsersSetPhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPhotoDataBody  |     UsersSetPhotoJsonBody  | Unset = UNSET,

) -> Response[UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema]:
    """  Set the user profile photo

    Args:
        body (UsersSetPhotoDataBody):
        body (UsersSetPhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    UsersSetPhotoDataBody  |     UsersSetPhotoJsonBody  | Unset = UNSET,

) -> UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema | None:
    """  Set the user profile photo

    Args:
        body (UsersSetPhotoDataBody):
        body (UsersSetPhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersSetPhotoUsersSetPhotoErrorSchema | UsersSetPhotoUsersSetPhotoSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
