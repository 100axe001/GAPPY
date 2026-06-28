from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project import Project
from ...models.string_list import StringList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    expand: str | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand

    json_properties: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = []
        for properties_item_data in properties:
            properties_item = properties_item_data.to_dict()
            json_properties.append(properties_item)


    params["properties"] = json_properties


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/recent",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Project] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Project.from_dict(response_200_item_data)



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Project]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,

) -> Response[Any | list[Project]]:
    """ Get recent projects

     Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        expand (str | Unset):
        properties (list[StringList] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Project]]
     """


    kwargs = _get_kwargs(
        expand=expand,
properties=properties,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,

) -> Any | list[Project] | None:
    """ Get recent projects

     Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        expand (str | Unset):
        properties (list[StringList] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Project]
     """


    return sync_detailed(
        client=client,
expand=expand,
properties=properties,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,

) -> Response[Any | list[Project]]:
    """ Get recent projects

     Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        expand (str | Unset):
        properties (list[StringList] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Project]]
     """


    kwargs = _get_kwargs(
        expand=expand,
properties=properties,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,

) -> Any | list[Project] | None:
    """ Get recent projects

     Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        expand (str | Unset):
        properties (list[StringList] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Project]
     """


    return (await asyncio_detailed(
        client=client,
expand=expand,
properties=properties,

    )).parsed
