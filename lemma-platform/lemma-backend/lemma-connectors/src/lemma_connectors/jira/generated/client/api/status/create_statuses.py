from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.jira_status import JiraStatus
from ...models.status_create_request import StatusCreateRequest
from typing import cast



def _get_kwargs(
    *,
    body: StatusCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/statuses",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[JiraStatus] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = JiraStatus.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[JiraStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StatusCreateRequest,

) -> Response[Any | list[JiraStatus]]:
    """ Bulk create statuses

     Creates statuses for a global or project scope.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        body (StatusCreateRequest): Details of the statuses being created and their scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[JiraStatus]]
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
    body: StatusCreateRequest,

) -> Any | list[JiraStatus] | None:
    """ Bulk create statuses

     Creates statuses for a global or project scope.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        body (StatusCreateRequest): Details of the statuses being created and their scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[JiraStatus]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StatusCreateRequest,

) -> Response[Any | list[JiraStatus]]:
    """ Bulk create statuses

     Creates statuses for a global or project scope.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        body (StatusCreateRequest): Details of the statuses being created and their scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[JiraStatus]]
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
    body: StatusCreateRequest,

) -> Any | list[JiraStatus] | None:
    """ Bulk create statuses

     Creates statuses for a global or project scope.

    **[Permissions](#permissions) required:**

     *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
     *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    Args:
        body (StatusCreateRequest): Details of the statuses being created and their scope.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[JiraStatus]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
