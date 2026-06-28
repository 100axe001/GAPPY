from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PivotGroupLimit")



@_attrs_define
class PivotGroupLimit:
    """ The count limit on rows or columns in the pivot group.

        Attributes:
            apply_order (int | Unset): The order in which the group limit is applied to the pivot table. Pivot group limits
                are applied from lower to higher order number. Order numbers are normalized to consecutive integers from 0. For
                write request, to fully customize the applying orders, all pivot group limits should have this field set with an
                unique number. Otherwise, the order is determined by the index in the PivotTable.rows list and then the
                PivotTable.columns list.
            count_limit (int | Unset): The count limit.
     """

    apply_order: int | Unset = UNSET
    count_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        apply_order = self.apply_order

        count_limit = self.count_limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if apply_order is not UNSET:
            field_dict["applyOrder"] = apply_order
        if count_limit is not UNSET:
            field_dict["countLimit"] = count_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apply_order = d.pop("applyOrder", UNSET)

        count_limit = d.pop("countLimit", UNSET)

        pivot_group_limit = cls(
            apply_order=apply_order,
            count_limit=count_limit,
        )


        pivot_group_limit.additional_properties = d
        return pivot_group_limit

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
