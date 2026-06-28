from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.locale import Locale
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/mypreferences/locale",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Locale | None:
    if response.status_code == 200:
        response_200 = Locale.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Locale]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | Locale]:
    """ Get locale

     Returns the locale for the user.

    If the user has no language preference set (which is the default setting) or this resource is
    accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale
    using the *Accept-Language* header in the request. However, if this doesn't match a locale available
    Jira, the site default locale is returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Locale]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Any | Locale | None:
    """ Get locale

     Returns the locale for the user.

    If the user has no language preference set (which is the default setting) or this resource is
    accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale
    using the *Accept-Language* header in the request. However, if this doesn't match a locale available
    Jira, the site default locale is returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Locale
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | Locale]:
    """ Get locale

     Returns the locale for the user.

    If the user has no language preference set (which is the default setting) or this resource is
    accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale
    using the *Accept-Language* header in the request. However, if this doesn't match a locale available
    Jira, the site default locale is returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Locale]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Any | Locale | None:
    """ Get locale

     Returns the locale for the user.

    If the user has no language preference set (which is the default setting) or this resource is
    accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale
    using the *Accept-Language* header in the request. However, if this doesn't match a locale available
    Jira, the site default locale is returned.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Locale
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
