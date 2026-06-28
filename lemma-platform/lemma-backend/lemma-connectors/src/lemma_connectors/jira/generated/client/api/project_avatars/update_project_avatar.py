from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.avatar import Avatar
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    body: Avatar,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/project/{project_id_or_key}/avatar".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
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
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: Avatar,

) -> Response[Any]:
    """ Set project avatar

     Sets the avatar displayed for a project.

    Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars
    against the project, before using this operation to set the displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        body (Avatar): Details of an avatar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: Avatar,

) -> Response[Any]:
    """ Set project avatar

     Sets the avatar displayed for a project.

    Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars
    against the project, before using this operation to set the displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        body (Avatar): Details of an avatar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

