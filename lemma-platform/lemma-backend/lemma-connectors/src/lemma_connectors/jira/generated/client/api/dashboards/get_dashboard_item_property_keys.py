from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.property_keys import PropertyKeys
from typing import cast



def _get_kwargs(
    dashboard_id: str,
    item_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties".format(dashboard_id=quote(str(dashboard_id), safe=""),item_id=quote(str(item_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PropertyKeys | None:
    if response.status_code == 200:
        response_200 = PropertyKeys.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PropertyKeys]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | PropertyKeys]:
    """ Get dashboard item property keys

     Returns the keys of all properties for a dashboard item.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PropertyKeys]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dashboard_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | PropertyKeys | None:
    """ Get dashboard item property keys

     Returns the keys of all properties for a dashboard item.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PropertyKeys
     """


    return sync_detailed(
        dashboard_id=dashboard_id,
item_id=item_id,
client=client,

    ).parsed

async def asyncio_detailed(
    dashboard_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | PropertyKeys]:
    """ Get dashboard item property keys

     Returns the keys of all properties for a dashboard item.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PropertyKeys]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dashboard_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | PropertyKeys | None:
    """ Get dashboard item property keys

     Returns the keys of all properties for a dashboard item.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PropertyKeys
     """


    return (await asyncio_detailed(
        dashboard_id=dashboard_id,
item_id=item_id,
client=client,

    )).parsed
