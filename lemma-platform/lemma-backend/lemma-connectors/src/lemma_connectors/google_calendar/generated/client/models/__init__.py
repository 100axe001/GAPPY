""" Contains all the data models used in inputs/outputs """

from .acl import Acl
from .acl_rule import AclRule
from .acl_rule_scope import AclRuleScope
from .calendar import Calendar
from .calendar_acl_delete_alt import CalendarAclDeleteAlt
from .calendar_acl_get_alt import CalendarAclGetAlt
from .calendar_acl_insert_alt import CalendarAclInsertAlt
from .calendar_acl_list_alt import CalendarAclListAlt
from .calendar_acl_patch_alt import CalendarAclPatchAlt
from .calendar_acl_update_alt import CalendarAclUpdateAlt
from .calendar_acl_watch_alt import CalendarAclWatchAlt
from .calendar_calendar_list_delete_alt import CalendarCalendarListDeleteAlt
from .calendar_calendar_list_get_alt import CalendarCalendarListGetAlt
from .calendar_calendar_list_insert_alt import CalendarCalendarListInsertAlt
from .calendar_calendar_list_list_alt import CalendarCalendarListListAlt
from .calendar_calendar_list_list_min_access_role import CalendarCalendarListListMinAccessRole
from .calendar_calendar_list_patch_alt import CalendarCalendarListPatchAlt
from .calendar_calendar_list_update_alt import CalendarCalendarListUpdateAlt
from .calendar_calendar_list_watch_alt import CalendarCalendarListWatchAlt
from .calendar_calendar_list_watch_min_access_role import CalendarCalendarListWatchMinAccessRole
from .calendar_calendars_clear_alt import CalendarCalendarsClearAlt
from .calendar_calendars_delete_alt import CalendarCalendarsDeleteAlt
from .calendar_calendars_get_alt import CalendarCalendarsGetAlt
from .calendar_calendars_insert_alt import CalendarCalendarsInsertAlt
from .calendar_calendars_patch_alt import CalendarCalendarsPatchAlt
from .calendar_calendars_update_alt import CalendarCalendarsUpdateAlt
from .calendar_channels_stop_alt import CalendarChannelsStopAlt
from .calendar_colors_get_alt import CalendarColorsGetAlt
from .calendar_events_delete_alt import CalendarEventsDeleteAlt
from .calendar_events_delete_send_updates import CalendarEventsDeleteSendUpdates
from .calendar_events_get_alt import CalendarEventsGetAlt
from .calendar_events_import_alt import CalendarEventsImportAlt
from .calendar_events_insert_alt import CalendarEventsInsertAlt
from .calendar_events_insert_send_updates import CalendarEventsInsertSendUpdates
from .calendar_events_instances_alt import CalendarEventsInstancesAlt
from .calendar_events_list_alt import CalendarEventsListAlt
from .calendar_events_list_order_by import CalendarEventsListOrderBy
from .calendar_events_move_alt import CalendarEventsMoveAlt
from .calendar_events_move_send_updates import CalendarEventsMoveSendUpdates
from .calendar_events_patch_alt import CalendarEventsPatchAlt
from .calendar_events_patch_send_updates import CalendarEventsPatchSendUpdates
from .calendar_events_quick_add_alt import CalendarEventsQuickAddAlt
from .calendar_events_quick_add_send_updates import CalendarEventsQuickAddSendUpdates
from .calendar_events_update_alt import CalendarEventsUpdateAlt
from .calendar_events_update_send_updates import CalendarEventsUpdateSendUpdates
from .calendar_events_watch_alt import CalendarEventsWatchAlt
from .calendar_events_watch_order_by import CalendarEventsWatchOrderBy
from .calendar_freebusy_query_alt import CalendarFreebusyQueryAlt
from .calendar_list import CalendarList
from .calendar_list_entry import CalendarListEntry
from .calendar_list_entry_notification_settings import CalendarListEntryNotificationSettings
from .calendar_notification import CalendarNotification
from .calendar_settings_get_alt import CalendarSettingsGetAlt
from .calendar_settings_list_alt import CalendarSettingsListAlt
from .calendar_settings_watch_alt import CalendarSettingsWatchAlt
from .channel import Channel
from .channel_params import ChannelParams
from .color_definition import ColorDefinition
from .colors import Colors
from .colors_calendar import ColorsCalendar
from .colors_event import ColorsEvent
from .conference_data import ConferenceData
from .conference_parameters import ConferenceParameters
from .conference_parameters_add_on_parameters import ConferenceParametersAddOnParameters
from .conference_parameters_add_on_parameters_parameters import ConferenceParametersAddOnParametersParameters
from .conference_properties import ConferenceProperties
from .conference_request_status import ConferenceRequestStatus
from .conference_solution import ConferenceSolution
from .conference_solution_key import ConferenceSolutionKey
from .create_conference_request import CreateConferenceRequest
from .entry_point import EntryPoint
from .error import Error
from .event import Event
from .event_attachment import EventAttachment
from .event_attendee import EventAttendee
from .event_creator import EventCreator
from .event_date_time import EventDateTime
from .event_extended_properties import EventExtendedProperties
from .event_extended_properties_private import EventExtendedPropertiesPrivate
from .event_extended_properties_shared import EventExtendedPropertiesShared
from .event_gadget import EventGadget
from .event_gadget_preferences import EventGadgetPreferences
from .event_organizer import EventOrganizer
from .event_reminder import EventReminder
from .event_reminders import EventReminders
from .event_source import EventSource
from .event_working_location_properties import EventWorkingLocationProperties
from .event_working_location_properties_custom_location import EventWorkingLocationPropertiesCustomLocation
from .event_working_location_properties_office_location import EventWorkingLocationPropertiesOfficeLocation
from .events import Events
from .free_busy_calendar import FreeBusyCalendar
from .free_busy_group import FreeBusyGroup
from .free_busy_request import FreeBusyRequest
from .free_busy_request_item import FreeBusyRequestItem
from .free_busy_response import FreeBusyResponse
from .free_busy_response_calendars import FreeBusyResponseCalendars
from .free_busy_response_groups import FreeBusyResponseGroups
from .setting import Setting
from .settings import Settings
from .time_period import TimePeriod

__all__ = (
    "Acl",
    "AclRule",
    "AclRuleScope",
    "Calendar",
    "CalendarAclDeleteAlt",
    "CalendarAclGetAlt",
    "CalendarAclInsertAlt",
    "CalendarAclListAlt",
    "CalendarAclPatchAlt",
    "CalendarAclUpdateAlt",
    "CalendarAclWatchAlt",
    "CalendarCalendarListDeleteAlt",
    "CalendarCalendarListGetAlt",
    "CalendarCalendarListInsertAlt",
    "CalendarCalendarListListAlt",
    "CalendarCalendarListListMinAccessRole",
    "CalendarCalendarListPatchAlt",
    "CalendarCalendarListUpdateAlt",
    "CalendarCalendarListWatchAlt",
    "CalendarCalendarListWatchMinAccessRole",
    "CalendarCalendarsClearAlt",
    "CalendarCalendarsDeleteAlt",
    "CalendarCalendarsGetAlt",
    "CalendarCalendarsInsertAlt",
    "CalendarCalendarsPatchAlt",
    "CalendarCalendarsUpdateAlt",
    "CalendarChannelsStopAlt",
    "CalendarColorsGetAlt",
    "CalendarEventsDeleteAlt",
    "CalendarEventsDeleteSendUpdates",
    "CalendarEventsGetAlt",
    "CalendarEventsImportAlt",
    "CalendarEventsInsertAlt",
    "CalendarEventsInsertSendUpdates",
    "CalendarEventsInstancesAlt",
    "CalendarEventsListAlt",
    "CalendarEventsListOrderBy",
    "CalendarEventsMoveAlt",
    "CalendarEventsMoveSendUpdates",
    "CalendarEventsPatchAlt",
    "CalendarEventsPatchSendUpdates",
    "CalendarEventsQuickAddAlt",
    "CalendarEventsQuickAddSendUpdates",
    "CalendarEventsUpdateAlt",
    "CalendarEventsUpdateSendUpdates",
    "CalendarEventsWatchAlt",
    "CalendarEventsWatchOrderBy",
    "CalendarFreebusyQueryAlt",
    "CalendarList",
    "CalendarListEntry",
    "CalendarListEntryNotificationSettings",
    "CalendarNotification",
    "CalendarSettingsGetAlt",
    "CalendarSettingsListAlt",
    "CalendarSettingsWatchAlt",
    "Channel",
    "ChannelParams",
    "ColorDefinition",
    "Colors",
    "ColorsCalendar",
    "ColorsEvent",
    "ConferenceData",
    "ConferenceParameters",
    "ConferenceParametersAddOnParameters",
    "ConferenceParametersAddOnParametersParameters",
    "ConferenceProperties",
    "ConferenceRequestStatus",
    "ConferenceSolution",
    "ConferenceSolutionKey",
    "CreateConferenceRequest",
    "EntryPoint",
    "Error",
    "Event",
    "EventAttachment",
    "EventAttendee",
    "EventCreator",
    "EventDateTime",
    "EventExtendedProperties",
    "EventExtendedPropertiesPrivate",
    "EventExtendedPropertiesShared",
    "EventGadget",
    "EventGadgetPreferences",
    "EventOrganizer",
    "EventReminder",
    "EventReminders",
    "Events",
    "EventSource",
    "EventWorkingLocationProperties",
    "EventWorkingLocationPropertiesCustomLocation",
    "EventWorkingLocationPropertiesOfficeLocation",
    "FreeBusyCalendar",
    "FreeBusyGroup",
    "FreeBusyRequest",
    "FreeBusyRequestItem",
    "FreeBusyResponse",
    "FreeBusyResponseCalendars",
    "FreeBusyResponseGroups",
    "Setting",
    "Settings",
    "TimePeriod",
)
