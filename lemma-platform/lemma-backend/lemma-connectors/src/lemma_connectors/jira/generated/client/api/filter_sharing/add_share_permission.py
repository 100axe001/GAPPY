from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.share_permission import SharePermission
from ...models.share_permission_input_bean import SharePermissionInputBean
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SharePermissionInputBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/filter/{id}/permission".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[SharePermission] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in (_response_201):
            response_201_item = SharePermission.from_dict(response_201_item_data)



            response_201.append(response_201_item)

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[SharePermission]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SharePermissionInputBean,

) -> Response[Any | list[SharePermission]]:
    """ Add share permission

     Add a share permissions to a filter. If you add a global share permission (one for all logged-in
    users or the public) it will overwrite all share permissions for the filter.

    Be aware that this operation uses different objects for updating share permissions compared to
    [Update filter](#api-rest-api-3-filter-id-put).

    **[Permissions](#permissions) required:** *Share dashboards and filters* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

    Args:
        id (int):
        body (SharePermissionInputBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[SharePermission]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SharePermissionInputBean,

) -> Any | list[SharePermission] | None:
    """ Add share permission

     Add a share permissions to a filter. If you add a global share permission (one for all logged-in
    users or the public) it will overwrite all share permissions for the filter.

    Be aware that this operation uses different objects for updating share permissions compared to
    [Update filter](#api-rest-api-3-filter-id-put).

    **[Permissions](#permissions) required:** *Share dashboards and filters* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

    Args:
        id (int):
        body (SharePermissionInputBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[SharePermission]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SharePermissionInputBean,

) -> Response[Any | list[SharePermission]]:
    """ Add share permission

     Add a share permissions to a filter. If you add a global share permission (one for all logged-in
    users or the public) it will overwrite all share permissions for the filter.

    Be aware that this operation uses different objects for updating share permissions compared to
    [Update filter](#api-rest-api-3-filter-id-put).

    **[Permissions](#permissions) required:** *Share dashboards and filters* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

    Args:
        id (int):
        body (SharePermissionInputBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[SharePermission]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SharePermissionInputBean,

) -> Any | list[SharePermission] | None:
    """ Add share permission

     Add a share permissions to a filter. If you add a global share permission (one for all logged-in
    users or the public) it will overwrite all share permissions for the filter.

    Be aware that this operation uses different objects for updating share permissions compared to
    [Update filter](#api-rest-api-3-filter-id-put).

    **[Permissions](#permissions) required:** *Share dashboards and filters* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

    Args:
        id (int):
        body (SharePermissionInputBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[SharePermission]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
