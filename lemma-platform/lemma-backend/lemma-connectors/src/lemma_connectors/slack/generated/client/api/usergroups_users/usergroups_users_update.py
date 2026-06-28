from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.usergroups_users_update_data_body import UsergroupsUsersUpdateDataBody
from ...models.usergroups_users_update_json_body import UsergroupsUsersUpdateJsonBody
from ...models.usergroups_users_update_usergroups_users_update_error_schema import UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema
from ...models.usergroups_users_update_usergroups_users_update_schema import UsergroupsUsersUpdateUsergroupsUsersUpdateSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    UsergroupsUsersUpdateDataBody  |     UsergroupsUsersUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/usergroups.users.update",
    }

    if isinstance(body, UsergroupsUsersUpdateDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsergroupsUsersUpdateJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema:
    if response.status_code == 200:
        response_200 = UsergroupsUsersUpdateUsergroupsUsersUpdateSchema.from_dict(response.json())



        return response_200

    response_default = UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsUsersUpdateDataBody  |     UsergroupsUsersUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema]:
    """  Update the list of users for a User Group

    Args:
        token (str):
        body (UsergroupsUsersUpdateDataBody | Unset):
        body (UsergroupsUsersUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema]
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
    body:    UsergroupsUsersUpdateDataBody  |     UsergroupsUsersUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema | None:
    """  Update the list of users for a User Group

    Args:
        token (str):
        body (UsergroupsUsersUpdateDataBody | Unset):
        body (UsergroupsUsersUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsUsersUpdateDataBody  |     UsergroupsUsersUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema]:
    """  Update the list of users for a User Group

    Args:
        token (str):
        body (UsergroupsUsersUpdateDataBody | Unset):
        body (UsergroupsUsersUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema]
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
    body:    UsergroupsUsersUpdateDataBody  |     UsergroupsUsersUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema | None:
    """  Update the list of users for a User Group

    Args:
        token (str):
        body (UsergroupsUsersUpdateDataBody | Unset):
        body (UsergroupsUsersUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsUsersUpdateUsergroupsUsersUpdateErrorSchema | UsergroupsUsersUpdateUsergroupsUsersUpdateSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
