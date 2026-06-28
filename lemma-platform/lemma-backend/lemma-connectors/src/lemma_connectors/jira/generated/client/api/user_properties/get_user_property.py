from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.entity_property import EntityProperty
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    property_key: str,
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
        "url": "/rest/api/3/user/properties/{property_key}".format(property_key=quote(str(property_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EntityProperty | None:
    if response.status_code == 200:
        response_200 = EntityProperty.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | EntityProperty]:
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
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any | EntityProperty]:
    """ Get user property

     Returns the value of a user's property. If no property key is provided [Get user property
    keys](#api-rest-api-3-user-properties-get) is called.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a
    property from any user.
     *  Access to Jira, to get a property from the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
account_id=account_id,
user_key=user_key,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    property_key: str,
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | EntityProperty | None:
    """ Get user property

     Returns the value of a user's property. If no property key is provided [Get user property
    keys](#api-rest-api-3-user-properties-get) is called.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a
    property from any user.
     *  Access to Jira, to get a property from the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return sync_detailed(
        property_key=property_key,
client=client,
account_id=account_id,
user_key=user_key,
username=username,

    ).parsed

async def asyncio_detailed(
    property_key: str,
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Response[Any | EntityProperty]:
    """ Get user property

     Returns the value of a user's property. If no property key is provided [Get user property
    keys](#api-rest-api-3-user-properties-get) is called.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a
    property from any user.
     *  Access to Jira, to get a property from the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        property_key=property_key,
account_id=account_id,
user_key=user_key,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    property_key: str,
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    user_key: str | Unset = UNSET,
    username: str | Unset = UNSET,

) -> Any | EntityProperty | None:
    """ Get user property

     Returns the value of a user's property. If no property key is provided [Get user property
    keys](#api-rest-api-3-user-properties-get) is called.

    Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL)
    created and maintained in Jira.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a
    property from any user.
     *  Access to Jira, to get a property from the calling user's record.

    Args:
        property_key (str):
        account_id (str | Unset):  Example: 5b10ac8d82e05b22cc7d4ef5.
        user_key (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return (await asyncio_detailed(
        property_key=property_key,
client=client,
account_id=account_id,
user_key=user_key,
username=username,

    )).parsed
