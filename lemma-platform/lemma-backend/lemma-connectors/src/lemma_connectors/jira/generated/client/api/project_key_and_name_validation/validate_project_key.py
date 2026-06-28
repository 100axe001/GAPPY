from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    key: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["key"] = key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/projectvalidate/key",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = ErrorCollection.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,

) -> Response[Any | ErrorCollection]:
    """ Validate project key

     Validates a project key by confirming the key is a valid string and not in use.

    **[Permissions](#permissions) required:** None.

    Args:
        key (str | Unset):  Example: HSP.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,

) -> Any | ErrorCollection | None:
    """ Validate project key

     Validates a project key by confirming the key is a valid string and not in use.

    **[Permissions](#permissions) required:** None.

    Args:
        key (str | Unset):  Example: HSP.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return sync_detailed(
        client=client,
key=key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,

) -> Response[Any | ErrorCollection]:
    """ Validate project key

     Validates a project key by confirming the key is a valid string and not in use.

    **[Permissions](#permissions) required:** None.

    Args:
        key (str | Unset):  Example: HSP.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,

) -> Any | ErrorCollection | None:
    """ Validate project key

     Validates a project key by confirming the key is a valid string and not in use.

    **[Permissions](#permissions) required:** None.

    Args:
        key (str | Unset):  Example: HSP.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,
key=key,

    )).parsed
