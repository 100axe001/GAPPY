from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_types_workflow_mapping import IssueTypesWorkflowMapping
from ...models.workflow_scheme import WorkflowScheme
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: IssueTypesWorkflowMapping,
    workflow_name: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["workflowName"] = workflow_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/workflowscheme/{id}/workflow".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | WorkflowScheme | None:
    if response.status_code == 200:
        response_200 = WorkflowScheme.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | WorkflowScheme]:
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
    body: IssueTypesWorkflowMapping,
    workflow_name: str,

) -> Response[Any | WorkflowScheme]:
    """ Set issue types for workflow in workflow scheme

     Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the
    default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or
    updated with the new workflow-issue types mappings. The draft workflow scheme can be published in
    Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        workflow_name (str):
        body (IssueTypesWorkflowMapping): Details about the mapping between issue types and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
workflow_name=workflow_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: IssueTypesWorkflowMapping,
    workflow_name: str,

) -> Any | WorkflowScheme | None:
    """ Set issue types for workflow in workflow scheme

     Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the
    default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or
    updated with the new workflow-issue types mappings. The draft workflow scheme can be published in
    Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        workflow_name (str):
        body (IssueTypesWorkflowMapping): Details about the mapping between issue types and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
workflow_name=workflow_name,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: IssueTypesWorkflowMapping,
    workflow_name: str,

) -> Response[Any | WorkflowScheme]:
    """ Set issue types for workflow in workflow scheme

     Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the
    default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or
    updated with the new workflow-issue types mappings. The draft workflow scheme can be published in
    Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        workflow_name (str):
        body (IssueTypesWorkflowMapping): Details about the mapping between issue types and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
workflow_name=workflow_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: IssueTypesWorkflowMapping,
    workflow_name: str,

) -> Any | WorkflowScheme | None:
    """ Set issue types for workflow in workflow scheme

     Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the
    default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow.

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or
    updated with the new workflow-issue types mappings. The draft workflow scheme can be published in
    Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        workflow_name (str):
        body (IssueTypesWorkflowMapping): Details about the mapping between issue types and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
workflow_name=workflow_name,

    )).parsed
