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





T = TypeVar("T", bound="AddDimensionGroupRequest")



@_attrs_define
class AddDimensionGroupRequest:
    """ Creates a group over the specified range. If the requested range is a superset of the range of an existing group G,
    then the depth of G is incremented and this new group G' has the depth of that group. For example, a group [C:D,
    depth 1] + [B:E] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range is a subset of the
    range of an existing group G, then the depth of the new group G' becomes one greater than the depth of G. For
    example, a group [B:E, depth 1] + [C:D] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range
    starts before and ends within, or starts within and ends after, the range of an existing group G, then the range of
    the existing group G becomes the union of the ranges, and the new group G' has depth one greater than the depth of G
    and range as the intersection of the ranges. For example, a group [B:D, depth 1] + [C:E] results in groups [B:E,
    depth 1] and [C:D, depth 2].

        Attributes:
            range_ (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-based.
                Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the
                range is unbounded on that side.
     """

    range_: DimensionRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_range import DimensionRange
        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        _range_ = d.pop("range", UNSET)
        range_: DimensionRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = DimensionRange.from_dict(_range_)




        add_dimension_group_request = cls(
            range_=range_,
        )


        add_dimension_group_request.additional_properties = d
        return add_dimension_group_request

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
