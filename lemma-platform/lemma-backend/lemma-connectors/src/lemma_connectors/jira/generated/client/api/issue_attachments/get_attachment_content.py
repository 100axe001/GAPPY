from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_attachment_content_response_200 import GetAttachmentContentResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    redirect: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["redirect"] = redirect


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/attachment/content/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GetAttachmentContentResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAttachmentContentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 206:
        response_206 = cast(Any, None)
        return response_206

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

    if response.status_code == 416:
        response_416 = cast(Any, None)
        return response_416

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | GetAttachmentContentResponse200]:
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

) -> Response[Any | GetAttachmentContentResponse200]:
    """ Get attachment content

     Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within
    the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-
    US/docs/Web/HTTP/Headers/Range) for details.

    To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-
    thumbnail-id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentContentResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
redirect=redirect,

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

) -> Any | GetAttachmentContentResponse200 | None:
    """ Get attachment content

     Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within
    the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-
    US/docs/Web/HTTP/Headers/Range) for details.

    To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-
    thumbnail-id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentContentResponse200
     """


    return sync_detailed(
        id=id,
client=client,
redirect=redirect,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    redirect: bool | Unset = True,

) -> Response[Any | GetAttachmentContentResponse200]:
    """ Get attachment content

     Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within
    the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-
    US/docs/Web/HTTP/Headers/Range) for details.

    To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-
    thumbnail-id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAttachmentContentResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
redirect=redirect,

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

) -> Any | GetAttachmentContentResponse200 | None:
    """ Get attachment content

     Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within
    the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-
    US/docs/Web/HTTP/Headers/Range) for details.

    To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-
    thumbnail-id-get).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):
        redirect (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAttachmentContentResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
redirect=redirect,

    )).parsed
