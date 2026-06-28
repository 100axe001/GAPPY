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
    task_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/task/{task_id}".format(task_id=quote(str(task_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | TaskProgressBeanObject | None:
    if response.status_code == 200:
        response_200 = TaskProgressBeanObject.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | TaskProgressBeanObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | TaskProgressBeanObject]:
    """ Get task

     Returns the status of a [long-running asynchronous task](#async).

    When a task has finished, this operation returns the JSON blob applicable to the task. See the
    documentation of the operation that created the task for details. Task details are not permanently
    retained. As of September 2019, details are retained for 14 days although this period may change
    without notice.

    **[Permissions](#permissions) required:** either of:

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  Creator of the task.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    task_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | TaskProgressBeanObject | None:
    """ Get task

     Returns the status of a [long-running asynchronous task](#async).

    When a task has finished, this operation returns the JSON blob applicable to the task. See the
    documentation of the operation that created the task for details. Task details are not permanently
    retained. As of September 2019, details are retained for 14 days although this period may change
    without notice.

    **[Permissions](#permissions) required:** either of:

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  Creator of the task.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return sync_detailed(
        task_id=task_id,
client=client,

    ).parsed

async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | TaskProgressBeanObject]:
    """ Get task

     Returns the status of a [long-running asynchronous task](#async).

    When a task has finished, this operation returns the JSON blob applicable to the task. See the
    documentation of the operation that created the task for details. Task details are not permanently
    retained. As of September 2019, details are retained for 14 days although this period may change
    without notice.

    **[Permissions](#permissions) required:** either of:

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  Creator of the task.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaskProgressBeanObject]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | TaskProgressBeanObject | None:
    """ Get task

     Returns the status of a [long-running asynchronous task](#async).

    When a task has finished, this operation returns the JSON blob applicable to the task. See the
    documentation of the operation that created the task for details. Task details are not permanently
    retained. As of September 2019, details are retained for 14 days although this period may change
    without notice.

    **[Permissions](#permissions) required:** either of:

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  Creator of the task.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaskProgressBeanObject
     """


    return (await asyncio_detailed(
        task_id=task_id,
client=client,

    )).parsed
