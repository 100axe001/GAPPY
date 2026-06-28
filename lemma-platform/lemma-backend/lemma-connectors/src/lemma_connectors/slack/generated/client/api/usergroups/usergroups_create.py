from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.usergroups_create_data_body import UsergroupsCreateDataBody
from ...models.usergroups_create_json_body import UsergroupsCreateJsonBody
from ...models.usergroups_create_usergroups_create_error_schema import UsergroupsCreateUsergroupsCreateErrorSchema
from ...models.usergroups_create_usergroups_create_schema import UsergroupsCreateUsergroupsCreateSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    UsergroupsCreateDataBody  |     UsergroupsCreateJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/usergroups.create",
    }

    if isinstance(body, UsergroupsCreateDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsergroupsCreateJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema:
    if response.status_code == 200:
        response_200 = UsergroupsCreateUsergroupsCreateSchema.from_dict(response.json())



        return response_200

    response_default = UsergroupsCreateUsergroupsCreateErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsCreateDataBody  |     UsergroupsCreateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema]:
    """  Create a User Group

    Args:
        token (str):
        body (UsergroupsCreateDataBody | Unset):
        body (UsergroupsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema]
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
    body:    UsergroupsCreateDataBody  |     UsergroupsCreateJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema | None:
    """  Create a User Group

    Args:
        token (str):
        body (UsergroupsCreateDataBody | Unset):
        body (UsergroupsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsCreateDataBody  |     UsergroupsCreateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema]:
    """  Create a User Group

    Args:
        token (str):
        body (UsergroupsCreateDataBody | Unset):
        body (UsergroupsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema]
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
    body:    UsergroupsCreateDataBody  |     UsergroupsCreateJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema | None:
    """  Create a User Group

    Args:
        token (str):
        body (UsergroupsCreateDataBody | Unset):
        body (UsergroupsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsCreateUsergroupsCreateErrorSchema | UsergroupsCreateUsergroupsCreateSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
