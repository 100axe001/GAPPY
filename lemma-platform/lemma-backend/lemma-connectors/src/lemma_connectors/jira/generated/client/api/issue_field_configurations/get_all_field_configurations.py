from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_field_configuration_details import PageBeanFieldConfigurationDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    is_default: bool | Unset = False,
    query: str | Unset = '',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_id: list[int] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id


    params["id"] = json_id

    params["isDefault"] = is_default

    params["query"] = query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/fieldconfiguration",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanFieldConfigurationDetails | None:
    if response.status_code == 200:
        response_200 = PageBeanFieldConfigurationDetails.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanFieldConfigurationDetails]:
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
    id: list[int] | Unset = UNSET,
    is_default: bool | Unset = False,
    query: str | Unset = '',

) -> Response[Any | PageBeanFieldConfigurationDetails]:
    """ Get all field configurations

     Returns a [paginated](#pagination) list of field configurations. The list can be for all field
    configurations or a subset determined by any combination of these criteria:

     *  a list of field configuration item IDs.
     *  whether the field configuration is a default.
     *  whether the field configuration name or description contains a query string.

    Only field configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        is_default (bool | Unset):  Default: False.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationDetails]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
is_default=is_default,
query=query,

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
    id: list[int] | Unset = UNSET,
    is_default: bool | Unset = False,
    query: str | Unset = '',

) -> Any | PageBeanFieldConfigurationDetails | None:
    """ Get all field configurations

     Returns a [paginated](#pagination) list of field configurations. The list can be for all field
    configurations or a subset determined by any combination of these criteria:

     *  a list of field configuration item IDs.
     *  whether the field configuration is a default.
     *  whether the field configuration name or description contains a query string.

    Only field configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        is_default (bool | Unset):  Default: False.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationDetails
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
is_default=is_default,
query=query,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    id: list[int] | Unset = UNSET,
    is_default: bool | Unset = False,
    query: str | Unset = '',

) -> Response[Any | PageBeanFieldConfigurationDetails]:
    """ Get all field configurations

     Returns a [paginated](#pagination) list of field configurations. The list can be for all field
    configurations or a subset determined by any combination of these criteria:

     *  a list of field configuration item IDs.
     *  whether the field configuration is a default.
     *  whether the field configuration name or description contains a query string.

    Only field configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        is_default (bool | Unset):  Default: False.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationDetails]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
id=id,
is_default=is_default,
query=query,

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
    id: list[int] | Unset = UNSET,
    is_default: bool | Unset = False,
    query: str | Unset = '',

) -> Any | PageBeanFieldConfigurationDetails | None:
    """ Get all field configurations

     Returns a [paginated](#pagination) list of field configurations. The list can be for all field
    configurations or a subset determined by any combination of these criteria:

     *  a list of field configuration item IDs.
     *  whether the field configuration is a default.
     *  whether the field configuration name or description contains a query string.

    Only field configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        id (list[int] | Unset):
        is_default (bool | Unset):  Default: False.
        query (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationDetails
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
id=id,
is_default=is_default,
query=query,

    )).parsed
