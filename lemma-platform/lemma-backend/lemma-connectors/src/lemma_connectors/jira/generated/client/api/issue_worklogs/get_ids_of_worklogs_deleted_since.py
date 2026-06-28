from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.changed_worklogs import ChangedWorklogs
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    since: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["since"] = since


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/worklog/deleted",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ChangedWorklogs | None:
    if response.status_code == 200:
        response_200 = ChangedWorklogs.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ChangedWorklogs]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: int | Unset = 0,

) -> Response[Any | ChangedWorklogs]:
    """ Get IDs of deleted worklogs

     Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

    This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from
    oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the
    timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of
    worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

    This resource does not return worklogs deleted during the minute preceding the request.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        since (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChangedWorklogs]
     """


    kwargs = _get_kwargs(
        since=since,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    since: int | Unset = 0,

) -> Any | ChangedWorklogs | None:
    """ Get IDs of deleted worklogs

     Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

    This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from
    oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the
    timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of
    worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

    This resource does not return worklogs deleted during the minute preceding the request.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        since (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChangedWorklogs
     """


    return sync_detailed(
        client=client,
since=since,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: int | Unset = 0,

) -> Response[Any | ChangedWorklogs]:
    """ Get IDs of deleted worklogs

     Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

    This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from
    oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the
    timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of
    worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

    This resource does not return worklogs deleted during the minute preceding the request.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        since (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChangedWorklogs]
     """


    kwargs = _get_kwargs(
        since=since,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    since: int | Unset = 0,

) -> Any | ChangedWorklogs | None:
    """ Get IDs of deleted worklogs

     Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.

    This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from
    oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the
    timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of
    worklogs. The `lastPage` parameter is set to true on the last page of worklogs.

    This resource does not return worklogs deleted during the minute preceding the request.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        since (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChangedWorklogs
     """


    return (await asyncio_detailed(
        client=client,
since=since,

    )).parsed
