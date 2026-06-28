from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.users_delete_photo_data_body import UsersDeletePhotoDataBody
from ...models.users_delete_photo_json_body import UsersDeletePhotoJsonBody
from ...models.users_delete_photo_users_delete_photo_error_schema import UsersDeletePhotoUsersDeletePhotoErrorSchema
from ...models.users_delete_photo_users_delete_photo_schema import UsersDeletePhotoUsersDeletePhotoSchema
from typing import cast



def _get_kwargs(
    *,
    body:    UsersDeletePhotoDataBody  |     UsersDeletePhotoJsonBody  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users.deletePhoto",
    }

    if isinstance(body, UsersDeletePhotoDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsersDeletePhotoJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema:
    if response.status_code == 200:
        response_200 = UsersDeletePhotoUsersDeletePhotoSchema.from_dict(response.json())



        return response_200

    response_default = UsersDeletePhotoUsersDeletePhotoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersDeletePhotoDataBody  |     UsersDeletePhotoJsonBody  | Unset = UNSET,

) -> Response[UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema]:
    """  Delete the user profile photo

    Args:
        body (UsersDeletePhotoDataBody):
        body (UsersDeletePhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema]
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
    body:    UsersDeletePhotoDataBody  |     UsersDeletePhotoJsonBody  | Unset = UNSET,

) -> UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema | None:
    """  Delete the user profile photo

    Args:
        body (UsersDeletePhotoDataBody):
        body (UsersDeletePhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsersDeletePhotoDataBody  |     UsersDeletePhotoJsonBody  | Unset = UNSET,

) -> Response[UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema]:
    """  Delete the user profile photo

    Args:
        body (UsersDeletePhotoDataBody):
        body (UsersDeletePhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema]
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
    body:    UsersDeletePhotoDataBody  |     UsersDeletePhotoJsonBody  | Unset = UNSET,

) -> UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema | None:
    """  Delete the user profile photo

    Args:
        body (UsersDeletePhotoDataBody):
        body (UsersDeletePhotoJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsersDeletePhotoUsersDeletePhotoErrorSchema | UsersDeletePhotoUsersDeletePhotoSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
