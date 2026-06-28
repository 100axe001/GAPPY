from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EventReminder")



@_attrs_define
class EventReminder:
    """ 
        Attributes:
            method (str | Unset): The method used by this reminder. Possible values are:
                - "email" - Reminders are sent via email.
                - "popup" - Reminders are sent via a UI popup.
                Required when adding a reminder.
            minutes (int | Unset): Number of minutes before the start of the event when the reminder should trigger. Valid
                values are between 0 and 40320 (4 weeks in minutes).
                Required when adding a reminder.
     """

    method: str | Unset = UNSET
    minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method

        minutes = self.minutes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method", UNSET)

        minutes = d.pop("minutes", UNSET)

        event_reminder = cls(
            method=method,
            minutes=minutes,
        )


        event_reminder.additional_properties = d
        return event_reminder

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
