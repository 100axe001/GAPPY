from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_create_conversations_create_error_schema import ConversationsCreateConversationsCreateErrorSchema
from ...models.conversations_create_conversations_create_success_schema import ConversationsCreateConversationsCreateSuccessSchema
from ...models.conversations_create_data_body import ConversationsCreateDataBody
from ...models.conversations_create_json_body import ConversationsCreateJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsCreateDataBody  |     ConversationsCreateJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.create",
    }

    if isinstance(body, ConversationsCreateDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsCreateJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsCreateConversationsCreateSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsCreateConversationsCreateErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsCreateDataBody  |     ConversationsCreateJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema]:
    """  Initiates a public or private channel-based conversation

    Args:
        token (str | Unset):
        body (ConversationsCreateDataBody | Unset):
        body (ConversationsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema]
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
    body:    ConversationsCreateDataBody  |     ConversationsCreateJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema | None:
    """  Initiates a public or private channel-based conversation

    Args:
        token (str | Unset):
        body (ConversationsCreateDataBody | Unset):
        body (ConversationsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsCreateDataBody  |     ConversationsCreateJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema]:
    """  Initiates a public or private channel-based conversation

    Args:
        token (str | Unset):
        body (ConversationsCreateDataBody | Unset):
        body (ConversationsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema]
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
    body:    ConversationsCreateDataBody  |     ConversationsCreateJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema | None:
    """  Initiates a public or private channel-based conversation

    Args:
        token (str | Unset):
        body (ConversationsCreateDataBody | Unset):
        body (ConversationsCreateJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsCreateConversationsCreateErrorSchema | ConversationsCreateConversationsCreateSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
