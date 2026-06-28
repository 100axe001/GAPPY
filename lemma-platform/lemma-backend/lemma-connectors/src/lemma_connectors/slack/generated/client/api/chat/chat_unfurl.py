from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chat_unfurl_chat_unfurl_error_schema import ChatUnfurlChatUnfurlErrorSchema
from ...models.chat_unfurl_chat_unfurl_success_schema import ChatUnfurlChatUnfurlSuccessSchema
from ...models.chat_unfurl_data_body import ChatUnfurlDataBody
from ...models.chat_unfurl_json_body import ChatUnfurlJsonBody
from typing import cast



def _get_kwargs(
    *,
    body:    ChatUnfurlDataBody  |     ChatUnfurlJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat.unfurl",
    }

    if isinstance(body, ChatUnfurlDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChatUnfurlJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema:
    if response.status_code == 200:
        response_200 = ChatUnfurlChatUnfurlSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ChatUnfurlChatUnfurlErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatUnfurlDataBody  |     ChatUnfurlJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema]:
    """  Provide custom unfurl behavior for user-posted URLs

    Args:
        token (str):
        body (ChatUnfurlDataBody):
        body (ChatUnfurlJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema]
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
    body:    ChatUnfurlDataBody  |     ChatUnfurlJsonBody  | Unset = UNSET,
    token: str,

) -> ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema | None:
    """  Provide custom unfurl behavior for user-posted URLs

    Args:
        token (str):
        body (ChatUnfurlDataBody):
        body (ChatUnfurlJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ChatUnfurlDataBody  |     ChatUnfurlJsonBody  | Unset = UNSET,
    token: str,

) -> Response[ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema]:
    """  Provide custom unfurl behavior for user-posted URLs

    Args:
        token (str):
        body (ChatUnfurlDataBody):
        body (ChatUnfurlJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema]
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
    body:    ChatUnfurlDataBody  |     ChatUnfurlJsonBody  | Unset = UNSET,
    token: str,

) -> ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema | None:
    """  Provide custom unfurl behavior for user-posted URLs

    Args:
        token (str):
        body (ChatUnfurlDataBody):
        body (ChatUnfurlJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatUnfurlChatUnfurlErrorSchema | ChatUnfurlChatUnfurlSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
