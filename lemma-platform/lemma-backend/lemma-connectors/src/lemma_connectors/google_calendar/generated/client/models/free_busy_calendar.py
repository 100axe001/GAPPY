from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error import Error
  from ..models.time_period import TimePeriod





T = TypeVar("T", bound="FreeBusyCalendar")



@_attrs_define
class FreeBusyCalendar:
    """ 
        Attributes:
            busy (list[TimePeriod] | Unset): List of time ranges during which this calendar should be regarded as busy.
            errors (list[Error] | Unset): Optional error(s) (if computation for the calendar failed).
     """

    busy: list[TimePeriod] | Unset = UNSET
    errors: list[Error] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error import Error
        from ..models.time_period import TimePeriod
        busy: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.busy, Unset):
            busy = []
            for busy_item_data in self.busy:
                busy_item = busy_item_data.to_dict()
                busy.append(busy_item)



        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if busy is not UNSET:
            field_dict["busy"] = busy
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error import Error
        from ..models.time_period import TimePeriod
        d = dict(src_dict)
        _busy = d.pop("busy", UNSET)
        busy: list[TimePeriod] | Unset = UNSET
        if _busy is not UNSET:
            busy = []
            for busy_item_data in _busy:
                busy_item = TimePeriod.from_dict(busy_item_data)



                busy.append(busy_item)


        _errors = d.pop("errors", UNSET)
        errors: list[Error] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = Error.from_dict(errors_item_data)



                errors.append(errors_item)


        free_busy_calendar = cls(
            busy=busy,
            errors=errors,
        )


        free_busy_calendar.additional_properties = d
        return free_busy_calendar

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
