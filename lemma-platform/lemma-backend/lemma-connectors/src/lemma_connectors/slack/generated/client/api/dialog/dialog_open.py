from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dialog_open_dialog_open_error_schema import DialogOpenDialogOpenErrorSchema
from ...models.dialog_open_dialog_open_schema import DialogOpenDialogOpenSchema
from typing import cast



def _get_kwargs(
    *,
    dialog: str,
    trigger_id: str,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["dialog"] = dialog

    params["trigger_id"] = trigger_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dialog.open",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema:
    if response.status_code == 200:
        response_200 = DialogOpenDialogOpenSchema.from_dict(response.json())



        return response_200

    response_default = DialogOpenDialogOpenErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dialog: str,
    trigger_id: str,
    token: str,

) -> Response[DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema]:
    """  Open a dialog with a user

    Args:
        dialog (str):
        trigger_id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema]
     """


    kwargs = _get_kwargs(
        dialog=dialog,
trigger_id=trigger_id,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    dialog: str,
    trigger_id: str,
    token: str,

) -> DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema | None:
    """  Open a dialog with a user

    Args:
        dialog (str):
        trigger_id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema
     """


    return sync_detailed(
        client=client,
dialog=dialog,
trigger_id=trigger_id,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dialog: str,
    trigger_id: str,
    token: str,

) -> Response[DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema]:
    """  Open a dialog with a user

    Args:
        dialog (str):
        trigger_id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema]
     """


    kwargs = _get_kwargs(
        dialog=dialog,
trigger_id=trigger_id,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    dialog: str,
    trigger_id: str,
    token: str,

) -> DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema | None:
    """  Open a dialog with a user

    Args:
        dialog (str):
        trigger_id (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DialogOpenDialogOpenErrorSchema | DialogOpenDialogOpenSchema
     """


    return (await asyncio_detailed(
        client=client,
dialog=dialog,
trigger_id=trigger_id,
token=token,

    )).parsed
