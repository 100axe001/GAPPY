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






T = TypeVar("T", bound="TimePeriod")



@_attrs_define
class TimePeriod:
    """ 
        Attributes:
            end (datetime.datetime | Unset): The (exclusive) end of the time period.
            start (datetime.datetime | Unset): The (inclusive) start of the time period.
     """

    end: datetime.datetime | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end,  Unset):
            end = UNSET
        else:
            end = isoparse(_end)




        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = isoparse(_start)




        time_period = cls(
            end=end,
            start=start,
        )


        time_period.additional_properties = d
        return time_period

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
