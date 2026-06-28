from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_project import PageBeanProject
from ...models.search_projects_action import SearchProjectsAction
from ...models.search_projects_order_by import SearchProjectsOrderBy
from ...models.search_projects_status_item import SearchProjectsStatusItem
from ...models.string_list import StringList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: SearchProjectsOrderBy | Unset = SearchProjectsOrderBy.KEY,
    id: list[int] | Unset = UNSET,
    keys: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    type_key: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    action: SearchProjectsAction | Unset = SearchProjectsAction.VIEW,
    expand: str | Unset = UNSET,
    status: list[SearchProjectsStatusItem] | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,
    property_query: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    json_keys: list[str] | Unset = UNSET
    if not isinstance(keys, Unset):
        json_keys = keys


    params["keys"] = json_keys

    params["query"] = query

    params["typeKey"] = type_key

    params["categoryId"] = category_id

    json_action: str | Unset = UNSET
    if not isinstance(action, Unset):
        json_action = action.value

    params["action"] = json_action

    params["expand"] = expand

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)


    params["status"] = json_status

    json_properties: list[dict[str, Any]] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = []
        for properties_item_data in properties:
            properties_item = properties_item_data.to_dict()
            json_properties.append(properties_item)


    params["properties"] = json_properties

    params["propertyQuery"] = property_query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanProject | None:
    if response.status_code == 200:
        response_200 = PageBeanProject.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanProject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: SearchProjectsOrderBy | Unset = SearchProjectsOrderBy.KEY,
    id: list[int] | Unset = UNSET,
    keys: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    type_key: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    action: SearchProjectsAction | Unset = SearchProjectsAction.VIEW,
    expand: str | Unset = UNSET,
    status: list[SearchProjectsStatusItem] | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,
    property_query: str | Unset = UNSET,

) -> Response[Any | PageBeanProject]:
    """ Get projects paginated

     Returns a [paginated](#pagination) list of projects visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (SearchProjectsOrderBy | Unset):  Default: SearchProjectsOrderBy.KEY.
        id (list[int] | Unset):
        keys (list[str] | Unset):
        query (str | Unset):
        type_key (str | Unset):
        category_id (int | Unset):
        action (SearchProjectsAction | Unset):  Default: SearchProjectsAction.VIEW.
        expand (str | Unset):
        status (list[SearchProjectsStatusItem] | Unset):
        properties (list[StringList] | Unset):
        property_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanProject]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
order_by=order_by,
id=id,
keys=keys,
query=query,
type_key=type_key,
category_id=category_id,
action=action,
expand=expand,
status=status,
properties=properties,
property_query=property_query,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: SearchProjectsOrderBy | Unset = SearchProjectsOrderBy.KEY,
    id: list[int] | Unset = UNSET,
    keys: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    type_key: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    action: SearchProjectsAction | Unset = SearchProjectsAction.VIEW,
    expand: str | Unset = UNSET,
    status: list[SearchProjectsStatusItem] | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,
    property_query: str | Unset = UNSET,

) -> Any | PageBeanProject | None:
    """ Get projects paginated

     Returns a [paginated](#pagination) list of projects visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (SearchProjectsOrderBy | Unset):  Default: SearchProjectsOrderBy.KEY.
        id (list[int] | Unset):
        keys (list[str] | Unset):
        query (str | Unset):
        type_key (str | Unset):
        category_id (int | Unset):
        action (SearchProjectsAction | Unset):  Default: SearchProjectsAction.VIEW.
        expand (str | Unset):
        status (list[SearchProjectsStatusItem] | Unset):
        properties (list[StringList] | Unset):
        property_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanProject
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
id=id,
keys=keys,
query=query,
type_key=type_key,
category_id=category_id,
action=action,
expand=expand,
status=status,
properties=properties,
property_query=property_query,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: SearchProjectsOrderBy | Unset = SearchProjectsOrderBy.KEY,
    id: list[int] | Unset = UNSET,
    keys: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    type_key: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    action: SearchProjectsAction | Unset = SearchProjectsAction.VIEW,
    expand: str | Unset = UNSET,
    status: list[SearchProjectsStatusItem] | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,
    property_query: str | Unset = UNSET,

) -> Response[Any | PageBeanProject]:
    """ Get projects paginated

     Returns a [paginated](#pagination) list of projects visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (SearchProjectsOrderBy | Unset):  Default: SearchProjectsOrderBy.KEY.
        id (list[int] | Unset):
        keys (list[str] | Unset):
        query (str | Unset):
        type_key (str | Unset):
        category_id (int | Unset):
        action (SearchProjectsAction | Unset):  Default: SearchProjectsAction.VIEW.
        expand (str | Unset):
        status (list[SearchProjectsStatusItem] | Unset):
        properties (list[StringList] | Unset):
        property_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanProject]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
order_by=order_by,
id=id,
keys=keys,
query=query,
type_key=type_key,
category_id=category_id,
action=action,
expand=expand,
status=status,
properties=properties,
property_query=property_query,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    order_by: SearchProjectsOrderBy | Unset = SearchProjectsOrderBy.KEY,
    id: list[int] | Unset = UNSET,
    keys: list[str] | Unset = UNSET,
    query: str | Unset = UNSET,
    type_key: str | Unset = UNSET,
    category_id: int | Unset = UNSET,
    action: SearchProjectsAction | Unset = SearchProjectsAction.VIEW,
    expand: str | Unset = UNSET,
    status: list[SearchProjectsStatusItem] | Unset = UNSET,
    properties: list[StringList] | Unset = UNSET,
    property_query: str | Unset = UNSET,

) -> Any | PageBeanProject | None:
    """ Get projects paginated

     Returns a [paginated](#pagination) list of projects visible to the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Projects are returned only where the user has one of:

     *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project.
     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        order_by (SearchProjectsOrderBy | Unset):  Default: SearchProjectsOrderBy.KEY.
        id (list[int] | Unset):
        keys (list[str] | Unset):
        query (str | Unset):
        type_key (str | Unset):
        category_id (int | Unset):
        action (SearchProjectsAction | Unset):  Default: SearchProjectsAction.VIEW.
        expand (str | Unset):
        status (list[SearchProjectsStatusItem] | Unset):
        properties (list[StringList] | Unset):
        property_query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanProject
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
order_by=order_by,
id=id,
keys=keys,
query=query,
type_key=type_key,
category_id=category_id,
action=action,
expand=expand,
status=status,
properties=properties,
property_query=property_query,

    )).parsed
