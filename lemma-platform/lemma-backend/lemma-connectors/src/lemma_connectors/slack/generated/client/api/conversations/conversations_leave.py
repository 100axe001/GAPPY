from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_leave_conversations_leave_error_schema import ConversationsLeaveConversationsLeaveErrorSchema
from ...models.conversations_leave_conversations_leave_success_schema import ConversationsLeaveConversationsLeaveSuccessSchema
from ...models.conversations_leave_data_body import ConversationsLeaveDataBody
from ...models.conversations_leave_json_body import ConversationsLeaveJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsLeaveDataBody  |     ConversationsLeaveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.leave",
    }

    if isinstance(body, ConversationsLeaveDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsLeaveJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsLeaveConversationsLeaveSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsLeaveConversationsLeaveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsLeaveDataBody  |     ConversationsLeaveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema]:
    """  Leaves a conversation.

    Args:
        token (str | Unset):
        body (ConversationsLeaveDataBody | Unset):
        body (ConversationsLeaveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema]
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
    body:    ConversationsLeaveDataBody  |     ConversationsLeaveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema | None:
    """  Leaves a conversation.

    Args:
        token (str | Unset):
        body (ConversationsLeaveDataBody | Unset):
        body (ConversationsLeaveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsLeaveDataBody  |     ConversationsLeaveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema]:
    """  Leaves a conversation.

    Args:
        token (str | Unset):
        body (ConversationsLeaveDataBody | Unset):
        body (ConversationsLeaveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema]
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
    body:    ConversationsLeaveDataBody  |     ConversationsLeaveJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema | None:
    """  Leaves a conversation.

    Args:
        token (str | Unset):
        body (ConversationsLeaveDataBody | Unset):
        body (ConversationsLeaveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsLeaveConversationsLeaveErrorSchema | ConversationsLeaveConversationsLeaveSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
