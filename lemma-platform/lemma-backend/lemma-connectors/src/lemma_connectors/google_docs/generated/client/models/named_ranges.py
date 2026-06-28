from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.named_range import NamedRange





T = TypeVar("T", bound="NamedRanges")



@_attrs_define
class NamedRanges:
    """ A collection of all the NamedRanges in the document that share a given name.

        Attributes:
            name (str | Unset): The name that all the named ranges share.
            named_ranges (list[NamedRange] | Unset): The NamedRanges that share the same name.
     """

    name: str | Unset = UNSET
    named_ranges: list[NamedRange] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.named_range import NamedRange
        name = self.name

        named_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.named_ranges, Unset):
            named_ranges = []
            for named_ranges_item_data in self.named_ranges:
                named_ranges_item = named_ranges_item_data.to_dict()
                named_ranges.append(named_ranges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if named_ranges is not UNSET:
            field_dict["namedRanges"] = named_ranges

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_range import NamedRange
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _named_ranges = d.pop("namedRanges", UNSET)
        named_ranges: list[NamedRange] | Unset = UNSET
        if _named_ranges is not UNSET:
            named_ranges = []
            for named_ranges_item_data in _named_ranges:
                named_ranges_item = NamedRange.from_dict(named_ranges_item_data)



                named_ranges.append(named_ranges_item)


        named_ranges = cls(
            name=name,
            named_ranges=named_ranges,
        )


        named_ranges.additional_properties = d
        return named_ranges

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
