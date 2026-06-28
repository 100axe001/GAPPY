from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_workflow_mapping import IssueTypeWorkflowMapping
from ...models.workflow_scheme import WorkflowScheme
from typing import cast



def _get_kwargs(
    id: int,
    issue_type: str,
    *,
    body: IssueTypeWorkflowMapping,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/workflowscheme/{id}/draft/issuetype/{issue_type}".format(id=quote(str(id), safe=""),issue_type=quote(str(issue_type), safe=""),),
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
    issue_type: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeWorkflowMapping,

) -> Response[Any | WorkflowScheme]:
    """ Set workflow for issue type in draft workflow scheme

     Sets the workflow for an issue type in a workflow scheme's draft.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        body (IssueTypeWorkflowMapping): Details about the mapping between an issue type and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
issue_type=issue_type,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    issue_type: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeWorkflowMapping,

) -> Any | WorkflowScheme | None:
    """ Set workflow for issue type in draft workflow scheme

     Sets the workflow for an issue type in a workflow scheme's draft.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        body (IssueTypeWorkflowMapping): Details about the mapping between an issue type and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return sync_detailed(
        id=id,
issue_type=issue_type,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    issue_type: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeWorkflowMapping,

) -> Response[Any | WorkflowScheme]:
    """ Set workflow for issue type in draft workflow scheme

     Sets the workflow for an issue type in a workflow scheme's draft.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        body (IssueTypeWorkflowMapping): Details about the mapping between an issue type and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
issue_type=issue_type,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    issue_type: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeWorkflowMapping,

) -> Any | WorkflowScheme | None:
    """ Set workflow for issue type in draft workflow scheme

     Sets the workflow for an issue type in a workflow scheme's draft.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        body (IssueTypeWorkflowMapping): Details about the mapping between an issue type and a
            workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return (await asyncio_detailed(
        id=id,
issue_type=issue_type,
client=client,
body=body,

    )).parsed
