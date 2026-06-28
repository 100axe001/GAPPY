from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextDefaultValueDateTime")



@_attrs_define
class CustomFieldContextDefaultValueDateTime:
    """ The default value for a date time custom field.

        Attributes:
            type_ (str):
            date_time (str | Unset): The default date-time in ISO format. Ignored if `useCurrent` is true.
            use_current (bool | Unset): Whether to use the current date. Default: False.
     """

    type_: str
    date_time: str | Unset = UNSET
    use_current: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        date_time = self.date_time

        use_current = self.use_current


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if use_current is not UNSET:
            field_dict["useCurrent"] = use_current

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        date_time = d.pop("dateTime", UNSET)

        use_current = d.pop("useCurrent", UNSET)

        custom_field_context_default_value_date_time = cls(
            type_=type_,
            date_time=date_time,
            use_current=use_current,
        )


        custom_field_context_default_value_date_time.additional_properties = d
        return custom_field_context_default_value_date_time

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
