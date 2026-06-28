from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_update_chat_update_error_schema import ChatUpdateChatUpdateErrorSchema
from ...models.chat_update_chat_update_success_schema import ChatUpdateChatUpdateSuccessSchema
from ...models.chat_update_data_body import ChatUpdateDataBody
from ...models.chat_update_json_body import ChatUpdateJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ChatUpdateDataBody  |     ChatUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.update",
    }

    if isinstance(body, ChatUpdateDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatUpdateJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatUpdateChatUpdateSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatUpdateChatUpdateErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatUpdateDataBody  |     ChatUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema]:
    """  Updates a message.

    Args:
        token (str):
        body (ChatUpdateDataBody | Unset):
        body (ChatUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema]
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
    body:    ChatUpdateDataBody  |     ChatUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema | None:
    """  Updates a message.

    Args:
        token (str):
        body (ChatUpdateDataBody | Unset):
        body (ChatUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatUpdateDataBody  |     ChatUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema]:
    """  Updates a message.

    Args:
        token (str):
        body (ChatUpdateDataBody | Unset):
        body (ChatUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema]
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
    body:    ChatUpdateDataBody  |     ChatUpdateJsonBody  | Unset = UNSET,
    token: str,

) -> ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema | None:
    """  Updates a message.

    Args:
        token (str):
        body (ChatUpdateDataBody | Unset):
        body (ChatUpdateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatUpdateChatUpdateErrorSchema | ChatUpdateChatUpdateSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
