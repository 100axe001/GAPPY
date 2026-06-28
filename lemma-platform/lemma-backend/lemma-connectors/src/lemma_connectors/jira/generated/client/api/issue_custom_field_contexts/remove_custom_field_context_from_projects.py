from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_ids import ProjectIds
from typing import cast



def _get_kwargs(
    field_id: str,
    context_id: int,
    *,
    body: ProjectIds,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/field/{field_id}/context/{context_id}/project/remove".format(field_id=quote(str(field_id), safe=""),context_id=quote(str(context_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectIds,

) -> Response[Any]:
    """ Remove custom field context from projects

     Removes a custom field context from projects.

    A custom field context without any projects applies to all projects. Removing all projects from a
    custom field context would result in it applying to all projects.

    If any project in the request is not assigned to the context, or the operation would result in two
    global contexts for the field, the operation fails.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (ProjectIds): A list of project IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectIds,

) -> Response[Any]:
    """ Remove custom field context from projects

     Removes a custom field context from projects.

    A custom field context without any projects applies to all projects. Removing all projects from a
    custom field context would result in it applying to all projects.

    If any project in the request is not assigned to the context, or the operation would result in two
    global contexts for the field, the operation fails.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (ProjectIds): A list of project IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

