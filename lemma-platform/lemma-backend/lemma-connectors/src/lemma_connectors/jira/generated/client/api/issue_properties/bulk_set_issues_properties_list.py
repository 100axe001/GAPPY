from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.issue_entity_properties import IssueEntityProperties
from typing import cast



def _get_kwargs(
    *,
    body: IssueEntityProperties,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issue/properties",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | None:
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueEntityProperties,

) -> Response[Any | ErrorCollection]:
    """ Bulk set issues properties by list

     Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can
    be specified along with up to 10,000 issues on which to set or update that list of entity
    properties.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.
    The maximum length of single issue property value is 32768 characters. This operation can be
    accessed anonymously.

    This operation is:

     *  transactional, either all properties are updated in all eligible issues or, when errors occur,
    no properties are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueEntityProperties): Lists of issues and entity properties. See [Entity
            properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/)
            for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
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
    body: IssueEntityProperties,

) -> Any | ErrorCollection | None:
    """ Bulk set issues properties by list

     Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can
    be specified along with up to 10,000 issues on which to set or update that list of entity
    properties.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.
    The maximum length of single issue property value is 32768 characters. This operation can be
    accessed anonymously.

    This operation is:

     *  transactional, either all properties are updated in all eligible issues or, when errors occur,
    no properties are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueEntityProperties): Lists of issues and entity properties. See [Entity
            properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/)
            for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueEntityProperties,

) -> Response[Any | ErrorCollection]:
    """ Bulk set issues properties by list

     Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can
    be specified along with up to 10,000 issues on which to set or update that list of entity
    properties.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.
    The maximum length of single issue property value is 32768 characters. This operation can be
    accessed anonymously.

    This operation is:

     *  transactional, either all properties are updated in all eligible issues or, when errors occur,
    no properties are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueEntityProperties): Lists of issues and entity properties. See [Entity
            properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/)
            for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection]
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
    body: IssueEntityProperties,

) -> Any | ErrorCollection | None:
    """ Bulk set issues properties by list

     Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can
    be specified along with up to 10,000 issues on which to set or update that list of entity
    properties.

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.
    The maximum length of single issue property value is 32768 characters. This operation can be
    accessed anonymously.

    This operation is:

     *  transactional, either all properties are updated in all eligible issues or, when errors occur,
    no properties are updated.
     *  [asynchronous](#async). Follow the `location` link in the response to determine the status of
    the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

    **[Permissions](#permissions) required:**

     *  *Browse projects* and *Edit issues* [project
    permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        body (IssueEntityProperties): Lists of issues and entity properties. See [Entity
            properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/)
            for more information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
