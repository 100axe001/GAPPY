from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.task_progress_bean_object import TaskProgressBeanObject
from typing import cast



def _get_kwargs(
    id: str,
    *,
    replace_with: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["replaceWith"] = replace_with


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/rest/api/3/priority/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | TaskProgressBeanObject | None:
    if response.status_code == 303:
        response_303 = TaskProgressBeanObject.from_dict(response.json())



        return response_303

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ErrorCollection.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | TaskProgressBeanObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    replace_with: str,

) -> Response[ErrorCollection | TaskProgressBeanObject]:
    """ Delete priority

     Deletes an issue priority.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent
    updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        replace_with (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        id=id,
replace_with=replace_with,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    replace_with: str,

) -> ErrorCollection | TaskProgressBeanObject | None:
    """ Delete priority

     Deletes an issue priority.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent
    updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        replace_with (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | TaskProgressBeanObject
     """


    return sync_detailed(
        id=id,
client=client,
replace_with=replace_with,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    replace_with: str,

) -> Response[ErrorCollection | TaskProgressBeanObject]:
    """ Delete priority

     Deletes an issue priority.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent
    updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        replace_with (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        id=id,
replace_with=replace_with,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    replace_with: str,

) -> ErrorCollection | TaskProgressBeanObject | None:
    """ Delete priority

     Deletes an issue priority.

    This operation is [asynchronous](#async). Follow the `location` link in the response to determine
    the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent
    updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        replace_with (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | TaskProgressBeanObject
     """


    return (await asyncio_detailed(
        id=id,
client=client,
replace_with=replace_with,

    )).parsed
