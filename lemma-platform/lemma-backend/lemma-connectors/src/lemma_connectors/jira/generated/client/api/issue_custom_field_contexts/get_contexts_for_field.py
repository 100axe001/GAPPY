from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_custom_field_context import PageBeanCustomFieldContext
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id: str,
    *,
    is_any_issue_type: bool | Unset = UNSET,
    is_global_context: bool | Unset = UNSET,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["isAnyIssueType"] = is_any_issue_type

    params["isGlobalContext"] = is_global_context

    json_context_id: list[int] | Unset = UNSET
    if not isinstance(context_id, Unset):
        json_context_id = context_id


    params["contextId"] = json_context_id

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/{field_id}/context".format(field_id=quote(str(field_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanCustomFieldContext | None:
    if response.status_code == 200:
        response_200 = PageBeanCustomFieldContext.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanCustomFieldContext]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    is_any_issue_type: bool | Unset = UNSET,
    is_global_context: bool | Unset = UNSET,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanCustomFieldContext]:
    """ Get custom field contexts

     Returns a [paginated](#pagination) list of [
    contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-
    contexts-991923859.html) for a custom field. Contexts can be returned as follows:

     *  With no other parameters set, all contexts.
     *  By defining `id` only, all contexts from the list of IDs.
     *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to
    all issue types (true) or those that apply to only a subset of issue types (false)
     *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to
    all projects (global contexts) (true) or those that apply to only a subset of projects (false).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        is_any_issue_type (bool | Unset):
        is_global_context (bool | Unset):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContext]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
is_any_issue_type=is_any_issue_type,
is_global_context=is_global_context,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    *,
    client: AuthenticatedClient,
    is_any_issue_type: bool | Unset = UNSET,
    is_global_context: bool | Unset = UNSET,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanCustomFieldContext | None:
    """ Get custom field contexts

     Returns a [paginated](#pagination) list of [
    contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-
    contexts-991923859.html) for a custom field. Contexts can be returned as follows:

     *  With no other parameters set, all contexts.
     *  By defining `id` only, all contexts from the list of IDs.
     *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to
    all issue types (true) or those that apply to only a subset of issue types (false)
     *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to
    all projects (global contexts) (true) or those that apply to only a subset of projects (false).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        is_any_issue_type (bool | Unset):
        is_global_context (bool | Unset):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContext
     """


    return sync_detailed(
        field_id=field_id,
client=client,
is_any_issue_type=is_any_issue_type,
is_global_context=is_global_context,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    is_any_issue_type: bool | Unset = UNSET,
    is_global_context: bool | Unset = UNSET,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanCustomFieldContext]:
    """ Get custom field contexts

     Returns a [paginated](#pagination) list of [
    contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-
    contexts-991923859.html) for a custom field. Contexts can be returned as follows:

     *  With no other parameters set, all contexts.
     *  By defining `id` only, all contexts from the list of IDs.
     *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to
    all issue types (true) or those that apply to only a subset of issue types (false)
     *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to
    all projects (global contexts) (true) or those that apply to only a subset of projects (false).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        is_any_issue_type (bool | Unset):
        is_global_context (bool | Unset):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContext]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
is_any_issue_type=is_any_issue_type,
is_global_context=is_global_context,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    *,
    client: AuthenticatedClient,
    is_any_issue_type: bool | Unset = UNSET,
    is_global_context: bool | Unset = UNSET,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanCustomFieldContext | None:
    """ Get custom field contexts

     Returns a [paginated](#pagination) list of [
    contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-
    contexts-991923859.html) for a custom field. Contexts can be returned as follows:

     *  With no other parameters set, all contexts.
     *  By defining `id` only, all contexts from the list of IDs.
     *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to
    all issue types (true) or those that apply to only a subset of issue types (false)
     *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to
    all projects (global contexts) (true) or those that apply to only a subset of projects (false).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        is_any_issue_type (bool | Unset):
        is_global_context (bool | Unset):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContext
     """


    return (await asyncio_detailed(
        field_id=field_id,
client=client,
is_any_issue_type=is_any_issue_type,
is_global_context=is_global_context,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )).parsed
