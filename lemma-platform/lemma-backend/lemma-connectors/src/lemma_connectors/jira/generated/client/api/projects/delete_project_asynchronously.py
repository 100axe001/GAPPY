from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.task_progress_bean_object import TaskProgressBeanObject
from typing import cast



def _get_kwargs(
    project_id_or_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/project/{project_id_or_key}/delete".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TaskProgressBeanObject | None:
    if response.status_code == 303:
        response_303 = TaskProgressBeanObject.from_dict(response.json())



        return response_303

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | TaskProgressBeanObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | TaskProgressBeanObject]:
    """ Delete project asynchronously

     Deletes a project asynchronously.

    This operation is:

     *  transactional, that is, if part of the delete fails the project is not deleted.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | TaskProgressBeanObject | None:
    """ Delete project asynchronously

     Deletes a project asynchronously.

    This operation is:

     *  transactional, that is, if part of the delete fails the project is not deleted.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | TaskProgressBeanObject]:
    """ Delete project asynchronously

     Deletes a project asynchronously.

    This operation is:

     *  transactional, that is, if part of the delete fails the project is not deleted.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | TaskProgressBeanObject | None:
    """ Delete project asynchronously

     Deletes a project asynchronously.

    This operation is:

     *  transactional, that is, if part of the delete fails the project is not deleted.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        project_id_or_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,

    )).parsed
