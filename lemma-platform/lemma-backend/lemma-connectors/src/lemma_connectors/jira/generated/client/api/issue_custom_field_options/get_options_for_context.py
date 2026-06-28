from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_custom_field_context_option import PageBeanCustomFieldContextOption
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id: str,
    context_id: int,
    *,
    option_id: int | Unset = UNSET,
    only_options: bool | Unset = False,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["optionId"] = option_id

    params["onlyOptions"] = only_options

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/{field_id}/context/{context_id}/option".format(field_id=quote(str(field_id), safe=""),context_id=quote(str(context_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanCustomFieldContextOption | None:
    if response.status_code == 200:
        response_200 = PageBeanCustomFieldContextOption.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanCustomFieldContextOption]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    option_id: int | Unset = UNSET,
    only_options: bool | Unset = False,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanCustomFieldContextOption]:
    """ Get custom field options (context)

     Returns a [paginated](#pagination) list of all custom field option for a context. Options are
    returned first then cascading options, in the order they display in Jira.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        option_id (int | Unset):
        only_options (bool | Unset):  Default: False.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContextOption]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
option_id=option_id,
only_options=only_options,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    option_id: int | Unset = UNSET,
    only_options: bool | Unset = False,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanCustomFieldContextOption | None:
    """ Get custom field options (context)

     Returns a [paginated](#pagination) list of all custom field option for a context. Options are
    returned first then cascading options, in the order they display in Jira.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        option_id (int | Unset):
        only_options (bool | Unset):  Default: False.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContextOption
     """


    return sync_detailed(
        field_id=field_id,
context_id=context_id,
client=client,
option_id=option_id,
only_options=only_options,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    option_id: int | Unset = UNSET,
    only_options: bool | Unset = False,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[Any | PageBeanCustomFieldContextOption]:
    """ Get custom field options (context)

     Returns a [paginated](#pagination) list of all custom field option for a context. Options are
    returned first then cascading options, in the order they display in Jira.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        option_id (int | Unset):
        only_options (bool | Unset):  Default: False.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContextOption]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
option_id=option_id,
only_options=only_options,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    option_id: int | Unset = UNSET,
    only_options: bool | Unset = False,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Any | PageBeanCustomFieldContextOption | None:
    """ Get custom field options (context)

     Returns a [paginated](#pagination) list of all custom field option for a context. Options are
    returned first then cascading options, in the order they display in Jira.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        option_id (int | Unset):
        only_options (bool | Unset):  Default: False.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContextOption
     """


    return (await asyncio_detailed(
        field_id=field_id,
context_id=context_id,
client=client,
option_id=option_id,
only_options=only_options,
start_at=start_at,
max_results=max_results,

    )).parsed
