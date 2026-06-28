from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.jql_queries_to_parse import JqlQueriesToParse
from ...models.parse_jql_queries_validation import ParseJqlQueriesValidation
from ...models.parsed_jql_queries import ParsedJqlQueries
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: JqlQueriesToParse,
    validation: ParseJqlQueriesValidation | Unset = ParseJqlQueriesValidation.STRICT,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_validation: str | Unset = UNSET
    if not isinstance(validation, Unset):
        json_validation = validation.value

    params["validation"] = json_validation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/jql/parse",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | ParsedJqlQueries | None:
    if response.status_code == 200:
        response_200 = ParsedJqlQueries.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | ParsedJqlQueries]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToParse,
    validation: ParseJqlQueriesValidation | Unset = ParseJqlQueriesValidation.STRICT,

) -> Response[Any | ErrorCollection | ParsedJqlQueries]:
    """ Parse JQL query

     Parses and validates JQL queries.

    Validation is performed in context of the current user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        validation (ParseJqlQueriesValidation | Unset):  Default:
            ParseJqlQueriesValidation.STRICT.
        body (JqlQueriesToParse): A list of JQL queries to parse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | ParsedJqlQueries]
     """


    kwargs = _get_kwargs(
        body=body,
validation=validation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToParse,
    validation: ParseJqlQueriesValidation | Unset = ParseJqlQueriesValidation.STRICT,

) -> Any | ErrorCollection | ParsedJqlQueries | None:
    """ Parse JQL query

     Parses and validates JQL queries.

    Validation is performed in context of the current user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        validation (ParseJqlQueriesValidation | Unset):  Default:
            ParseJqlQueriesValidation.STRICT.
        body (JqlQueriesToParse): A list of JQL queries to parse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | ParsedJqlQueries
     """


    return sync_detailed(
        client=client,
body=body,
validation=validation,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToParse,
    validation: ParseJqlQueriesValidation | Unset = ParseJqlQueriesValidation.STRICT,

) -> Response[Any | ErrorCollection | ParsedJqlQueries]:
    """ Parse JQL query

     Parses and validates JQL queries.

    Validation is performed in context of the current user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        validation (ParseJqlQueriesValidation | Unset):  Default:
            ParseJqlQueriesValidation.STRICT.
        body (JqlQueriesToParse): A list of JQL queries to parse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | ParsedJqlQueries]
     """


    kwargs = _get_kwargs(
        body=body,
validation=validation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JqlQueriesToParse,
    validation: ParseJqlQueriesValidation | Unset = ParseJqlQueriesValidation.STRICT,

) -> Any | ErrorCollection | ParsedJqlQueries | None:
    """ Parse JQL query

     Parses and validates JQL queries.

    Validation is performed in context of the current user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        validation (ParseJqlQueriesValidation | Unset):  Default:
            ParseJqlQueriesValidation.STRICT.
        body (JqlQueriesToParse): A list of JQL queries to parse.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | ParsedJqlQueries
     """


    return (await asyncio_detailed(
        client=client,
body=body,
validation=validation,

    )).parsed
