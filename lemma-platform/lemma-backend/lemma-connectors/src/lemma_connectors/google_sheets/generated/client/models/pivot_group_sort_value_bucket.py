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





T = TypeVar("T", bound="PivotGroupSortValueBucket")



@_attrs_define
class PivotGroupSortValueBucket:
    """ Information about which values in a pivot group should be used for sorting.

        Attributes:
            buckets (list[ExtendedValue] | Unset): Determines the bucket from which values are chosen to sort. For example,
                in a pivot table with one row group & two column groups, the row group can list up to two values. The first
                value corresponds to a value within the first column group, and the second value corresponds to a value in the
                second column group. If no values are listed, this would indicate that the row should be sorted according to the
                "Grand Total" over the column groups. If a single value is listed, this would correspond to using the "Total" of
                that bucket.
            values_index (int | Unset): The offset in the PivotTable.values list which the values in this grouping should be
                sorted by.
     """

    buckets: list[ExtendedValue] | Unset = UNSET
    values_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.extended_value import ExtendedValue
        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)



        values_index = self.values_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if values_index is not UNSET:
            field_dict["valuesIndex"] = values_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extended_value import ExtendedValue
        d = dict(src_dict)
        _buckets = d.pop("buckets", UNSET)
        buckets: list[ExtendedValue] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ExtendedValue.from_dict(buckets_item_data)



                buckets.append(buckets_item)


        values_index = d.pop("valuesIndex", UNSET)

        pivot_group_sort_value_bucket = cls(
            buckets=buckets,
            values_index=values_index,
        )


        pivot_group_sort_value_bucket.additional_properties = d
        return pivot_group_sort_value_bucket

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
