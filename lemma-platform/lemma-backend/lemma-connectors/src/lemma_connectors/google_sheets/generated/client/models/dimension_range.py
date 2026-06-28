from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dimension_range_dimension import DimensionRangeDimension
from ..types import UNSET, Unset






T = TypeVar("T", bound="DimensionRange")



@_attrs_define
class DimensionRange:
    """ A range along a single dimension on a sheet. All indexes are zero-based. Indexes are half open: the start index is
    inclusive and the end index is exclusive. Missing indexes indicate the range is unbounded on that side.

        Attributes:
            dimension (DimensionRangeDimension | Unset): The dimension of the span.
            end_index (int | Unset): The end (exclusive) of the span, or not set if unbounded.
            sheet_id (int | Unset): The sheet this span is on.
            start_index (int | Unset): The start (inclusive) of the span, or not set if unbounded.
     """

    dimension: DimensionRangeDimension | Unset = UNSET
    end_index: int | Unset = UNSET
    sheet_id: int | Unset = UNSET
    start_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dimension: str | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.value


        end_index = self.end_index

        sheet_id = self.sheet_id

        start_index = self.start_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _dimension = d.pop("dimension", UNSET)
        dimension: DimensionRangeDimension | Unset
        if isinstance(_dimension,  Unset):
            dimension = UNSET
        else:
            dimension = DimensionRangeDimension(_dimension)




        end_index = d.pop("endIndex", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        start_index = d.pop("startIndex", UNSET)

        dimension_range = cls(
            dimension=dimension,
            end_index=end_index,
            sheet_id=sheet_id,
            start_index=start_index,
        )


        dimension_range.additional_properties = d
        return dimension_range

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
