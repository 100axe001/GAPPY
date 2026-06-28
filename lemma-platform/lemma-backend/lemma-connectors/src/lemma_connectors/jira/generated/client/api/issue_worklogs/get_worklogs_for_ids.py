from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.worklog import Worklog
from ...models.worklog_ids_request_bean import WorklogIdsRequestBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: WorklogIdsRequestBean,
    expand: str | Unset = '',

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/worklog/list",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Worklog] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Worklog.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Worklog]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WorklogIdsRequestBean,
    expand: str | Unset = '',

) -> Response[Any | list[Worklog]]:
    """ Get worklogs

     Returns worklog details for a list of worklog IDs.

    The returned list of worklogs is limited to 1000 items.

    **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only
    returned where either of the following is true:

     *  the worklog is set as *Viewable by All Users*.
     *  the user is a member of a project role or group with permission to view the worklog.

    Args:
        expand (str | Unset):  Default: ''.
        body (WorklogIdsRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Worklog]]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: WorklogIdsRequestBean,
    expand: str | Unset = '',

) -> Any | list[Worklog] | None:
    """ Get worklogs

     Returns worklog details for a list of worklog IDs.

    The returned list of worklogs is limited to 1000 items.

    **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only
    returned where either of the following is true:

     *  the worklog is set as *Viewable by All Users*.
     *  the user is a member of a project role or group with permission to view the worklog.

    Args:
        expand (str | Unset):  Default: ''.
        body (WorklogIdsRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Worklog]
     """


    return sync_detailed(
        client=client,
body=body,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WorklogIdsRequestBean,
    expand: str | Unset = '',

) -> Response[Any | list[Worklog]]:
    """ Get worklogs

     Returns worklog details for a list of worklog IDs.

    The returned list of worklogs is limited to 1000 items.

    **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only
    returned where either of the following is true:

     *  the worklog is set as *Viewable by All Users*.
     *  the user is a member of a project role or group with permission to view the worklog.

    Args:
        expand (str | Unset):  Default: ''.
        body (WorklogIdsRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Worklog]]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WorklogIdsRequestBean,
    expand: str | Unset = '',

) -> Any | list[Worklog] | None:
    """ Get worklogs

     Returns worklog details for a list of worklog IDs.

    The returned list of worklogs is limited to 1000 items.

    **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only
    returned where either of the following is true:

     *  the worklog is set as *Viewable by All Users*.
     *  the user is a member of a project role or group with permission to view the worklog.

    Args:
        expand (str | Unset):  Default: ''.
        body (WorklogIdsRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Worklog]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
expand=expand,

    )).parsed
