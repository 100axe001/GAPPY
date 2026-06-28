from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_mark_conversations_mark_error_schema import ConversationsMarkConversationsMarkErrorSchema
from ...models.conversations_mark_conversations_mark_success_schema import ConversationsMarkConversationsMarkSuccessSchema
from ...models.conversations_mark_data_body import ConversationsMarkDataBody
from ...models.conversations_mark_json_body import ConversationsMarkJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsMarkDataBody  |     ConversationsMarkJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.mark",
    }

    if isinstance(body, ConversationsMarkDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsMarkJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsMarkConversationsMarkSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsMarkConversationsMarkErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsMarkDataBody  |     ConversationsMarkJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema]:
    """  Sets the read cursor in a channel.

    Args:
        token (str | Unset):
        body (ConversationsMarkDataBody | Unset):
        body (ConversationsMarkJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema]
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
    body:    ConversationsMarkDataBody  |     ConversationsMarkJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema | None:
    """  Sets the read cursor in a channel.

    Args:
        token (str | Unset):
        body (ConversationsMarkDataBody | Unset):
        body (ConversationsMarkJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsMarkDataBody  |     ConversationsMarkJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema]:
    """  Sets the read cursor in a channel.

    Args:
        token (str | Unset):
        body (ConversationsMarkDataBody | Unset):
        body (ConversationsMarkJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema]
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
    body:    ConversationsMarkDataBody  |     ConversationsMarkJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema | None:
    """  Sets the read cursor in a channel.

    Args:
        token (str | Unset):
        body (ConversationsMarkDataBody | Unset):
        body (ConversationsMarkJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsMarkConversationsMarkErrorSchema | ConversationsMarkConversationsMarkSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
