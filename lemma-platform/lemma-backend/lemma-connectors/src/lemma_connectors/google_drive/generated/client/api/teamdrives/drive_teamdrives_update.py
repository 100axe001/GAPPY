from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_teamdrives_update_alt import DriveTeamdrivesUpdateAlt
from ...models.team_drive import TeamDrive
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    team_drive_id: str,
    *,
    body: TeamDrive | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DriveTeamdrivesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["useDomainAdminAccess"] = use_domain_admin_access

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
        "method": "patch",
        "url": "/teamdrives/{team_drive_id}".format(team_drive_id=quote(str(team_drive_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TeamDrive | None:
    if response.status_code == 200:
        response_200 = TeamDrive.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TeamDrive]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_drive_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamDrive | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DriveTeamdrivesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[TeamDrive]:
    """  Deprecated use drives.update instead

    Args:
        team_drive_id (str):
        use_domain_admin_access (bool | Unset):
        alt (DriveTeamdrivesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (TeamDrive | Unset): Deprecated: use the drive collection instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamDrive]
     """


    kwargs = _get_kwargs(
        team_drive_id=team_drive_id,
body=body,
use_domain_admin_access=use_domain_admin_access,
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
    team_drive_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamDrive | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DriveTeamdrivesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> TeamDrive | None:
    """  Deprecated use drives.update instead

    Args:
        team_drive_id (str):
        use_domain_admin_access (bool | Unset):
        alt (DriveTeamdrivesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (TeamDrive | Unset): Deprecated: use the drive collection instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamDrive
     """


    return sync_detailed(
        team_drive_id=team_drive_id,
client=client,
body=body,
use_domain_admin_access=use_domain_admin_access,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    ).parsed

async def asyncio_detailed(
    team_drive_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamDrive | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DriveTeamdrivesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[TeamDrive]:
    """  Deprecated use drives.update instead

    Args:
        team_drive_id (str):
        use_domain_admin_access (bool | Unset):
        alt (DriveTeamdrivesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (TeamDrive | Unset): Deprecated: use the drive collection instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamDrive]
     """


    kwargs = _get_kwargs(
        team_drive_id=team_drive_id,
body=body,
use_domain_admin_access=use_domain_admin_access,
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
    team_drive_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamDrive | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DriveTeamdrivesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> TeamDrive | None:
    """  Deprecated use drives.update instead

    Args:
        team_drive_id (str):
        use_domain_admin_access (bool | Unset):
        alt (DriveTeamdrivesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (TeamDrive | Unset): Deprecated: use the drive collection instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamDrive
     """


    return (await asyncio_detailed(
        team_drive_id=team_drive_id,
client=client,
body=body,
use_domain_admin_access=use_domain_admin_access,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
