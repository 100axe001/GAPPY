from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from typing import cast



def _get_kwargs(
    notification_scheme_id: str,
    notification_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/notificationscheme/{notification_scheme_id}/notification/{notification_id}".format(notification_scheme_id=quote(str(notification_scheme_id), safe=""),notification_id=quote(str(notification_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | None:
    if response.status_code == 204:
        response_204 = response.json()
        return response_204

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

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
    notification_scheme_id: str,
    notification_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ErrorCollection]:
    """ Remove notification from notification scheme

     Removes a notification from a notification scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        notification_scheme_id (str):
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        notification_scheme_id=notification_scheme_id,
notification_id=notification_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    notification_scheme_id: str,
    notification_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | ErrorCollection | None:
    """ Remove notification from notification scheme

     Removes a notification from a notification scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        notification_scheme_id (str):
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return sync_detailed(
        notification_scheme_id=notification_scheme_id,
notification_id=notification_id,
client=client,

    ).parsed

async def asyncio_detailed(
    notification_scheme_id: str,
    notification_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | ErrorCollection]:
    """ Remove notification from notification scheme

     Removes a notification from a notification scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        notification_scheme_id (str):
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
     """


    kwargs = _get_kwargs(
        notification_scheme_id=notification_scheme_id,
notification_id=notification_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    notification_scheme_id: str,
    notification_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | ErrorCollection | None:
    """ Remove notification from notification scheme

     Removes a notification from a notification scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        notification_scheme_id (str):
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return (await asyncio_detailed(
        notification_scheme_id=notification_scheme_id,
notification_id=notification_id,
client=client,

    )).parsed
