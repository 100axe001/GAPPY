from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflow_scheme import WorkflowScheme
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    update_draft_if_needed: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["updateDraftIfNeeded"] = update_draft_if_needed


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/workflowscheme/{id}/default".format(id=quote(str(id), safe=""),),
        "params": params,
    }


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
    update_draft_if_needed: bool | Unset = UNSET,

) -> Response[Any | WorkflowScheme]:
    """ Delete default workflow

     Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's
    system workflow (the *jira* workflow).

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default
    workflow reset. The draft workflow scheme can be published in Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        update_draft_if_needed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
update_draft_if_needed=update_draft_if_needed,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    update_draft_if_needed: bool | Unset = UNSET,

) -> Any | WorkflowScheme | None:
    """ Delete default workflow

     Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's
    system workflow (the *jira* workflow).

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default
    workflow reset. The draft workflow scheme can be published in Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        update_draft_if_needed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return sync_detailed(
        id=id,
client=client,
update_draft_if_needed=update_draft_if_needed,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    update_draft_if_needed: bool | Unset = UNSET,

) -> Response[Any | WorkflowScheme]:
    """ Delete default workflow

     Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's
    system workflow (the *jira* workflow).

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default
    workflow reset. The draft workflow scheme can be published in Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        update_draft_if_needed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowScheme]
     """


    kwargs = _get_kwargs(
        id=id,
update_draft_if_needed=update_draft_if_needed,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    update_draft_if_needed: bool | Unset = UNSET,

) -> Any | WorkflowScheme | None:
    """ Delete default workflow

     Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's
    system workflow (the *jira* workflow).

    Note that active workflow schemes cannot be edited. If the workflow scheme is active, set
    `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default
    workflow reset. The draft workflow scheme can be published in Jira.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        update_draft_if_needed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowScheme
     """


    return (await asyncio_detailed(
        id=id,
client=client,
update_draft_if_needed=update_draft_if_needed,

    )).parsed
