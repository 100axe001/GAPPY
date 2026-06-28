from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_field_configuration_issue_type_item import PageBeanFieldConfigurationIssueTypeItem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    field_configuration_scheme_id: list[int] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_field_configuration_scheme_id: list[int] | Unset = UNSET
    if not isinstance(field_configuration_scheme_id, Unset):
        json_field_configuration_scheme_id = field_configuration_scheme_id


    params["fieldConfigurationSchemeId"] = json_field_configuration_scheme_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/fieldconfigurationscheme/mapping",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanFieldConfigurationIssueTypeItem | None:
    if response.status_code == 200:
        response_200 = PageBeanFieldConfigurationIssueTypeItem.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanFieldConfigurationIssueTypeItem]:
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
    field_configuration_scheme_id: list[int] | Unset = UNSET,

) -> Response[Any | PageBeanFieldConfigurationIssueTypeItem]:
    """ Get field configuration issue type items

     Returns a [paginated](#pagination) list of field configuration issue type items.

    Only items used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        field_configuration_scheme_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationIssueTypeItem]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
field_configuration_scheme_id=field_configuration_scheme_id,

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
    field_configuration_scheme_id: list[int] | Unset = UNSET,

) -> Any | PageBeanFieldConfigurationIssueTypeItem | None:
    """ Get field configuration issue type items

     Returns a [paginated](#pagination) list of field configuration issue type items.

    Only items used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        field_configuration_scheme_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationIssueTypeItem
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
field_configuration_scheme_id=field_configuration_scheme_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    field_configuration_scheme_id: list[int] | Unset = UNSET,

) -> Response[Any | PageBeanFieldConfigurationIssueTypeItem]:
    """ Get field configuration issue type items

     Returns a [paginated](#pagination) list of field configuration issue type items.

    Only items used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        field_configuration_scheme_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanFieldConfigurationIssueTypeItem]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,
field_configuration_scheme_id=field_configuration_scheme_id,

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
    field_configuration_scheme_id: list[int] | Unset = UNSET,

) -> Any | PageBeanFieldConfigurationIssueTypeItem | None:
    """ Get field configuration issue type items

     Returns a [paginated](#pagination) list of field configuration issue type items.

    Only items used in classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        field_configuration_scheme_id (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanFieldConfigurationIssueTypeItem
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,
field_configuration_scheme_id=field_configuration_scheme_id,

    )).parsed
