from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reminders_complete_data_body import RemindersCompleteDataBody
from ...models.reminders_complete_json_body import RemindersCompleteJsonBody
from ...models.reminders_complete_reminders_complete_error_schema import RemindersCompleteRemindersCompleteErrorSchema
from ...models.reminders_complete_reminders_complete_schema import RemindersCompleteRemindersCompleteSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    RemindersCompleteDataBody  |     RemindersCompleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reminders.complete",
    }

    if isinstance(body, RemindersCompleteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RemindersCompleteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema:
    if response.status_code == 200:
        response_200 = RemindersCompleteRemindersCompleteSchema.from_dict(response.json())



        return response_200

    response_default = RemindersCompleteRemindersCompleteErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersCompleteDataBody  |     RemindersCompleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema]:
    """  Marks a reminder as complete.

    Args:
        token (str | Unset):
        body (RemindersCompleteDataBody | Unset):
        body (RemindersCompleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema]
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
    body:    RemindersCompleteDataBody  |     RemindersCompleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema | None:
    """  Marks a reminder as complete.

    Args:
        token (str | Unset):
        body (RemindersCompleteDataBody | Unset):
        body (RemindersCompleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersCompleteDataBody  |     RemindersCompleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema]:
    """  Marks a reminder as complete.

    Args:
        token (str | Unset):
        body (RemindersCompleteDataBody | Unset):
        body (RemindersCompleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema]
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
    body:    RemindersCompleteDataBody  |     RemindersCompleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema | None:
    """  Marks a reminder as complete.

    Args:
        token (str | Unset):
        body (RemindersCompleteDataBody | Unset):
        body (RemindersCompleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersCompleteRemindersCompleteErrorSchema | RemindersCompleteRemindersCompleteSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
