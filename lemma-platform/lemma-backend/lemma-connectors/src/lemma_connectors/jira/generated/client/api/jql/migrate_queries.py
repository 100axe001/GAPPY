from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.converted_jql_queries import ConvertedJQLQueries
from ...models.jql_personal_data_migration_request import JQLPersonalDataMigrationRequest
from typing import cast



def _get_kwargs(
    *,
    body: JQLPersonalDataMigrationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/jql/pdcleaner",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ConvertedJQLQueries | None:
    if response.status_code == 200:
        response_200 = ConvertedJQLQueries.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ConvertedJQLQueries]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JQLPersonalDataMigrationRequest,

) -> Response[Any | ConvertedJQLQueries]:
    """ Convert user identifiers to account IDs in JQL queries

     Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL
    queries with account IDs.

    You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-
    compliant. For more information about GDPR-related changes, see the [migration
    guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
    migration-guide/).

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (JQLPersonalDataMigrationRequest): The JQL queries to be converted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConvertedJQLQueries]
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
    body: JQLPersonalDataMigrationRequest,

) -> Any | ConvertedJQLQueries | None:
    """ Convert user identifiers to account IDs in JQL queries

     Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL
    queries with account IDs.

    You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-
    compliant. For more information about GDPR-related changes, see the [migration
    guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
    migration-guide/).

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (JQLPersonalDataMigrationRequest): The JQL queries to be converted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConvertedJQLQueries
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JQLPersonalDataMigrationRequest,

) -> Response[Any | ConvertedJQLQueries]:
    """ Convert user identifiers to account IDs in JQL queries

     Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL
    queries with account IDs.

    You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-
    compliant. For more information about GDPR-related changes, see the [migration
    guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
    migration-guide/).

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (JQLPersonalDataMigrationRequest): The JQL queries to be converted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConvertedJQLQueries]
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
    body: JQLPersonalDataMigrationRequest,

) -> Any | ConvertedJQLQueries | None:
    """ Convert user identifiers to account IDs in JQL queries

     Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL
    queries with account IDs.

    You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-
    compliant. For more information about GDPR-related changes, see the [migration
    guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-
    migration-guide/).

    **[Permissions](#permissions) required:** Permission to access Jira.

    Args:
        body (JQLPersonalDataMigrationRequest): The JQL queries to be converted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConvertedJQLQueries
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
