from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.time_tracking_configuration_default_unit import TimeTrackingConfigurationDefaultUnit
from ..models.time_tracking_configuration_time_format import TimeTrackingConfigurationTimeFormat






T = TypeVar("T", bound="TimeTrackingConfiguration")



@_attrs_define
class TimeTrackingConfiguration:
    """ Details of the time tracking configuration.

        Attributes:
            default_unit (TimeTrackingConfigurationDefaultUnit): The default unit of time applied to logged time.
            time_format (TimeTrackingConfigurationTimeFormat): The format that will appear on an issue's *Time Spent* field.
            working_days_per_week (float): The number of days in a working week.
            working_hours_per_day (float): The number of hours in a working day.
     """

    default_unit: TimeTrackingConfigurationDefaultUnit
    time_format: TimeTrackingConfigurationTimeFormat
    working_days_per_week: float
    working_hours_per_day: float





    def to_dict(self) -> dict[str, Any]:
        default_unit = self.default_unit.value

        time_format = self.time_format.value

        working_days_per_week = self.working_days_per_week

        working_hours_per_day = self.working_hours_per_day


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "defaultUnit": default_unit,
            "timeFormat": time_format,
            "workingDaysPerWeek": working_days_per_week,
            "workingHoursPerDay": working_hours_per_day,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_unit = TimeTrackingConfigurationDefaultUnit(d.pop("defaultUnit"))




        time_format = TimeTrackingConfigurationTimeFormat(d.pop("timeFormat"))




        working_days_per_week = d.pop("workingDaysPerWeek")

        working_hours_per_day = d.pop("workingHoursPerDay")

        time_tracking_configuration = cls(
            default_unit=default_unit,
            time_format=time_format,
            working_days_per_week=working_days_per_week,
            working_hours_per_day=working_hours_per_day,
        )

        return time_tracking_configuration

