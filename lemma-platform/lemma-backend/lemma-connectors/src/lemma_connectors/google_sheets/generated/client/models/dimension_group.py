from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension_range import DimensionRange





T = TypeVar("T", bound="DimensionGroup")



@_attrs_define
class DimensionGroup:
    """ A group over an interval of rows or columns on a sheet, which can contain or be contained within other groups. A
    group can be collapsed or expanded as a unit on the sheet.

        Attributes:
            collapsed (bool | Unset): This field is true if this group is collapsed. A collapsed group remains collapsed if
                an overlapping group at a shallower depth is expanded. A true value does not imply that all dimensions within
                the group are hidden, since a dimension's visibility can change independently from this group property. However,
                when this property is updated, all dimensions within it are set to hidden if this field is true, or set to
                visible if this field is false.
            depth (int | Unset): The depth of the group, representing how many groups have a range that wholly contains the
                range of this group.
            range_ (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-based.
                Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the
                range is unbounded on that side.
     """

    collapsed: bool | Unset = UNSET
    depth: int | Unset = UNSET
    range_: DimensionRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_range import DimensionRange
        collapsed = self.collapsed

        depth = self.depth

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if collapsed is not UNSET:
            field_dict["collapsed"] = collapsed
        if depth is not UNSET:
            field_dict["depth"] = depth
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        collapsed = d.pop("collapsed", UNSET)

        depth = d.pop("depth", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: DimensionRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = DimensionRange.from_dict(_range_)




        dimension_group = cls(
            collapsed=collapsed,
            depth=depth,
            range_=range_,
        )


        dimension_group.additional_properties = d
        return dimension_group

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
