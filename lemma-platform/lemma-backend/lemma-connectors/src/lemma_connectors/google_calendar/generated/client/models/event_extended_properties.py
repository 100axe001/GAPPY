from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.event_extended_properties_private import EventExtendedPropertiesPrivate
  from ..models.event_extended_properties_shared import EventExtendedPropertiesShared





T = TypeVar("T", bound="EventExtendedProperties")



@_attrs_define
class EventExtendedProperties:
    """ Extended properties of the event.

        Attributes:
            private (EventExtendedPropertiesPrivate | Unset): Properties that are private to the copy of the event that
                appears on this calendar.
            shared (EventExtendedPropertiesShared | Unset): Properties that are shared between copies of the event on other
                attendees' calendars.
     """

    private: EventExtendedPropertiesPrivate | Unset = UNSET
    shared: EventExtendedPropertiesShared | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_extended_properties_private import EventExtendedPropertiesPrivate
        from ..models.event_extended_properties_shared import EventExtendedPropertiesShared
        private: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private, Unset):
            private = self.private.to_dict()

        shared: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared, Unset):
            shared = self.shared.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if private is not UNSET:
            field_dict["private"] = private
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_extended_properties_private import EventExtendedPropertiesPrivate
        from ..models.event_extended_properties_shared import EventExtendedPropertiesShared
        d = dict(src_dict)
        _private = d.pop("private", UNSET)
        private: EventExtendedPropertiesPrivate | Unset
        if isinstance(_private,  Unset):
            private = UNSET
        else:
            private = EventExtendedPropertiesPrivate.from_dict(_private)




        _shared = d.pop("shared", UNSET)
        shared: EventExtendedPropertiesShared | Unset
        if isinstance(_shared,  Unset):
            shared = UNSET
        else:
            shared = EventExtendedPropertiesShared.from_dict(_shared)




        event_extended_properties = cls(
            private=private,
            shared=shared,
        )


        event_extended_properties.additional_properties = d
        return event_extended_properties

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
