from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflows_step_failed_default_error_template import WorkflowsStepFailedDefaultErrorTemplate
from ...models.workflows_step_failed_default_success_template import WorkflowsStepFailedDefaultSuccessTemplate
from typing import cast



def _get_kwargs(
    *,
    workflow_step_execute_id: str,
    error: str,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["workflow_step_execute_id"] = workflow_step_execute_id

    params["error"] = error


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflows.stepFailed",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = WorkflowsStepFailedDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = WorkflowsStepFailedDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workflow_step_execute_id: str,
    error: str,
    token: str,

) -> Response[WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate]:
    """  Indicate that an app's step in a workflow failed to execute.

    Args:
        workflow_step_execute_id (str):
        error (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        workflow_step_execute_id=workflow_step_execute_id,
error=error,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    workflow_step_execute_id: str,
    error: str,
    token: str,

) -> WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate | None:
    """  Indicate that an app's step in a workflow failed to execute.

    Args:
        workflow_step_execute_id (str):
        error (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
workflow_step_execute_id=workflow_step_execute_id,
error=error,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workflow_step_execute_id: str,
    error: str,
    token: str,

) -> Response[WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate]:
    """  Indicate that an app's step in a workflow failed to execute.

    Args:
        workflow_step_execute_id (str):
        error (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        workflow_step_execute_id=workflow_step_execute_id,
error=error,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    workflow_step_execute_id: str,
    error: str,
    token: str,

) -> WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate | None:
    """  Indicate that an app's step in a workflow failed to execute.

    Args:
        workflow_step_execute_id (str):
        error (str):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsStepFailedDefaultErrorTemplate | WorkflowsStepFailedDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
workflow_step_execute_id=workflow_step_execute_id,
error=error,
token=token,

    )).parsed
