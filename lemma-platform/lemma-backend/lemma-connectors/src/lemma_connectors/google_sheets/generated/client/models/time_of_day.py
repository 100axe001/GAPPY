from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TimeOfDay")



@_attrs_define
class TimeOfDay:
    """ Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may
    choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`.

        Attributes:
            hours (int | Unset): Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the
                value "24:00:00" for scenarios like business closing time.
            minutes (int | Unset): Minutes of hour of day. Must be from 0 to 59.
            nanos (int | Unset): Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
            seconds (int | Unset): Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value
                60 if it allows leap-seconds.
     """

    hours: int | Unset = UNSET
    minutes: int | Unset = UNSET
    nanos: int | Unset = UNSET
    seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hours = self.hours

        minutes = self.minutes

        nanos = self.nanos

        seconds = self.seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if nanos is not UNSET:
            field_dict["nanos"] = nanos
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        nanos = d.pop("nanos", UNSET)

        seconds = d.pop("seconds", UNSET)

        time_of_day = cls(
            hours=hours,
            minutes=minutes,
            nanos=nanos,
            seconds=seconds,
        )


        time_of_day.additional_properties = d
        return time_of_day

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
