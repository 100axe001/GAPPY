from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.range_ import Range





T = TypeVar("T", bound="NamedRange")



@_attrs_define
class NamedRange:
    """ A collection of Ranges with the same named range ID. Named ranges allow developers to associate parts of a document
    with an arbitrary user-defined label so their contents can be programmatically read or edited later. A document can
    contain multiple named ranges with the same name, but every named range has a unique ID. A named range is created
    with a single Range, and content inserted inside a named range generally expands that range. However, certain
    document changes can cause the range to be split into multiple ranges. Named ranges are not private. All
    applications and collaborators that have access to the document can see its named ranges.

        Attributes:
            name (str | Unset): The name of the named range.
            named_range_id (str | Unset): The ID of the named range.
            ranges (list[Range] | Unset): The ranges that belong to this named range.
     """

    name: str | Unset = UNSET
    named_range_id: str | Unset = UNSET
    ranges: list[Range] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.range_ import Range
        name = self.name

        named_range_id = self.named_range_id

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if named_range_id is not UNSET:
            field_dict["namedRangeId"] = named_range_id
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_ import Range
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        named_range_id = d.pop("namedRangeId", UNSET)

        _ranges = d.pop("ranges", UNSET)
        ranges: list[Range] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = Range.from_dict(ranges_item_data)



                ranges.append(ranges_item)


        named_range = cls(
            name=name,
            named_range_id=named_range_id,
            ranges=ranges,
        )


        named_range.additional_properties = d
        return named_range

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
