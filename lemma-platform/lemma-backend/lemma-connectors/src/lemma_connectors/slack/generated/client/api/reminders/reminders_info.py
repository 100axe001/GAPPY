from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reminders_info_reminders_info_error_schema import RemindersInfoRemindersInfoErrorSchema
from ...models.reminders_info_reminders_info_schema import RemindersInfoRemindersInfoSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    reminder: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token

    params["reminder"] = reminder


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reminders.info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema:
    if response.status_code == 200:
        response_200 = RemindersInfoRemindersInfoSchema.from_dict(response.json())



        return response_200

    response_default = RemindersInfoRemindersInfoErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    reminder: str | Unset = UNSET,

) -> Response[RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema]:
    """  Gets information about a reminder.

    Args:
        token (str | Unset):
        reminder (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
reminder=reminder,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    reminder: str | Unset = UNSET,

) -> RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema | None:
    """  Gets information about a reminder.

    Args:
        token (str | Unset):
        reminder (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema
     """


    return sync_detailed(
        client=client,
token=token,
reminder=reminder,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    reminder: str | Unset = UNSET,

) -> Response[RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema]:
    """  Gets information about a reminder.

    Args:
        token (str | Unset):
        reminder (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema]
     """


    kwargs = _get_kwargs(
        token=token,
reminder=reminder,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    reminder: str | Unset = UNSET,

) -> RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema | None:
    """  Gets information about a reminder.

    Args:
        token (str | Unset):
        reminder (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersInfoRemindersInfoErrorSchema | RemindersInfoRemindersInfoSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,
reminder=reminder,

    )).parsed
