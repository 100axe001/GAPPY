from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reminders_delete_data_body import RemindersDeleteDataBody
from ...models.reminders_delete_json_body import RemindersDeleteJsonBody
from ...models.reminders_delete_reminders_delete_error_schema import RemindersDeleteRemindersDeleteErrorSchema
from ...models.reminders_delete_reminders_delete_schema import RemindersDeleteRemindersDeleteSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    RemindersDeleteDataBody  |     RemindersDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(token, Unset):
        headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reminders.delete",
    }

    if isinstance(body, RemindersDeleteDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RemindersDeleteJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema:
    if response.status_code == 200:
        response_200 = RemindersDeleteRemindersDeleteSchema.from_dict(response.json())



        return response_200

    response_default = RemindersDeleteRemindersDeleteErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersDeleteDataBody  |     RemindersDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema]:
    """  Deletes a reminder.

    Args:
        token (str | Unset):
        body (RemindersDeleteDataBody | Unset):
        body (RemindersDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema]
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
    body:    RemindersDeleteDataBody  |     RemindersDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema | None:
    """  Deletes a reminder.

    Args:
        token (str | Unset):
        body (RemindersDeleteDataBody | Unset):
        body (RemindersDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersDeleteDataBody  |     RemindersDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> Response[RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema]:
    """  Deletes a reminder.

    Args:
        token (str | Unset):
        body (RemindersDeleteDataBody | Unset):
        body (RemindersDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema]
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
    body:    RemindersDeleteDataBody  |     RemindersDeleteJsonBody  | Unset = UNSET,
    token: str | Unset = UNSET,

) -> RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema | None:
    """  Deletes a reminder.

    Args:
        token (str | Unset):
        body (RemindersDeleteDataBody | Unset):
        body (RemindersDeleteJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersDeleteRemindersDeleteErrorSchema | RemindersDeleteRemindersDeleteSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
