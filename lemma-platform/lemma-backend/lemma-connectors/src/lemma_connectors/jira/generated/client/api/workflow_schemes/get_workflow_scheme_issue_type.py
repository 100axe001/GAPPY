from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_workflow_mapping import IssueTypeWorkflowMapping
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    issue_type: str,
    *,
    return_draft_if_exists: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["returnDraftIfExists"] = return_draft_if_exists


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/workflowscheme/{id}/issuetype/{issue_type}".format(id=quote(str(id), safe=""),issue_type=quote(str(issue_type), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueTypeWorkflowMapping | None:
    if response.status_code == 200:
        response_200 = IssueTypeWorkflowMapping.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueTypeWorkflowMapping]:
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
    return_draft_if_exists: bool | Unset = False,

) -> Response[Any | IssueTypeWorkflowMapping]:
    """ Get workflow for issue type in workflow scheme

     Returns the issue type-workflow mapping for an issue type in a workflow scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        return_draft_if_exists (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueTypeWorkflowMapping]
     """


    kwargs = _get_kwargs(
        id=id,
issue_type=issue_type,
return_draft_if_exists=return_draft_if_exists,

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
    return_draft_if_exists: bool | Unset = False,

) -> Any | IssueTypeWorkflowMapping | None:
    """ Get workflow for issue type in workflow scheme

     Returns the issue type-workflow mapping for an issue type in a workflow scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        return_draft_if_exists (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueTypeWorkflowMapping
     """


    return sync_detailed(
        id=id,
issue_type=issue_type,
client=client,
return_draft_if_exists=return_draft_if_exists,

    ).parsed

async def asyncio_detailed(
    id: int,
    issue_type: str,
    *,
    client: AuthenticatedClient,
    return_draft_if_exists: bool | Unset = False,

) -> Response[Any | IssueTypeWorkflowMapping]:
    """ Get workflow for issue type in workflow scheme

     Returns the issue type-workflow mapping for an issue type in a workflow scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        return_draft_if_exists (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueTypeWorkflowMapping]
     """


    kwargs = _get_kwargs(
        id=id,
issue_type=issue_type,
return_draft_if_exists=return_draft_if_exists,

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
    return_draft_if_exists: bool | Unset = False,

) -> Any | IssueTypeWorkflowMapping | None:
    """ Get workflow for issue type in workflow scheme

     Returns the issue type-workflow mapping for an issue type in a workflow scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        issue_type (str):
        return_draft_if_exists (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueTypeWorkflowMapping
     """


    return (await asyncio_detailed(
        id=id,
issue_type=issue_type,
client=client,
return_draft_if_exists=return_draft_if_exists,

    )).parsed
