from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reminders_list_reminders_list_error_schema import RemindersListRemindersListErrorSchema
from ...models.reminders_list_reminders_list_schema import RemindersListRemindersListSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token"] = token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reminders.list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema:
    if response.status_code == 200:
        response_200 = RemindersListRemindersListSchema.from_dict(response.json())



        return response_200

    response_default = RemindersListRemindersListErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema]:
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

) -> Response[RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema]:
    """  Lists all reminders created by or for a given user.

    Args:
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,

) -> RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema | None:
    """  Lists all reminders created by or for a given user.

    Args:
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema
     """


    return sync_detailed(
        client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,

) -> Response[RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema]:
    """  Lists all reminders created by or for a given user.

    Args:
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,

) -> RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema | None:
    """  Lists all reminders created by or for a given user.

    Args:
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersListRemindersListErrorSchema | RemindersListRemindersListSchema
     """


    return (await asyncio_detailed(
        client=client,
token=token,

    )).parsed
