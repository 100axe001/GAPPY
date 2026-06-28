from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_delete_chat_delete_error_schema import ChatDeleteChatDeleteErrorSchema
from ...models.chat_delete_chat_delete_success_schema import ChatDeleteChatDeleteSuccessSchema
from ...models.chat_delete_data_body import ChatDeleteDataBody
from ...models.chat_delete_json_body import ChatDeleteJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ChatDeleteDataBody  |     ChatDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.delete",
    }

    if isinstance(body, ChatDeleteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatDeleteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatDeleteChatDeleteSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatDeleteChatDeleteErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatDeleteDataBody  |     ChatDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema]:
    """  Deletes a message.

    Args:
        token (str | Unset):
        body (ChatDeleteDataBody | Unset):
        body (ChatDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema]
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
    body:    ChatDeleteDataBody  |     ChatDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema | None:
    """  Deletes a message.

    Args:
        token (str | Unset):
        body (ChatDeleteDataBody | Unset):
        body (ChatDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatDeleteDataBody  |     ChatDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema]:
    """  Deletes a message.

    Args:
        token (str | Unset):
        body (ChatDeleteDataBody | Unset):
        body (ChatDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema]
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
    body:    ChatDeleteDataBody  |     ChatDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema | None:
    """  Deletes a message.

    Args:
        token (str | Unset):
        body (ChatDeleteDataBody | Unset):
        body (ChatDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatDeleteChatDeleteErrorSchema | ChatDeleteChatDeleteSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
