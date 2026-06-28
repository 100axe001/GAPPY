from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.page_bean_priority import PageBeanPriority
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["onlyDefault"] = only_default


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/priority/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | PageBeanPriority | None:
    if response.status_code == 200:
        response_200 = PageBeanPriority.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | PageBeanPriority]:
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
    only_default: bool | Unset = False,

) -> Response[ErrorCollection | PageBeanPriority]:
    """ Search priorities

     Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a
    subset determined by any combination of these criteria:

     *  a list of priority IDs. Any invalid priority IDs are ignored.
     *  whether the field configuration is a default. This returns priorities from company-managed
    (classic) projects only, as there is no concept of default priorities in team-managed projects.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanPriority]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
only_default=only_default,

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
    only_default: bool | Unset = False,

) -> ErrorCollection | PageBeanPriority | None:
    """ Search priorities

     Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a
    subset determined by any combination of these criteria:

     *  a list of priority IDs. Any invalid priority IDs are ignored.
     *  whether the field configuration is a default. This returns priorities from company-managed
    (classic) projects only, as there is no concept of default priorities in team-managed projects.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanPriority
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
only_default=only_default,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    id: list[str] | Unset = UNSET,
    only_default: bool | Unset = False,

) -> Response[ErrorCollection | PageBeanPriority]:
    """ Search priorities

     Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a
    subset determined by any combination of these criteria:

     *  a list of priority IDs. Any invalid priority IDs are ignored.
     *  whether the field configuration is a default. This returns priorities from company-managed
    (classic) projects only, as there is no concept of default priorities in team-managed projects.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanPriority]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
only_default=only_default,

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
    only_default: bool | Unset = False,

) -> ErrorCollection | PageBeanPriority | None:
    """ Search priorities

     Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a
    subset determined by any combination of these criteria:

     *  a list of priority IDs. Any invalid priority IDs are ignored.
     *  whether the field configuration is a default. This returns priorities from company-managed
    (classic) projects only, as there is no concept of default priorities in team-managed projects.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        id (list[str] | Unset):
        only_default (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanPriority
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
only_default=only_default,

    )).parsed
