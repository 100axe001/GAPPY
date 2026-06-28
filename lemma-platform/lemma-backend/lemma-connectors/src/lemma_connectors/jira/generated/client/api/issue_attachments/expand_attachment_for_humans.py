from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attachment_archive_metadata_readable import AttachmentArchiveMetadataReadable
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/attachment/{id}/expand/human".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | AttachmentArchiveMetadataReadable | None:
    if response.status_code == 200:
        response_200 = AttachmentArchiveMetadataReadable.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | AttachmentArchiveMetadataReadable]:
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

) -> Response[Any | AttachmentArchiveMetadataReadable]:
    """ Get all metadata for an expanded attachment

     Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the
    attachment itself. For example, if the attachment is a ZIP archive, then information about the files
    in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format
    is supported.

    Use this operation to retrieve data that is presented to the user, as this operation returns the
    metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get
    contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which
    only returns the metadata for the attachment's contents.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentArchiveMetadataReadable]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | AttachmentArchiveMetadataReadable | None:
    """ Get all metadata for an expanded attachment

     Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the
    attachment itself. For example, if the attachment is a ZIP archive, then information about the files
    in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format
    is supported.

    Use this operation to retrieve data that is presented to the user, as this operation returns the
    metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get
    contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which
    only returns the metadata for the attachment's contents.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentArchiveMetadataReadable
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | AttachmentArchiveMetadataReadable]:
    """ Get all metadata for an expanded attachment

     Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the
    attachment itself. For example, if the attachment is a ZIP archive, then information about the files
    in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format
    is supported.

    Use this operation to retrieve data that is presented to the user, as this operation returns the
    metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get
    contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which
    only returns the metadata for the attachment's contents.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentArchiveMetadataReadable]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | AttachmentArchiveMetadataReadable | None:
    """ Get all metadata for an expanded attachment

     Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the
    attachment itself. For example, if the attachment is a ZIP archive, then information about the files
    in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format
    is supported.

    Use this operation to retrieve data that is presented to the user, as this operation returns the
    metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get
    contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which
    only returns the metadata for the attachment's contents.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** For the issue containing the attachment:

     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the
    project that the issue is in.
     *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level
    security permission to view the issue.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentArchiveMetadataReadable
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
