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
    id: int,
    *,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/filter/{id}/columns".format(id=quote(str(id), safe=""),),
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

    if response.status_code == 403:
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
    id: int,
    *,
    client: AuthenticatedClient,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> Response[Any]:
    """ Set columns

     Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-
    rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to
    `true`.

    The parameters for this resource are expressed as HTML form data. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/filter/10000/columns`

    **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only set
    for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        body (list[str] | Unset):
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body:    list[str]  |     list[str]  | Unset = UNSET,

) -> Response[Any]:
    """ Set columns

     Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-
    rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to
    `true`.

    The parameters for this resource are expressed as HTML form data. For example, in curl:

    `curl -X PUT -d columns=summary -d columns=description https://your-
    domain.atlassian.net/rest/api/3/filter/10000/columns`

    **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only set
    for:

     *  filters owned by the user.
     *  filters shared with a group that the user is a member of.
     *  filters shared with a private project that the user has *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for.
     *  filters shared with a public project.
     *  filters shared with the public.

    Args:
        id (int):
        body (list[str] | Unset):
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

