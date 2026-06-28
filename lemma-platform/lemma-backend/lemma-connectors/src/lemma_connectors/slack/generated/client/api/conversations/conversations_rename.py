from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversations_rename_conversations_rename_error_schema import ConversationsRenameConversationsRenameErrorSchema
from ...models.conversations_rename_conversations_rename_success_schema import ConversationsRenameConversationsRenameSuccessSchema
from ...models.conversations_rename_data_body import ConversationsRenameDataBody
from ...models.conversations_rename_json_body import ConversationsRenameJsonBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    ConversationsRenameDataBody  |     ConversationsRenameJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/conversations.rename",
    }

    if isinstance(body, ConversationsRenameDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationsRenameJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema:
    if response.status_code == 200:
        response_200 = ConversationsRenameConversationsRenameSuccessSchema.from_dict(response.json())



        return response_200

    response_default = ConversationsRenameConversationsRenameErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsRenameDataBody  |     ConversationsRenameJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema]:
    """  Renames a conversation.

    Args:
        token (str | Unset):
        body (ConversationsRenameDataBody | Unset):
        body (ConversationsRenameJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema]
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
    body:    ConversationsRenameDataBody  |     ConversationsRenameJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema | None:
    """  Renames a conversation.

    Args:
        token (str | Unset):
        body (ConversationsRenameDataBody | Unset):
        body (ConversationsRenameJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    ConversationsRenameDataBody  |     ConversationsRenameJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema]:
    """  Renames a conversation.

    Args:
        token (str | Unset):
        body (ConversationsRenameDataBody | Unset):
        body (ConversationsRenameJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema]
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
    body:    ConversationsRenameDataBody  |     ConversationsRenameJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema | None:
    """  Renames a conversation.

    Args:
        token (str | Unset):
        body (ConversationsRenameDataBody | Unset):
        body (ConversationsRenameJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationsRenameConversationsRenameErrorSchema | ConversationsRenameConversationsRenameSuccessSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
