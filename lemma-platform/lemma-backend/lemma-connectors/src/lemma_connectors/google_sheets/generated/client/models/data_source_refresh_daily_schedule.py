from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time_of_day import TimeOfDay





T = TypeVar("T", bound="DataSourceRefreshDailySchedule")



@_attrs_define
class DataSourceRefreshDailySchedule:
    """ A schedule for data to refresh every day in a given time interval.

        Attributes:
            start_time (TimeOfDay | Unset): Represents a time of day. The date and time zone are either not significant or
                are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and
                `google.protobuf.Timestamp`.
     """

    start_time: TimeOfDay | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.time_of_day import TimeOfDay
        start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_of_day import TimeOfDay
        d = dict(src_dict)
        _start_time = d.pop("startTime", UNSET)
        start_time: TimeOfDay | Unset
        if isinstance(_start_time,  Unset):
            start_time = UNSET
        else:
            start_time = TimeOfDay.from_dict(_start_time)




        data_source_refresh_daily_schedule = cls(
            start_time=start_time,
        )


        data_source_refresh_daily_schedule.additional_properties = d
        return data_source_refresh_daily_schedule

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
