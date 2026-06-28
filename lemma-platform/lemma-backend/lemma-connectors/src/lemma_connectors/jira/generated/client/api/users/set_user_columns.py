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
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["accountId"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/user/columns",
        "params": params,
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

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 429:
        return None

    if response.status_code == 500:
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
    account_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Set user default columns

     Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If
    an account ID is not passed, the calling user's default columns are set. If no column details are
    sent, then all default columns are removed.

    The parameters for this resource are expressed as HTML form data. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'`

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the
    columns on any user.
     *  Permission to access Jira, to set the calling user's columns.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
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
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    list[str]  |     list[str]  | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Any]:
    """ Set user default columns

     Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If
    an account ID is not passed, the calling user's default columns are set. If no column details are
    sent, then all default columns are removed.

    The parameters for this resource are expressed as HTML form data. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'`

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set the
    columns on any user.
     *  Permission to access Jira, to set the calling user's columns.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
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
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

