from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.acl_rule import AclRule
from ...models.calendar_acl_patch_alt import CalendarAclPatchAlt
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    calendar_id: str,
    rule_id: str,
    *,
    body: AclRule | Unset = UNSET,
    send_notifications: bool | Unset = UNSET,
    alt: CalendarAclPatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["sendNotifications"] = send_notifications

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
        "url": "/calendars/{calendar_id}/acl/{rule_id}".format(calendar_id=quote(str(calendar_id), safe=""),rule_id=quote(str(rule_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AclRule | None:
    if response.status_code == 200:
        response_200 = AclRule.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AclRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    calendar_id: str,
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: AclRule | Unset = UNSET,
    send_notifications: bool | Unset = UNSET,
    alt: CalendarAclPatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[AclRule]:
    """  Updates an access control rule. This method supports patch semantics.

    Args:
        calendar_id (str):
        rule_id (str):
        send_notifications (bool | Unset):
        alt (CalendarAclPatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (AclRule | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclRule]
     """


    kwargs = _get_kwargs(
        calendar_id=calendar_id,
rule_id=rule_id,
body=body,
send_notifications=send_notifications,
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
    calendar_id: str,
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: AclRule | Unset = UNSET,
    send_notifications: bool | Unset = UNSET,
    alt: CalendarAclPatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> AclRule | None:
    """  Updates an access control rule. This method supports patch semantics.

    Args:
        calendar_id (str):
        rule_id (str):
        send_notifications (bool | Unset):
        alt (CalendarAclPatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (AclRule | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclRule
     """


    return sync_detailed(
        calendar_id=calendar_id,
rule_id=rule_id,
client=client,
body=body,
send_notifications=send_notifications,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    ).parsed

async def asyncio_detailed(
    calendar_id: str,
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: AclRule | Unset = UNSET,
    send_notifications: bool | Unset = UNSET,
    alt: CalendarAclPatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[AclRule]:
    """  Updates an access control rule. This method supports patch semantics.

    Args:
        calendar_id (str):
        rule_id (str):
        send_notifications (bool | Unset):
        alt (CalendarAclPatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (AclRule | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AclRule]
     """


    kwargs = _get_kwargs(
        calendar_id=calendar_id,
rule_id=rule_id,
body=body,
send_notifications=send_notifications,
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
    calendar_id: str,
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: AclRule | Unset = UNSET,
    send_notifications: bool | Unset = UNSET,
    alt: CalendarAclPatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> AclRule | None:
    """  Updates an access control rule. This method supports patch semantics.

    Args:
        calendar_id (str):
        rule_id (str):
        send_notifications (bool | Unset):
        alt (CalendarAclPatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (AclRule | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AclRule
     """


    return (await asyncio_detailed(
        calendar_id=calendar_id,
rule_id=rule_id,
client=client,
body=body,
send_notifications=send_notifications,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
