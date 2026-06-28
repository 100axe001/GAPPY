from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Interval")



@_attrs_define
class Interval:
    """ Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must
    be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both
    start and end are unspecified, the interval matches any time.

        Attributes:
            end_time (str | Unset): Optional. Exclusive end of the interval. If specified, a Timestamp matching this
                interval will have to be before the end.
            start_time (str | Unset): Optional. Inclusive start of the interval. If specified, a Timestamp matching this
                interval will have to be the same or after the start.
     """

    end_time: str | Unset = UNSET
    start_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        start_time = self.start_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_time = d.pop("endTime", UNSET)

        start_time = d.pop("startTime", UNSET)

        interval = cls(
            end_time=end_time,
            start_time=start_time,
        )


        interval.additional_properties = d
        return interval

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
