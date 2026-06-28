from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_files_get_alt import DriveFilesGetAlt
from ...models.file import File
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    file_id: str,
    *,
    acknowledge_abuse: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    alt: DriveFilesGetAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["acknowledgeAbuse"] = acknowledge_abuse

    params["includeLabels"] = include_labels

    params["includePermissionsForView"] = include_permissions_for_view

    params["supportsAllDrives"] = supports_all_drives

    params["supportsTeamDrives"] = supports_team_drives

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
        "url": "/files/{file_id}".format(file_id=quote(str(file_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == 200:
        response_200 = File.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: str,
    *,
    client: AuthenticatedClient,
    acknowledge_abuse: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    alt: DriveFilesGetAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[File]:
    """  Gets a file's metadata or content by ID.

    Args:
        file_id (str):
        acknowledge_abuse (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        alt (DriveFilesGetAlt | Unset):
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
        Response[File]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
acknowledge_abuse=acknowledge_abuse,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    acknowledge_abuse: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    alt: DriveFilesGetAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> File | None:
    """  Gets a file's metadata or content by ID.

    Args:
        file_id (str):
        acknowledge_abuse (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        alt (DriveFilesGetAlt | Unset):
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
        File
     """


    return sync_detailed(
        file_id=file_id,
client=client,
acknowledge_abuse=acknowledge_abuse,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    ).parsed

async def asyncio_detailed(
    file_id: str,
    *,
    client: AuthenticatedClient,
    acknowledge_abuse: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    alt: DriveFilesGetAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[File]:
    """  Gets a file's metadata or content by ID.

    Args:
        file_id (str):
        acknowledge_abuse (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        alt (DriveFilesGetAlt | Unset):
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
        Response[File]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
acknowledge_abuse=acknowledge_abuse,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    acknowledge_abuse: bool | Unset = UNSET,
    include_labels: str | Unset = UNSET,
    include_permissions_for_view: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    alt: DriveFilesGetAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> File | None:
    """  Gets a file's metadata or content by ID.

    Args:
        file_id (str):
        acknowledge_abuse (bool | Unset):
        include_labels (str | Unset):
        include_permissions_for_view (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        alt (DriveFilesGetAlt | Unset):
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
        File
     """


    return (await asyncio_detailed(
        file_id=file_id,
client=client,
acknowledge_abuse=acknowledge_abuse,
include_labels=include_labels,
include_permissions_for_view=include_permissions_for_view,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
