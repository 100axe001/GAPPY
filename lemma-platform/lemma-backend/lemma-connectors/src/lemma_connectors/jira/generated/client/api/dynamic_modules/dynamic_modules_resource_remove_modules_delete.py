from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    module_key: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_module_key: list[str] | Unset = UNSET
    if not isinstance(module_key, Unset):
        json_module_key = module_key


    params["moduleKey"] = json_module_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/atlassian-connect/1/app/module/dynamic",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorMessage | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    module_key: list[str] | Unset = UNSET,

) -> Response[Any | ErrorMessage]:
    """ Remove modules

     Remove all or a list of modules registered by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        module_key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorMessage]
     """


    kwargs = _get_kwargs(
        module_key=module_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    module_key: list[str] | Unset = UNSET,

) -> Any | ErrorMessage | None:
    """ Remove modules

     Remove all or a list of modules registered by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        module_key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorMessage
     """


    return sync_detailed(
        client=client,
module_key=module_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    module_key: list[str] | Unset = UNSET,

) -> Response[Any | ErrorMessage]:
    """ Remove modules

     Remove all or a list of modules registered by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        module_key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorMessage]
     """


    kwargs = _get_kwargs(
        module_key=module_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    module_key: list[str] | Unset = UNSET,

) -> Any | ErrorMessage | None:
    """ Remove modules

     Remove all or a list of modules registered by the calling app.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        module_key (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorMessage
     """


    return (await asyncio_detailed(
        client=client,
module_key=module_key,

    )).parsed
