from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedule_list_response import ScheduleListResponse
from ...models.schedule_type import ScheduleType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pod_id: UUID,
    *,
    schedule_type: None | ScheduleType | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    workflow_name: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_schedule_type: None | str | Unset
    if isinstance(schedule_type, Unset):
        json_schedule_type = UNSET
    elif isinstance(schedule_type, ScheduleType):
        json_schedule_type = schedule_type.value
    else:
        json_schedule_type = schedule_type
    params["schedule_type"] = json_schedule_type

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    json_agent_name: None | str | Unset
    if isinstance(agent_name, Unset):
        json_agent_name = UNSET
    else:
        json_agent_name = agent_name
    params["agent_name"] = json_agent_name

    json_workflow_name: None | str | Unset
    if isinstance(workflow_name, Unset):
        json_workflow_name = UNSET
    else:
        json_workflow_name = workflow_name
    params["workflow_name"] = json_workflow_name

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    params["limit"] = limit

    json_page_token: None | str | Unset
    if isinstance(page_token, Unset):
        json_page_token = UNSET
    else:
        json_page_token = page_token
    params["page_token"] = json_page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pods/{pod_id}/schedules".format(
            pod_id=quote(str(pod_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ScheduleListResponse | None:
    if response.status_code == 200:
        response_200 = ScheduleListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ScheduleListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    schedule_type: None | ScheduleType | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    workflow_name: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[ErrorResponse | ScheduleListResponse]:
    """List Schedules

     List pod schedules.

    Args:
        pod_id (UUID):
        schedule_type (None | ScheduleType | Unset):
        is_active (bool | None | Unset):
        agent_name (None | str | Unset):
        workflow_name (None | str | Unset):
        name (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduleListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        schedule_type=schedule_type,
        is_active=is_active,
        agent_name=agent_name,
        workflow_name=workflow_name,
        name=name,
        limit=limit,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    schedule_type: None | ScheduleType | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    workflow_name: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> ErrorResponse | ScheduleListResponse | None:
    """List Schedules

     List pod schedules.

    Args:
        pod_id (UUID):
        schedule_type (None | ScheduleType | Unset):
        is_active (bool | None | Unset):
        agent_name (None | str | Unset):
        workflow_name (None | str | Unset):
        name (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduleListResponse
    """

    return sync_detailed(
        pod_id=pod_id,
        client=client,
        schedule_type=schedule_type,
        is_active=is_active,
        agent_name=agent_name,
        workflow_name=workflow_name,
        name=name,
        limit=limit,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    schedule_type: None | ScheduleType | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    workflow_name: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> Response[ErrorResponse | ScheduleListResponse]:
    """List Schedules

     List pod schedules.

    Args:
        pod_id (UUID):
        schedule_type (None | ScheduleType | Unset):
        is_active (bool | None | Unset):
        agent_name (None | str | Unset):
        workflow_name (None | str | Unset):
        name (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ScheduleListResponse]
    """

    kwargs = _get_kwargs(
        pod_id=pod_id,
        schedule_type=schedule_type,
        is_active=is_active,
        agent_name=agent_name,
        workflow_name=workflow_name,
        name=name,
        limit=limit,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pod_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    schedule_type: None | ScheduleType | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    workflow_name: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    page_token: None | str | Unset = UNSET,
) -> ErrorResponse | ScheduleListResponse | None:
    """List Schedules

     List pod schedules.

    Args:
        pod_id (UUID):
        schedule_type (None | ScheduleType | Unset):
        is_active (bool | None | Unset):
        agent_name (None | str | Unset):
        workflow_name (None | str | Unset):
        name (None | str | Unset):
        limit (int | Unset):  Default: 100.
        page_token (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ScheduleListResponse
    """

    return (
        await asyncio_detailed(
            pod_id=pod_id,
            client=client,
            schedule_type=schedule_type,
            is_active=is_active,
            agent_name=agent_name,
            workflow_name=workflow_name,
            name=name,
            limit=limit,
            page_token=page_token,
        )
    ).parsed
