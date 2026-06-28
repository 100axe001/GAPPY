from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_picker_suggestions import IssuePickerSuggestions
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    current_jql: str | Unset = UNSET,
    current_issue_key: str | Unset = UNSET,
    current_project_id: str | Unset = UNSET,
    show_sub_tasks: bool | Unset = UNSET,
    show_sub_task_parent: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["currentJQL"] = current_jql

    params["currentIssueKey"] = current_issue_key

    params["currentProjectId"] = current_project_id

    params["showSubTasks"] = show_sub_tasks

    params["showSubTaskParent"] = show_sub_task_parent


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/picker",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssuePickerSuggestions | None:
    if response.status_code == 200:
        response_200 = IssuePickerSuggestions.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssuePickerSuggestions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    current_jql: str | Unset = UNSET,
    current_issue_key: str | Unset = UNSET,
    current_project_id: str | Unset = UNSET,
    show_sub_tasks: bool | Unset = UNSET,
    show_sub_task_parent: bool | Unset = UNSET,

) -> Response[Any | IssuePickerSuggestions]:
    """ Get issue picker suggestions

     Returns lists of issues matching a query string. Use this resource to provide auto-completion
    suggestions when the user is looking for an issue using a word or string.

    This operation returns two lists:

     *  `History Search` which includes issues from the user's history of created, edited, or viewed
    issues that contain the string in the `query` parameter.
     *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain
    the string in the `query` parameter.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        query (str | Unset):  Example: query.
        current_jql (str | Unset):
        current_issue_key (str | Unset):
        current_project_id (str | Unset):
        show_sub_tasks (bool | Unset):
        show_sub_task_parent (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssuePickerSuggestions]
     """


    kwargs = _get_kwargs(
        query=query,
current_jql=current_jql,
current_issue_key=current_issue_key,
current_project_id=current_project_id,
show_sub_tasks=show_sub_tasks,
show_sub_task_parent=show_sub_task_parent,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    current_jql: str | Unset = UNSET,
    current_issue_key: str | Unset = UNSET,
    current_project_id: str | Unset = UNSET,
    show_sub_tasks: bool | Unset = UNSET,
    show_sub_task_parent: bool | Unset = UNSET,

) -> Any | IssuePickerSuggestions | None:
    """ Get issue picker suggestions

     Returns lists of issues matching a query string. Use this resource to provide auto-completion
    suggestions when the user is looking for an issue using a word or string.

    This operation returns two lists:

     *  `History Search` which includes issues from the user's history of created, edited, or viewed
    issues that contain the string in the `query` parameter.
     *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain
    the string in the `query` parameter.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        query (str | Unset):  Example: query.
        current_jql (str | Unset):
        current_issue_key (str | Unset):
        current_project_id (str | Unset):
        show_sub_tasks (bool | Unset):
        show_sub_task_parent (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssuePickerSuggestions
     """


    return sync_detailed(
        client=client,
query=query,
current_jql=current_jql,
current_issue_key=current_issue_key,
current_project_id=current_project_id,
show_sub_tasks=show_sub_tasks,
show_sub_task_parent=show_sub_task_parent,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    current_jql: str | Unset = UNSET,
    current_issue_key: str | Unset = UNSET,
    current_project_id: str | Unset = UNSET,
    show_sub_tasks: bool | Unset = UNSET,
    show_sub_task_parent: bool | Unset = UNSET,

) -> Response[Any | IssuePickerSuggestions]:
    """ Get issue picker suggestions

     Returns lists of issues matching a query string. Use this resource to provide auto-completion
    suggestions when the user is looking for an issue using a word or string.

    This operation returns two lists:

     *  `History Search` which includes issues from the user's history of created, edited, or viewed
    issues that contain the string in the `query` parameter.
     *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain
    the string in the `query` parameter.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        query (str | Unset):  Example: query.
        current_jql (str | Unset):
        current_issue_key (str | Unset):
        current_project_id (str | Unset):
        show_sub_tasks (bool | Unset):
        show_sub_task_parent (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssuePickerSuggestions]
     """


    kwargs = _get_kwargs(
        query=query,
current_jql=current_jql,
current_issue_key=current_issue_key,
current_project_id=current_project_id,
show_sub_tasks=show_sub_tasks,
show_sub_task_parent=show_sub_task_parent,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    current_jql: str | Unset = UNSET,
    current_issue_key: str | Unset = UNSET,
    current_project_id: str | Unset = UNSET,
    show_sub_tasks: bool | Unset = UNSET,
    show_sub_task_parent: bool | Unset = UNSET,

) -> Any | IssuePickerSuggestions | None:
    """ Get issue picker suggestions

     Returns lists of issues matching a query string. Use this resource to provide auto-completion
    suggestions when the user is looking for an issue using a word or string.

    This operation returns two lists:

     *  `History Search` which includes issues from the user's history of created, edited, or viewed
    issues that contain the string in the `query` parameter.
     *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain
    the string in the `query` parameter.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        query (str | Unset):  Example: query.
        current_jql (str | Unset):
        current_issue_key (str | Unset):
        current_project_id (str | Unset):
        show_sub_tasks (bool | Unset):
        show_sub_task_parent (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssuePickerSuggestions
     """


    return (await asyncio_detailed(
        client=client,
query=query,
current_jql=current_jql,
current_issue_key=current_issue_key,
current_project_id=current_project_id,
show_sub_tasks=show_sub_tasks,
show_sub_task_parent=show_sub_task_parent,

    )).parsed
