from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EventAttendee")



@_attrs_define
class EventAttendee:
    """ 
        Attributes:
            additional_guests (int | Unset): Number of additional guests. Optional. The default is 0. Default: 0.
            comment (str | Unset): The attendee's response comment. Optional.
            display_name (str | Unset): The attendee's name, if available. Optional.
            email (str | Unset): The attendee's email address, if available. This field must be present when adding an
                attendee. It must be a valid email address as per RFC5322.
                Required when adding an attendee.
            id (str | Unset): The attendee's Profile ID, if available.
            optional (bool | Unset): Whether this is an optional attendee. Optional. The default is False. Default: False.
            organizer (bool | Unset): Whether the attendee is the organizer of the event. Read-only. The default is False.
            resource (bool | Unset): Whether the attendee is a resource. Can only be set when the attendee is added to the
                event for the first time. Subsequent modifications are ignored. Optional. The default is False. Default: False.
            response_status (str | Unset): The attendee's response status. Possible values are:
                - "needsAction" - The attendee has not responded to the invitation (recommended for new events).
                - "declined" - The attendee has declined the invitation.
                - "tentative" - The attendee has tentatively accepted the invitation.
                - "accepted" - The attendee has accepted the invitation.  Warning: If you add an event using the values
                declined, tentative, or accepted, attendees with the "Add invitations to my calendar" setting set to "When I
                respond to invitation in email" won't see an event on their calendar unless they choose to change their
                invitation response in the event invitation email.
            self_ (bool | Unset): Whether this entry represents the calendar on which this copy of the event appears. Read-
                only. The default is False. Default: False.
     """

    additional_guests: int | Unset = 0
    comment: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    optional: bool | Unset = False
    organizer: bool | Unset = UNSET
    resource: bool | Unset = False
    response_status: str | Unset = UNSET
    self_: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        additional_guests = self.additional_guests

        comment = self.comment

        display_name = self.display_name

        email = self.email

        id = self.id

        optional = self.optional

        organizer = self.organizer

        resource = self.resource

        response_status = self.response_status

        self_ = self.self_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if additional_guests is not UNSET:
            field_dict["additionalGuests"] = additional_guests
        if comment is not UNSET:
            field_dict["comment"] = comment
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if optional is not UNSET:
            field_dict["optional"] = optional
        if organizer is not UNSET:
            field_dict["organizer"] = organizer
        if resource is not UNSET:
            field_dict["resource"] = resource
        if response_status is not UNSET:
            field_dict["responseStatus"] = response_status
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_guests = d.pop("additionalGuests", UNSET)

        comment = d.pop("comment", UNSET)

        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        optional = d.pop("optional", UNSET)

        organizer = d.pop("organizer", UNSET)

        resource = d.pop("resource", UNSET)

        response_status = d.pop("responseStatus", UNSET)

        self_ = d.pop("self", UNSET)

        event_attendee = cls(
            additional_guests=additional_guests,
            comment=comment,
            display_name=display_name,
            email=email,
            id=id,
            optional=optional,
            organizer=organizer,
            resource=resource,
            response_status=response_status,
            self_=self_,
        )


        event_attendee.additional_properties = d
        return event_attendee

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
