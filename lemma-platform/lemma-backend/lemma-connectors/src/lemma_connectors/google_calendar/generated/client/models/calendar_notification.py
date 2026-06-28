from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CalendarNotification")



@_attrs_define
class CalendarNotification:
    """ 
        Attributes:
            method (str | Unset): The method used to deliver the notification. The possible value is:
                - "email" - Notifications are sent via email.
                Required when adding a notification.
            type_ (str | Unset): The type of notification. Possible values are:
                - "eventCreation" - Notification sent when a new event is put on the calendar.
                - "eventChange" - Notification sent when an event is changed.
                - "eventCancellation" - Notification sent when an event is cancelled.
                - "eventResponse" - Notification sent when an attendee responds to the event invitation.
                - "agenda" - An agenda with the events of the day (sent out in the morning).
                Required when adding a notification.
     """

    method: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = d.pop("method", UNSET)

        type_ = d.pop("type", UNSET)

        calendar_notification = cls(
            method=method,
            type_=type_,
        )


        calendar_notification.additional_properties = d
        return calendar_notification

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
