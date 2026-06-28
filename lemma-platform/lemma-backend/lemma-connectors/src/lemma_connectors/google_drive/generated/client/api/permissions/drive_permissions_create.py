from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_permissions_create_alt import DrivePermissionsCreateAlt
from ...models.permission import Permission
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    file_id: str,
    *,
    body: Permission | Unset = UNSET,
    email_message: str | Unset = UNSET,
    enforce_single_parent: bool | Unset = UNSET,
    move_to_new_owners_root: bool | Unset = UNSET,
    send_notification_email: bool | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    transfer_ownership: bool | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DrivePermissionsCreateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["emailMessage"] = email_message

    params["enforceSingleParent"] = enforce_single_parent

    params["moveToNewOwnersRoot"] = move_to_new_owners_root

    params["sendNotificationEmail"] = send_notification_email

    params["supportsAllDrives"] = supports_all_drives

    params["supportsTeamDrives"] = supports_team_drives

    params["transferOwnership"] = transfer_ownership

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
        "method": "post",
        "url": "/files/{file_id}/permissions".format(file_id=quote(str(file_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Permission | None:
    if response.status_code == 200:
        response_200 = Permission.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Permission]:
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
    body: Permission | Unset = UNSET,
    email_message: str | Unset = UNSET,
    enforce_single_parent: bool | Unset = UNSET,
    move_to_new_owners_root: bool | Unset = UNSET,
    send_notification_email: bool | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    transfer_ownership: bool | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DrivePermissionsCreateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Permission]:
    """  Creates a permission for a file or shared drive. For more information on creating permissions, see
    Share files, folders & drives.

    Args:
        file_id (str):
        email_message (str | Unset):
        enforce_single_parent (bool | Unset):
        move_to_new_owners_root (bool | Unset):
        send_notification_email (bool | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        transfer_ownership (bool | Unset):
        use_domain_admin_access (bool | Unset):
        alt (DrivePermissionsCreateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Permission | Unset): A permission for a file. A permission grants a user, group,
            domain, or the world access to a file or a folder hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permission]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
body=body,
email_message=email_message,
enforce_single_parent=enforce_single_parent,
move_to_new_owners_root=move_to_new_owners_root,
send_notification_email=send_notification_email,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
transfer_ownership=transfer_ownership,
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Permission | Unset = UNSET,
    email_message: str | Unset = UNSET,
    enforce_single_parent: bool | Unset = UNSET,
    move_to_new_owners_root: bool | Unset = UNSET,
    send_notification_email: bool | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    transfer_ownership: bool | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DrivePermissionsCreateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Permission | None:
    """  Creates a permission for a file or shared drive. For more information on creating permissions, see
    Share files, folders & drives.

    Args:
        file_id (str):
        email_message (str | Unset):
        enforce_single_parent (bool | Unset):
        move_to_new_owners_root (bool | Unset):
        send_notification_email (bool | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        transfer_ownership (bool | Unset):
        use_domain_admin_access (bool | Unset):
        alt (DrivePermissionsCreateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Permission | Unset): A permission for a file. A permission grants a user, group,
            domain, or the world access to a file or a folder hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permission
     """


    return sync_detailed(
        file_id=file_id,
client=client,
body=body,
email_message=email_message,
enforce_single_parent=enforce_single_parent,
move_to_new_owners_root=move_to_new_owners_root,
send_notification_email=send_notification_email,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
transfer_ownership=transfer_ownership,
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Permission | Unset = UNSET,
    email_message: str | Unset = UNSET,
    enforce_single_parent: bool | Unset = UNSET,
    move_to_new_owners_root: bool | Unset = UNSET,
    send_notification_email: bool | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    transfer_ownership: bool | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DrivePermissionsCreateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Permission]:
    """  Creates a permission for a file or shared drive. For more information on creating permissions, see
    Share files, folders & drives.

    Args:
        file_id (str):
        email_message (str | Unset):
        enforce_single_parent (bool | Unset):
        move_to_new_owners_root (bool | Unset):
        send_notification_email (bool | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        transfer_ownership (bool | Unset):
        use_domain_admin_access (bool | Unset):
        alt (DrivePermissionsCreateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Permission | Unset): A permission for a file. A permission grants a user, group,
            domain, or the world access to a file or a folder hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permission]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
body=body,
email_message=email_message,
enforce_single_parent=enforce_single_parent,
move_to_new_owners_root=move_to_new_owners_root,
send_notification_email=send_notification_email,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
transfer_ownership=transfer_ownership,
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
    file_id: str,
    *,
    client: AuthenticatedClient,
    body: Permission | Unset = UNSET,
    email_message: str | Unset = UNSET,
    enforce_single_parent: bool | Unset = UNSET,
    move_to_new_owners_root: bool | Unset = UNSET,
    send_notification_email: bool | Unset = UNSET,
    supports_all_drives: bool | Unset = UNSET,
    supports_team_drives: bool | Unset = UNSET,
    transfer_ownership: bool | Unset = UNSET,
    use_domain_admin_access: bool | Unset = UNSET,
    alt: DrivePermissionsCreateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Permission | None:
    """  Creates a permission for a file or shared drive. For more information on creating permissions, see
    Share files, folders & drives.

    Args:
        file_id (str):
        email_message (str | Unset):
        enforce_single_parent (bool | Unset):
        move_to_new_owners_root (bool | Unset):
        send_notification_email (bool | Unset):
        supports_all_drives (bool | Unset):
        supports_team_drives (bool | Unset):
        transfer_ownership (bool | Unset):
        use_domain_admin_access (bool | Unset):
        alt (DrivePermissionsCreateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Permission | Unset): A permission for a file. A permission grants a user, group,
            domain, or the world access to a file or a folder hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permission
     """


    return (await asyncio_detailed(
        file_id=file_id,
client=client,
body=body,
email_message=email_message,
enforce_single_parent=enforce_single_parent,
move_to_new_owners_root=move_to_new_owners_root,
send_notification_email=send_notification_email,
supports_all_drives=supports_all_drives,
supports_team_drives=supports_team_drives,
transfer_ownership=transfer_ownership,
use_domain_admin_access=use_domain_admin_access,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
