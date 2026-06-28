from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_join_conversations_join_error_schema import ConversationsJoinConversationsJoinErrorSchema
from ...models.conversations_join_conversations_join_success_schema import ConversationsJoinConversationsJoinSuccessSchema
from ...models.conversations_join_data_body import ConversationsJoinDataBody
from ...models.conversations_join_json_body import ConversationsJoinJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsJoinDataBody  |     ConversationsJoinJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.join",
    }

    if isinstance(body, ConversationsJoinDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsJoinJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsJoinConversationsJoinSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsJoinConversationsJoinErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsJoinDataBody  |     ConversationsJoinJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema]:
    """  Joins an existing conversation.

    Args:
        token (str | Unset):
        body (ConversationsJoinDataBody | Unset):
        body (ConversationsJoinJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema]
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
    body:    ConversationsJoinDataBody  |     ConversationsJoinJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema | None:
    """  Joins an existing conversation.

    Args:
        token (str | Unset):
        body (ConversationsJoinDataBody | Unset):
        body (ConversationsJoinJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsJoinDataBody  |     ConversationsJoinJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema]:
    """  Joins an existing conversation.

    Args:
        token (str | Unset):
        body (ConversationsJoinDataBody | Unset):
        body (ConversationsJoinJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema]
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
    body:    ConversationsJoinDataBody  |     ConversationsJoinJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema | None:
    """  Joins an existing conversation.

    Args:
        token (str | Unset):
        body (ConversationsJoinDataBody | Unset):
        body (ConversationsJoinJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsJoinConversationsJoinErrorSchema | ConversationsJoinConversationsJoinSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
