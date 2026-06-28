from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_unarchive_conversations_unarchive_error_schema import ConversationsUnarchiveConversationsUnarchiveErrorSchema
from ...models.conversations_unarchive_conversations_unarchive_success_schema import ConversationsUnarchiveConversationsUnarchiveSuccessSchema
from ...models.conversations_unarchive_data_body import ConversationsUnarchiveDataBody
from ...models.conversations_unarchive_json_body import ConversationsUnarchiveJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsUnarchiveDataBody  |     ConversationsUnarchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.unarchive",
    }

    if isinstance(body, ConversationsUnarchiveDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsUnarchiveJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsUnarchiveConversationsUnarchiveSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsUnarchiveConversationsUnarchiveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsUnarchiveDataBody  |     ConversationsUnarchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema]:
    """  Reverses conversation archival.

    Args:
        token (str | Unset):
        body (ConversationsUnarchiveDataBody | Unset):
        body (ConversationsUnarchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema]
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
    body:    ConversationsUnarchiveDataBody  |     ConversationsUnarchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema | None:
    """  Reverses conversation archival.

    Args:
        token (str | Unset):
        body (ConversationsUnarchiveDataBody | Unset):
        body (ConversationsUnarchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsUnarchiveDataBody  |     ConversationsUnarchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema]:
    """  Reverses conversation archival.

    Args:
        token (str | Unset):
        body (ConversationsUnarchiveDataBody | Unset):
        body (ConversationsUnarchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema]
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
    body:    ConversationsUnarchiveDataBody  |     ConversationsUnarchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema | None:
    """  Reverses conversation archival.

    Args:
        token (str | Unset):
        body (ConversationsUnarchiveDataBody | Unset):
        body (ConversationsUnarchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsUnarchiveConversationsUnarchiveErrorSchema | ConversationsUnarchiveConversationsUnarchiveSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
