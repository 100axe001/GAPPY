from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_source_refresh_weekly_schedule_days_of_week_item import DataSourceRefreshWeeklyScheduleDaysOfWeekItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time_of_day import TimeOfDay





T = TypeVar("T", bound="DataSourceRefreshWeeklySchedule")



@_attrs_define
class DataSourceRefreshWeeklySchedule:
    """ A weekly schedule for data to refresh on specific days in a given time interval.

        Attributes:
            days_of_week (list[DataSourceRefreshWeeklyScheduleDaysOfWeekItem] | Unset): Days of the week to refresh. At
                least one day must be specified.
            start_time (TimeOfDay | Unset): Represents a time of day. The date and time zone are either not significant or
                are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and
                `google.protobuf.Timestamp`.
     """

    days_of_week: list[DataSourceRefreshWeeklyScheduleDaysOfWeekItem] | Unset = UNSET
    start_time: TimeOfDay | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.time_of_day import TimeOfDay
        days_of_week: list[str] | Unset = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = []
            for days_of_week_item_data in self.days_of_week:
                days_of_week_item = days_of_week_item_data.value
                days_of_week.append(days_of_week_item)



        start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if days_of_week is not UNSET:
            field_dict["daysOfWeek"] = days_of_week
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_of_day import TimeOfDay
        d = dict(src_dict)
        _days_of_week = d.pop("daysOfWeek", UNSET)
        days_of_week: list[DataSourceRefreshWeeklyScheduleDaysOfWeekItem] | Unset = UNSET
        if _days_of_week is not UNSET:
            days_of_week = []
            for days_of_week_item_data in _days_of_week:
                days_of_week_item = DataSourceRefreshWeeklyScheduleDaysOfWeekItem(days_of_week_item_data)



                days_of_week.append(days_of_week_item)


        _start_time = d.pop("startTime", UNSET)
        start_time: TimeOfDay | Unset
        if isinstance(_start_time,  Unset):
            start_time = UNSET
        else:
            start_time = TimeOfDay.from_dict(_start_time)




        data_source_refresh_weekly_schedule = cls(
            days_of_week=days_of_week,
            start_time=start_time,
        )


        data_source_refresh_weekly_schedule.additional_properties = d
        return data_source_refresh_weekly_schedule

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
