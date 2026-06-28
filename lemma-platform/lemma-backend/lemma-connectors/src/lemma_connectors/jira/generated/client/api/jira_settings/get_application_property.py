from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.application_property import ApplicationProperty
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    key: str | Unset = UNSET,
    permission_level: str | Unset = UNSET,
    key_filter: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["key"] = key

    params["permissionLevel"] = permission_level

    params["keyFilter"] = key_filter


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/application-properties",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[ApplicationProperty] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ApplicationProperty.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[ApplicationProperty]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    permission_level: str | Unset = UNSET,
    key_filter: str | Unset = UNSET,

) -> Response[Any | list[ApplicationProperty]]:
    """ Get application property

     Returns all application properties or an application property.

    If you specify a value for the `key` parameter, then an application property is returned as an
    object (not in an array). Otherwise, an array of all editable application properties is returned.
    See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of
    editable properties.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        key (str | Unset):
        permission_level (str | Unset):
        key_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ApplicationProperty]]
     """


    kwargs = _get_kwargs(
        key=key,
permission_level=permission_level,
key_filter=key_filter,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    permission_level: str | Unset = UNSET,
    key_filter: str | Unset = UNSET,

) -> Any | list[ApplicationProperty] | None:
    """ Get application property

     Returns all application properties or an application property.

    If you specify a value for the `key` parameter, then an application property is returned as an
    object (not in an array). Otherwise, an array of all editable application properties is returned.
    See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of
    editable properties.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        key (str | Unset):
        permission_level (str | Unset):
        key_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ApplicationProperty]
     """


    return sync_detailed(
        client=client,
key=key,
permission_level=permission_level,
key_filter=key_filter,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    permission_level: str | Unset = UNSET,
    key_filter: str | Unset = UNSET,

) -> Response[Any | list[ApplicationProperty]]:
    """ Get application property

     Returns all application properties or an application property.

    If you specify a value for the `key` parameter, then an application property is returned as an
    object (not in an array). Otherwise, an array of all editable application properties is returned.
    See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of
    editable properties.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        key (str | Unset):
        permission_level (str | Unset):
        key_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ApplicationProperty]]
     """


    kwargs = _get_kwargs(
        key=key,
permission_level=permission_level,
key_filter=key_filter,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    key: str | Unset = UNSET,
    permission_level: str | Unset = UNSET,
    key_filter: str | Unset = UNSET,

) -> Any | list[ApplicationProperty] | None:
    """ Get application property

     Returns all application properties or an application property.

    If you specify a value for the `key` parameter, then an application property is returned as an
    object (not in an array). Otherwise, an array of all editable application properties is returned.
    See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of
    editable properties.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        key (str | Unset):
        permission_level (str | Unset):
        key_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ApplicationProperty]
     """


    return (await asyncio_detailed(
        client=client,
key=key,
permission_level=permission_level,
key_filter=key_filter,

    )).parsed
