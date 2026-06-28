from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflows_update_step_default_error_template import WorkflowsUpdateStepDefaultErrorTemplate
from ...models.workflows_update_step_default_success_template import WorkflowsUpdateStepDefaultSuccessTemplate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    workflow_step_edit_id: str,
    inputs: str | Unset = UNSET,
    outputs: str | Unset = UNSET,
    step_name: str | Unset = UNSET,
    step_image_url: str | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    params: dict[str, Any] = {}

    params["workflow_step_edit_id"] = workflow_step_edit_id

    params["inputs"] = inputs

    params["outputs"] = outputs

    params["step_name"] = step_name

    params["step_image_url"] = step_image_url


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflows.updateStep",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate:
    if response.status_code == 200:
        response_200 = WorkflowsUpdateStepDefaultSuccessTemplate.from_dict(response.json())



        return response_200

    response_default = WorkflowsUpdateStepDefaultErrorTemplate.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workflow_step_edit_id: str,
    inputs: str | Unset = UNSET,
    outputs: str | Unset = UNSET,
    step_name: str | Unset = UNSET,
    step_image_url: str | Unset = UNSET,
    token: str,

) -> Response[WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate]:
    """  Update the configuration for a workflow extension step.

    Args:
        workflow_step_edit_id (str):
        inputs (str | Unset):
        outputs (str | Unset):
        step_name (str | Unset):
        step_image_url (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        workflow_step_edit_id=workflow_step_edit_id,
inputs=inputs,
outputs=outputs,
step_name=step_name,
step_image_url=step_image_url,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    workflow_step_edit_id: str,
    inputs: str | Unset = UNSET,
    outputs: str | Unset = UNSET,
    step_name: str | Unset = UNSET,
    step_image_url: str | Unset = UNSET,
    token: str,

) -> WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate | None:
    """  Update the configuration for a workflow extension step.

    Args:
        workflow_step_edit_id (str):
        inputs (str | Unset):
        outputs (str | Unset):
        step_name (str | Unset):
        step_image_url (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate
     """


    return sync_detailed(
        client=client,
workflow_step_edit_id=workflow_step_edit_id,
inputs=inputs,
outputs=outputs,
step_name=step_name,
step_image_url=step_image_url,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workflow_step_edit_id: str,
    inputs: str | Unset = UNSET,
    outputs: str | Unset = UNSET,
    step_name: str | Unset = UNSET,
    step_image_url: str | Unset = UNSET,
    token: str,

) -> Response[WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate]:
    """  Update the configuration for a workflow extension step.

    Args:
        workflow_step_edit_id (str):
        inputs (str | Unset):
        outputs (str | Unset):
        step_name (str | Unset):
        step_image_url (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate]
     """


    kwargs = _get_kwargs(
        workflow_step_edit_id=workflow_step_edit_id,
inputs=inputs,
outputs=outputs,
step_name=step_name,
step_image_url=step_image_url,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    workflow_step_edit_id: str,
    inputs: str | Unset = UNSET,
    outputs: str | Unset = UNSET,
    step_name: str | Unset = UNSET,
    step_image_url: str | Unset = UNSET,
    token: str,

) -> WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate | None:
    """  Update the configuration for a workflow extension step.

    Args:
        workflow_step_edit_id (str):
        inputs (str | Unset):
        outputs (str | Unset):
        step_name (str | Unset):
        step_image_url (str | Unset):
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowsUpdateStepDefaultErrorTemplate | WorkflowsUpdateStepDefaultSuccessTemplate
     """


    return (await asyncio_detailed(
        client=client,
workflow_step_edit_id=workflow_step_edit_id,
inputs=inputs,
outputs=outputs,
step_name=step_name,
step_image_url=step_image_url,
token=token,

    )).parsed
