from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_archive_conversations_archive_error_schema import ConversationsArchiveConversationsArchiveErrorSchema
from ...models.conversations_archive_conversations_archive_success_schema import ConversationsArchiveConversationsArchiveSuccessSchema
from ...models.conversations_archive_data_body import ConversationsArchiveDataBody
from ...models.conversations_archive_json_body import ConversationsArchiveJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsArchiveDataBody  |     ConversationsArchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.archive",
    }

    if isinstance(body, ConversationsArchiveDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsArchiveJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsArchiveConversationsArchiveSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsArchiveConversationsArchiveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsArchiveDataBody  |     ConversationsArchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema]:
    """  Archives a conversation.

    Args:
        token (str | Unset):
        body (ConversationsArchiveDataBody | Unset):
        body (ConversationsArchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema]
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
    body:    ConversationsArchiveDataBody  |     ConversationsArchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema | None:
    """  Archives a conversation.

    Args:
        token (str | Unset):
        body (ConversationsArchiveDataBody | Unset):
        body (ConversationsArchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsArchiveDataBody  |     ConversationsArchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema]:
    """  Archives a conversation.

    Args:
        token (str | Unset):
        body (ConversationsArchiveDataBody | Unset):
        body (ConversationsArchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema]
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
    body:    ConversationsArchiveDataBody  |     ConversationsArchiveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema | None:
    """  Archives a conversation.

    Args:
        token (str | Unset):
        body (ConversationsArchiveDataBody | Unset):
        body (ConversationsArchiveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsArchiveConversationsArchiveErrorSchema | ConversationsArchiveConversationsArchiveSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
