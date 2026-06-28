from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_me_message_chat_me_message_error_schema import ChatMeMessageChatMeMessageErrorSchema
from ...models.chat_me_message_chat_me_message_schema import ChatMeMessageChatMeMessageSchema
from ...models.chat_me_message_data_body import ChatMeMessageDataBody
from ...models.chat_me_message_json_body import ChatMeMessageJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ChatMeMessageDataBody  |     ChatMeMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.meMessage",
    }

    if isinstance(body, ChatMeMessageDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatMeMessageJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema:
    if response.status_code == 200:
        response_200 = ChatMeMessageChatMeMessageSchema.from_dict(response.json())



        return response_200

    response_default = ChatMeMessageChatMeMessageErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatMeMessageDataBody  |     ChatMeMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema]:
    """  Share a me message into a channel.

    Args:
        token (str | Unset):
        body (ChatMeMessageDataBody | Unset):
        body (ChatMeMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema]
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
    body:    ChatMeMessageDataBody  |     ChatMeMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema | None:
    """  Share a me message into a channel.

    Args:
        token (str | Unset):
        body (ChatMeMessageDataBody | Unset):
        body (ChatMeMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatMeMessageDataBody  |     ChatMeMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema]:
    """  Share a me message into a channel.

    Args:
        token (str | Unset):
        body (ChatMeMessageDataBody | Unset):
        body (ChatMeMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema]
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
    body:    ChatMeMessageDataBody  |     ChatMeMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema | None:
    """  Share a me message into a channel.

    Args:
        token (str | Unset):
        body (ChatMeMessageDataBody | Unset):
        body (ChatMeMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMeMessageChatMeMessageErrorSchema | ChatMeMessageChatMeMessageSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
