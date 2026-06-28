from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_set_purpose_conversations_set_purpose_error_schema import ConversationsSetPurposeConversationsSetPurposeErrorSchema
from ...models.conversations_set_purpose_conversations_set_purpose_success_schema import ConversationsSetPurposeConversationsSetPurposeSuccessSchema
from ...models.conversations_set_purpose_data_body import ConversationsSetPurposeDataBody
from ...models.conversations_set_purpose_json_body import ConversationsSetPurposeJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsSetPurposeDataBody  |     ConversationsSetPurposeJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.setPurpose",
    }

    if isinstance(body, ConversationsSetPurposeDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsSetPurposeJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsSetPurposeConversationsSetPurposeSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsSetPurposeConversationsSetPurposeErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsSetPurposeDataBody  |     ConversationsSetPurposeJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema]:
    """  Sets the purpose for a conversation.

    Args:
        token (str | Unset):
        body (ConversationsSetPurposeDataBody | Unset):
        body (ConversationsSetPurposeJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema]
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
    body:    ConversationsSetPurposeDataBody  |     ConversationsSetPurposeJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema | None:
    """  Sets the purpose for a conversation.

    Args:
        token (str | Unset):
        body (ConversationsSetPurposeDataBody | Unset):
        body (ConversationsSetPurposeJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsSetPurposeDataBody  |     ConversationsSetPurposeJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema]:
    """  Sets the purpose for a conversation.

    Args:
        token (str | Unset):
        body (ConversationsSetPurposeDataBody | Unset):
        body (ConversationsSetPurposeJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema]
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
    body:    ConversationsSetPurposeDataBody  |     ConversationsSetPurposeJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema | None:
    """  Sets the purpose for a conversation.

    Args:
        token (str | Unset):
        body (ConversationsSetPurposeDataBody | Unset):
        body (ConversationsSetPurposeJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsSetPurposeConversationsSetPurposeErrorSchema | ConversationsSetPurposeConversationsSetPurposeSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
