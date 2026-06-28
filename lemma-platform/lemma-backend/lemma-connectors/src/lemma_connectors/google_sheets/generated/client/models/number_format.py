from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.number_format_type import NumberFormatType
from ..types import UNSET, Unset






T = TypeVar("T", bound="NumberFormat")



@_attrs_define
class NumberFormat:
    """ The number format of a cell.

        Attributes:
            pattern (str | Unset): Pattern string used for formatting. If not set, a default pattern based on the user's
                locale will be used if necessary for the given type. See the [Date and Number Formats
                guide](/sheets/api/guides/formats) for more information about the supported patterns.
            type_ (NumberFormatType | Unset): The type of the number format. When writing, this field must be set.
     """

    pattern: str | Unset = UNSET
    type_: NumberFormatType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pattern = d.pop("pattern", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NumberFormatType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = NumberFormatType(_type_)




        number_format = cls(
            pattern=pattern,
            type_=type_,
        )


        number_format.additional_properties = d
        return number_format

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
