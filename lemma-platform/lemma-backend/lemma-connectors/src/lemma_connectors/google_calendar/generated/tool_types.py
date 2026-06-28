from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.google_calendar.generated.pydantic_models import Acl, AclRule, Calendar, CalendarList, CalendarListEntry, Channel, Colors, Event, Events, FreeBusyRequest, FreeBusyResponse, Setting, Settings

class CalendarAclDeleteToolInput(BaseModel):
    """Input for tool `calendar_acl_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    rule_id: str = Field(..., description='ACL rule identifier.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_acl_delete`."""
    pass

class CalendarAclGetToolInput(BaseModel):
    """Input for tool `calendar_acl_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    rule_id: str = Field(..., description='ACL rule identifier.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclGetToolOutput(AclRule):
    """Output for tool `calendar_acl_get`."""
    pass

class CalendarAclInsertToolInput(BaseModel):
    """Input for tool `calendar_acl_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    send_notifications: bool | None = Field(default=None, description='Whether to send notifications about the calendar sharing change. Optional. The default is True.')
    body: AclRule | None = Field(default=None, description='Request body for `calendar_acl_insert`.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclInsertToolOutput(AclRule):
    """Output for tool `calendar_acl_insert`."""
    pass

class CalendarAclListToolInput(BaseModel):
    """Input for tool `calendar_acl_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to "none". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclListToolOutput(Acl):
    """Output for tool `calendar_acl_list`."""
    pass

class CalendarAclPatchToolInput(BaseModel):
    """Input for tool `calendar_acl_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    rule_id: str = Field(..., description='ACL rule identifier.')
    send_notifications: bool | None = Field(default=None, description='Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.')
    body: AclRule | None = Field(default=None, description='Request body for `calendar_acl_patch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclPatchToolOutput(AclRule):
    """Output for tool `calendar_acl_patch`."""
    pass

class CalendarAclUpdateToolInput(BaseModel):
    """Input for tool `calendar_acl_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    rule_id: str = Field(..., description='ACL rule identifier.')
    send_notifications: bool | None = Field(default=None, description='Whether to send notifications about the calendar sharing change. Note that there are no notifications on access removal. Optional. The default is True.')
    body: AclRule | None = Field(default=None, description='Request body for `calendar_acl_update`.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclUpdateToolOutput(AclRule):
    """Output for tool `calendar_acl_update`."""
    pass

class CalendarAclWatchToolInput(BaseModel):
    """Input for tool `calendar_acl_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to "none". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    body: Channel | None = Field(default=None, description='Request body for `calendar_acl_watch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarAclWatchToolOutput(Channel):
    """Output for tool `calendar_acl_watch`."""
    pass

class CalendarCalendarListDeleteToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_calendar_list_delete`."""
    pass

class CalendarCalendarListGetToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListGetToolOutput(CalendarListEntry):
    """Output for tool `calendar_calendar_list_get`."""
    pass

class CalendarCalendarListInsertToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    color_rgb_format: bool | None = Field(default=None, description='Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.')
    body: CalendarListEntry | None = Field(default=None, description='Request body for `calendar_calendar_list_insert`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListInsertToolOutput(CalendarListEntry):
    """Output for tool `calendar_calendar_list_insert`."""
    pass

class CalendarCalendarListListToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    min_access_role: Literal['freeBusyReader', 'owner', 'reader', 'writer'] | None = Field(default=None, description='The minimum access role for the user in the returned entries. Optional. The default is no restriction.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted calendar list entries in the result. Optional. The default is False.')
    show_hidden: bool | None = Field(default=None, description='Whether to show hidden entries. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description="Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False.\nTo ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.")
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListListToolOutput(CalendarList):
    """Output for tool `calendar_calendar_list_list`."""
    pass

class CalendarCalendarListPatchToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    color_rgb_format: bool | None = Field(default=None, description='Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.')
    body: CalendarListEntry | None = Field(default=None, description='Request body for `calendar_calendar_list_patch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListPatchToolOutput(CalendarListEntry):
    """Output for tool `calendar_calendar_list_patch`."""
    pass

class CalendarCalendarListUpdateToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    color_rgb_format: bool | None = Field(default=None, description='Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.')
    body: CalendarListEntry | None = Field(default=None, description='Request body for `calendar_calendar_list_update`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListUpdateToolOutput(CalendarListEntry):
    """Output for tool `calendar_calendar_list_update`."""
    pass

class CalendarCalendarListWatchToolInput(BaseModel):
    """Input for tool `calendar_calendar_list_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    min_access_role: Literal['freeBusyReader', 'owner', 'reader', 'writer'] | None = Field(default=None, description='The minimum access role for the user in the returned entries. Optional. The default is no restriction.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted calendar list entries in the result. Optional. The default is False.')
    show_hidden: bool | None = Field(default=None, description='Whether to show hidden entries. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description="Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False.\nTo ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.")
    body: Channel | None = Field(default=None, description='Request body for `calendar_calendar_list_watch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarListWatchToolOutput(Channel):
    """Output for tool `calendar_calendar_list_watch`."""
    pass

class CalendarCalendarsClearToolInput(BaseModel):
    """Input for tool `calendar_calendars_clear`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsClearToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_calendars_clear`."""
    pass

class CalendarCalendarsDeleteToolInput(BaseModel):
    """Input for tool `calendar_calendars_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_calendars_delete`."""
    pass

class CalendarCalendarsGetToolInput(BaseModel):
    """Input for tool `calendar_calendars_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsGetToolOutput(Calendar):
    """Output for tool `calendar_calendars_get`."""
    pass

class CalendarCalendarsInsertToolInput(BaseModel):
    """Input for tool `calendar_calendars_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: Calendar | None = Field(default=None, description='Request body for `calendar_calendars_insert`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsInsertToolOutput(Calendar):
    """Output for tool `calendar_calendars_insert`."""
    pass

class CalendarCalendarsPatchToolInput(BaseModel):
    """Input for tool `calendar_calendars_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    body: Calendar | None = Field(default=None, description='Request body for `calendar_calendars_patch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsPatchToolOutput(Calendar):
    """Output for tool `calendar_calendars_patch`."""
    pass

class CalendarCalendarsUpdateToolInput(BaseModel):
    """Input for tool `calendar_calendars_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    body: Calendar | None = Field(default=None, description='Request body for `calendar_calendars_update`.')
    model_config = ConfigDict(extra='forbid')

class CalendarCalendarsUpdateToolOutput(Calendar):
    """Output for tool `calendar_calendars_update`."""
    pass

class CalendarChannelsStopToolInput(BaseModel):
    """Input for tool `calendar_channels_stop`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: Channel | None = Field(default=None, description='Request body for `calendar_channels_stop`.')
    model_config = ConfigDict(extra='forbid')

class CalendarChannelsStopToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_channels_stop`."""
    pass

class CalendarColorsGetToolInput(BaseModel):
    """Input for tool `calendar_colors_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    model_config = ConfigDict(extra='forbid')

class CalendarColorsGetToolOutput(Colors):
    """Output for tool `calendar_colors_get`."""
    pass

class CalendarEventsDeleteToolInput(BaseModel):
    """Input for tool `calendar_events_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    event_id: str = Field(..., description='Event identifier.')
    send_notifications: bool | None = Field(default=None, description='Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the deletion of the event. Note that some emails might still be sent even if you set the value to false. The default is false.')
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description='Guests who should receive notifications about the deletion of the event.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `calendar_events_delete`."""
    pass

class CalendarEventsGetToolInput(BaseModel):
    """Input for tool `calendar_events_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    event_id: str = Field(..., description='Event identifier.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    time_zone: str | None = Field(default=None, description='Time zone used in the response. Optional. The default is the time zone of the calendar.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsGetToolOutput(Event):
    """Output for tool `calendar_events_get`."""
    pass

class CalendarEventsImportToolInput(BaseModel):
    """Input for tool `calendar_events_import`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    conference_data_version: int | None = Field(default=None, description="Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.")
    supports_attachments: bool | None = Field(default=None, description='Whether API client performing operation supports event attachments. Optional. The default is False.')
    body: Event | None = Field(default=None, description='Request body for `calendar_events_import`.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsImportToolOutput(Event):
    """Output for tool `calendar_events_import`."""
    pass

class CalendarEventsInsertToolInput(BaseModel):
    """Input for tool `calendar_events_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    conference_data_version: int | None = Field(default=None, description="Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.")
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    send_notifications: bool | None = Field(default=None, description='Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the creation of the new event. Note that some emails might still be sent even if you set the value to false. The default is false.')
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description='Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false.')
    supports_attachments: bool | None = Field(default=None, description='Whether API client performing operation supports event attachments. Optional. The default is False.')
    body: Event | None = Field(default=None, description='Request body for `calendar_events_insert`.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsInsertToolOutput(Event):
    """Output for tool `calendar_events_insert`."""
    pass

class CalendarEventsInstancesToolInput(BaseModel):
    """Input for tool `calendar_events_instances`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    event_id: str = Field(..., description='Recurring event identifier.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    max_results: int | None = Field(default=None, description='Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.')
    original_start: str | None = Field(default=None, description='The original start time of the instance in the result. Optional.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events will still be included if singleEvents is False. Optional. The default is False.')
    time_max: str | None = Field(default=None, description="Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset.")
    time_min: str | None = Field(default=None, description="Lower bound (inclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset.")
    time_zone: str | None = Field(default=None, description='Time zone used in the response. Optional. The default is the time zone of the calendar.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsInstancesToolOutput(Events):
    """Output for tool `calendar_events_instances`."""
    pass

class CalendarEventsListToolInput(BaseModel):
    """Input for tool `calendar_events_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    event_types: list[str] | None = Field(default=None, description='Event types to return. Optional. Possible values are: \n- "default" \n- "focusTime" \n- "outOfOffice"This parameter can be repeated multiple times to return events of different types. Currently, this is the only allowed value for this field: \n- ["default", "focusTime", "outOfOffice"] This value will be the default.\n\nIf you\'re enrolled in the Working Location developer preview program, in addition to the default value above you can also set the "workingLocation" event type: \n- ["default", "focusTime", "outOfOffice", "workingLocation"] \n- ["workingLocation"] Additional combinations of these 4 event types will be made available in later releases. Developer Preview.')
    i_cal_uid: str | None = Field(default=None, description='Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.')
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    max_results: int | None = Field(default=None, description='Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.')
    order_by: Literal['startTime', 'updated'] | None = Field(default=None, description='The order of the events returned in the result. Optional. The default is an unspecified, stable order.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    private_extended_property: list[str] | None = Field(default=None, description='Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.')
    q: str | None = Field(default=None, description="Free text search terms to find events that match these terms in the following fields: summary, description, location, attendee's displayName, attendee's email. Optional.")
    shared_extended_property: list[str] | None = Field(default=None, description='Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.')
    show_hidden_invitations: bool | None = Field(default=None, description='Whether to include hidden invitations in the result. Optional. The default is False.')
    single_events: bool | None = Field(default=None, description='Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.\nThere are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.\n\nThese are: \n- iCalUID \n- orderBy \n- privateExtendedProperty \n- q \n- sharedExtendedProperty \n- timeMin \n- timeMax \n- updatedMin If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    time_max: str | None = Field(default=None, description="Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.")
    time_min: str | None = Field(default=None, description="Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.")
    time_zone: str | None = Field(default=None, description='Time zone used in the response. Optional. The default is the time zone of the calendar.')
    updated_min: str | None = Field(default=None, description="Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.")
    model_config = ConfigDict(extra='forbid')

class CalendarEventsListToolOutput(Events):
    """Output for tool `calendar_events_list`."""
    pass

class CalendarEventsMoveToolInput(BaseModel):
    """Input for tool `calendar_events_move`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier of the source calendar where the event currently is on.')
    event_id: str = Field(..., description='Event identifier.')
    destination: str = Field(..., description='Calendar identifier of the target calendar where the event is to be moved to.')
    send_notifications: bool | None = Field(default=None, description="Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the change of the event's organizer. Note that some emails might still be sent even if you set the value to false. The default is false.")
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description="Guests who should receive notifications about the change of the event's organizer.")
    model_config = ConfigDict(extra='forbid')

class CalendarEventsMoveToolOutput(Event):
    """Output for tool `calendar_events_move`."""
    pass

class CalendarEventsPatchToolInput(BaseModel):
    """Input for tool `calendar_events_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    event_id: str = Field(..., description='Event identifier.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    conference_data_version: int | None = Field(default=None, description="Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.")
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    send_notifications: bool | None = Field(default=None, description='Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.')
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description='Guests who should receive notifications about the event update (for example, title changes, etc.).')
    supports_attachments: bool | None = Field(default=None, description='Whether API client performing operation supports event attachments. Optional. The default is False.')
    body: Event | None = Field(default=None, description='Request body for `calendar_events_patch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsPatchToolOutput(Event):
    """Output for tool `calendar_events_patch`."""
    pass

class CalendarEventsQuickAddToolInput(BaseModel):
    """Input for tool `calendar_events_quick_add`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    text: str = Field(..., description='The text describing the event to be created.')
    send_notifications: bool | None = Field(default=None, description='Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the creation of the event. Note that some emails might still be sent even if you set the value to false. The default is false.')
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description='Guests who should receive notifications about the creation of the new event.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsQuickAddToolOutput(Event):
    """Output for tool `calendar_events_quick_add`."""
    pass

class CalendarEventsUpdateToolInput(BaseModel):
    """Input for tool `calendar_events_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    event_id: str = Field(..., description='Event identifier.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    conference_data_version: int | None = Field(default=None, description="Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.")
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    send_notifications: bool | None = Field(default=None, description='Deprecated. Please use sendUpdates instead.\n\nWhether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.')
    send_updates: Literal['all', 'externalOnly', 'none'] | None = Field(default=None, description='Guests who should receive notifications about the event update (for example, title changes, etc.).')
    supports_attachments: bool | None = Field(default=None, description='Whether API client performing operation supports event attachments. Optional. The default is False.')
    body: Event | None = Field(default=None, description='Request body for `calendar_events_update`.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsUpdateToolOutput(Event):
    """Output for tool `calendar_events_update`."""
    pass

class CalendarEventsWatchToolInput(BaseModel):
    """Input for tool `calendar_events_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    calendar_id: str = Field(..., description='Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.')
    always_include_email: bool | None = Field(default=None, description='Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).')
    event_types: list[str] | None = Field(default=None, description='Event types to return. Optional. Possible values are: \n- "default" \n- "focusTime" \n- "outOfOffice"This parameter can be repeated multiple times to return events of different types. Currently, this is the only allowed value for this field: \n- ["default", "focusTime", "outOfOffice"] This value will be the default.\n\nIf you\'re enrolled in the Working Location developer preview program, in addition to the default value above you can also set the "workingLocation" event type: \n- ["default", "focusTime", "outOfOffice", "workingLocation"] \n- ["workingLocation"] Additional combinations of these 4 event types will be made available in later releases. Developer Preview.')
    i_cal_uid: str | None = Field(default=None, description='Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.')
    max_attendees: int | None = Field(default=None, description='The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.')
    max_results: int | None = Field(default=None, description='Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.')
    order_by: Literal['startTime', 'updated'] | None = Field(default=None, description='The order of the events returned in the result. Optional. The default is an unspecified, stable order.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    private_extended_property: list[str] | None = Field(default=None, description='Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.')
    q: str | None = Field(default=None, description="Free text search terms to find events that match these terms in the following fields: summary, description, location, attendee's displayName, attendee's email. Optional.")
    shared_extended_property: list[str] | None = Field(default=None, description='Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.')
    show_deleted: bool | None = Field(default=None, description='Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.')
    show_hidden_invitations: bool | None = Field(default=None, description='Whether to include hidden invitations in the result. Optional. The default is False.')
    single_events: bool | None = Field(default=None, description='Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.\nThere are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.\n\nThese are: \n- iCalUID \n- orderBy \n- privateExtendedProperty \n- q \n- sharedExtendedProperty \n- timeMin \n- timeMax \n- updatedMin If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    time_max: str | None = Field(default=None, description="Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.")
    time_min: str | None = Field(default=None, description="Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.")
    time_zone: str | None = Field(default=None, description='Time zone used in the response. Optional. The default is the time zone of the calendar.')
    updated_min: str | None = Field(default=None, description="Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.")
    body: Channel | None = Field(default=None, description='Request body for `calendar_events_watch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarEventsWatchToolOutput(Channel):
    """Output for tool `calendar_events_watch`."""
    pass

class CalendarFreebusyQueryToolInput(BaseModel):
    """Input for tool `calendar_freebusy_query`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: FreeBusyRequest | None = Field(default=None, description='Request body for `calendar_freebusy_query`.')
    model_config = ConfigDict(extra='forbid')

class CalendarFreebusyQueryToolOutput(FreeBusyResponse):
    """Output for tool `calendar_freebusy_query`."""
    pass

class CalendarSettingsGetToolInput(BaseModel):
    """Input for tool `calendar_settings_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    setting: str = Field(..., description='The id of the user setting.')
    model_config = ConfigDict(extra='forbid')

class CalendarSettingsGetToolOutput(Setting):
    """Output for tool `calendar_settings_get`."""
    pass

class CalendarSettingsListToolInput(BaseModel):
    """Input for tool `calendar_settings_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    model_config = ConfigDict(extra='forbid')

class CalendarSettingsListToolOutput(Settings):
    """Output for tool `calendar_settings_list`."""
    pass

class CalendarSettingsWatchToolInput(BaseModel):
    """Input for tool `calendar_settings_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    max_results: int | None = Field(default=None, description='Maximum number of entries returned on one result page. By default the value is 100 entries. The page size can never be larger than 250 entries. Optional.')
    page_token: str | None = Field(default=None, description='Token specifying which result page to return. Optional.')
    sync_token: str | None = Field(default=None, description='Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then.\nIf the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.\nLearn more about incremental synchronization.\nOptional. The default is to return all entries.')
    body: Channel | None = Field(default=None, description='Request body for `calendar_settings_watch`.')
    model_config = ConfigDict(extra='forbid')

class CalendarSettingsWatchToolOutput(Channel):
    """Output for tool `calendar_settings_watch`."""
    pass

INPUT_MODELS = {
    'calendar_acl_delete': CalendarAclDeleteToolInput,
    'calendar_acl_get': CalendarAclGetToolInput,
    'calendar_acl_insert': CalendarAclInsertToolInput,
    'calendar_acl_list': CalendarAclListToolInput,
    'calendar_acl_patch': CalendarAclPatchToolInput,
    'calendar_acl_update': CalendarAclUpdateToolInput,
    'calendar_acl_watch': CalendarAclWatchToolInput,
    'calendar_calendar_list_delete': CalendarCalendarListDeleteToolInput,
    'calendar_calendar_list_get': CalendarCalendarListGetToolInput,
    'calendar_calendar_list_insert': CalendarCalendarListInsertToolInput,
    'calendar_calendar_list_list': CalendarCalendarListListToolInput,
    'calendar_calendar_list_patch': CalendarCalendarListPatchToolInput,
    'calendar_calendar_list_update': CalendarCalendarListUpdateToolInput,
    'calendar_calendar_list_watch': CalendarCalendarListWatchToolInput,
    'calendar_calendars_clear': CalendarCalendarsClearToolInput,
    'calendar_calendars_delete': CalendarCalendarsDeleteToolInput,
    'calendar_calendars_get': CalendarCalendarsGetToolInput,
    'calendar_calendars_insert': CalendarCalendarsInsertToolInput,
    'calendar_calendars_patch': CalendarCalendarsPatchToolInput,
    'calendar_calendars_update': CalendarCalendarsUpdateToolInput,
    'calendar_channels_stop': CalendarChannelsStopToolInput,
    'calendar_colors_get': CalendarColorsGetToolInput,
    'calendar_events_delete': CalendarEventsDeleteToolInput,
    'calendar_events_get': CalendarEventsGetToolInput,
    'calendar_events_import': CalendarEventsImportToolInput,
    'calendar_events_insert': CalendarEventsInsertToolInput,
    'calendar_events_instances': CalendarEventsInstancesToolInput,
    'calendar_events_list': CalendarEventsListToolInput,
    'calendar_events_move': CalendarEventsMoveToolInput,
    'calendar_events_patch': CalendarEventsPatchToolInput,
    'calendar_events_quick_add': CalendarEventsQuickAddToolInput,
    'calendar_events_update': CalendarEventsUpdateToolInput,
    'calendar_events_watch': CalendarEventsWatchToolInput,
    'calendar_freebusy_query': CalendarFreebusyQueryToolInput,
    'calendar_settings_get': CalendarSettingsGetToolInput,
    'calendar_settings_list': CalendarSettingsListToolInput,
    'calendar_settings_watch': CalendarSettingsWatchToolInput,
}

OUTPUT_MODELS = {
    'calendar_acl_delete': CalendarAclDeleteToolOutput,
    'calendar_acl_get': CalendarAclGetToolOutput,
    'calendar_acl_insert': CalendarAclInsertToolOutput,
    'calendar_acl_list': CalendarAclListToolOutput,
    'calendar_acl_patch': CalendarAclPatchToolOutput,
    'calendar_acl_update': CalendarAclUpdateToolOutput,
    'calendar_acl_watch': CalendarAclWatchToolOutput,
    'calendar_calendar_list_delete': CalendarCalendarListDeleteToolOutput,
    'calendar_calendar_list_get': CalendarCalendarListGetToolOutput,
    'calendar_calendar_list_insert': CalendarCalendarListInsertToolOutput,
    'calendar_calendar_list_list': CalendarCalendarListListToolOutput,
    'calendar_calendar_list_patch': CalendarCalendarListPatchToolOutput,
    'calendar_calendar_list_update': CalendarCalendarListUpdateToolOutput,
    'calendar_calendar_list_watch': CalendarCalendarListWatchToolOutput,
    'calendar_calendars_clear': CalendarCalendarsClearToolOutput,
    'calendar_calendars_delete': CalendarCalendarsDeleteToolOutput,
    'calendar_calendars_get': CalendarCalendarsGetToolOutput,
    'calendar_calendars_insert': CalendarCalendarsInsertToolOutput,
    'calendar_calendars_patch': CalendarCalendarsPatchToolOutput,
    'calendar_calendars_update': CalendarCalendarsUpdateToolOutput,
    'calendar_channels_stop': CalendarChannelsStopToolOutput,
    'calendar_colors_get': CalendarColorsGetToolOutput,
    'calendar_events_delete': CalendarEventsDeleteToolOutput,
    'calendar_events_get': CalendarEventsGetToolOutput,
    'calendar_events_import': CalendarEventsImportToolOutput,
    'calendar_events_insert': CalendarEventsInsertToolOutput,
    'calendar_events_instances': CalendarEventsInstancesToolOutput,
    'calendar_events_list': CalendarEventsListToolOutput,
    'calendar_events_move': CalendarEventsMoveToolOutput,
    'calendar_events_patch': CalendarEventsPatchToolOutput,
    'calendar_events_quick_add': CalendarEventsQuickAddToolOutput,
    'calendar_events_update': CalendarEventsUpdateToolOutput,
    'calendar_events_watch': CalendarEventsWatchToolOutput,
    'calendar_freebusy_query': CalendarFreebusyQueryToolOutput,
    'calendar_settings_get': CalendarSettingsGetToolOutput,
    'calendar_settings_list': CalendarSettingsListToolOutput,
    'calendar_settings_watch': CalendarSettingsWatchToolOutput,
}
