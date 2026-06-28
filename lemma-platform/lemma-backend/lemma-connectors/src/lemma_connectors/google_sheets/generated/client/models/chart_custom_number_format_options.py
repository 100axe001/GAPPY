from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChartCustomNumberFormatOptions")



@_attrs_define
class ChartCustomNumberFormatOptions:
    """ Custom number formatting options for chart attributes.

        Attributes:
            prefix (str | Unset): Custom prefix to be prepended to the chart attribute. This field is optional.
            suffix (str | Unset): Custom suffix to be appended to the chart attribute. This field is optional.
     """

    prefix: str | Unset = UNSET
    suffix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        prefix = self.prefix

        suffix = self.suffix


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        chart_custom_number_format_options = cls(
            prefix=prefix,
            suffix=suffix,
        )


        chart_custom_number_format_options.additional_properties = d
        return chart_custom_number_format_options

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
