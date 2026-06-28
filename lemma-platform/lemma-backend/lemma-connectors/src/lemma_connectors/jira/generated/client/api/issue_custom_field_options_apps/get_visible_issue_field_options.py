from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_issue_field_option import PageBeanIssueFieldOption
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_key: str,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = UNSET,
    project_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    params["projectId"] = project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/{field_key}/option/suggestions/search".format(field_key=quote(str(field_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueFieldOption | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueFieldOption.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueFieldOption]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = UNSET,
    project_id: int | Unset = UNSET,

) -> Response[Any | PageBeanIssueFieldOption]:
    """ Get visible issue field options

     Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed
    by the user.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):
        project_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = UNSET,
    project_id: int | Unset = UNSET,

) -> Any | PageBeanIssueFieldOption | None:
    """ Get visible issue field options

     Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed
    by the user.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):
        project_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueFieldOption
     """


    return sync_detailed(
        field_key=field_key,
client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = UNSET,
    project_id: int | Unset = UNSET,

) -> Response[Any | PageBeanIssueFieldOption]:
    """ Get visible issue field options

     Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed
    by the user.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):
        project_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = UNSET,
    project_id: int | Unset = UNSET,

) -> Any | PageBeanIssueFieldOption | None:
    """ Get visible issue field options

     Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed
    by the user.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):
        project_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueFieldOption
     """


    return (await asyncio_detailed(
        field_key=field_key,
client=client,
start_at=start_at,
max_results=max_results,
project_id=project_id,

    )).parsed
