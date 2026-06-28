from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calendar_calendar_list_list_alt import CalendarCalendarListListAlt
from ...models.calendar_calendar_list_list_min_access_role import CalendarCalendarListListMinAccessRole
from ...models.calendar_list import CalendarList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListListMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

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
        "method": "get",
        "url": "/users/me/calendarList",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CalendarList | None:
    if response.status_code == 200:
        response_200 = CalendarList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CalendarList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListListMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[CalendarList]:
    """  Returns the calendars on the user's calendar list.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListListMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListListAlt | Unset):
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
        Response[CalendarList]
     """


    kwargs = _get_kwargs(
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
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListListMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> CalendarList | None:
    """  Returns the calendars on the user's calendar list.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListListMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListListAlt | Unset):
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
        CalendarList
     """


    return sync_detailed(
        client=client,
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
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListListMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[CalendarList]:
    """  Returns the calendars on the user's calendar list.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListListMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListListAlt | Unset):
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
        Response[CalendarList]
     """


    kwargs = _get_kwargs(
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
    max_results: int | Unset = UNSET,
    min_access_role: CalendarCalendarListListMinAccessRole | Unset = UNSET,
    page_token: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
    show_hidden: bool | Unset = UNSET,
    sync_token: str | Unset = UNSET,
    alt: CalendarCalendarListListAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> CalendarList | None:
    """  Returns the calendars on the user's calendar list.

    Args:
        max_results (int | Unset):
        min_access_role (CalendarCalendarListListMinAccessRole | Unset):
        page_token (str | Unset):
        show_deleted (bool | Unset):
        show_hidden (bool | Unset):
        sync_token (str | Unset):
        alt (CalendarCalendarListListAlt | Unset):
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
        CalendarList
     """


    return (await asyncio_detailed(
        client=client,
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
