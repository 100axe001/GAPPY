from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard import Dashboard
from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Dashboard | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Dashboard | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Dashboard | ErrorCollection]:
    """ Get dashboard

     Returns a dashboard.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    However, to get a dashboard, the dashboard must be shared with the user or the user must own it.
    Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dashboard | ErrorCollection]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Dashboard | ErrorCollection | None:
    """ Get dashboard

     Returns a dashboard.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    However, to get a dashboard, the dashboard must be shared with the user or the user must own it.
    Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dashboard | ErrorCollection
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Dashboard | ErrorCollection]:
    """ Get dashboard

     Returns a dashboard.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    However, to get a dashboard, the dashboard must be shared with the user or the user must own it.
    Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Dashboard | ErrorCollection]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Dashboard | ErrorCollection | None:
    """ Get dashboard

     Returns a dashboard.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    However, to get a dashboard, the dashboard must be shared with the user or the user must own it.
    Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Dashboard | ErrorCollection
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
