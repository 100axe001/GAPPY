from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.jql_reference_data import JQLReferenceData
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/jql/autocompletedata",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | JQLReferenceData | None:
    if response.status_code == 200:
        response_200 = JQLReferenceData.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | JQLReferenceData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | JQLReferenceData]:
    """ Get field reference data (GET)

     Returns reference data for JQL searches. This is a downloadable version of the documentation
    provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and
    [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a
    list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL
    queries or the validation of queries built in a custom query builder.

    To filter visible field details by project or collapse non-unique fields by field type then [Get
    field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JQLReferenceData]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Any | JQLReferenceData | None:
    """ Get field reference data (GET)

     Returns reference data for JQL searches. This is a downloadable version of the documentation
    provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and
    [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a
    list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL
    queries or the validation of queries built in a custom query builder.

    To filter visible field details by project or collapse non-unique fields by field type then [Get
    field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JQLReferenceData
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | JQLReferenceData]:
    """ Get field reference data (GET)

     Returns reference data for JQL searches. This is a downloadable version of the documentation
    provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and
    [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a
    list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL
    queries or the validation of queries built in a custom query builder.

    To filter visible field details by project or collapse non-unique fields by field type then [Get
    field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JQLReferenceData]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Any | JQLReferenceData | None:
    """ Get field reference data (GET)

     Returns reference data for JQL searches. This is a downloadable version of the documentation
    provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and
    [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a
    list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL
    queries or the validation of queries built in a custom query builder.

    To filter visible field details by project or collapse non-unique fields by field type then [Get
    field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JQLReferenceData
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
