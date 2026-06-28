from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldContextDefaultValueDate")



@_attrs_define
class CustomFieldContextDefaultValueDate:
    """ The default value for a Date custom field.

        Attributes:
            type_ (str):
            date (str | Unset): The default date in ISO format. Ignored if `useCurrent` is true.
            use_current (bool | Unset): Whether to use the current date. Default: False.
     """

    type_: str
    date: str | Unset = UNSET
    use_current: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        date = self.date

        use_current = self.use_current


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if date is not UNSET:
            field_dict["date"] = date
        if use_current is not UNSET:
            field_dict["useCurrent"] = use_current

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        date = d.pop("date", UNSET)

        use_current = d.pop("useCurrent", UNSET)

        custom_field_context_default_value_date = cls(
            type_=type_,
            date=date,
            use_current=use_current,
        )


        custom_field_context_default_value_date.additional_properties = d
        return custom_field_context_default_value_date

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
