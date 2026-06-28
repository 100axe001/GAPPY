from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reminders_add_data_body import RemindersAddDataBody
from ...models.reminders_add_json_body import RemindersAddJsonBody
from ...models.reminders_add_reminders_add_error_schema import RemindersAddRemindersAddErrorSchema
from ...models.reminders_add_reminders_add_schema import RemindersAddRemindersAddSchema
from typing import cast



def _get_kwargs(
    *,
    body:    RemindersAddDataBody  |     RemindersAddJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reminders.add",
    }

    if isinstance(body, RemindersAddDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RemindersAddJsonBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema:
    if response.status_code == 200:
        response_200 = RemindersAddRemindersAddSchema.from_dict(response.json())



        return response_200

    response_default = RemindersAddRemindersAddErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersAddDataBody  |     RemindersAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema]:
    """  Creates a reminder.

    Args:
        token (str):
        body (RemindersAddDataBody):
        body (RemindersAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema]
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
    body:    RemindersAddDataBody  |     RemindersAddJsonBody  | Unset = UNSET,
    token: str,

) -> RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema | None:
    """  Creates a reminder.

    Args:
        token (str):
        body (RemindersAddDataBody):
        body (RemindersAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    RemindersAddDataBody  |     RemindersAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema]:
    """  Creates a reminder.

    Args:
        token (str):
        body (RemindersAddDataBody):
        body (RemindersAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema]
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
    body:    RemindersAddDataBody  |     RemindersAddJsonBody  | Unset = UNSET,
    token: str,

) -> RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema | None:
    """  Creates a reminder.

    Args:
        token (str):
        body (RemindersAddDataBody):
        body (RemindersAddJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemindersAddRemindersAddErrorSchema | RemindersAddRemindersAddSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
