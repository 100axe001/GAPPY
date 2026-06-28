from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_for_issues_using_jql_validate_query import SearchForIssuesUsingJqlValidateQuery
from ...models.search_results import SearchResults
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    jql: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    validate_query: SearchForIssuesUsingJqlValidateQuery | Unset = SearchForIssuesUsingJqlValidateQuery.STRICT,
    fields: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["jql"] = jql

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_validate_query: str | Unset = UNSET
    if not isinstance(validate_query, Unset):
        json_validate_query = validate_query.value

    params["validateQuery"] = json_validate_query

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields


    params["fields"] = json_fields

    params["expand"] = expand

    json_properties: list[str] | Unset = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties


    params["properties"] = json_properties

    params["fieldsByKeys"] = fields_by_keys


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | SearchResults | None:
    if response.status_code == 200:
        response_200 = SearchResults.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | SearchResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    jql: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    validate_query: SearchForIssuesUsingJqlValidateQuery | Unset = SearchForIssuesUsingJqlValidateQuery.STRICT,
    fields: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,

) -> Response[Any | SearchResults]:
    """ Search for issues using JQL (GET)

     Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).

    If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-
    rest-api-3-search-post) version of this resource.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issues are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        jql (str | Unset):  Example: project = HSP.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        validate_query (SearchForIssuesUsingJqlValidateQuery | Unset):  Default:
            SearchForIssuesUsingJqlValidateQuery.STRICT.
        fields (list[str] | Unset):
        expand (str | Unset):
        properties (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchResults]
     """


    kwargs = _get_kwargs(
        jql=jql,
start_at=start_at,
max_results=max_results,
validate_query=validate_query,
fields=fields,
expand=expand,
properties=properties,
fields_by_keys=fields_by_keys,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    jql: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    validate_query: SearchForIssuesUsingJqlValidateQuery | Unset = SearchForIssuesUsingJqlValidateQuery.STRICT,
    fields: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,

) -> Any | SearchResults | None:
    """ Search for issues using JQL (GET)

     Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).

    If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-
    rest-api-3-search-post) version of this resource.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issues are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        jql (str | Unset):  Example: project = HSP.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        validate_query (SearchForIssuesUsingJqlValidateQuery | Unset):  Default:
            SearchForIssuesUsingJqlValidateQuery.STRICT.
        fields (list[str] | Unset):
        expand (str | Unset):
        properties (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchResults
     """


    return sync_detailed(
        client=client,
jql=jql,
start_at=start_at,
max_results=max_results,
validate_query=validate_query,
fields=fields,
expand=expand,
properties=properties,
fields_by_keys=fields_by_keys,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    jql: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    validate_query: SearchForIssuesUsingJqlValidateQuery | Unset = SearchForIssuesUsingJqlValidateQuery.STRICT,
    fields: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,

) -> Response[Any | SearchResults]:
    """ Search for issues using JQL (GET)

     Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).

    If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-
    rest-api-3-search-post) version of this resource.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issues are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        jql (str | Unset):  Example: project = HSP.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        validate_query (SearchForIssuesUsingJqlValidateQuery | Unset):  Default:
            SearchForIssuesUsingJqlValidateQuery.STRICT.
        fields (list[str] | Unset):
        expand (str | Unset):
        properties (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchResults]
     """


    kwargs = _get_kwargs(
        jql=jql,
start_at=start_at,
max_results=max_results,
validate_query=validate_query,
fields=fields,
expand=expand,
properties=properties,
fields_by_keys=fields_by_keys,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    jql: str | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    validate_query: SearchForIssuesUsingJqlValidateQuery | Unset = SearchForIssuesUsingJqlValidateQuery.STRICT,
    fields: list[str] | Unset = UNSET,
    expand: str | Unset = UNSET,
    properties: list[str] | Unset = UNSET,
    fields_by_keys: bool | Unset = False,

) -> Any | SearchResults | None:
    """ Search for issues using JQL (GET)

     Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).

    If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-
    rest-api-3-search-post) version of this resource.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issues are included in the response where the user has:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project containing the issue.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        jql (str | Unset):  Example: project = HSP.
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        validate_query (SearchForIssuesUsingJqlValidateQuery | Unset):  Default:
            SearchForIssuesUsingJqlValidateQuery.STRICT.
        fields (list[str] | Unset):
        expand (str | Unset):
        properties (list[str] | Unset):
        fields_by_keys (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchResults
     """


    return (await asyncio_detailed(
        client=client,
jql=jql,
start_at=start_at,
max_results=max_results,
validate_query=validate_query,
fields=fields,
expand=expand,
properties=properties,
fields_by_keys=fields_by_keys,

    )).parsed
