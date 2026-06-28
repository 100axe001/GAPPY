from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.get_workflow_transition_rule_configurations_types_item import GetWorkflowTransitionRuleConfigurationsTypesItem
from ...models.page_bean_workflow_transition_rules import PageBeanWorkflowTransitionRules
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    types: list[GetWorkflowTransitionRuleConfigurationsTypesItem],
    keys: list[str] | Unset = UNSET,
    workflow_names: list[str] | Unset = UNSET,
    with_tags: list[str] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_types = []
    for types_item_data in types:
        types_item = types_item_data.value
        json_types.append(types_item)


    params["types"] = json_types

    json_keys: list[str] | Unset = UNSET
    if not isinstance(keys, Unset):
        json_keys = keys


    params["keys"] = json_keys

    json_workflow_names: list[str] | Unset = UNSET
    if not isinstance(workflow_names, Unset):
        json_workflow_names = workflow_names


    params["workflowNames"] = json_workflow_names

    json_with_tags: list[str] | Unset = UNSET
    if not isinstance(with_tags, Unset):
        json_with_tags = with_tags


    params["withTags"] = json_with_tags

    params["draft"] = draft

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/workflow/rule/config",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | PageBeanWorkflowTransitionRules | None:
    if response.status_code == 200:
        response_200 = PageBeanWorkflowTransitionRules.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | PageBeanWorkflowTransitionRules]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    types: list[GetWorkflowTransitionRuleConfigurationsTypesItem],
    keys: list[str] | Unset = UNSET,
    workflow_names: list[str] | Unset = UNSET,
    with_tags: list[str] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanWorkflowTransitionRules]:
    """ Get workflow transition rule configurations

     Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be
    filtered to return only those containing workflow transition rules:

     *  of one or more transition rule types, such as [workflow post
    functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
     *  matching one or more transition rule keys.

    Only workflows containing transition rules created by the calling Connect app are returned.

    Due to server-side optimizations, workflows with an empty list of rules may be returned; these
    workflows can be ignored.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        types (list[GetWorkflowTransitionRuleConfigurationsTypesItem]):
        keys (list[str] | Unset):
        workflow_names (list[str] | Unset):
        with_tags (list[str] | Unset):
        draft (bool | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanWorkflowTransitionRules]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
types=types,
keys=keys,
workflow_names=workflow_names,
with_tags=with_tags,
draft=draft,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    types: list[GetWorkflowTransitionRuleConfigurationsTypesItem],
    keys: list[str] | Unset = UNSET,
    workflow_names: list[str] | Unset = UNSET,
    with_tags: list[str] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanWorkflowTransitionRules | None:
    """ Get workflow transition rule configurations

     Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be
    filtered to return only those containing workflow transition rules:

     *  of one or more transition rule types, such as [workflow post
    functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
     *  matching one or more transition rule keys.

    Only workflows containing transition rules created by the calling Connect app are returned.

    Due to server-side optimizations, workflows with an empty list of rules may be returned; these
    workflows can be ignored.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        types (list[GetWorkflowTransitionRuleConfigurationsTypesItem]):
        keys (list[str] | Unset):
        workflow_names (list[str] | Unset):
        with_tags (list[str] | Unset):
        draft (bool | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanWorkflowTransitionRules
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
types=types,
keys=keys,
workflow_names=workflow_names,
with_tags=with_tags,
draft=draft,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    types: list[GetWorkflowTransitionRuleConfigurationsTypesItem],
    keys: list[str] | Unset = UNSET,
    workflow_names: list[str] | Unset = UNSET,
    with_tags: list[str] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | PageBeanWorkflowTransitionRules]:
    """ Get workflow transition rule configurations

     Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be
    filtered to return only those containing workflow transition rules:

     *  of one or more transition rule types, such as [workflow post
    functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
     *  matching one or more transition rule keys.

    Only workflows containing transition rules created by the calling Connect app are returned.

    Due to server-side optimizations, workflows with an empty list of rules may be returned; these
    workflows can be ignored.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        types (list[GetWorkflowTransitionRuleConfigurationsTypesItem]):
        keys (list[str] | Unset):
        workflow_names (list[str] | Unset):
        with_tags (list[str] | Unset):
        draft (bool | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | PageBeanWorkflowTransitionRules]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
types=types,
keys=keys,
workflow_names=workflow_names,
with_tags=with_tags,
draft=draft,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 10,
    types: list[GetWorkflowTransitionRuleConfigurationsTypesItem],
    keys: list[str] | Unset = UNSET,
    workflow_names: list[str] | Unset = UNSET,
    with_tags: list[str] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | PageBeanWorkflowTransitionRules | None:
    """ Get workflow transition rule configurations

     Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be
    filtered to return only those containing workflow transition rules:

     *  of one or more transition rule types, such as [workflow post
    functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
     *  matching one or more transition rule keys.

    Only workflows containing transition rules created by the calling Connect app are returned.

    Due to server-side optimizations, workflows with an empty list of rules may be returned; these
    workflows can be ignored.

    **[Permissions](#permissions) required:** Only Connect apps can use this operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 10.
        types (list[GetWorkflowTransitionRuleConfigurationsTypesItem]):
        keys (list[str] | Unset):
        workflow_names (list[str] | Unset):
        with_tags (list[str] | Unset):
        draft (bool | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | PageBeanWorkflowTransitionRules
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
types=types,
keys=keys,
workflow_names=workflow_names,
with_tags=with_tags,
draft=draft,
expand=expand,

    )).parsed
