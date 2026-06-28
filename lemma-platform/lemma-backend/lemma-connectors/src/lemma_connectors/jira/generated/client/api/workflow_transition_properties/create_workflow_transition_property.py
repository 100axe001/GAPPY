from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_workflow_transition_property_workflow_mode import CreateWorkflowTransitionPropertyWorkflowMode
from ...models.workflow_transition_property import WorkflowTransitionProperty
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    transition_id: int,
    *,
    body: WorkflowTransitionProperty,
    key: str,
    workflow_name: str,
    workflow_mode: CreateWorkflowTransitionPropertyWorkflowMode | Unset = CreateWorkflowTransitionPropertyWorkflowMode.LIVE,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["key"] = key

    params["workflowName"] = workflow_name

    json_workflow_mode: str | Unset = UNSET
    if not isinstance(workflow_mode, Unset):
        json_workflow_mode = workflow_mode.value

    params["workflowMode"] = json_workflow_mode


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/workflow/transitions/{transition_id}/properties".format(transition_id=quote(str(transition_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | WorkflowTransitionProperty | None:
    if response.status_code == 200:
        response_200 = WorkflowTransitionProperty.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | WorkflowTransitionProperty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transition_id: int,
    *,
    client: AuthenticatedClient,
    body: WorkflowTransitionProperty,
    key: str,
    workflow_name: str,
    workflow_mode: CreateWorkflowTransitionPropertyWorkflowMode | Unset = CreateWorkflowTransitionPropertyWorkflowMode.LIVE,

) -> Response[Any | WorkflowTransitionProperty]:
    """ Create workflow transition property

     Adds a property to a workflow transition. Transition properties are used to change the behavior of a
    transition. For more information, see [Transition
    properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-
    transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        transition_id (int):
        key (str):
        workflow_name (str):
        workflow_mode (CreateWorkflowTransitionPropertyWorkflowMode | Unset):  Default:
            CreateWorkflowTransitionPropertyWorkflowMode.LIVE.
        body (WorkflowTransitionProperty): Details about the server Jira is running on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowTransitionProperty]
     """


    kwargs = _get_kwargs(
        transition_id=transition_id,
body=body,
key=key,
workflow_name=workflow_name,
workflow_mode=workflow_mode,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    transition_id: int,
    *,
    client: AuthenticatedClient,
    body: WorkflowTransitionProperty,
    key: str,
    workflow_name: str,
    workflow_mode: CreateWorkflowTransitionPropertyWorkflowMode | Unset = CreateWorkflowTransitionPropertyWorkflowMode.LIVE,

) -> Any | WorkflowTransitionProperty | None:
    """ Create workflow transition property

     Adds a property to a workflow transition. Transition properties are used to change the behavior of a
    transition. For more information, see [Transition
    properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-
    transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        transition_id (int):
        key (str):
        workflow_name (str):
        workflow_mode (CreateWorkflowTransitionPropertyWorkflowMode | Unset):  Default:
            CreateWorkflowTransitionPropertyWorkflowMode.LIVE.
        body (WorkflowTransitionProperty): Details about the server Jira is running on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowTransitionProperty
     """


    return sync_detailed(
        transition_id=transition_id,
client=client,
body=body,
key=key,
workflow_name=workflow_name,
workflow_mode=workflow_mode,

    ).parsed

async def asyncio_detailed(
    transition_id: int,
    *,
    client: AuthenticatedClient,
    body: WorkflowTransitionProperty,
    key: str,
    workflow_name: str,
    workflow_mode: CreateWorkflowTransitionPropertyWorkflowMode | Unset = CreateWorkflowTransitionPropertyWorkflowMode.LIVE,

) -> Response[Any | WorkflowTransitionProperty]:
    """ Create workflow transition property

     Adds a property to a workflow transition. Transition properties are used to change the behavior of a
    transition. For more information, see [Transition
    properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-
    transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        transition_id (int):
        key (str):
        workflow_name (str):
        workflow_mode (CreateWorkflowTransitionPropertyWorkflowMode | Unset):  Default:
            CreateWorkflowTransitionPropertyWorkflowMode.LIVE.
        body (WorkflowTransitionProperty): Details about the server Jira is running on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowTransitionProperty]
     """


    kwargs = _get_kwargs(
        transition_id=transition_id,
body=body,
key=key,
workflow_name=workflow_name,
workflow_mode=workflow_mode,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    transition_id: int,
    *,
    client: AuthenticatedClient,
    body: WorkflowTransitionProperty,
    key: str,
    workflow_name: str,
    workflow_mode: CreateWorkflowTransitionPropertyWorkflowMode | Unset = CreateWorkflowTransitionPropertyWorkflowMode.LIVE,

) -> Any | WorkflowTransitionProperty | None:
    """ Create workflow transition property

     Adds a property to a workflow transition. Transition properties are used to change the behavior of a
    transition. For more information, see [Transition
    properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-
    transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        transition_id (int):
        key (str):
        workflow_name (str):
        workflow_mode (CreateWorkflowTransitionPropertyWorkflowMode | Unset):  Default:
            CreateWorkflowTransitionPropertyWorkflowMode.LIVE.
        body (WorkflowTransitionProperty): Details about the server Jira is running on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowTransitionProperty
     """


    return (await asyncio_detailed(
        transition_id=transition_id,
client=client,
body=body,
key=key,
workflow_name=workflow_name,
workflow_mode=workflow_mode,

    )).parsed
