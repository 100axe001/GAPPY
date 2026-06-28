from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.screenable_tab import ScreenableTab
from typing import cast



def _get_kwargs(
    screen_id: int,
    *,
    body: ScreenableTab,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/screens/{screen_id}/tabs".format(screen_id=quote(str(screen_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ScreenableTab | None:
    if response.status_code == 200:
        response_200 = ScreenableTab.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ScreenableTab]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    screen_id: int,
    *,
    client: AuthenticatedClient,
    body: ScreenableTab,

) -> Response[Any | ScreenableTab]:
    """ Create screen tab

     Creates a tab for a screen.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        body (ScreenableTab): A screen tab.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScreenableTab]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    screen_id: int,
    *,
    client: AuthenticatedClient,
    body: ScreenableTab,

) -> Any | ScreenableTab | None:
    """ Create screen tab

     Creates a tab for a screen.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        body (ScreenableTab): A screen tab.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScreenableTab
     """


    return sync_detailed(
        screen_id=screen_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    screen_id: int,
    *,
    client: AuthenticatedClient,
    body: ScreenableTab,

) -> Response[Any | ScreenableTab]:
    """ Create screen tab

     Creates a tab for a screen.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        body (ScreenableTab): A screen tab.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScreenableTab]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    screen_id: int,
    *,
    client: AuthenticatedClient,
    body: ScreenableTab,

) -> Any | ScreenableTab | None:
    """ Create screen tab

     Creates a tab for a screen.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        body (ScreenableTab): A screen tab.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScreenableTab
     """


    return (await asyncio_detailed(
        screen_id=screen_id,
client=client,
body=body,

    )).parsed
