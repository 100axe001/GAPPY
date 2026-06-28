from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_post_message_chat_post_message_error_schema import ChatPostMessageChatPostMessageErrorSchema
from ...models.chat_post_message_chat_post_message_success_schema import ChatPostMessageChatPostMessageSuccessSchema
from ...models.chat_post_message_data_body import ChatPostMessageDataBody
from ...models.chat_post_message_json_body import ChatPostMessageJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ChatPostMessageDataBody  |     ChatPostMessageJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.postMessage",
    }

    if isinstance(body, ChatPostMessageDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatPostMessageJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatPostMessageChatPostMessageSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatPostMessageChatPostMessageErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatPostMessageDataBody  |     ChatPostMessageJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema]:
    """  Sends a message to a channel.

    Args:
        token (str):
        body (ChatPostMessageDataBody | Unset):
        body (ChatPostMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema]
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
    body:    ChatPostMessageDataBody  |     ChatPostMessageJsonBody  | Unset = UNSET,
    token: str,

) -> ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema | None:
    """  Sends a message to a channel.

    Args:
        token (str):
        body (ChatPostMessageDataBody | Unset):
        body (ChatPostMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatPostMessageDataBody  |     ChatPostMessageJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema]:
    """  Sends a message to a channel.

    Args:
        token (str):
        body (ChatPostMessageDataBody | Unset):
        body (ChatPostMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema]
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
    body:    ChatPostMessageDataBody  |     ChatPostMessageJsonBody  | Unset = UNSET,
    token: str,

) -> ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema | None:
    """  Sends a message to a channel.

    Args:
        token (str):
        body (ChatPostMessageDataBody | Unset):
        body (ChatPostMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatPostMessageChatPostMessageErrorSchema | ChatPostMessageChatPostMessageSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
