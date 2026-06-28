from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_source_refresh_schedule_refresh_scope import DataSourceRefreshScheduleRefreshScope
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_refresh_daily_schedule import DataSourceRefreshDailySchedule
  from ..models.data_source_refresh_monthly_schedule import DataSourceRefreshMonthlySchedule
  from ..models.data_source_refresh_weekly_schedule import DataSourceRefreshWeeklySchedule
  from ..models.interval import Interval





T = TypeVar("T", bound="DataSourceRefreshSchedule")



@_attrs_define
class DataSourceRefreshSchedule:
    """ Schedule for refreshing the data source. Data sources in the spreadsheet are refreshed within a time interval. You
    can specify the start time by clicking the Scheduled Refresh button in the Sheets editor, but the interval is fixed
    at 4 hours. For example, if you specify a start time of 8am , the refresh will take place between 8am and 12pm every
    day.

        Attributes:
            daily_schedule (DataSourceRefreshDailySchedule | Unset): A schedule for data to refresh every day in a given
                time interval.
            enabled (bool | Unset): True if the refresh schedule is enabled, or false otherwise.
            monthly_schedule (DataSourceRefreshMonthlySchedule | Unset): A monthly schedule for data to refresh on specific
                days in the month in a given time interval.
            next_run (Interval | Unset): Represents a time interval, encoded as a Timestamp start (inclusive) and a
                Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the
                interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.
            refresh_scope (DataSourceRefreshScheduleRefreshScope | Unset): The scope of the refresh. Must be
                ALL_DATA_SOURCES.
            weekly_schedule (DataSourceRefreshWeeklySchedule | Unset): A weekly schedule for data to refresh on specific
                days in a given time interval.
     """

    daily_schedule: DataSourceRefreshDailySchedule | Unset = UNSET
    enabled: bool | Unset = UNSET
    monthly_schedule: DataSourceRefreshMonthlySchedule | Unset = UNSET
    next_run: Interval | Unset = UNSET
    refresh_scope: DataSourceRefreshScheduleRefreshScope | Unset = UNSET
    weekly_schedule: DataSourceRefreshWeeklySchedule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_refresh_daily_schedule import DataSourceRefreshDailySchedule
        from ..models.data_source_refresh_monthly_schedule import DataSourceRefreshMonthlySchedule
        from ..models.data_source_refresh_weekly_schedule import DataSourceRefreshWeeklySchedule
        from ..models.interval import Interval
        daily_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_schedule, Unset):
            daily_schedule = self.daily_schedule.to_dict()

        enabled = self.enabled

        monthly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_schedule, Unset):
            monthly_schedule = self.monthly_schedule.to_dict()

        next_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_run, Unset):
            next_run = self.next_run.to_dict()

        refresh_scope: str | Unset = UNSET
        if not isinstance(self.refresh_scope, Unset):
            refresh_scope = self.refresh_scope.value


        weekly_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weekly_schedule, Unset):
            weekly_schedule = self.weekly_schedule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if daily_schedule is not UNSET:
            field_dict["dailySchedule"] = daily_schedule
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if monthly_schedule is not UNSET:
            field_dict["monthlySchedule"] = monthly_schedule
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if refresh_scope is not UNSET:
            field_dict["refreshScope"] = refresh_scope
        if weekly_schedule is not UNSET:
            field_dict["weeklySchedule"] = weekly_schedule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_refresh_daily_schedule import DataSourceRefreshDailySchedule
        from ..models.data_source_refresh_monthly_schedule import DataSourceRefreshMonthlySchedule
        from ..models.data_source_refresh_weekly_schedule import DataSourceRefreshWeeklySchedule
        from ..models.interval import Interval
        d = dict(src_dict)
        _daily_schedule = d.pop("dailySchedule", UNSET)
        daily_schedule: DataSourceRefreshDailySchedule | Unset
        if isinstance(_daily_schedule,  Unset):
            daily_schedule = UNSET
        else:
            daily_schedule = DataSourceRefreshDailySchedule.from_dict(_daily_schedule)




        enabled = d.pop("enabled", UNSET)

        _monthly_schedule = d.pop("monthlySchedule", UNSET)
        monthly_schedule: DataSourceRefreshMonthlySchedule | Unset
        if isinstance(_monthly_schedule,  Unset):
            monthly_schedule = UNSET
        else:
            monthly_schedule = DataSourceRefreshMonthlySchedule.from_dict(_monthly_schedule)




        _next_run = d.pop("nextRun", UNSET)
        next_run: Interval | Unset
        if isinstance(_next_run,  Unset):
            next_run = UNSET
        else:
            next_run = Interval.from_dict(_next_run)




        _refresh_scope = d.pop("refreshScope", UNSET)
        refresh_scope: DataSourceRefreshScheduleRefreshScope | Unset
        if isinstance(_refresh_scope,  Unset):
            refresh_scope = UNSET
        else:
            refresh_scope = DataSourceRefreshScheduleRefreshScope(_refresh_scope)




        _weekly_schedule = d.pop("weeklySchedule", UNSET)
        weekly_schedule: DataSourceRefreshWeeklySchedule | Unset
        if isinstance(_weekly_schedule,  Unset):
            weekly_schedule = UNSET
        else:
            weekly_schedule = DataSourceRefreshWeeklySchedule.from_dict(_weekly_schedule)




        data_source_refresh_schedule = cls(
            daily_schedule=daily_schedule,
            enabled=enabled,
            monthly_schedule=monthly_schedule,
            next_run=next_run,
            refresh_scope=refresh_scope,
            weekly_schedule=weekly_schedule,
        )


        data_source_refresh_schedule.additional_properties = d
        return data_source_refresh_schedule

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
