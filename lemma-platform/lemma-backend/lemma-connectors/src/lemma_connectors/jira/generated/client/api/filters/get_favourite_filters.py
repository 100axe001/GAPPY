from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.filter_ import Filter
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/filter/favourite",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[Filter] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Filter.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[Filter]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | list[Filter]]:
    """ Get favorite filters

     Returns the visible favorite filters of the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the
    filter is:

     *  owned by the user.
     *  shared with a group that the user is a member of.
     *  shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  shared with a public project.
     *  shared with the public.

    For example, if the user favorites a public filter that is subsequently made private that filter is
    not returned by this operation.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Filter]]
     """


    kwargs = _get_kwargs(
        expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | list[Filter] | None:
    """ Get favorite filters

     Returns the visible favorite filters of the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the
    filter is:

     *  owned by the user.
     *  shared with a group that the user is a member of.
     *  shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  shared with a public project.
     *  shared with the public.

    For example, if the user favorites a public filter that is subsequently made private that filter is
    not returned by this operation.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Filter]
     """


    return sync_detailed(
        client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Response[Any | list[Filter]]:
    """ Get favorite filters

     Returns the visible favorite filters of the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the
    filter is:

     *  owned by the user.
     *  shared with a group that the user is a member of.
     *  shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  shared with a public project.
     *  shared with the public.

    For example, if the user favorites a public filter that is subsequently made private that filter is
    not returned by this operation.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[Filter]]
     """


    kwargs = _get_kwargs(
        expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: str | Unset = UNSET,

) -> Any | list[Filter] | None:
    """ Get favorite filters

     Returns the visible favorite filters of the user.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the
    filter is:

     *  owned by the user.
     *  shared with a group that the user is a member of.
     *  shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  shared with a public project.
     *  shared with the public.

    For example, if the user favorites a public filter that is subsequently made private that filter is
    not returned by this operation.

    Args:
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[Filter]
     """


    return (await asyncio_detailed(
        client=client,
expand=expand,

    )).parsed
