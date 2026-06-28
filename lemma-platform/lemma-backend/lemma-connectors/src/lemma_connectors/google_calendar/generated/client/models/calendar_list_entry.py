from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.calendar_list_entry_notification_settings import CalendarListEntryNotificationSettings
  from ..models.conference_properties import ConferenceProperties
  from ..models.event_reminder import EventReminder





T = TypeVar("T", bound="CalendarListEntry")



@_attrs_define
class CalendarListEntry:
    """ 
        Attributes:
            access_role (str | Unset): The effective access role that the authenticated user has on the calendar. Read-only.
                Possible values are:
                - "freeBusyReader" - Provides read access to free/busy information.
                - "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but
                event details will be hidden.
                - "writer" - Provides read and write access to the calendar. Private events will appear to users with writer
                access, and event details will be visible.
                - "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the
                additional ability to see and manipulate ACLs.
            background_color (str | Unset): The main color of the calendar in the hexadecimal format "#0088aa". This
                property supersedes the index-based colorId property. To set or change this property, you need to specify
                colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.
            color_id (str | Unset): The color of the calendar. This is an ID referring to an entry in the calendar section
                of the colors definition (see the colors endpoint). This property is superseded by the backgroundColor and
                foregroundColor properties and can be ignored when using these properties. Optional.
            conference_properties (ConferenceProperties | Unset):
            default_reminders (list[EventReminder] | Unset): The default reminders that the authenticated user has for this
                calendar.
            deleted (bool | Unset): Whether this calendar list entry has been deleted from the calendar list. Read-only.
                Optional. The default is False. Default: False.
            description (str | Unset): Description of the calendar. Optional. Read-only.
            etag (str | Unset): ETag of the resource.
            foreground_color (str | Unset): The foreground color of the calendar in the hexadecimal format "#ffffff". This
                property supersedes the index-based colorId property. To set or change this property, you need to specify
                colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.
            hidden (bool | Unset): Whether the calendar has been hidden from the list. Optional. The attribute is only
                returned when the calendar is hidden, in which case the value is true. Default: False.
            id (str | Unset): Identifier of the calendar.
            kind (str | Unset): Type of the resource ("calendar#calendarListEntry"). Default: 'calendar#calendarListEntry'.
            location (str | Unset): Geographic location of the calendar as free-form text. Optional. Read-only.
            notification_settings (CalendarListEntryNotificationSettings | Unset): The notifications that the authenticated
                user is receiving for this calendar.
            primary (bool | Unset): Whether the calendar is the primary calendar of the authenticated user. Read-only.
                Optional. The default is False. Default: False.
            selected (bool | Unset): Whether the calendar content shows up in the calendar UI. Optional. The default is
                False. Default: False.
            summary (str | Unset): Title of the calendar. Read-only.
            summary_override (str | Unset): The summary that the authenticated user has set for this calendar. Optional.
            time_zone (str | Unset): The time zone of the calendar. Optional. Read-only.
     """

    access_role: str | Unset = UNSET
    background_color: str | Unset = UNSET
    color_id: str | Unset = UNSET
    conference_properties: ConferenceProperties | Unset = UNSET
    default_reminders: list[EventReminder] | Unset = UNSET
    deleted: bool | Unset = False
    description: str | Unset = UNSET
    etag: str | Unset = UNSET
    foreground_color: str | Unset = UNSET
    hidden: bool | Unset = False
    id: str | Unset = UNSET
    kind: str | Unset = 'calendar#calendarListEntry'
    location: str | Unset = UNSET
    notification_settings: CalendarListEntryNotificationSettings | Unset = UNSET
    primary: bool | Unset = False
    selected: bool | Unset = False
    summary: str | Unset = UNSET
    summary_override: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_list_entry_notification_settings import CalendarListEntryNotificationSettings
        from ..models.conference_properties import ConferenceProperties
        from ..models.event_reminder import EventReminder
        access_role = self.access_role

        background_color = self.background_color

        color_id = self.color_id

        conference_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_properties, Unset):
            conference_properties = self.conference_properties.to_dict()

        default_reminders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_reminders, Unset):
            default_reminders = []
            for default_reminders_item_data in self.default_reminders:
                default_reminders_item = default_reminders_item_data.to_dict()
                default_reminders.append(default_reminders_item)



        deleted = self.deleted

        description = self.description

        etag = self.etag

        foreground_color = self.foreground_color

        hidden = self.hidden

        id = self.id

        kind = self.kind

        location = self.location

        notification_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        primary = self.primary

        selected = self.selected

        summary = self.summary

        summary_override = self.summary_override

        time_zone = self.time_zone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_role is not UNSET:
            field_dict["accessRole"] = access_role
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if color_id is not UNSET:
            field_dict["colorId"] = color_id
        if conference_properties is not UNSET:
            field_dict["conferenceProperties"] = conference_properties
        if default_reminders is not UNSET:
            field_dict["defaultReminders"] = default_reminders
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if location is not UNSET:
            field_dict["location"] = location
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if primary is not UNSET:
            field_dict["primary"] = primary
        if selected is not UNSET:
            field_dict["selected"] = selected
        if summary is not UNSET:
            field_dict["summary"] = summary
        if summary_override is not UNSET:
            field_dict["summaryOverride"] = summary_override
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_list_entry_notification_settings import CalendarListEntryNotificationSettings
        from ..models.conference_properties import ConferenceProperties
        from ..models.event_reminder import EventReminder
        d = dict(src_dict)
        access_role = d.pop("accessRole", UNSET)

        background_color = d.pop("backgroundColor", UNSET)

        color_id = d.pop("colorId", UNSET)

        _conference_properties = d.pop("conferenceProperties", UNSET)
        conference_properties: ConferenceProperties | Unset
        if isinstance(_conference_properties,  Unset):
            conference_properties = UNSET
        else:
            conference_properties = ConferenceProperties.from_dict(_conference_properties)




        _default_reminders = d.pop("defaultReminders", UNSET)
        default_reminders: list[EventReminder] | Unset = UNSET
        if _default_reminders is not UNSET:
            default_reminders = []
            for default_reminders_item_data in _default_reminders:
                default_reminders_item = EventReminder.from_dict(default_reminders_item_data)



                default_reminders.append(default_reminders_item)


        deleted = d.pop("deleted", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        foreground_color = d.pop("foregroundColor", UNSET)

        hidden = d.pop("hidden", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        location = d.pop("location", UNSET)

        _notification_settings = d.pop("notificationSettings", UNSET)
        notification_settings: CalendarListEntryNotificationSettings | Unset
        if isinstance(_notification_settings,  Unset):
            notification_settings = UNSET
        else:
            notification_settings = CalendarListEntryNotificationSettings.from_dict(_notification_settings)




        primary = d.pop("primary", UNSET)

        selected = d.pop("selected", UNSET)

        summary = d.pop("summary", UNSET)

        summary_override = d.pop("summaryOverride", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        calendar_list_entry = cls(
            access_role=access_role,
            background_color=background_color,
            color_id=color_id,
            conference_properties=conference_properties,
            default_reminders=default_reminders,
            deleted=deleted,
            description=description,
            etag=etag,
            foreground_color=foreground_color,
            hidden=hidden,
            id=id,
            kind=kind,
            location=location,
            notification_settings=notification_settings,
            primary=primary,
            selected=selected,
            summary=summary,
            summary_override=summary_override,
            time_zone=time_zone,
        )


        calendar_list_entry.additional_properties = d
        return calendar_list_entry

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
