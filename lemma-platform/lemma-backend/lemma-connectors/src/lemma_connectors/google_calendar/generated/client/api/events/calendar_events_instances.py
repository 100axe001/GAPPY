from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calendar_events_instances_alt import CalendarEventsInstancesAlt
from ...models.events import Events
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    calendar_id: str,
    event_id: str,
    *,
    always_include_email: bool | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    original_start: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    alt: CalendarEventsInstancesAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["alwaysIncludeEmail"] = always_include_email

    params["maxAttendees"] = max_attendees

    params["maxResults"] = max_results

    params["originalStart"] = original_start

    params["pageToken"] = page_token

    params["showDeleted"] = show_deleted

    params["timeMax"] = time_max

    params["timeMin"] = time_min

    params["timeZone"] = time_zone

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
        "url": "/calendars/{calendar_id}/events/{event_id}/instances".format(calendar_id=quote(str(calendar_id), safe=""),event_id=quote(str(event_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Events | None:
    if response.status_code == 200:
        response_200 = Events.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Events]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    calendar_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
    always_include_email: bool | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    original_start: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    alt: CalendarEventsInstancesAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Events]:
    """  Returns instances of the specified recurring event.

    Args:
        calendar_id (str):
        event_id (str):
        always_include_email (bool | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        original_start (str | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        alt (CalendarEventsInstancesAlt | Unset):
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
        Response[Events]
     """


    kwargs = _get_kwargs(
        calendar_id=calendar_id,
event_id=event_id,
always_include_email=always_include_email,
max_attendees=max_attendees,
max_results=max_results,
original_start=original_start,
page_token=page_token,
show_deleted=show_deleted,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
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
    event_id: str,
    *,
    client: AuthenticatedClient,
    always_include_email: bool | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    original_start: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    alt: CalendarEventsInstancesAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Events | None:
    """  Returns instances of the specified recurring event.

    Args:
        calendar_id (str):
        event_id (str):
        always_include_email (bool | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        original_start (str | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        alt (CalendarEventsInstancesAlt | Unset):
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
        Events
     """


    return sync_detailed(
        calendar_id=calendar_id,
event_id=event_id,
client=client,
always_include_email=always_include_email,
max_attendees=max_attendees,
max_results=max_results,
original_start=original_start,
page_token=page_token,
show_deleted=show_deleted,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
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
    event_id: str,
    *,
    client: AuthenticatedClient,
    always_include_email: bool | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    original_start: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    alt: CalendarEventsInstancesAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Events]:
    """  Returns instances of the specified recurring event.

    Args:
        calendar_id (str):
        event_id (str):
        always_include_email (bool | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        original_start (str | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        alt (CalendarEventsInstancesAlt | Unset):
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
        Response[Events]
     """


    kwargs = _get_kwargs(
        calendar_id=calendar_id,
event_id=event_id,
always_include_email=always_include_email,
max_attendees=max_attendees,
max_results=max_results,
original_start=original_start,
page_token=page_token,
show_deleted=show_deleted,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
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
    event_id: str,
    *,
    client: AuthenticatedClient,
    always_include_email: bool | Unset = UNSET,
    max_attendees: int | Unset = UNSET,
    max_results: int | Unset = UNSET,
    original_start: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    time_max: str | Unset = UNSET,
    time_min: str | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    alt: CalendarEventsInstancesAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Events | None:
    """  Returns instances of the specified recurring event.

    Args:
        calendar_id (str):
        event_id (str):
        always_include_email (bool | Unset):
        max_attendees (int | Unset):
        max_results (int | Unset):
        original_start (str | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        time_max (str | Unset):
        time_min (str | Unset):
        time_zone (str | Unset):
        alt (CalendarEventsInstancesAlt | Unset):
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
        Events
     """


    return (await asyncio_detailed(
        calendar_id=calendar_id,
event_id=event_id,
client=client,
always_include_email=always_include_email,
max_attendees=max_attendees,
max_results=max_results,
original_start=original_start,
page_token=page_token,
show_deleted=show_deleted,
time_max=time_max,
time_min=time_min,
time_zone=time_zone,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
