from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.avatar import Avatar
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    body: Any,
    x: int | Unset = 0,
    y: int | Unset = 0,
    size: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["x"] = x

    params["y"] = y

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/project/{project_id_or_key}/avatar2".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Avatar | None:
    if response.status_code == 201:
        response_201 = Avatar.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Avatar]:
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
    body: Any,
    x: int | Unset = 0,
    y: int | Unset = 0,
    size: int | Unset = UNSET,

) -> Response[Any | Avatar]:
    r""" Load project avatar

     Loads an avatar for a project.

    Specify the avatar's local file location in the body of the request. Also, include the following
    headers:

     *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more
    information see [Special Headers](#special-request-headers).
     *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

    For example:
    `curl --request POST `

    `--user email@example.com:<api_token> `

    `--header 'X-Atlassian-Token: no-check' `

    `--header 'Content-Type: image/< image_type>' `

    `--data-binary \"<@/path/to/file/with/your/avatar>\" `

    `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

    The avatar is cropped to a square. If no crop parameters are specified, the square originates at the
    top left of the image. The length of the square's sides is set to the smaller of the height or width
    of the image.

    The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

    After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-
    put) to set it as the project's displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        x (int | Unset):  Default: 0.
        y (int | Unset):  Default: 0.
        size (int | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Avatar]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
body=body,
x=x,
y=y,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    x: int | Unset = 0,
    y: int | Unset = 0,
    size: int | Unset = UNSET,

) -> Any | Avatar | None:
    r""" Load project avatar

     Loads an avatar for a project.

    Specify the avatar's local file location in the body of the request. Also, include the following
    headers:

     *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more
    information see [Special Headers](#special-request-headers).
     *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

    For example:
    `curl --request POST `

    `--user email@example.com:<api_token> `

    `--header 'X-Atlassian-Token: no-check' `

    `--header 'Content-Type: image/< image_type>' `

    `--data-binary \"<@/path/to/file/with/your/avatar>\" `

    `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

    The avatar is cropped to a square. If no crop parameters are specified, the square originates at the
    top left of the image. The length of the square's sides is set to the smaller of the height or width
    of the image.

    The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

    After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-
    put) to set it as the project's displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        x (int | Unset):  Default: 0.
        y (int | Unset):  Default: 0.
        size (int | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Avatar
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
body=body,
x=x,
y=y,
size=size,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    x: int | Unset = 0,
    y: int | Unset = 0,
    size: int | Unset = UNSET,

) -> Response[Any | Avatar]:
    r""" Load project avatar

     Loads an avatar for a project.

    Specify the avatar's local file location in the body of the request. Also, include the following
    headers:

     *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more
    information see [Special Headers](#special-request-headers).
     *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

    For example:
    `curl --request POST `

    `--user email@example.com:<api_token> `

    `--header 'X-Atlassian-Token: no-check' `

    `--header 'Content-Type: image/< image_type>' `

    `--data-binary \"<@/path/to/file/with/your/avatar>\" `

    `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

    The avatar is cropped to a square. If no crop parameters are specified, the square originates at the
    top left of the image. The length of the square's sides is set to the smaller of the height or width
    of the image.

    The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

    After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-
    put) to set it as the project's displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        x (int | Unset):  Default: 0.
        y (int | Unset):  Default: 0.
        size (int | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Avatar]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
body=body,
x=x,
y=y,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    x: int | Unset = 0,
    y: int | Unset = 0,
    size: int | Unset = UNSET,

) -> Any | Avatar | None:
    r""" Load project avatar

     Loads an avatar for a project.

    Specify the avatar's local file location in the body of the request. Also, include the following
    headers:

     *  `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more
    information see [Special Headers](#special-request-headers).
     *  `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG.

    For example:
    `curl --request POST `

    `--user email@example.com:<api_token> `

    `--header 'X-Atlassian-Token: no-check' `

    `--header 'Content-Type: image/< image_type>' `

    `--data-binary \"<@/path/to/file/with/your/avatar>\" `

    `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'`

    The avatar is cropped to a square. If no crop parameters are specified, the square originates at the
    top left of the image. The length of the square's sides is set to the smaller of the height or width
    of the image.

    The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.

    After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-
    put) to set it as the project's displayed avatar.

    **[Permissions](#permissions) required:** *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        project_id_or_key (str):
        x (int | Unset):  Default: 0.
        y (int | Unset):  Default: 0.
        size (int | Unset):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Avatar
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
body=body,
x=x,
y=y,
size=size,

    )).parsed
