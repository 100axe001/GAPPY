from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.extended_value import ExtendedValue





T = TypeVar("T", bound="PivotGroupValueMetadata")



@_attrs_define
class PivotGroupValueMetadata:
    """ Metadata about a value in a pivot grouping.

        Attributes:
            collapsed (bool | Unset): True if the data corresponding to the value is collapsed.
            value (ExtendedValue | Unset): The kinds of value that a cell in a spreadsheet can have.
     """

    collapsed: bool | Unset = UNSET
    value: ExtendedValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.extended_value import ExtendedValue
        collapsed = self.collapsed

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if collapsed is not UNSET:
            field_dict["collapsed"] = collapsed
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extended_value import ExtendedValue
        d = dict(src_dict)
        collapsed = d.pop("collapsed", UNSET)

        _value = d.pop("value", UNSET)
        value: ExtendedValue | Unset
        if isinstance(_value,  Unset):
            value = UNSET
        else:
            value = ExtendedValue.from_dict(_value)




        pivot_group_value_metadata = cls(
            collapsed=collapsed,
            value=value,
        )


        pivot_group_value_metadata.additional_properties = d
        return pivot_group_value_metadata

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
