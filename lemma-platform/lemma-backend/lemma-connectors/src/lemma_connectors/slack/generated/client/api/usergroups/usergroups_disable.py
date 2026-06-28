from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.usergroups_disable_data_body import UsergroupsDisableDataBody
from ...models.usergroups_disable_json_body import UsergroupsDisableJsonBody
from ...models.usergroups_disable_usergroups_disable_error_schema import UsergroupsDisableUsergroupsDisableErrorSchema
from ...models.usergroups_disable_usergroups_disable_schema import UsergroupsDisableUsergroupsDisableSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    UsergroupsDisableDataBody  |     UsergroupsDisableJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/usergroups.disable",
    }

    if isinstance(body, UsergroupsDisableDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsergroupsDisableJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema:
    if response.status_code == 200:
        response_200 = UsergroupsDisableUsergroupsDisableSchema.from_dict(response.json())



        return response_200

    response_default = UsergroupsDisableUsergroupsDisableErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsDisableDataBody  |     UsergroupsDisableJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema]:
    """  Disable an existing User Group

    Args:
        token (str):
        body (UsergroupsDisableDataBody | Unset):
        body (UsergroupsDisableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema]
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
    body:    UsergroupsDisableDataBody  |     UsergroupsDisableJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema | None:
    """  Disable an existing User Group

    Args:
        token (str):
        body (UsergroupsDisableDataBody | Unset):
        body (UsergroupsDisableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    UsergroupsDisableDataBody  |     UsergroupsDisableJsonBody  | Unset = UNSET,
    token: str,

) -> Response[UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema]:
    """  Disable an existing User Group

    Args:
        token (str):
        body (UsergroupsDisableDataBody | Unset):
        body (UsergroupsDisableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema]
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
    body:    UsergroupsDisableDataBody  |     UsergroupsDisableJsonBody  | Unset = UNSET,
    token: str,

) -> UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema | None:
    """  Disable an existing User Group

    Args:
        token (str):
        body (UsergroupsDisableDataBody | Unset):
        body (UsergroupsDisableJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsergroupsDisableUsergroupsDisableErrorSchema | UsergroupsDisableUsergroupsDisableSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
