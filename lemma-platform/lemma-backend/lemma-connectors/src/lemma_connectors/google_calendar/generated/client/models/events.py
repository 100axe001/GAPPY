from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.event import Event
  from ..models.event_reminder import EventReminder





T = TypeVar("T", bound="Events")



@_attrs_define
class Events:
    """ 
        Attributes:
            access_role (str | Unset): The user's access role for this calendar. Read-only. Possible values are:
                - "none" - The user has no access.
                - "freeBusyReader" - The user has read access to free/busy information.
                - "reader" - The user has read access to the calendar. Private events will appear to users with reader access,
                but event details will be hidden.
                - "writer" - The user has read and write access to the calendar. Private events will appear to users with writer
                access, and event details will be visible.
                - "owner" - The user has ownership of the calendar. This role has all of the permissions of the writer role with
                the additional ability to see and manipulate ACLs.
            default_reminders (list[EventReminder] | Unset): The default reminders on the calendar for the authenticated
                user. These reminders apply to all events on this calendar that do not explicitly override them (i.e. do not
                have reminders.useDefault set to True).
            description (str | Unset): Description of the calendar. Read-only.
            etag (str | Unset): ETag of the collection.
            items (list[Event] | Unset): List of events on the calendar.
            kind (str | Unset): Type of the collection ("calendar#events"). Default: 'calendar#events'.
            next_page_token (str | Unset): Token used to access the next page of this result. Omitted if no further results
                are available, in which case nextSyncToken is provided.
            next_sync_token (str | Unset): Token used at a later point in time to retrieve only the entries that have
                changed since this result was returned. Omitted if further results are available, in which case nextPageToken is
                provided.
            summary (str | Unset): Title of the calendar. Read-only.
            time_zone (str | Unset): The time zone of the calendar. Read-only.
            updated (datetime.datetime | Unset): Last modification time of the calendar (as a RFC3339 timestamp). Read-only.
     """

    access_role: str | Unset = UNSET
    default_reminders: list[EventReminder] | Unset = UNSET
    description: str | Unset = UNSET
    etag: str | Unset = UNSET
    items: list[Event] | Unset = UNSET
    kind: str | Unset = 'calendar#events'
    next_page_token: str | Unset = UNSET
    next_sync_token: str | Unset = UNSET
    summary: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event import Event
        from ..models.event_reminder import EventReminder
        access_role = self.access_role

        default_reminders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_reminders, Unset):
            default_reminders = []
            for default_reminders_item_data in self.default_reminders:
                default_reminders_item = default_reminders_item_data.to_dict()
                default_reminders.append(default_reminders_item)



        description = self.description

        etag = self.etag

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        kind = self.kind

        next_page_token = self.next_page_token

        next_sync_token = self.next_sync_token

        summary = self.summary

        time_zone = self.time_zone

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_role is not UNSET:
            field_dict["accessRole"] = access_role
        if default_reminders is not UNSET:
            field_dict["defaultReminders"] = default_reminders
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if items is not UNSET:
            field_dict["items"] = items
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if next_sync_token is not UNSET:
            field_dict["nextSyncToken"] = next_sync_token
        if summary is not UNSET:
            field_dict["summary"] = summary
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event import Event
        from ..models.event_reminder import EventReminder
        d = dict(src_dict)
        access_role = d.pop("accessRole", UNSET)

        _default_reminders = d.pop("defaultReminders", UNSET)
        default_reminders: list[EventReminder] | Unset = UNSET
        if _default_reminders is not UNSET:
            default_reminders = []
            for default_reminders_item_data in _default_reminders:
                default_reminders_item = EventReminder.from_dict(default_reminders_item_data)



                default_reminders.append(default_reminders_item)


        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        _items = d.pop("items", UNSET)
        items: list[Event] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = Event.from_dict(items_item_data)



                items.append(items_item)


        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        next_sync_token = d.pop("nextSyncToken", UNSET)

        summary = d.pop("summary", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        events = cls(
            access_role=access_role,
            default_reminders=default_reminders,
            description=description,
            etag=etag,
            items=items,
            kind=kind,
            next_page_token=next_page_token,
            next_sync_token=next_sync_token,
            summary=summary,
            time_zone=time_zone,
            updated=updated,
        )


        events.additional_properties = d
        return events

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
