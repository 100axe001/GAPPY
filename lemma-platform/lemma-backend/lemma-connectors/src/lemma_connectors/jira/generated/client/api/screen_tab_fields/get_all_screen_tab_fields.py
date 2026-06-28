from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.screenable_field import ScreenableField
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    screen_id: int,
    tab_id: int,
    *,
    project_key: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["projectKey"] = project_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields".format(screen_id=quote(str(screen_id), safe=""),tab_id=quote(str(tab_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[ScreenableField] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ScreenableField.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[ScreenableField]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    screen_id: int,
    tab_id: int,
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,

) -> Response[Any | list[ScreenableField]]:
    """ Get all screen tab fields

     Returns all fields for a screen tab.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the
    project key is specified, providing that the screen is associated with the project through a Screen
    Scheme and Issue Type Screen Scheme.

    Args:
        screen_id (int):
        tab_id (int):
        project_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ScreenableField]]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
tab_id=tab_id,
project_key=project_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    screen_id: int,
    tab_id: int,
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,

) -> Any | list[ScreenableField] | None:
    """ Get all screen tab fields

     Returns all fields for a screen tab.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the
    project key is specified, providing that the screen is associated with the project through a Screen
    Scheme and Issue Type Screen Scheme.

    Args:
        screen_id (int):
        tab_id (int):
        project_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ScreenableField]
     """


    return sync_detailed(
        screen_id=screen_id,
tab_id=tab_id,
client=client,
project_key=project_key,

    ).parsed

async def asyncio_detailed(
    screen_id: int,
    tab_id: int,
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,

) -> Response[Any | list[ScreenableField]]:
    """ Get all screen tab fields

     Returns all fields for a screen tab.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the
    project key is specified, providing that the screen is associated with the project through a Screen
    Scheme and Issue Type Screen Scheme.

    Args:
        screen_id (int):
        tab_id (int):
        project_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ScreenableField]]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
tab_id=tab_id,
project_key=project_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    screen_id: int,
    tab_id: int,
    *,
    client: AuthenticatedClient,
    project_key: str | Unset = UNSET,

) -> Any | list[ScreenableField] | None:
    """ Get all screen tab fields

     Returns all fields for a screen tab.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
     *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the
    project key is specified, providing that the screen is associated with the project through a Screen
    Scheme and Issue Type Screen Scheme.

    Args:
        screen_id (int):
        tab_id (int):
        project_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ScreenableField]
     """


    return (await asyncio_detailed(
        screen_id=screen_id,
tab_id=tab_id,
client=client,
project_key=project_key,

    )).parsed
