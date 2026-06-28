from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_contextual_configuration import PageBeanContextualConfiguration
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id_or_key: str,
    *,
    id: list[int] | Unset = UNSET,
    field_context_id: list[int] | Unset = UNSET,
    issue_id: int | Unset = UNSET,
    project_key_or_id: str | Unset = UNSET,
    issue_type_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    json_field_context_id: list[int] | Unset = UNSET
    if not isinstance(field_context_id, Unset):
        json_field_context_id = field_context_id


    params["fieldContextId"] = json_field_context_id

    params["issueId"] = issue_id

    params["projectKeyOrId"] = project_key_or_id

    params["issueTypeId"] = issue_type_id

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/app/field/{field_id_or_key}/context/configuration".format(field_id_or_key=quote(str(field_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanContextualConfiguration | None:
    if response.status_code == 200:
        response_200 = PageBeanContextualConfiguration.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanContextualConfiguration]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    id: list[int] | Unset = UNSET,
    field_context_id: list[int] | Unset = UNSET,
    issue_id: int | Unset = UNSET,
    project_key_or_id: str | Unset = UNSET,
    issue_type_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanContextualConfiguration]:
    """ Get custom field configurations

     Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge
    app](https://developer.atlassian.com/platform/forge/).

    The result can be filtered by one of these criteria:

     *  `id`.
     *  `fieldContextId`.
     *  `issueId`.
     *  `projectKeyOrId` and `issueTypeId`.

    Otherwise, all configurations are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    Forge app that created the custom field.

    Args:
        field_id_or_key (str):
        id (list[int] | Unset):
        field_context_id (list[int] | Unset):
        issue_id (int | Unset):
        project_key_or_id (str | Unset):
        issue_type_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContextualConfiguration]
     """


    kwargs = _get_kwargs(
        field_id_or_key=field_id_or_key,
id=id,
field_context_id=field_context_id,
issue_id=issue_id,
project_key_or_id=project_key_or_id,
issue_type_id=issue_type_id,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    id: list[int] | Unset = UNSET,
    field_context_id: list[int] | Unset = UNSET,
    issue_id: int | Unset = UNSET,
    project_key_or_id: str | Unset = UNSET,
    issue_type_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanContextualConfiguration | None:
    """ Get custom field configurations

     Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge
    app](https://developer.atlassian.com/platform/forge/).

    The result can be filtered by one of these criteria:

     *  `id`.
     *  `fieldContextId`.
     *  `issueId`.
     *  `projectKeyOrId` and `issueTypeId`.

    Otherwise, all configurations are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    Forge app that created the custom field.

    Args:
        field_id_or_key (str):
        id (list[int] | Unset):
        field_context_id (list[int] | Unset):
        issue_id (int | Unset):
        project_key_or_id (str | Unset):
        issue_type_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContextualConfiguration
     """


    return sync_detailed(
        field_id_or_key=field_id_or_key,
client=client,
id=id,
field_context_id=field_context_id,
issue_id=issue_id,
project_key_or_id=project_key_or_id,
issue_type_id=issue_type_id,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    id: list[int] | Unset = UNSET,
    field_context_id: list[int] | Unset = UNSET,
    issue_id: int | Unset = UNSET,
    project_key_or_id: str | Unset = UNSET,
    issue_type_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanContextualConfiguration]:
    """ Get custom field configurations

     Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge
    app](https://developer.atlassian.com/platform/forge/).

    The result can be filtered by one of these criteria:

     *  `id`.
     *  `fieldContextId`.
     *  `issueId`.
     *  `projectKeyOrId` and `issueTypeId`.

    Otherwise, all configurations are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    Forge app that created the custom field.

    Args:
        field_id_or_key (str):
        id (list[int] | Unset):
        field_context_id (list[int] | Unset):
        issue_id (int | Unset):
        project_key_or_id (str | Unset):
        issue_type_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanContextualConfiguration]
     """


    kwargs = _get_kwargs(
        field_id_or_key=field_id_or_key,
id=id,
field_context_id=field_context_id,
issue_id=issue_id,
project_key_or_id=project_key_or_id,
issue_type_id=issue_type_id,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    id: list[int] | Unset = UNSET,
    field_context_id: list[int] | Unset = UNSET,
    issue_id: int | Unset = UNSET,
    project_key_or_id: str | Unset = UNSET,
    issue_type_id: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanContextualConfiguration | None:
    """ Get custom field configurations

     Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge
    app](https://developer.atlassian.com/platform/forge/).

    The result can be filtered by one of these criteria:

     *  `id`.
     *  `fieldContextId`.
     *  `issueId`.
     *  `projectKeyOrId` and `issueTypeId`.

    Otherwise, all configurations are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    Forge app that created the custom field.

    Args:
        field_id_or_key (str):
        id (list[int] | Unset):
        field_context_id (list[int] | Unset):
        issue_id (int | Unset):
        project_key_or_id (str | Unset):
        issue_type_id (str | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanContextualConfiguration
     """


    return (await asyncio_detailed(
        field_id_or_key=field_id_or_key,
client=client,
id=id,
field_context_id=field_context_id,
issue_id=issue_id,
project_key_or_id=project_key_or_id,
issue_type_id=issue_type_id,
start_at=start_at,
max_results=max_results,

    )).parsed
