from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.page_bean_notification_scheme_and_project_mapping_json_bean import PageBeanNotificationSchemeAndProjectMappingJsonBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    notification_scheme_id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_notification_scheme_id: list[str] | Unset = UNSET
    if not isinstance(notification_scheme_id, Unset):
        json_notification_scheme_id = notification_scheme_id


    params["notificationSchemeId"] = json_notification_scheme_id

    json_project_id: list[str] | Unset = UNSET
    if not isinstance(project_id, Unset):
        json_project_id = project_id


    params["projectId"] = json_project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/notificationscheme/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean | None:
    if response.status_code == 200:
        response_200 = PageBeanNotificationSchemeAndProjectMappingJsonBean.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean]:
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
    notification_scheme_id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,

) -> Response[ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean]:
    """ Get projects using notification schemes paginated

     Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You
    can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't
    provide any, this will return a list of all mappings. Note that only company-managed (classic)
    projects are supported. This is because team-managed projects don't have a concept of a default
    notification scheme. The mappings are ordered by projectId.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        notification_scheme_id (list[str] | Unset):
        project_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
notification_scheme_id=notification_scheme_id,
project_id=project_id,

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
    notification_scheme_id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,

) -> ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean | None:
    """ Get projects using notification schemes paginated

     Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You
    can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't
    provide any, this will return a list of all mappings. Note that only company-managed (classic)
    projects are supported. This is because team-managed projects don't have a concept of a default
    notification scheme. The mappings are ordered by projectId.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        notification_scheme_id (list[str] | Unset):
        project_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
notification_scheme_id=notification_scheme_id,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: str | Unset = '0',
    max_results: str | Unset = '50',
    notification_scheme_id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,

) -> Response[ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean]:
    """ Get projects using notification schemes paginated

     Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You
    can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't
    provide any, this will return a list of all mappings. Note that only company-managed (classic)
    projects are supported. This is because team-managed projects don't have a concept of a default
    notification scheme. The mappings are ordered by projectId.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        notification_scheme_id (list[str] | Unset):
        project_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
notification_scheme_id=notification_scheme_id,
project_id=project_id,

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
    notification_scheme_id: list[str] | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,

) -> ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean | None:
    """ Get projects using notification schemes paginated

     Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You
    can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't
    provide any, this will return a list of all mappings. Note that only company-managed (classic)
    projects are supported. This is because team-managed projects don't have a concept of a default
    notification scheme. The mappings are ordered by projectId.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        start_at (str | Unset):  Default: '0'.
        max_results (str | Unset):  Default: '50'.
        notification_scheme_id (list[str] | Unset):
        project_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanNotificationSchemeAndProjectMappingJsonBean
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
notification_scheme_id=notification_scheme_id,
project_id=project_id,

    )).parsed
