from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.status_details import StatusDetails
from typing import cast



def _get_kwargs(
    id_or_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/status/{id_or_name}".format(id_or_name=quote(str(id_or_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | StatusDetails | None:
    if response.status_code == 200:
        response_200 = StatusDetails.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | StatusDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_or_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | StatusDetails]:
    """ Get status

     Returns a status. The status must be associated with an active workflow to be returned.

    If a name is used on more than one status, only the status found first is returned. Therefore,
    identifying the status by its ID may be preferable.

    This operation can be accessed anonymously.

    [Permissions](#permissions) required: None.

    Args:
        id_or_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StatusDetails]
     """


    kwargs = _get_kwargs(
        id_or_name=id_or_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id_or_name: str,
    *,
    client: AuthenticatedClient,

) -> Any | StatusDetails | None:
    """ Get status

     Returns a status. The status must be associated with an active workflow to be returned.

    If a name is used on more than one status, only the status found first is returned. Therefore,
    identifying the status by its ID may be preferable.

    This operation can be accessed anonymously.

    [Permissions](#permissions) required: None.

    Args:
        id_or_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StatusDetails
     """


    return sync_detailed(
        id_or_name=id_or_name,
client=client,

    ).parsed

async def asyncio_detailed(
    id_or_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | StatusDetails]:
    """ Get status

     Returns a status. The status must be associated with an active workflow to be returned.

    If a name is used on more than one status, only the status found first is returned. Therefore,
    identifying the status by its ID may be preferable.

    This operation can be accessed anonymously.

    [Permissions](#permissions) required: None.

    Args:
        id_or_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StatusDetails]
     """


    kwargs = _get_kwargs(
        id_or_name=id_or_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id_or_name: str,
    *,
    client: AuthenticatedClient,

) -> Any | StatusDetails | None:
    """ Get status

     Returns a status. The status must be associated with an active workflow to be returned.

    If a name is used on more than one status, only the status found first is returned. Therefore,
    identifying the status by its ID may be preferable.

    This operation can be accessed anonymously.

    [Permissions](#permissions) required: None.

    Args:
        id_or_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StatusDetails
     """


    return (await asyncio_detailed(
        id_or_name=id_or_name,
client=client,

    )).parsed
