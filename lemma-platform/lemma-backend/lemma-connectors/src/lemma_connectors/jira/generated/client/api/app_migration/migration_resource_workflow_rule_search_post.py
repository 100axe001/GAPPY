from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflow_rules_search import WorkflowRulesSearch
from ...models.workflow_rules_search_details import WorkflowRulesSearchDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    body: WorkflowRulesSearch,
    atlassian_transfer_id: UUID,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Atlassian-Transfer-Id"] = atlassian_transfer_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/atlassian-connect/1/migration/workflow/rule/search",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | WorkflowRulesSearchDetails | None:
    if response.status_code == 200:
        response_200 = WorkflowRulesSearchDetails.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | WorkflowRulesSearchDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowRulesSearch,
    atlassian_transfer_id: UUID,

) -> Response[Any | WorkflowRulesSearchDetails]:
    """ Get workflow transition rule configurations

     Returns configurations for workflow transition rules migrated from server to cloud and owned by the
    calling Connect app.

    Args:
        atlassian_transfer_id (UUID):
        body (WorkflowRulesSearch): Details of the workflow and its transition rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowRulesSearchDetails]
     """


    kwargs = _get_kwargs(
        body=body,
atlassian_transfer_id=atlassian_transfer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowRulesSearch,
    atlassian_transfer_id: UUID,

) -> Any | WorkflowRulesSearchDetails | None:
    """ Get workflow transition rule configurations

     Returns configurations for workflow transition rules migrated from server to cloud and owned by the
    calling Connect app.

    Args:
        atlassian_transfer_id (UUID):
        body (WorkflowRulesSearch): Details of the workflow and its transition rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowRulesSearchDetails
     """


    return sync_detailed(
        client=client,
body=body,
atlassian_transfer_id=atlassian_transfer_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowRulesSearch,
    atlassian_transfer_id: UUID,

) -> Response[Any | WorkflowRulesSearchDetails]:
    """ Get workflow transition rule configurations

     Returns configurations for workflow transition rules migrated from server to cloud and owned by the
    calling Connect app.

    Args:
        atlassian_transfer_id (UUID):
        body (WorkflowRulesSearch): Details of the workflow and its transition rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowRulesSearchDetails]
     """


    kwargs = _get_kwargs(
        body=body,
atlassian_transfer_id=atlassian_transfer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowRulesSearch,
    atlassian_transfer_id: UUID,

) -> Any | WorkflowRulesSearchDetails | None:
    """ Get workflow transition rule configurations

     Returns configurations for workflow transition rules migrated from server to cloud and owned by the
    calling Connect app.

    Args:
        atlassian_transfer_id (UUID):
        body (WorkflowRulesSearch): Details of the workflow and its transition rules.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowRulesSearchDetails
     """


    return (await asyncio_detailed(
        client=client,
body=body,
atlassian_transfer_id=atlassian_transfer_id,

    )).parsed
