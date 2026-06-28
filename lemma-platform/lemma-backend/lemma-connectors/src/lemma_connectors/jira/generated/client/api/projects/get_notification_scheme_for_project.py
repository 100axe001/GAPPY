from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notification_scheme import NotificationScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_key_or_id: str,
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_key_or_id}/notificationscheme".format(project_key_or_id=quote(str(project_key_or_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | NotificationScheme | None:
    if response.status_code == 200:
        response_200 = NotificationScheme.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | NotificationScheme]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | NotificationScheme]:
    """ Get project notification scheme

     Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.
    Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get)
    supporting search and pagination.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_key_or_id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationScheme]
     """


    kwargs = _get_kwargs(
        project_key_or_id=project_key_or_id,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | NotificationScheme | None:
    """ Get project notification scheme

     Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.
    Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get)
    supporting search and pagination.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_key_or_id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationScheme
     """


    return sync_detailed(
        project_key_or_id=project_key_or_id,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | NotificationScheme]:
    """ Get project notification scheme

     Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.
    Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get)
    supporting search and pagination.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_key_or_id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | NotificationScheme]
     """


    kwargs = _get_kwargs(
        project_key_or_id=project_key_or_id,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_key_or_id: str,
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | NotificationScheme | None:
    """ Get project notification scheme

     Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.
    Deprecated, use [Get notification schemes paginated](#api-rest-api-3-notificationscheme-get)
    supporting search and pagination.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_key_or_id (str):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | NotificationScheme
     """


    return (await asyncio_detailed(
        project_key_or_id=project_key_or_id,
client=client,
expand=expand,

    )).parsed
