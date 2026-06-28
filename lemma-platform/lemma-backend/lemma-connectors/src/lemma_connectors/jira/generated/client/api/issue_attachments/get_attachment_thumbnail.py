from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_attachment_thumbnail_response_200 import GetAttachmentThumbnailResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    redirect: bool | Unset = True,
    fallback_to_default: bool | Unset = True,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["redirect"] = redirect

    params["fallbackToDefault"] = fallback_to_default

    params["width"] = width

    params["height"] = height


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/attachment/thumbnail/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GetAttachmentThumbnailResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAttachmentThumbnailResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | GetAttachmentThumbnailResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    fallback_to_default: bool | Unset = True,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,

) -> Response[Any | GetAttachmentThumbnailResponse200]:
    """ Get attachment thumbnail

     Returns the thumbnail of an attachment.

    To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-
    id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.
        fallback_to_default (bool | Unset):  Default: True.
        width (int | Unset):
        height (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentThumbnailResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
redirect=redirect,
fallback_to_default=fallback_to_default,
width=width,
height=height,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    fallback_to_default: bool | Unset = True,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,

) -> Any | GetAttachmentThumbnailResponse200 | None:
    """ Get attachment thumbnail

     Returns the thumbnail of an attachment.

    To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-
    id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.
        fallback_to_default (bool | Unset):  Default: True.
        width (int | Unset):
        height (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentThumbnailResponse200
     """


    return sync_detailed(
        id=id,
client=client,
redirect=redirect,
fallback_to_default=fallback_to_default,
width=width,
height=height,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    fallback_to_default: bool | Unset = True,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,

) -> Response[Any | GetAttachmentThumbnailResponse200]:
    """ Get attachment thumbnail

     Returns the thumbnail of an attachment.

    To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-
    id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.
        fallback_to_default (bool | Unset):  Default: True.
        width (int | Unset):
        height (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentThumbnailResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
redirect=redirect,
fallback_to_default=fallback_to_default,
width=width,
height=height,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,
    fallback_to_default: bool | Unset = True,
    width: int | Unset = UNSET,
    height: int | Unset = UNSET,

) -> Any | GetAttachmentThumbnailResponse200 | None:
    """ Get attachment thumbnail

     Returns the thumbnail of an attachment.

    To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-
    id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.
        fallback_to_default (bool | Unset):  Default: True.
        width (int | Unset):
        height (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentThumbnailResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
redirect=redirect,
fallback_to_default=fallback_to_default,
width=width,
height=height,

    )).parsed
