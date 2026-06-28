from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.workflow_transition_rules_update import WorkflowTransitionRulesUpdate
from ...models.workflow_transition_rules_update_errors import WorkflowTransitionRulesUpdateErrors
from typing import cast



def _get_kwargs(
    *,
    body: WorkflowTransitionRulesUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/workflow/rule/config",
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
    body: WorkflowTransitionRulesUpdate,

) -> Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]:
    """ Update workflow transition rule configurations

     Updates configuration of workflow transition rules. The following rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be updated.

    To assist with app migration, this operation can be used to:

     *  Disable a rule.
     *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule
    configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-
    transition-rules/#api-rest-api-3-workflow-rule-config-get).

    Rules are enabled if the `disabled` parameter is not provided.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowTransitionRulesUpdate): Details about a workflow configuration update
            request.

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
    body: WorkflowTransitionRulesUpdate,

) -> ErrorCollection | WorkflowTransitionRulesUpdateErrors | None:
    """ Update workflow transition rule configurations

     Updates configuration of workflow transition rules. The following rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be updated.

    To assist with app migration, this operation can be used to:

     *  Disable a rule.
     *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule
    configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-
    transition-rules/#api-rest-api-3-workflow-rule-config-get).

    Rules are enabled if the `disabled` parameter is not provided.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowTransitionRulesUpdate): Details about a workflow configuration update
            request.

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
    body: WorkflowTransitionRulesUpdate,

) -> Response[ErrorCollection | WorkflowTransitionRulesUpdateErrors]:
    """ Update workflow transition rule configurations

     Updates configuration of workflow transition rules. The following rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be updated.

    To assist with app migration, this operation can be used to:

     *  Disable a rule.
     *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule
    configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-
    transition-rules/#api-rest-api-3-workflow-rule-config-get).

    Rules are enabled if the `disabled` parameter is not provided.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowTransitionRulesUpdate): Details about a workflow configuration update
            request.

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
    body: WorkflowTransitionRulesUpdate,

) -> ErrorCollection | WorkflowTransitionRulesUpdateErrors | None:
    """ Update workflow transition rule configurations

     Updates configuration of workflow transition rules. The following rule types are supported:

     *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-
    function/)
     *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
     *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

    Only rules created by the calling Connect app can be updated.

    To assist with app migration, this operation can be used to:

     *  Disable a rule.
     *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule
    configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-
    transition-rules/#api-rest-api-3-workflow-rule-config-get).

    Rules are enabled if the `disabled` parameter is not provided.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        body (WorkflowTransitionRulesUpdate): Details about a workflow configuration update
            request.

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
