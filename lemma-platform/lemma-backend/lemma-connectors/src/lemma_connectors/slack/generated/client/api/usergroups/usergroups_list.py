from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.usergroups_list_usergroups_list_error_schema import UsergroupsListUsergroupsListErrorSchema
from ...models.usergroups_list_usergroups_list_schema import UsergroupsListUsergroupsListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include_users: bool | Unset = UNSET,
    token: str,
    include_count: bool | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include_users"] = include_users

    params["token"] = token

    params["include_count"] = include_count

    params["include_disabled"] = include_disabled


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/usergroups.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema:
    if response.status_code == 200:
        response_200 = UsergroupsListUsergroupsListSchema.from_dict(response.json())



        return response_200

    response_default = UsergroupsListUsergroupsListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include_users: bool | Unset = UNSET,
    token: str,
    include_count: bool | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,

) -> Response[UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema]:
    """  List all User Groups for a team

    Args:
        include_users (bool | Unset):
        token (str):
        include_count (bool | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema]
     """


    kwargs = _get_kwargs(
        include_users=include_users,
token=token,
include_count=include_count,
include_disabled=include_disabled,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    include_users: bool | Unset = UNSET,
    token: str,
    include_count: bool | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,

) -> UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema | None:
    """  List all User Groups for a team

    Args:
        include_users (bool | Unset):
        token (str):
        include_count (bool | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema
     """


    return sync_detailed(
        client=client,
include_users=include_users,
token=token,
include_count=include_count,
include_disabled=include_disabled,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_users: bool | Unset = UNSET,
    token: str,
    include_count: bool | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,

) -> Response[UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema]:
    """  List all User Groups for a team

    Args:
        include_users (bool | Unset):
        token (str):
        include_count (bool | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema]
     """


    kwargs = _get_kwargs(
        include_users=include_users,
token=token,
include_count=include_count,
include_disabled=include_disabled,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include_users: bool | Unset = UNSET,
    token: str,
    include_count: bool | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,

) -> UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema | None:
    """  List all User Groups for a team

    Args:
        include_users (bool | Unset):
        token (str):
        include_count (bool | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsListUsergroupsListErrorSchema | UsergroupsListUsergroupsListSchema
     """


    return (await asyncio_detailed(
        client=client,
include_users=include_users,
token=token,
include_count=include_count,
include_disabled=include_disabled,

    )).parsed
