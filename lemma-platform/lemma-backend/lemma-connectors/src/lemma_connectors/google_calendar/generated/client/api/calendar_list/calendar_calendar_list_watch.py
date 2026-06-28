from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calendar_calendar_list_watch_alt import CalendarCalendarListWatchAlt
from ...models.calendar_calendar_list_watch_min_access_role import CalendarCalendarListWatchMinAccessRole
from ...models.channel import Channel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: Channel | Unset = UNSET,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListWatchMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["maxResults"] = max_results

    json_min_access_role: str | Unset = UNSET
    if not isinstance(min_access_role, Unset):
        json_min_access_role = min_access_role.value

    params["minAccessRole"] = json_min_access_role

    params["pageToken"] = page_token

    params["showDeleted"] = show_deleted

    params["showHidden"] = show_hidden

    params["syncToken"] = sync_token

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
        "url": "/users/me/calendarList/watch",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Channel | None:
    if response.status_code == 200:
        response_200 = Channel.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Channel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Channel | Unset = UNSET,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListWatchMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Channel]:
    """  Watch for changes to CalendarList resources.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListWatchMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListWatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Channel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Channel]
     """


    kwargs = _get_kwargs(
        body=body,
max_results=max_results,
min_access_role=min_access_role,
page_token=page_token,
show_deleted=show_deleted,
show_hidden=show_hidden,
sync_token=sync_token,
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
    body: Channel | Unset = UNSET,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListWatchMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Channel | None:
    """  Watch for changes to CalendarList resources.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListWatchMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListWatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Channel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Channel
     """


    return sync_detailed(
        client=client,
body=body,
max_results=max_results,
min_access_role=min_access_role,
page_token=page_token,
show_deleted=show_deleted,
show_hidden=show_hidden,
sync_token=sync_token,
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
    body: Channel | Unset = UNSET,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListWatchMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Channel]:
    """  Watch for changes to CalendarList resources.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListWatchMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListWatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Channel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Channel]
     """


    kwargs = _get_kwargs(
        body=body,
max_results=max_results,
min_access_role=min_access_role,
page_token=page_token,
show_deleted=show_deleted,
show_hidden=show_hidden,
sync_token=sync_token,
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
    body: Channel | Unset = UNSET,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListWatchMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Channel | None:
    """  Watch for changes to CalendarList resources.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListWatchMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListWatchAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Channel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Channel
     """


    return (await asyncio_detailed(
        client=client,
body=body,
max_results=max_results,
min_access_role=min_access_role,
page_token=page_token,
show_deleted=show_deleted,
show_hidden=show_hidden,
sync_token=sync_token,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
