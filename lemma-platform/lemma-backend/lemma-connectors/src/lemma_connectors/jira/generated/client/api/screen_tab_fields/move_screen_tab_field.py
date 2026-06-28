from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.move_field_bean import MoveFieldBean
from typing import cast



def _get_kwargs(
    screen_id: int,
    tab_id: int,
    id: str,
    *,
    body: MoveFieldBean,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/screens/{screen_id}/tabs/{tab_id}/fields/{id}/move".format(screen_id=quote(str(screen_id), safe=""),tab_id=quote(str(tab_id), safe=""),id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
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
    screen_id: int,
    tab_id: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: MoveFieldBean,

) -> Response[Any]:
    """ Move screen tab field

     Moves a screen tab field.

    If `after` and `position` are provided in the request, `position` is ignored.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        tab_id (int):
        id (str):
        body (MoveFieldBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
tab_id=tab_id,
id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    screen_id: int,
    tab_id: int,
    id: str,
    *,
    client: AuthenticatedClient,
    body: MoveFieldBean,

) -> Response[Any]:
    """ Move screen tab field

     Moves a screen tab field.

    If `after` and `position` are provided in the request, `position` is ignored.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        screen_id (int):
        tab_id (int):
        id (str):
        body (MoveFieldBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        screen_id=screen_id,
tab_id=tab_id,
id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

