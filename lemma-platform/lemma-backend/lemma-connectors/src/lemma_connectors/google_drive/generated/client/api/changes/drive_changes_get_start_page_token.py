from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_changes_get_start_page_token_alt import DriveChangesGetStartPageTokenAlt
from ...models.start_page_token import StartPageToken
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    drive_id: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveChangesGetStartPageTokenAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["driveId"] = drive_id

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
        "url": "/changes/startPageToken",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StartPageToken | None:
    if response.status_code == 200:
        response_200 = StartPageToken.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StartPageToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    drive_id: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveChangesGetStartPageTokenAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[StartPageToken]:
    """  Gets the starting pageToken for listing future changes.

    Args:
        drive_id (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveChangesGetStartPageTokenAlt | Unset):
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
        Response[StartPageToken]
     """


    kwargs = _get_kwargs(
        drive_id=drive_id,
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
    drive_id: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveChangesGetStartPageTokenAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> StartPageToken | None:
    """  Gets the starting pageToken for listing future changes.

    Args:
        drive_id (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveChangesGetStartPageTokenAlt | Unset):
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
        StartPageToken
     """


    return sync_detailed(
        client=client,
drive_id=drive_id,
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
    drive_id: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveChangesGetStartPageTokenAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[StartPageToken]:
    """  Gets the starting pageToken for listing future changes.

    Args:
        drive_id (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveChangesGetStartPageTokenAlt | Unset):
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
        Response[StartPageToken]
     """


    kwargs = _get_kwargs(
        drive_id=drive_id,
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
    drive_id: str | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    team_drive_id: str | Unset = UNSET,
    alt: DriveChangesGetStartPageTokenAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> StartPageToken | None:
    """  Gets the starting pageToken for listing future changes.

    Args:
        drive_id (str | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        team_drive_id (str | Unset):
        alt (DriveChangesGetStartPageTokenAlt | Unset):
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
        StartPageToken
     """


    return (await asyncio_detailed(
        client=client,
drive_id=drive_id,
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
