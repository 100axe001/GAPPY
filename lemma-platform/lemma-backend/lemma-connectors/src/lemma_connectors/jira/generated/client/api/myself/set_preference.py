from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    *,
    body: str,
    key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["key"] = key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/mypreferences",
        "params": params,
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,

) -> Response[Any]:
    """ Set preference

     Creates a preference for the user or updates a preference's value by sending a plain text string.
    For example, `false`. An arbitrary preference can be created with the value containing up to 255
    characters. In addition, the following keys define system preferences that can be set or created:

     *  *user.notifications.mimetype* The mime type used in notifications sent to the user. Defaults to
    `html`.
     *  *user.notify.own.changes* Whether the user gets notified of their own changes. Defaults to
    `false`.
     *  *user.default.share.private* Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ)
    are set to private. Defaults to `true`.
     *  *user.keyboard.shortcuts.disabled* Whether keyboard shortcuts are disabled. Defaults to `false`.
     *  *user.autowatch.disabled* Whether the user automatically watches issues they create or add a
    comment to. By default, not set: the user takes the instance autowatch setting.

    Note that these keys are deprecated:

     *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance
    locale.
     *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance
    timezone.

    Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-
    users-account-id-manage-profile-patch) from the user management REST API to manage timezone and
    locale instead.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        key (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,
key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: str,
    key: str,

) -> Response[Any]:
    """ Set preference

     Creates a preference for the user or updates a preference's value by sending a plain text string.
    For example, `false`. An arbitrary preference can be created with the value containing up to 255
    characters. In addition, the following keys define system preferences that can be set or created:

     *  *user.notifications.mimetype* The mime type used in notifications sent to the user. Defaults to
    `html`.
     *  *user.notify.own.changes* Whether the user gets notified of their own changes. Defaults to
    `false`.
     *  *user.default.share.private* Whether new [ filters](https://confluence.atlassian.com/x/eQiiLQ)
    are set to private. Defaults to `true`.
     *  *user.keyboard.shortcuts.disabled* Whether keyboard shortcuts are disabled. Defaults to `false`.
     *  *user.autowatch.disabled* Whether the user automatically watches issues they create or add a
    comment to. By default, not set: the user takes the instance autowatch setting.

    Note that these keys are deprecated:

     *  *jira.user.locale* The locale of the user. By default, not set. The user takes the instance
    locale.
     *  *jira.user.timezone* The time zone of the user. By default, not set. The user takes the instance
    timezone.

    Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-
    users-account-id-manage-profile-patch) from the user management REST API to manage timezone and
    locale instead.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        key (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,
key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

