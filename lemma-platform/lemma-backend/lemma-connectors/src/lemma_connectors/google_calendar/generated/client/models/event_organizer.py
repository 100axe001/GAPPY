from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EventOrganizer")



@_attrs_define
class EventOrganizer:
    """ The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in
    attendees with the organizer field set to True. To change the organizer, use the move operation. Read-only, except
    when importing an event.

        Attributes:
            display_name (str | Unset): The organizer's name, if available.
            email (str | Unset): The organizer's email address, if available. It must be a valid email address as per
                RFC5322.
            id (str | Unset): The organizer's Profile ID, if available.
            self_ (bool | Unset): Whether the organizer corresponds to the calendar on which this copy of the event appears.
                Read-only. The default is False. Default: False.
     """

    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    self_: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        email = self.email

        id = self.id

        self_ = self.self_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        self_ = d.pop("self", UNSET)

        event_organizer = cls(
            display_name=display_name,
            email=email,
            id=id,
            self_=self_,
        )


        event_organizer.additional_properties = d
        return event_organizer

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
