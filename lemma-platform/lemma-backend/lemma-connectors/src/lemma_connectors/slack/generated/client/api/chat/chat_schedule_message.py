from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_schedule_message_chat_schedule_message_error_schema import ChatScheduleMessageChatScheduleMessageErrorSchema
from ...models.chat_schedule_message_chat_schedule_message_success_schema import ChatScheduleMessageChatScheduleMessageSuccessSchema
from ...models.chat_schedule_message_data_body import ChatScheduleMessageDataBody
from ...models.chat_schedule_message_json_body import ChatScheduleMessageJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ChatScheduleMessageDataBody  |     ChatScheduleMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.scheduleMessage",
    }

    if isinstance(body, ChatScheduleMessageDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatScheduleMessageJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatScheduleMessageChatScheduleMessageSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatScheduleMessageChatScheduleMessageErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatScheduleMessageDataBody  |     ChatScheduleMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema]:
    """  Schedules a message to be sent to a channel.

    Args:
        token (str | Unset):
        body (ChatScheduleMessageDataBody | Unset):
        body (ChatScheduleMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema]
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
    body:    ChatScheduleMessageDataBody  |     ChatScheduleMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema | None:
    """  Schedules a message to be sent to a channel.

    Args:
        token (str | Unset):
        body (ChatScheduleMessageDataBody | Unset):
        body (ChatScheduleMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatScheduleMessageDataBody  |     ChatScheduleMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema]:
    """  Schedules a message to be sent to a channel.

    Args:
        token (str | Unset):
        body (ChatScheduleMessageDataBody | Unset):
        body (ChatScheduleMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema]
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
    body:    ChatScheduleMessageDataBody  |     ChatScheduleMessageJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema | None:
    """  Schedules a message to be sent to a channel.

    Args:
        token (str | Unset):
        body (ChatScheduleMessageDataBody | Unset):
        body (ChatScheduleMessageJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatScheduleMessageChatScheduleMessageErrorSchema | ChatScheduleMessageChatScheduleMessageSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
