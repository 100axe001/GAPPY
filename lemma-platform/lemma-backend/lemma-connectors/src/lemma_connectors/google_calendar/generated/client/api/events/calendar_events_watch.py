from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calendar_events_watch_alt import CalendarEventsWatchAlt
from ...models.calendar_events_watch_order_by import CalendarEventsWatchOrderBy
from ...models.channel import Channel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    calendar_id: str,
    *,
    body: Channel | Unset = UNSET,
    always_include_email: bool | Unset = UNSET,
    event_types: list[str] | Unset = UNSET,
    i_cal_uid: str | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    order_by: CalendarEventsWatchOrderBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
    private_extended_property: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    shared_extended_property: list[str] | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden_invitations: bool | Unset = UNSET,
    single_events: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    updated_min: str | Unset = UNSET,
    alt: CalendarEventsWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["alwaysIncludeEmail"] = always_include_email

    json_event_types: list[str] | Unset = UNSET
    if not isinstance(event_types, Unset):
        json_event_types = event_types


    params["eventTypes"] = json_event_types

    params["iCalUID"] = i_cal_uid

    params["maxAttendees"] = max_attendees

    params["maxResults"] = max_results

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["pageToken"] = page_token

    json_private_extended_property: list[str] | Unset = UNSET
    if not isinstance(private_extended_property, Unset):
        json_private_extended_property = private_extended_property


    params["privateExtendedProperty"] = json_private_extended_property

    params["q"] = q

    json_shared_extended_property: list[str] | Unset = UNSET
    if not isinstance(shared_extended_property, Unset):
        json_shared_extended_property = shared_extended_property


    params["sharedExtendedProperty"] = json_shared_extended_property

    params["showDeleted"] = show_deleted

    params["showHiddenInvitations"] = show_hidden_invitations

    params["singleEvents"] = single_events

    params["syncToken"] = sync_token

    params["timeMax"] = time_max

    params["timeMin"] = time_min

    params["timeZone"] = time_zone

    params["updatedMin"] = updated_min

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
        "url": "/calendars/{calendar_id}/events/watch".format(calendar_id=quote(str(calendar_id), safe=""),),
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
    calendar_id: str,
    *,
    client: AuthenticatedClient,
    body: Channel | Unset = UNSET,
    always_include_email: bool | Unset = UNSET,
    event_types: list[str] | Unset = UNSET,
    i_cal_uid: str | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    order_by: CalendarEventsWatchOrderBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
    private_extended_property: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    shared_extended_property: list[str] | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden_invitations: bool | Unset = UNSET,
    single_events: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    updated_min: str | Unset = UNSET,
    alt: CalendarEventsWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Channel]:
    """  Watch for changes to Events resources.

    Args:
        calendar_id (str):
        always_include_email (bool | Unset):
        event_types (list[str] | Unset):
        i_cal_uid (str | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        order_by (CalendarEventsWatchOrderBy | Unset):
        page_token (str | Unset):
        private_extended_property (list[str] | Unset):
        q (str | Unset):
        shared_extended_property (list[str] | Unset):
        show_deleted (bool | Unset):
        show_hidden_invitations (bool | Unset):
        single_events (bool | Unset):
        sync_token (str | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        updated_min (str | Unset):
        alt (CalendarEventsWatchAlt | Unset):
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
        calendar_id=calendar_id,
body=body,
always_include_email=always_include_email,
event_types=event_types,
i_cal_uid=i_cal_uid,
max_attendees=max_attendees,
max_results=max_results,
order_by=order_by,
page_token=page_token,
private_extended_property=private_extended_property,
q=q,
shared_extended_property=shared_extended_property,
show_deleted=show_deleted,
show_hidden_invitations=show_hidden_invitations,
single_events=single_events,
sync_token=sync_token,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
updated_min=updated_min,
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
    *,
    client: AuthenticatedClient,
    body: Channel | Unset = UNSET,
    always_include_email: bool | Unset = UNSET,
    event_types: list[str] | Unset = UNSET,
    i_cal_uid: str | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    order_by: CalendarEventsWatchOrderBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
    private_extended_property: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    shared_extended_property: list[str] | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden_invitations: bool | Unset = UNSET,
    single_events: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    updated_min: str | Unset = UNSET,
    alt: CalendarEventsWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Channel | None:
    """  Watch for changes to Events resources.

    Args:
        calendar_id (str):
        always_include_email (bool | Unset):
        event_types (list[str] | Unset):
        i_cal_uid (str | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        order_by (CalendarEventsWatchOrderBy | Unset):
        page_token (str | Unset):
        private_extended_property (list[str] | Unset):
        q (str | Unset):
        shared_extended_property (list[str] | Unset):
        show_deleted (bool | Unset):
        show_hidden_invitations (bool | Unset):
        single_events (bool | Unset):
        sync_token (str | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        updated_min (str | Unset):
        alt (CalendarEventsWatchAlt | Unset):
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
        calendar_id=calendar_id,
client=client,
body=body,
always_include_email=always_include_email,
event_types=event_types,
i_cal_uid=i_cal_uid,
max_attendees=max_attendees,
max_results=max_results,
order_by=order_by,
page_token=page_token,
private_extended_property=private_extended_property,
q=q,
shared_extended_property=shared_extended_property,
show_deleted=show_deleted,
show_hidden_invitations=show_hidden_invitations,
single_events=single_events,
sync_token=sync_token,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
updated_min=updated_min,
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
    *,
    client: AuthenticatedClient,
    body: Channel | Unset = UNSET,
    always_include_email: bool | Unset = UNSET,
    event_types: list[str] | Unset = UNSET,
    i_cal_uid: str | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    order_by: CalendarEventsWatchOrderBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
    private_extended_property: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    shared_extended_property: list[str] | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden_invitations: bool | Unset = UNSET,
    single_events: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    updated_min: str | Unset = UNSET,
    alt: CalendarEventsWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Channel]:
    """  Watch for changes to Events resources.

    Args:
        calendar_id (str):
        always_include_email (bool | Unset):
        event_types (list[str] | Unset):
        i_cal_uid (str | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        order_by (CalendarEventsWatchOrderBy | Unset):
        page_token (str | Unset):
        private_extended_property (list[str] | Unset):
        q (str | Unset):
        shared_extended_property (list[str] | Unset):
        show_deleted (bool | Unset):
        show_hidden_invitations (bool | Unset):
        single_events (bool | Unset):
        sync_token (str | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        updated_min (str | Unset):
        alt (CalendarEventsWatchAlt | Unset):
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
        calendar_id=calendar_id,
body=body,
always_include_email=always_include_email,
event_types=event_types,
i_cal_uid=i_cal_uid,
max_attendees=max_attendees,
max_results=max_results,
order_by=order_by,
page_token=page_token,
private_extended_property=private_extended_property,
q=q,
shared_extended_property=shared_extended_property,
show_deleted=show_deleted,
show_hidden_invitations=show_hidden_invitations,
single_events=single_events,
sync_token=sync_token,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
updated_min=updated_min,
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
    *,
    client: AuthenticatedClient,
    body: Channel | Unset = UNSET,
    always_include_email: bool | Unset = UNSET,
    event_types: list[str] | Unset = UNSET,
    i_cal_uid: str | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    order_by: CalendarEventsWatchOrderBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
    private_extended_property: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    shared_extended_property: list[str] | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden_invitations: bool | Unset = UNSET,
    single_events: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    updated_min: str | Unset = UNSET,
    alt: CalendarEventsWatchAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Channel | None:
    """  Watch for changes to Events resources.

    Args:
        calendar_id (str):
        always_include_email (bool | Unset):
        event_types (list[str] | Unset):
        i_cal_uid (str | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        order_by (CalendarEventsWatchOrderBy | Unset):
        page_token (str | Unset):
        private_extended_property (list[str] | Unset):
        q (str | Unset):
        shared_extended_property (list[str] | Unset):
        show_deleted (bool | Unset):
        show_hidden_invitations (bool | Unset):
        single_events (bool | Unset):
        sync_token (str | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        updated_min (str | Unset):
        alt (CalendarEventsWatchAlt | Unset):
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
        calendar_id=calendar_id,
client=client,
body=body,
always_include_email=always_include_email,
event_types=event_types,
i_cal_uid=i_cal_uid,
max_attendees=max_attendees,
max_results=max_results,
order_by=order_by,
page_token=page_token,
private_extended_property=private_extended_property,
q=q,
shared_extended_property=shared_extended_property,
show_deleted=show_deleted,
show_hidden_invitations=show_hidden_invitations,
single_events=single_events,
sync_token=sync_token,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
updated_min=updated_min,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
