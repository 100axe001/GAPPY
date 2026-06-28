from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_bean import IssueBean
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_id_or_key: str,
    *,
    fields: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    update_history: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields


    params["fields"] = json_fields

    params["fieldsByKeys"] = fields_by_keys

    params["expand"] = expand

    json_properties: list[str] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties


    params["properties"] = json_properties

    params["updateHistory"] = update_history


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issue/{issue_id_or_key}".format(issue_id_or_key=quote(str(issue_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueBean | None:
    if response.status_code == 200:
        response_200 = IssueBean.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueBean]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    update_history: bool | Unset = False,

) -> Response[Any | IssueBean]:
    """ Get issue

     Returns the details for an issue.

    The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-
    insensitive search and check for moved issues is performed. If a matching issue is found its details
    are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is
    the key of the issue found.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        fields (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.
        expand (str | Unset):
        properties (list[str] | Unset):
        update_history (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueBean]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
fields=fields,
fields_by_keys=fields_by_keys,
expand=expand,
properties=properties,
update_history=update_history,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    update_history: bool | Unset = False,

) -> Any | IssueBean | None:
    """ Get issue

     Returns the details for an issue.

    The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-
    insensitive search and check for moved issues is performed. If a matching issue is found its details
    are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is
    the key of the issue found.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        fields (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.
        expand (str | Unset):
        properties (list[str] | Unset):
        update_history (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueBean
     """


    return sync_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
fields=fields,
fields_by_keys=fields_by_keys,
expand=expand,
properties=properties,
update_history=update_history,

    ).parsed

async def asyncio_detailed(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    update_history: bool | Unset = False,

) -> Response[Any | IssueBean]:
    """ Get issue

     Returns the details for an issue.

    The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-
    insensitive search and check for moved issues is performed. If a matching issue is found its details
    are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is
    the key of the issue found.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        fields (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.
        expand (str | Unset):
        properties (list[str] | Unset):
        update_history (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueBean]
     """


    kwargs = _get_kwargs(
        issue_id_or_key=issue_id_or_key,
fields=fields,
fields_by_keys=fields_by_keys,
expand=expand,
properties=properties,
update_history=update_history,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_id_or_key: str,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    update_history: bool | Unset = False,

) -> Any | IssueBean | None:
    """ Get issue

     Returns the details for an issue.

    The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-
    insensitive search and check for moved issues is performed. If a matching issue is found its details
    are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is
    the key of the issue found.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        issue_id_or_key (str):
        fields (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.
        expand (str | Unset):
        properties (list[str] | Unset):
        update_history (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueBean
     """


    return (await asyncio_detailed(
        issue_id_or_key=issue_id_or_key,
client=client,
fields=fields,
fields_by_keys=fields_by_keys,
expand=expand,
properties=properties,
update_history=update_history,

    )).parsed
