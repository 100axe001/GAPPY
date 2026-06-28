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
  from ..models.conference_data import ConferenceData
  from ..models.event_attachment import EventAttachment
  from ..models.event_attendee import EventAttendee
  from ..models.event_creator import EventCreator
  from ..models.event_date_time import EventDateTime
  from ..models.event_extended_properties import EventExtendedProperties
  from ..models.event_gadget import EventGadget
  from ..models.event_organizer import EventOrganizer
  from ..models.event_reminders import EventReminders
  from ..models.event_source import EventSource
  from ..models.event_working_location_properties import EventWorkingLocationProperties





T = TypeVar("T", bound="Event")



@_attrs_define
class Event:
    """ 
        Attributes:
            anyone_can_add_self (bool | Unset): Whether anyone can invite themselves to the event (deprecated). Optional.
                The default is False. Default: False.
            attachments (list[EventAttachment] | Unset): File attachments for the event.
                In order to modify attachments the supportsAttachments request parameter should be set to true.
                There can be at most 25 attachments per event,
            attendees (list[EventAttendee] | Unset): The attendees of the event. See the Events with attendees guide for
                more information on scheduling events with other calendar users. Service accounts need to use domain-wide
                delegation of authority to populate the attendee list.
            attendees_omitted (bool | Unset): Whether attendees may have been omitted from the event's representation. When
                retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When
                updating an event, this can be used to only update the participant's response. Optional. The default is False.
                Default: False.
            color_id (str | Unset): The color of the event. This is an ID referring to an entry in the event section of the
                colors definition (see the  colors endpoint). Optional.
            conference_data (ConferenceData | Unset):
            created (datetime.datetime | Unset): Creation time of the event (as a RFC3339 timestamp). Read-only.
            creator (EventCreator | Unset): The creator of the event. Read-only.
            description (str | Unset): Description of the event. Can contain HTML. Optional.
            end (EventDateTime | Unset):
            end_time_unspecified (bool | Unset): Whether the end time is actually unspecified. An end time is still provided
                for compatibility reasons, even if this attribute is set to True. The default is False. Default: False.
            etag (str | Unset): ETag of the resource.
            event_type (str | Unset): Specific type of the event. Read-only. Possible values are:
                - "default" - A regular event or not further specified.
                - "outOfOffice" - An out-of-office event.
                - "focusTime" - A focus-time event.
                - "workingLocation" - A working location event. Developer Preview. Default: 'default'.
            extended_properties (EventExtendedProperties | Unset): Extended properties of the event.
            gadget (EventGadget | Unset): A gadget that extends this event. Gadgets are deprecated; this structure is
                instead only used for returning birthday calendar metadata.
            guests_can_invite_others (bool | Unset): Whether attendees other than the organizer can invite others to the
                event. Optional. The default is True. Default: True.
            guests_can_modify (bool | Unset): Whether attendees other than the organizer can modify the event. Optional. The
                default is False. Default: False.
            guests_can_see_other_guests (bool | Unset): Whether attendees other than the organizer can see who the event's
                attendees are. Optional. The default is True. Default: True.
            hangout_link (str | Unset): An absolute link to the Google Hangout associated with this event. Read-only.
            html_link (str | Unset): An absolute link to this event in the Google Calendar Web UI. Read-only.
            i_cal_uid (str | Unset): Event unique identifier as defined in RFC5545. It is used to uniquely identify events
                accross calendaring systems and must be supplied when importing events via the import method.
                Note that the iCalUID and the id are not identical and only one of them should be supplied at event creation
                time. One difference in their semantics is that in recurring events, all occurrences of one event have different
                ids while they all share the same iCalUIDs. To retrieve an event using its iCalUID, call the events.list method
                using the iCalUID parameter. To retrieve an event using its id, call the events.get method.
            id (str | Unset): Opaque identifier of the event. When creating new single or recurring events, you can specify
                their IDs. Provided IDs must follow these rules:
                - characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9,
                see section 3.1.2 in RFC2938
                - the length of the ID must be between 5 and 1024 characters
                - the ID must be unique per calendar  Due to the globally distributed nature of the system, we cannot guarantee
                that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend
                using an established UUID algorithm such as one described in RFC4122.
                If you do not specify an ID, it will be automatically generated by the server.
                Note that the icalUID and the id are not identical and only one of them should be supplied at event creation
                time. One difference in their semantics is that in recurring events, all occurrences of one event have different
                ids while they all share the same icalUIDs.
            kind (str | Unset): Type of the resource ("calendar#event"). Default: 'calendar#event'.
            location (str | Unset): Geographic location of the event as free-form text. Optional.
            locked (bool | Unset): Whether this is a locked event copy where no changes can be made to the main event fields
                "summary", "description", "location", "start", "end" or "recurrence". The default is False. Read-Only. Default:
                False.
            organizer (EventOrganizer | Unset): The organizer of the event. If the organizer is also an attendee, this is
                indicated with a separate entry in attendees with the organizer field set to True. To change the organizer, use
                the move operation. Read-only, except when importing an event.
            original_start_time (EventDateTime | Unset):
            private_copy (bool | Unset): If set to True, Event propagation is disabled. Note that it is not the same thing
                as Private event properties. Optional. Immutable. The default is False. Default: False.
            recurrence (list[str] | Unset): List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event, as
                specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times
                are specified in the start and end fields. This field is omitted for single events or instances of recurring
                events.
            recurring_event_id (str | Unset): For an instance of a recurring event, this is the id of the recurring event to
                which this instance belongs. Immutable.
            reminders (EventReminders | Unset): Information about the event's reminders for the authenticated user.
            sequence (int | Unset): Sequence number as per iCalendar.
            source (EventSource | Unset): Source from which the event was created. For example, a web page, an email message
                or any document identifiable by an URL with HTTP or HTTPS scheme. Can only be seen or modified by the creator of
                the event.
            start (EventDateTime | Unset):
            status (str | Unset): Status of the event. Optional. Possible values are:
                - "confirmed" - The event is confirmed. This is the default status.
                - "tentative" - The event is tentatively confirmed.
                - "cancelled" - The event is cancelled (deleted). The list method returns cancelled events only on incremental
                sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true. The get method
                always returns them.
                A cancelled status represents two different states depending on the event type:
                - Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be
                presented to the user. Clients should store these events for the lifetime of the parent recurring event.
                Cancelled exceptions are only guaranteed to have values for the id, recurringEventId and originalStartTime
                fields populated. The other fields might be empty.
                - All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such
                cancelled events will eventually disappear, so do not rely on them being available indefinitely.
                Deleted events are only guaranteed to have the id field populated.   On the organizer's calendar, cancelled
                events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted).
                Similarly, the events to which the user was invited and that they manually removed continue to provide details.
                However, incremental sync requests with showDeleted set to false will not return these details.
                If an event changes its organizer (for example via the move operation) and the original organizer is not on the
                attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated.
            summary (str | Unset): Title of the event.
            transparency (str | Unset): Whether the event blocks time on the calendar. Optional. Possible values are:
                - "opaque" - Default value. The event does block time on the calendar. This is equivalent to setting Show me as
                to Busy in the Calendar UI.
                - "transparent" - The event does not block time on the calendar. This is equivalent to setting Show me as to
                Available in the Calendar UI. Default: 'opaque'.
            updated (datetime.datetime | Unset): Last modification time of the event (as a RFC3339 timestamp). Read-only.
            visibility (str | Unset): Visibility of the event. Optional. Possible values are:
                - "default" - Uses the default visibility for events on the calendar. This is the default value.
                - "public" - The event is public and event details are visible to all readers of the calendar.
                - "private" - The event is private and only event attendees may view event details.
                - "confidential" - The event is private. This value is provided for compatibility reasons. Default: 'default'.
            working_location_properties (EventWorkingLocationProperties | Unset):
     """

    anyone_can_add_self: bool | Unset = False
    attachments: list[EventAttachment] | Unset = UNSET
    attendees: list[EventAttendee] | Unset = UNSET
    attendees_omitted: bool | Unset = False
    color_id: str | Unset = UNSET
    conference_data: ConferenceData | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    creator: EventCreator | Unset = UNSET
    description: str | Unset = UNSET
    end: EventDateTime | Unset = UNSET
    end_time_unspecified: bool | Unset = False
    etag: str | Unset = UNSET
    event_type: str | Unset = 'default'
    extended_properties: EventExtendedProperties | Unset = UNSET
    gadget: EventGadget | Unset = UNSET
    guests_can_invite_others: bool | Unset = True
    guests_can_modify: bool | Unset = False
    guests_can_see_other_guests: bool | Unset = True
    hangout_link: str | Unset = UNSET
    html_link: str | Unset = UNSET
    i_cal_uid: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = 'calendar#event'
    location: str | Unset = UNSET
    locked: bool | Unset = False
    organizer: EventOrganizer | Unset = UNSET
    original_start_time: EventDateTime | Unset = UNSET
    private_copy: bool | Unset = False
    recurrence: list[str] | Unset = UNSET
    recurring_event_id: str | Unset = UNSET
    reminders: EventReminders | Unset = UNSET
    sequence: int | Unset = UNSET
    source: EventSource | Unset = UNSET
    start: EventDateTime | Unset = UNSET
    status: str | Unset = UNSET
    summary: str | Unset = UNSET
    transparency: str | Unset = 'opaque'
    updated: datetime.datetime | Unset = UNSET
    visibility: str | Unset = 'default'
    working_location_properties: EventWorkingLocationProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_data import ConferenceData
        from ..models.event_attachment import EventAttachment
        from ..models.event_attendee import EventAttendee
        from ..models.event_creator import EventCreator
        from ..models.event_date_time import EventDateTime
        from ..models.event_extended_properties import EventExtendedProperties
        from ..models.event_gadget import EventGadget
        from ..models.event_organizer import EventOrganizer
        from ..models.event_reminders import EventReminders
        from ..models.event_source import EventSource
        from ..models.event_working_location_properties import EventWorkingLocationProperties
        anyone_can_add_self = self.anyone_can_add_self

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        attendees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)



        attendees_omitted = self.attendees_omitted

        color_id = self.color_id

        conference_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_data, Unset):
            conference_data = self.conference_data.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        description = self.description

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        end_time_unspecified = self.end_time_unspecified

        etag = self.etag

        event_type = self.event_type

        extended_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extended_properties, Unset):
            extended_properties = self.extended_properties.to_dict()

        gadget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gadget, Unset):
            gadget = self.gadget.to_dict()

        guests_can_invite_others = self.guests_can_invite_others

        guests_can_modify = self.guests_can_modify

        guests_can_see_other_guests = self.guests_can_see_other_guests

        hangout_link = self.hangout_link

        html_link = self.html_link

        i_cal_uid = self.i_cal_uid

        id = self.id

        kind = self.kind

        location = self.location

        locked = self.locked

        organizer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organizer, Unset):
            organizer = self.organizer.to_dict()

        original_start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_start_time, Unset):
            original_start_time = self.original_start_time.to_dict()

        private_copy = self.private_copy

        recurrence: list[str] | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence



        recurring_event_id = self.recurring_event_id

        reminders: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = self.reminders.to_dict()

        sequence = self.sequence

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        status = self.status

        summary = self.summary

        transparency = self.transparency

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        visibility = self.visibility

        working_location_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.working_location_properties, Unset):
            working_location_properties = self.working_location_properties.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if anyone_can_add_self is not UNSET:
            field_dict["anyoneCanAddSelf"] = anyone_can_add_self
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if attendees_omitted is not UNSET:
            field_dict["attendeesOmitted"] = attendees_omitted
        if color_id is not UNSET:
            field_dict["colorId"] = color_id
        if conference_data is not UNSET:
            field_dict["conferenceData"] = conference_data
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if end is not UNSET:
            field_dict["end"] = end
        if end_time_unspecified is not UNSET:
            field_dict["endTimeUnspecified"] = end_time_unspecified
        if etag is not UNSET:
            field_dict["etag"] = etag
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if extended_properties is not UNSET:
            field_dict["extendedProperties"] = extended_properties
        if gadget is not UNSET:
            field_dict["gadget"] = gadget
        if guests_can_invite_others is not UNSET:
            field_dict["guestsCanInviteOthers"] = guests_can_invite_others
        if guests_can_modify is not UNSET:
            field_dict["guestsCanModify"] = guests_can_modify
        if guests_can_see_other_guests is not UNSET:
            field_dict["guestsCanSeeOtherGuests"] = guests_can_see_other_guests
        if hangout_link is not UNSET:
            field_dict["hangoutLink"] = hangout_link
        if html_link is not UNSET:
            field_dict["htmlLink"] = html_link
        if i_cal_uid is not UNSET:
            field_dict["iCalUID"] = i_cal_uid
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if location is not UNSET:
            field_dict["location"] = location
        if locked is not UNSET:
            field_dict["locked"] = locked
        if organizer is not UNSET:
            field_dict["organizer"] = organizer
        if original_start_time is not UNSET:
            field_dict["originalStartTime"] = original_start_time
        if private_copy is not UNSET:
            field_dict["privateCopy"] = private_copy
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if recurring_event_id is not UNSET:
            field_dict["recurringEventId"] = recurring_event_id
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if source is not UNSET:
            field_dict["source"] = source
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if transparency is not UNSET:
            field_dict["transparency"] = transparency
        if updated is not UNSET:
            field_dict["updated"] = updated
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if working_location_properties is not UNSET:
            field_dict["workingLocationProperties"] = working_location_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_data import ConferenceData
        from ..models.event_attachment import EventAttachment
        from ..models.event_attendee import EventAttendee
        from ..models.event_creator import EventCreator
        from ..models.event_date_time import EventDateTime
        from ..models.event_extended_properties import EventExtendedProperties
        from ..models.event_gadget import EventGadget
        from ..models.event_organizer import EventOrganizer
        from ..models.event_reminders import EventReminders
        from ..models.event_source import EventSource
        from ..models.event_working_location_properties import EventWorkingLocationProperties
        d = dict(src_dict)
        anyone_can_add_self = d.pop("anyoneCanAddSelf", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[EventAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = EventAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        _attendees = d.pop("attendees", UNSET)
        attendees: list[EventAttendee] | Unset = UNSET
        if _attendees is not UNSET:
            attendees = []
            for attendees_item_data in _attendees:
                attendees_item = EventAttendee.from_dict(attendees_item_data)



                attendees.append(attendees_item)


        attendees_omitted = d.pop("attendeesOmitted", UNSET)

        color_id = d.pop("colorId", UNSET)

        _conference_data = d.pop("conferenceData", UNSET)
        conference_data: ConferenceData | Unset
        if isinstance(_conference_data,  Unset):
            conference_data = UNSET
        else:
            conference_data = ConferenceData.from_dict(_conference_data)




        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        _creator = d.pop("creator", UNSET)
        creator: EventCreator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = EventCreator.from_dict(_creator)




        description = d.pop("description", UNSET)

        _end = d.pop("end", UNSET)
        end: EventDateTime | Unset
        if isinstance(_end,  Unset):
            end = UNSET
        else:
            end = EventDateTime.from_dict(_end)




        end_time_unspecified = d.pop("endTimeUnspecified", UNSET)

        etag = d.pop("etag", UNSET)

        event_type = d.pop("eventType", UNSET)

        _extended_properties = d.pop("extendedProperties", UNSET)
        extended_properties: EventExtendedProperties | Unset
        if isinstance(_extended_properties,  Unset):
            extended_properties = UNSET
        else:
            extended_properties = EventExtendedProperties.from_dict(_extended_properties)




        _gadget = d.pop("gadget", UNSET)
        gadget: EventGadget | Unset
        if isinstance(_gadget,  Unset):
            gadget = UNSET
        else:
            gadget = EventGadget.from_dict(_gadget)




        guests_can_invite_others = d.pop("guestsCanInviteOthers", UNSET)

        guests_can_modify = d.pop("guestsCanModify", UNSET)

        guests_can_see_other_guests = d.pop("guestsCanSeeOtherGuests", UNSET)

        hangout_link = d.pop("hangoutLink", UNSET)

        html_link = d.pop("htmlLink", UNSET)

        i_cal_uid = d.pop("iCalUID", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        location = d.pop("location", UNSET)

        locked = d.pop("locked", UNSET)

        _organizer = d.pop("organizer", UNSET)
        organizer: EventOrganizer | Unset
        if isinstance(_organizer,  Unset):
            organizer = UNSET
        else:
            organizer = EventOrganizer.from_dict(_organizer)




        _original_start_time = d.pop("originalStartTime", UNSET)
        original_start_time: EventDateTime | Unset
        if isinstance(_original_start_time,  Unset):
            original_start_time = UNSET
        else:
            original_start_time = EventDateTime.from_dict(_original_start_time)




        private_copy = d.pop("privateCopy", UNSET)

        recurrence = cast(list[str], d.pop("recurrence", UNSET))


        recurring_event_id = d.pop("recurringEventId", UNSET)

        _reminders = d.pop("reminders", UNSET)
        reminders: EventReminders | Unset
        if isinstance(_reminders,  Unset):
            reminders = UNSET
        else:
            reminders = EventReminders.from_dict(_reminders)




        sequence = d.pop("sequence", UNSET)

        _source = d.pop("source", UNSET)
        source: EventSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = EventSource.from_dict(_source)




        _start = d.pop("start", UNSET)
        start: EventDateTime | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = EventDateTime.from_dict(_start)




        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        transparency = d.pop("transparency", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated,  Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)




        visibility = d.pop("visibility", UNSET)

        _working_location_properties = d.pop("workingLocationProperties", UNSET)
        working_location_properties: EventWorkingLocationProperties | Unset
        if isinstance(_working_location_properties,  Unset):
            working_location_properties = UNSET
        else:
            working_location_properties = EventWorkingLocationProperties.from_dict(_working_location_properties)




        event = cls(
            anyone_can_add_self=anyone_can_add_self,
            attachments=attachments,
            attendees=attendees,
            attendees_omitted=attendees_omitted,
            color_id=color_id,
            conference_data=conference_data,
            created=created,
            creator=creator,
            description=description,
            end=end,
            end_time_unspecified=end_time_unspecified,
            etag=etag,
            event_type=event_type,
            extended_properties=extended_properties,
            gadget=gadget,
            guests_can_invite_others=guests_can_invite_others,
            guests_can_modify=guests_can_modify,
            guests_can_see_other_guests=guests_can_see_other_guests,
            hangout_link=hangout_link,
            html_link=html_link,
            i_cal_uid=i_cal_uid,
            id=id,
            kind=kind,
            location=location,
            locked=locked,
            organizer=organizer,
            original_start_time=original_start_time,
            private_copy=private_copy,
            recurrence=recurrence,
            recurring_event_id=recurring_event_id,
            reminders=reminders,
            sequence=sequence,
            source=source,
            start=start,
            status=status,
            summary=summary,
            transparency=transparency,
            updated=updated,
            visibility=visibility,
            working_location_properties=working_location_properties,
        )


        event.additional_properties = d
        return event

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
