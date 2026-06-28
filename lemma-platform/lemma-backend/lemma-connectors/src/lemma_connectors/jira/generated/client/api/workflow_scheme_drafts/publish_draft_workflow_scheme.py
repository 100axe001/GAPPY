from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.publish_draft_workflow_scheme import PublishDraftWorkflowScheme
from ...models.task_progress_bean_object import TaskProgressBeanObject
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PublishDraftWorkflowScheme,
    validate_only: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["validateOnly"] = validate_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/workflowscheme/{id}/draft/publish".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TaskProgressBeanObject | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 303:
        response_303 = TaskProgressBeanObject.from_dict(response.json())



        return response_303

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | TaskProgressBeanObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PublishDraftWorkflowScheme,
    validate_only: bool | Unset = False,

) -> Response[Any | TaskProgressBeanObject]:
    """ Publish draft workflow scheme

     Publishes a draft workflow scheme.

    Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to
    update issues with the original workflow status to the new workflow status.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        validate_only (bool | Unset):  Default: False.
        body (PublishDraftWorkflowScheme): Details about the status mappings for publishing a
            draft workflow scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
validate_only=validate_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PublishDraftWorkflowScheme,
    validate_only: bool | Unset = False,

) -> Any | TaskProgressBeanObject | None:
    """ Publish draft workflow scheme

     Publishes a draft workflow scheme.

    Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to
    update issues with the original workflow status to the new workflow status.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        validate_only (bool | Unset):  Default: False.
        body (PublishDraftWorkflowScheme): Details about the status mappings for publishing a
            draft workflow scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
validate_only=validate_only,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PublishDraftWorkflowScheme,
    validate_only: bool | Unset = False,

) -> Response[Any | TaskProgressBeanObject]:
    """ Publish draft workflow scheme

     Publishes a draft workflow scheme.

    Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to
    update issues with the original workflow status to the new workflow status.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        validate_only (bool | Unset):  Default: False.
        body (PublishDraftWorkflowScheme): Details about the status mappings for publishing a
            draft workflow scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
validate_only=validate_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PublishDraftWorkflowScheme,
    validate_only: bool | Unset = False,

) -> Any | TaskProgressBeanObject | None:
    """ Publish draft workflow scheme

     Publishes a draft workflow scheme.

    Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to
    update issues with the original workflow status to the new workflow status.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        validate_only (bool | Unset):  Default: False.
        body (PublishDraftWorkflowScheme): Details about the status mappings for publishing a
            draft workflow scheme.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
validate_only=validate_only,

    )).parsed
