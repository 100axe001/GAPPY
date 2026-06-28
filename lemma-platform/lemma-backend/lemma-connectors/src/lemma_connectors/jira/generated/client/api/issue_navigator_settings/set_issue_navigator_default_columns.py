from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/settings/columns",
    }

    if isinstance(body, list[str]):
        

        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, list[str]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body




        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> Response[Any]:
    """ Set issue navigator default columns

     Sets the default issue navigator columns.

    The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To
    specify multiple columns, pass multiple `columns` parameters. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/settings/columns`

    If no column details are sent, then all default columns are removed.

    A navigable field is one that can be used as a column on the issue navigator. Find details of
    navigable issue columns using [Get fields](#api-rest-api-3-field-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (list[str] | Unset):
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> Response[Any]:
    """ Set issue navigator default columns

     Sets the default issue navigator columns.

    The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To
    specify multiple columns, pass multiple `columns` parameters. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/settings/columns`

    If no column details are sent, then all default columns are removed.

    A navigable field is one that can be used as a column on the issue navigator. Find details of
    navigable issue columns using [Get fields](#api-rest-api-3-field-get).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (list[str] | Unset):
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

