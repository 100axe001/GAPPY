from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.property_keys import PropertyKeys
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["userKey"] = user_key

    params["username"] = username


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/user/properties",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PropertyKeys | None:
    if response.status_code == 200:
        response_200 = PropertyKeys.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PropertyKeys]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any | PropertyKeys]:
    """ Get user property keys

     Returns the keys of all properties for a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the
    property keys on any user.
     *  Access to Jira, to access the calling user's property keys.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PropertyKeys]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
user_key=user_key,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | PropertyKeys | None:
    """ Get user property keys

     Returns the keys of all properties for a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the
    property keys on any user.
     *  Access to Jira, to access the calling user's property keys.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PropertyKeys
     """


    return sync_detailed(
        client=client,
account_id=account_id,
user_key=user_key,
username=username,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any | PropertyKeys]:
    """ Get user property keys

     Returns the keys of all properties for a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the
    property keys on any user.
     *  Access to Jira, to access the calling user's property keys.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PropertyKeys]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
user_key=user_key,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | PropertyKeys | None:
    """ Get user property keys

     Returns the keys of all properties for a user.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the
    property keys on any user.
     *  Access to Jira, to access the calling user's property keys.

    Args:
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PropertyKeys
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
user_key=user_key,
username=username,

    )).parsed
