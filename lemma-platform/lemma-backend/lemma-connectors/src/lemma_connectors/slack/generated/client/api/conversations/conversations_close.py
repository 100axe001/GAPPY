from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_close_conversations_close_error_schema import ConversationsCloseConversationsCloseErrorSchema
from ...models.conversations_close_conversations_close_success_schema import ConversationsCloseConversationsCloseSuccessSchema
from ...models.conversations_close_data_body import ConversationsCloseDataBody
from ...models.conversations_close_json_body import ConversationsCloseJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsCloseDataBody  |     ConversationsCloseJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.close",
    }

    if isinstance(body, ConversationsCloseDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsCloseJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsCloseConversationsCloseSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsCloseConversationsCloseErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsCloseDataBody  |     ConversationsCloseJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema]:
    """  Closes a direct message or multi-person direct message.

    Args:
        token (str | Unset):
        body (ConversationsCloseDataBody | Unset):
        body (ConversationsCloseJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema]
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
    body:    ConversationsCloseDataBody  |     ConversationsCloseJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema | None:
    """  Closes a direct message or multi-person direct message.

    Args:
        token (str | Unset):
        body (ConversationsCloseDataBody | Unset):
        body (ConversationsCloseJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsCloseDataBody  |     ConversationsCloseJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema]:
    """  Closes a direct message or multi-person direct message.

    Args:
        token (str | Unset):
        body (ConversationsCloseDataBody | Unset):
        body (ConversationsCloseJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema]
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
    body:    ConversationsCloseDataBody  |     ConversationsCloseJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema | None:
    """  Closes a direct message or multi-person direct message.

    Args:
        token (str | Unset):
        body (ConversationsCloseDataBody | Unset):
        body (ConversationsCloseJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsCloseConversationsCloseErrorSchema | ConversationsCloseConversationsCloseSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
