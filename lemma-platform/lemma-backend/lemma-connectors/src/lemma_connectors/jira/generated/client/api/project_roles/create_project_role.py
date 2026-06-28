from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_update_role_request_bean import CreateUpdateRoleRequestBean
from ...models.project_role import ProjectRole
from typing import cast



def _get_kwargs(
    *,
    body: CreateUpdateRoleRequestBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/role",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectRole | None:
    if response.status_code == 200:
        response_200 = ProjectRole.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectRole]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateRoleRequestBean,

) -> Response[Any | ProjectRole]:
    """ Create project role

     Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the
    [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default
    actors to the project role after creating it.

    *Note that although a new project role is available to all projects upon creation, any default
    actors that are associated with the project role are not added to projects that existed prior to the
    role being created.*<

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateUpdateRoleRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
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
    body: CreateUpdateRoleRequestBean,

) -> Any | ProjectRole | None:
    """ Create project role

     Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the
    [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default
    actors to the project role after creating it.

    *Note that although a new project role is available to all projects upon creation, any default
    actors that are associated with the project role are not added to projects that existed prior to the
    role being created.*<

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateUpdateRoleRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateRoleRequestBean,

) -> Response[Any | ProjectRole]:
    """ Create project role

     Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the
    [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default
    actors to the project role after creating it.

    *Note that although a new project role is available to all projects upon creation, any default
    actors that are associated with the project role are not added to projects that existed prior to the
    role being created.*<

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateUpdateRoleRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectRole]
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
    body: CreateUpdateRoleRequestBean,

) -> Any | ProjectRole | None:
    """ Create project role

     Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the
    [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default
    actors to the project role after creating it.

    *Note that although a new project role is available to all projects upon creation, any default
    actors that are associated with the project role are not added to projects that existed prior to the
    role being created.*<

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateUpdateRoleRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectRole
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
