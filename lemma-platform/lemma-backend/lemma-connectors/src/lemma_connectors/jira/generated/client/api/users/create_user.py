from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.new_user_details import NewUserDetails
from ...models.user import User
from typing import cast



def _get_kwargs(
    *,
    body: NewUserDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/user",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | User | None:
    if response.status_code == 201:
        response_201 = User.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | User]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewUserDetails,

) -> Response[Any | User]:
    """ Create user

     Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable
    alternative is available this resource will be deprecated.

    If the user exists and has access to Jira, the operation returns a 201 status. If the user exists
    but does not have access to Jira, the operation returns a 400 status.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (NewUserDetails): The user details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
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
    body: NewUserDetails,

) -> Any | User | None:
    """ Create user

     Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable
    alternative is available this resource will be deprecated.

    If the user exists and has access to Jira, the operation returns a 201 status. If the user exists
    but does not have access to Jira, the operation returns a 400 status.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (NewUserDetails): The user details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewUserDetails,

) -> Response[Any | User]:
    """ Create user

     Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable
    alternative is available this resource will be deprecated.

    If the user exists and has access to Jira, the operation returns a 201 status. If the user exists
    but does not have access to Jira, the operation returns a 400 status.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (NewUserDetails): The user details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | User]
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
    body: NewUserDetails,

) -> Any | User | None:
    """ Create user

     Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable
    alternative is available this resource will be deprecated.

    If the user exists and has access to Jira, the operation returns a 201 status. If the user exists
    but does not have access to Jira, the operation returns a 400 status.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (NewUserDetails): The user details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | User
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
