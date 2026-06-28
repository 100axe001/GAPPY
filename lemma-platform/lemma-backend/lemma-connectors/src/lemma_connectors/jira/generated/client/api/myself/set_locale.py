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
    *,
    body: Locale,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/mypreferences/locale",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
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
    body: Locale,

) -> Response[Any]:
    """ Set locale

     Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-
    management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API
    instead.

    Sets the locale of the user. The locale must be one supported by the instance of Jira.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (Locale): Details of a locale.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Locale,

) -> Response[Any]:
    """ Set locale

     Deprecated, use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-
    management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API
    instead.

    Sets the locale of the user. The locale must be one supported by the instance of Jira.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (Locale): Details of a locale.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

