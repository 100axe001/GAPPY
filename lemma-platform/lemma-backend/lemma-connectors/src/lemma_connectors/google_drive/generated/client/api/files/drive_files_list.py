from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_files_list_alt import DriveFilesListAlt
from ...models.drive_files_list_corpus import DriveFilesListCorpus
from ...models.file_list import FileList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    corpora: str | Unset = UNSET,
    corpus: DriveFilesListCorpus | Unset = UNSET,
    drive_id: str | Unset = UNSET,
    include_items_from_all_drives: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    include_team_drive_items: bool | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    q: str | Unset = UNSET,
    spaces: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveFilesListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["corpora"] = corpora

    json_corpus: str | Unset = UNSET
    if not isinstance(corpus, Unset):
        json_corpus = corpus.value

    params["corpus"] = json_corpus

    params["driveId"] = drive_id

    params["includeItemsFromAllDrives"] = include_items_from_all_drives

    params["includeLabels"] = include_labels

    params["includePermissionsForView"] = include_permissions_for_view

    params["includeTeamDriveItems"] = include_team_drive_items

    params["orderBy"] = order_by

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["q"] = q

    params["spaces"] = spaces

    params["supportsAllDrives"] = supports_all_drives

    params["supportsTeamDrives"] = supports_team_drives

    params["teamDriveId"] = team_drive_id

    json_alt: str | Unset = UNSET
    if not isinstance(alt, Unset):
        json_alt = alt.value

    params["alt"] = json_alt

    params["fields"] = fields

    params["key"] = key

    params["oauth_token"] = oauth_token

    params["prettyPrint"] = pretty_print

    params["quotaUser"] = quota_user

    params["userIp"] = user_ip


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FileList | None:
    if response.status_code == 200:
        response_200 = FileList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FileList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    corpora: str | Unset = UNSET,
    corpus: DriveFilesListCorpus | Unset = UNSET,
    drive_id: str | Unset = UNSET,
    include_items_from_all_drives: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    include_team_drive_items: bool | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    q: str | Unset = UNSET,
    spaces: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveFilesListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[FileList]:
    """  Lists or searches files.

    Args:
        corpora (str | Unset):
        corpus (DriveFilesListCorpus | Unset):
        drive_id (str | Unset):
        include_items_from_all_drives (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        include_team_drive_items (bool | Unset):
        order_by (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        q (str | Unset):
        spaces (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveFilesListAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileList]
     """


    kwargs = _get_kwargs(
        corpora=corpora,
corpus=corpus,
drive_id=drive_id,
include_items_from_all_drives=include_items_from_all_drives,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
include_team_drive_items=include_team_drive_items,
order_by=order_by,
page_size=page_size,
page_token=page_token,
q=q,
spaces=spaces,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
team_drive_id=team_drive_id,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    corpora: str | Unset = UNSET,
    corpus: DriveFilesListCorpus | Unset = UNSET,
    drive_id: str | Unset = UNSET,
    include_items_from_all_drives: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    include_team_drive_items: bool | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    q: str | Unset = UNSET,
    spaces: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveFilesListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> FileList | None:
    """  Lists or searches files.

    Args:
        corpora (str | Unset):
        corpus (DriveFilesListCorpus | Unset):
        drive_id (str | Unset):
        include_items_from_all_drives (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        include_team_drive_items (bool | Unset):
        order_by (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        q (str | Unset):
        spaces (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveFilesListAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileList
     """


    return sync_detailed(
        client=client,
corpora=corpora,
corpus=corpus,
drive_id=drive_id,
include_items_from_all_drives=include_items_from_all_drives,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
include_team_drive_items=include_team_drive_items,
order_by=order_by,
page_size=page_size,
page_token=page_token,
q=q,
spaces=spaces,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
team_drive_id=team_drive_id,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    corpora: str | Unset = UNSET,
    corpus: DriveFilesListCorpus | Unset = UNSET,
    drive_id: str | Unset = UNSET,
    include_items_from_all_drives: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    include_team_drive_items: bool | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    q: str | Unset = UNSET,
    spaces: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveFilesListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[FileList]:
    """  Lists or searches files.

    Args:
        corpora (str | Unset):
        corpus (DriveFilesListCorpus | Unset):
        drive_id (str | Unset):
        include_items_from_all_drives (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        include_team_drive_items (bool | Unset):
        order_by (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        q (str | Unset):
        spaces (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveFilesListAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileList]
     """


    kwargs = _get_kwargs(
        corpora=corpora,
corpus=corpus,
drive_id=drive_id,
include_items_from_all_drives=include_items_from_all_drives,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
include_team_drive_items=include_team_drive_items,
order_by=order_by,
page_size=page_size,
page_token=page_token,
q=q,
spaces=spaces,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
team_drive_id=team_drive_id,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    corpora: str | Unset = UNSET,
    corpus: DriveFilesListCorpus | Unset = UNSET,
    drive_id: str | Unset = UNSET,
    include_items_from_all_drives: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    include_team_drive_items: bool | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    q: str | Unset = UNSET,
    spaces: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveFilesListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> FileList | None:
    """  Lists or searches files.

    Args:
        corpora (str | Unset):
        corpus (DriveFilesListCorpus | Unset):
        drive_id (str | Unset):
        include_items_from_all_drives (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        include_team_drive_items (bool | Unset):
        order_by (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        q (str | Unset):
        spaces (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveFilesListAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileList
     """


    return (await asyncio_detailed(
        client=client,
corpora=corpora,
corpus=corpus,
drive_id=drive_id,
include_items_from_all_drives=include_items_from_all_drives,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
include_team_drive_items=include_team_drive_items,
order_by=order_by,
page_size=page_size,
page_token=page_token,
q=q,
spaces=spaces,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
team_drive_id=team_drive_id,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
