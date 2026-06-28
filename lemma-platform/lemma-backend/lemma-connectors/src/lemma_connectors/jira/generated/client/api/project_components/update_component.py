from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_component import ProjectComponent
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ProjectComponent,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/component/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectComponent | None:
    if response.status_code == 200:
        response_200 = ProjectComponent.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectComponent]:
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
    body: ProjectComponent,

) -> Response[Any | ProjectComponent]:
    r""" Update component

     Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an
    empty string (\"\") the component lead is removed.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or
    *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        body (ProjectComponent): Details about a project component.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectComponent]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectComponent,

) -> Any | ProjectComponent | None:
    r""" Update component

     Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an
    empty string (\"\") the component lead is removed.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or
    *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        body (ProjectComponent): Details about a project component.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectComponent
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectComponent,

) -> Response[Any | ProjectComponent]:
    r""" Update component

     Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an
    empty string (\"\") the component lead is removed.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or
    *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        body (ProjectComponent): Details about a project component.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectComponent]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectComponent,

) -> Any | ProjectComponent | None:
    r""" Update component

     Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an
    empty string (\"\") the component lead is removed.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or
    *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):
        body (ProjectComponent): Details about a project component.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectComponent
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
