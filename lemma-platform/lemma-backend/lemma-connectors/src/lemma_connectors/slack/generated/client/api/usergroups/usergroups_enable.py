from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.usergroups_enable_data_body import UsergroupsEnableDataBody
from ...models.usergroups_enable_json_body import UsergroupsEnableJsonBody
from ...models.usergroups_enable_usergroups_enable_error_schema import UsergroupsEnableUsergroupsEnableErrorSchema
from ...models.usergroups_enable_usergroups_enable_schema import UsergroupsEnableUsergroupsEnableSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    UsergroupsEnableDataBody  |     UsergroupsEnableJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/usergroups.enable",
    }

    if isinstance(body, UsergroupsEnableDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsergroupsEnableJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema:
    if response.status_code == 200:
        response_200 = UsergroupsEnableUsergroupsEnableSchema.from_dict(response.json())



        return response_200

    response_default = UsergroupsEnableUsergroupsEnableErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsEnableDataBody  |     UsergroupsEnableJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema]:
    """  Enable a User Group

    Args:
        token (str):
        body (UsergroupsEnableDataBody | Unset):
        body (UsergroupsEnableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema]
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
    body:    UsergroupsEnableDataBody  |     UsergroupsEnableJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema | None:
    """  Enable a User Group

    Args:
        token (str):
        body (UsergroupsEnableDataBody | Unset):
        body (UsergroupsEnableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsEnableDataBody  |     UsergroupsEnableJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema]:
    """  Enable a User Group

    Args:
        token (str):
        body (UsergroupsEnableDataBody | Unset):
        body (UsergroupsEnableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema]
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
    body:    UsergroupsEnableDataBody  |     UsergroupsEnableJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema | None:
    """  Enable a User Group

    Args:
        token (str):
        body (UsergroupsEnableDataBody | Unset):
        body (UsergroupsEnableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsEnableUsergroupsEnableErrorSchema | UsergroupsEnableUsergroupsEnableSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
