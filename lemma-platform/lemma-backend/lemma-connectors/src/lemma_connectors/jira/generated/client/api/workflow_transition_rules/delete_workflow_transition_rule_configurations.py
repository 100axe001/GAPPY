from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.workflow_transition_rules_update_errors import WorkflowTransitionRulesUpdateErrors
from ...models.workflows_with_transition_rules_details import WorkflowsWithTransitionRulesDetails
from typing import cast



def _get_kwargs(
    *,
    body: WorkflowsWithTransitionRulesDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/workflow/rule/config/delete",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | WorkflowTransitionRulesUpdateErrors | None:
    if response.status_code == 200:
        response_200 = WorkflowTransitionRulesUpdateErrors.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WorkflowsWithTransitionRulesDetails,

) -> Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]:
    """ Delete workflow transition rule configurations

     Deletes workflow transition rules from one or more workflows. These rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be deleted.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowsWithTransitionRulesDetails): Details of workflows and their transition
            rules to delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: WorkflowsWithTransitionRulesDetails,

) -> ErrorCollection | WorkflowTransitionRulesUpdateErrors | None:
    """ Delete workflow transition rule configurations

     Deletes workflow transition rules from one or more workflows. These rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be deleted.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowsWithTransitionRulesDetails): Details of workflows and their transition
            rules to delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | WorkflowTransitionRulesUpdateErrors
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WorkflowsWithTransitionRulesDetails,

) -> Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]:
    """ Delete workflow transition rule configurations

     Deletes workflow transition rules from one or more workflows. These rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be deleted.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowsWithTransitionRulesDetails): Details of workflows and their transition
            rules to delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WorkflowsWithTransitionRulesDetails,

) -> ErrorCollection | WorkflowTransitionRulesUpdateErrors | None:
    """ Delete workflow transition rule configurations

     Deletes workflow transition rules from one or more workflows. These rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be deleted.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowsWithTransitionRulesDetails): Details of workflows and their transition
            rules to delete.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | WorkflowTransitionRulesUpdateErrors
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
