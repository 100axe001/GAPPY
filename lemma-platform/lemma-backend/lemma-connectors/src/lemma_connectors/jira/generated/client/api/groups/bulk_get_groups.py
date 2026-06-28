from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_group_details import PageBeanGroupDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    group_id: list[str] | Unset = UNSET,
    group_name: list[str] | Unset = UNSET,
    access_type: str | Unset = UNSET,
    application_key: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_group_id: list[str] | Unset = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = group_id


    params["groupId"] = json_group_id

    json_group_name: list[str] | Unset = UNSET
    if not isinstance(group_name, Unset):
        json_group_name = group_name


    params["groupName"] = json_group_name

    params["accessType"] = access_type

    params["applicationKey"] = application_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/group/bulk",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanGroupDetails | None:
    if response.status_code == 200:
        response_200 = PageBeanGroupDetails.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanGroupDetails]:
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
    group_id: list[str] | Unset = UNSET,
    group_name: list[str] | Unset = UNSET,
    access_type: str | Unset = UNSET,
    application_key: str | Unset = UNSET,

) -> Response[Any | PageBeanGroupDetails]:
    """ Bulk get groups

     Returns a [paginated](#pagination) list of groups.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        group_id (list[str] | Unset):  Example: 3571b9a7-348f-414a-9087-8e1ea03a7df8.
        group_name (list[str] | Unset):
        access_type (str | Unset):
        application_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanGroupDetails]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
group_id=group_id,
group_name=group_name,
access_type=access_type,
application_key=application_key,

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
    group_id: list[str] | Unset = UNSET,
    group_name: list[str] | Unset = UNSET,
    access_type: str | Unset = UNSET,
    application_key: str | Unset = UNSET,

) -> Any | PageBeanGroupDetails | None:
    """ Bulk get groups

     Returns a [paginated](#pagination) list of groups.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        group_id (list[str] | Unset):  Example: 3571b9a7-348f-414a-9087-8e1ea03a7df8.
        group_name (list[str] | Unset):
        access_type (str | Unset):
        application_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanGroupDetails
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
group_id=group_id,
group_name=group_name,
access_type=access_type,
application_key=application_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    group_id: list[str] | Unset = UNSET,
    group_name: list[str] | Unset = UNSET,
    access_type: str | Unset = UNSET,
    application_key: str | Unset = UNSET,

) -> Response[Any | PageBeanGroupDetails]:
    """ Bulk get groups

     Returns a [paginated](#pagination) list of groups.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        group_id (list[str] | Unset):  Example: 3571b9a7-348f-414a-9087-8e1ea03a7df8.
        group_name (list[str] | Unset):
        access_type (str | Unset):
        application_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanGroupDetails]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
group_id=group_id,
group_name=group_name,
access_type=access_type,
application_key=application_key,

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
    group_id: list[str] | Unset = UNSET,
    group_name: list[str] | Unset = UNSET,
    access_type: str | Unset = UNSET,
    application_key: str | Unset = UNSET,

) -> Any | PageBeanGroupDetails | None:
    """ Bulk get groups

     Returns a [paginated](#pagination) list of groups.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        group_id (list[str] | Unset):  Example: 3571b9a7-348f-414a-9087-8e1ea03a7df8.
        group_name (list[str] | Unset):
        access_type (str | Unset):
        application_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanGroupDetails
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
group_id=group_id,
group_name=group_name,
access_type=access_type,
application_key=application_key,

    )).parsed
