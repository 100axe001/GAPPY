from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auto_complete_suggestions import AutoCompleteSuggestions
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    field_name: str | Unset = UNSET,
    field_value: str | Unset = UNSET,
    predicate_name: str | Unset = UNSET,
    predicate_value: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["fieldName"] = field_name

    params["fieldValue"] = field_value

    params["predicateName"] = predicate_name

    params["predicateValue"] = predicate_value


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/jql/autocompletedata/suggestions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | AutoCompleteSuggestions | None:
    if response.status_code == 200:
        response_200 = AutoCompleteSuggestions.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | AutoCompleteSuggestions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    field_name: str | Unset = UNSET,
    field_value: str | Unset = UNSET,
    predicate_name: str | Unset = UNSET,
    predicate_value: str | Unset = UNSET,

) -> Response[Any | AutoCompleteSuggestions]:
    """ Get field auto complete suggestions

     Returns the JQL search auto complete suggestions for a field.

    Suggestions can be obtained by providing:

     *  `fieldName` to get a list of all values for the field.
     *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
     *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
     *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing
    the text in `predicateValue`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        field_name (str | Unset):  Example: reporter.
        field_value (str | Unset):
        predicate_name (str | Unset):
        predicate_value (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutoCompleteSuggestions]
     """


    kwargs = _get_kwargs(
        field_name=field_name,
field_value=field_value,
predicate_name=predicate_name,
predicate_value=predicate_value,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    field_name: str | Unset = UNSET,
    field_value: str | Unset = UNSET,
    predicate_name: str | Unset = UNSET,
    predicate_value: str | Unset = UNSET,

) -> Any | AutoCompleteSuggestions | None:
    """ Get field auto complete suggestions

     Returns the JQL search auto complete suggestions for a field.

    Suggestions can be obtained by providing:

     *  `fieldName` to get a list of all values for the field.
     *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
     *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
     *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing
    the text in `predicateValue`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        field_name (str | Unset):  Example: reporter.
        field_value (str | Unset):
        predicate_name (str | Unset):
        predicate_value (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutoCompleteSuggestions
     """


    return sync_detailed(
        client=client,
field_name=field_name,
field_value=field_value,
predicate_name=predicate_name,
predicate_value=predicate_value,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    field_name: str | Unset = UNSET,
    field_value: str | Unset = UNSET,
    predicate_name: str | Unset = UNSET,
    predicate_value: str | Unset = UNSET,

) -> Response[Any | AutoCompleteSuggestions]:
    """ Get field auto complete suggestions

     Returns the JQL search auto complete suggestions for a field.

    Suggestions can be obtained by providing:

     *  `fieldName` to get a list of all values for the field.
     *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
     *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
     *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing
    the text in `predicateValue`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        field_name (str | Unset):  Example: reporter.
        field_value (str | Unset):
        predicate_name (str | Unset):
        predicate_value (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutoCompleteSuggestions]
     """


    kwargs = _get_kwargs(
        field_name=field_name,
field_value=field_value,
predicate_name=predicate_name,
predicate_value=predicate_value,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    field_name: str | Unset = UNSET,
    field_value: str | Unset = UNSET,
    predicate_name: str | Unset = UNSET,
    predicate_value: str | Unset = UNSET,

) -> Any | AutoCompleteSuggestions | None:
    """ Get field auto complete suggestions

     Returns the JQL search auto complete suggestions for a field.

    Suggestions can be obtained by providing:

     *  `fieldName` to get a list of all values for the field.
     *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.
     *  `fieldName` and `predicateName` to get a list of all predicate values for the field.
     *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing
    the text in `predicateValue`.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Args:
        field_name (str | Unset):  Example: reporter.
        field_value (str | Unset):
        predicate_name (str | Unset):
        predicate_value (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutoCompleteSuggestions
     """


    return (await asyncio_detailed(
        client=client,
field_name=field_name,
field_value=field_value,
predicate_name=predicate_name,
predicate_value=predicate_value,

    )).parsed
