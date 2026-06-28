from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.free_busy_calendar import FreeBusyCalendar





T = TypeVar("T", bound="FreeBusyResponseCalendars")



@_attrs_define
class FreeBusyResponseCalendars:
    """ List of free/busy information for calendars.

     """

    additional_properties: dict[str, FreeBusyCalendar] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.free_busy_calendar import FreeBusyCalendar
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.free_busy_calendar import FreeBusyCalendar
        d = dict(src_dict)
        free_busy_response_calendars = cls(
        )


        from ..models.error import Error
        from ..models.time_period import TimePeriod
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FreeBusyCalendar.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        free_busy_response_calendars.additional_properties = additional_properties
        return free_busy_response_calendars

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FreeBusyCalendar:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FreeBusyCalendar) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
