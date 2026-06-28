from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset



def _get_kwargs(
    property_key: str,
    *,
    body: Any,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["userKey"] = user_key

    params["username"] = username


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/user/properties/{property_key}".format(property_key=quote(str(property_key), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 201:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 405:
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
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any]:
    """ Set user property

     Sets the value of a user's property. Use this resource to store custom data against a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a
    property on any user.
     *  Access to Jira, to set a property on the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
body=body,
account_id=account_id,
user_key=user_key,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any]:
    """ Set user property

     Sets the value of a user's property. Use this resource to store custom data against a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to set a
    property on any user.
     *  Access to Jira, to set a property on the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
body=body,
account_id=account_id,
user_key=user_key,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

