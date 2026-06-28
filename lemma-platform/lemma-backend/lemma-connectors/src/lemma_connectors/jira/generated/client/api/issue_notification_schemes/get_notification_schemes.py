from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_notification_scheme import PageBeanNotificationScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    json_project_id: list[str] | Unset = UNSET
    if not isinstance(project_id, Unset):
        json_project_id = project_id


    params["projectId"] = json_project_id

    params["onlyDefault"] = only_default

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/notificationscheme",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanNotificationScheme | None:
    if response.status_code == 200:
        response_200 = PageBeanNotificationScheme.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanNotificationScheme]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanNotificationScheme]:
    """ Get notification schemes paginated

     Returns a [paginated](#pagination) list of [notification
    schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

    *Note that you should allow for events without recipients to appear in responses.*

    **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have
    permission to administer at least one project associated with a notification scheme for it to be
    returned.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        project_id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanNotificationScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
project_id=project_id,
only_default=only_default,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,
    expand: str | Unset = UNSET,

) -> Any | PageBeanNotificationScheme | None:
    """ Get notification schemes paginated

     Returns a [paginated](#pagination) list of [notification
    schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

    *Note that you should allow for events without recipients to appear in responses.*

    **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have
    permission to administer at least one project associated with a notification scheme for it to be
    returned.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        project_id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanNotificationScheme
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
project_id=project_id,
only_default=only_default,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanNotificationScheme]:
    """ Get notification schemes paginated

     Returns a [paginated](#pagination) list of [notification
    schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

    *Note that you should allow for events without recipients to appear in responses.*

    **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have
    permission to administer at least one project associated with a notification scheme for it to be
    returned.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        project_id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanNotificationScheme]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
project_id=project_id,
only_default=only_default,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,
    expand: str | Unset = UNSET,

) -> Any | PageBeanNotificationScheme | None:
    """ Get notification schemes paginated

     Returns a [paginated](#pagination) list of [notification
    schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.

    *Note that you should allow for events without recipients to appear in responses.*

    **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have
    permission to administer at least one project associated with a notification scheme for it to be
    returned.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        project_id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanNotificationScheme
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
project_id=project_id,
only_default=only_default,
expand=expand,

    )).parsed
