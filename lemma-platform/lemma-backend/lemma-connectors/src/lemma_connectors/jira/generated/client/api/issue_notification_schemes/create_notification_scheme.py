from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_notification_scheme_details import CreateNotificationSchemeDetails
from ...models.error_collection import ErrorCollection
from ...models.notification_scheme_id import NotificationSchemeId
from typing import cast



def _get_kwargs(
    *,
    body: CreateNotificationSchemeDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/notificationscheme",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | NotificationSchemeId | None:
    if response.status_code == 201:
        response_201 = NotificationSchemeId.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | NotificationSchemeId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateNotificationSchemeDetails,

) -> Response[ErrorCollection | NotificationSchemeId]:
    """ Create notification scheme

     Creates a notification scheme with notifications. You can create up to 1000 notifications per
    request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateNotificationSchemeDetails): Details of an notification scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | NotificationSchemeId]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CreateNotificationSchemeDetails,

) -> ErrorCollection | NotificationSchemeId | None:
    """ Create notification scheme

     Creates a notification scheme with notifications. You can create up to 1000 notifications per
    request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateNotificationSchemeDetails): Details of an notification scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | NotificationSchemeId
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateNotificationSchemeDetails,

) -> Response[ErrorCollection | NotificationSchemeId]:
    """ Create notification scheme

     Creates a notification scheme with notifications. You can create up to 1000 notifications per
    request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateNotificationSchemeDetails): Details of an notification scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | NotificationSchemeId]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateNotificationSchemeDetails,

) -> ErrorCollection | NotificationSchemeId | None:
    """ Create notification scheme

     Creates a notification scheme with notifications. You can create up to 1000 notifications per
    request.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateNotificationSchemeDetails): Details of an notification scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | NotificationSchemeId
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
