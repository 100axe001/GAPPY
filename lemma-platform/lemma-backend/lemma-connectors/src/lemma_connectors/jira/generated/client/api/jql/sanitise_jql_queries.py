from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.jql_queries_to_sanitize import JqlQueriesToSanitize
from ...models.sanitized_jql_queries import SanitizedJqlQueries
from typing import cast



def _get_kwargs(
    *,
    body: JqlQueriesToSanitize,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/jql/sanitize",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | SanitizedJqlQueries | None:
    if response.status_code == 200:
        response_200 = SanitizedJqlQueries.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorCollection.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | SanitizedJqlQueries]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToSanitize,

) -> Response[ErrorCollection | SanitizedJqlQueries]:
    r""" Sanitize JQL queries

     Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have
    permission to view the entity.

    For example, if the query contains the clause *project = 'Secret project'*, and a user does not have
    browse permission for the project \"Secret project\", the sanitized query replaces the clause with
    *project = 12345\"* (where 12345 is the ID of the project). If a user has the required permission,
    the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous
    user.

    Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user
    identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user
    identifiers to account IDs in JQL
    queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-
    api-3-jql-sanitize-post).

    Before sanitization each JQL query is parsed. The queries are returned in the same order that they
    were passed.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (JqlQueriesToSanitize): The list of JQL queries to sanitize for the given account
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | SanitizedJqlQueries]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToSanitize,

) -> ErrorCollection | SanitizedJqlQueries | None:
    r""" Sanitize JQL queries

     Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have
    permission to view the entity.

    For example, if the query contains the clause *project = 'Secret project'*, and a user does not have
    browse permission for the project \"Secret project\", the sanitized query replaces the clause with
    *project = 12345\"* (where 12345 is the ID of the project). If a user has the required permission,
    the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous
    user.

    Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user
    identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user
    identifiers to account IDs in JQL
    queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-
    api-3-jql-sanitize-post).

    Before sanitization each JQL query is parsed. The queries are returned in the same order that they
    were passed.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (JqlQueriesToSanitize): The list of JQL queries to sanitize for the given account
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | SanitizedJqlQueries
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToSanitize,

) -> Response[ErrorCollection | SanitizedJqlQueries]:
    r""" Sanitize JQL queries

     Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have
    permission to view the entity.

    For example, if the query contains the clause *project = 'Secret project'*, and a user does not have
    browse permission for the project \"Secret project\", the sanitized query replaces the clause with
    *project = 12345\"* (where 12345 is the ID of the project). If a user has the required permission,
    the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous
    user.

    Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user
    identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user
    identifiers to account IDs in JQL
    queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-
    api-3-jql-sanitize-post).

    Before sanitization each JQL query is parsed. The queries are returned in the same order that they
    were passed.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (JqlQueriesToSanitize): The list of JQL queries to sanitize for the given account
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | SanitizedJqlQueries]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToSanitize,

) -> ErrorCollection | SanitizedJqlQueries | None:
    r""" Sanitize JQL queries

     Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have
    permission to view the entity.

    For example, if the query contains the clause *project = 'Secret project'*, and a user does not have
    browse permission for the project \"Secret project\", the sanitized query replaces the clause with
    *project = 12345\"* (where 12345 is the ID of the project). If a user has the required permission,
    the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous
    user.

    Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user
    identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user
    identifiers to account IDs in JQL
    queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-
    api-3-jql-sanitize-post).

    Before sanitization each JQL query is parsed. The queries are returned in the same order that they
    were passed.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (JqlQueriesToSanitize): The list of JQL queries to sanitize for the given account
            IDs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | SanitizedJqlQueries
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
