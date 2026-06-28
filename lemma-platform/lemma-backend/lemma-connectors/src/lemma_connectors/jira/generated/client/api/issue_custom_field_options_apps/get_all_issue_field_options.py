from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_issue_field_option import PageBeanIssueFieldOption
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_key: str,
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
        "url": "/rest/api/3/field/{field_key}/option".format(field_key=quote(str(field_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueFieldOption | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueFieldOption.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueFieldOption]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanIssueFieldOption]:
    """ Get all issue field options

     Returns a [paginated](#pagination) list of all the options of a select list issue field. A select
    list issue field is a type of [issue
    field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user
    to select a value from a list of options.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanIssueFieldOption | None:
    """ Get all issue field options

     Returns a [paginated](#pagination) list of all the options of a select list issue field. A select
    list issue field is a type of [issue
    field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user
    to select a value from a list of options.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueFieldOption
     """


    return sync_detailed(
        field_key=field_key,
client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanIssueFieldOption]:
    """ Get all issue field options

     Returns a [paginated](#pagination) list of all the options of a select list issue field. A select
    list issue field is a type of [issue
    field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user
    to select a value from a list of options.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_key: str,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanIssueFieldOption | None:
    """ Get all issue field options

     Returns a [paginated](#pagination) list of all the options of a select list issue field. A select
    list issue field is a type of [issue
    field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user
    to select a value from a list of options.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueFieldOption
     """


    return (await asyncio_detailed(
        field_key=field_key,
client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
