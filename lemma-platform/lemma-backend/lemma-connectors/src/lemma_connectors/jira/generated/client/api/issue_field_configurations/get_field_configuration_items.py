from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_field_configuration_item import PageBeanFieldConfigurationItem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/fieldconfiguration/{id}/fields".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanFieldConfigurationItem | None:
    if response.status_code == 200:
        response_200 = PageBeanFieldConfigurationItem.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanFieldConfigurationItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanFieldConfigurationItem]:
    """ Get field configuration items

     Returns a [paginated](#pagination) list of all fields for a configuration.

    Only the fields from configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationItem]
     """


    kwargs = _get_kwargs(
        id=id,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanFieldConfigurationItem | None:
    """ Get field configuration items

     Returns a [paginated](#pagination) list of all fields for a configuration.

    Only the fields from configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationItem
     """


    return sync_detailed(
        id=id,
client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanFieldConfigurationItem]:
    """ Get field configuration items

     Returns a [paginated](#pagination) list of all fields for a configuration.

    Only the fields from configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationItem]
     """


    kwargs = _get_kwargs(
        id=id,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanFieldConfigurationItem | None:
    """ Get field configuration items

     Returns a [paginated](#pagination) list of all fields for a configuration.

    Only the fields from configurations used in company-managed (classic) projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationItem
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
