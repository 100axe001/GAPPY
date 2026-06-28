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
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="DeleteDuplicatesRequest")



@_attrs_define
class DeleteDuplicatesRequest:
    """ Removes rows within this range that contain values in the specified columns that are duplicates of values in any
    previous row. Rows with identical values but different letter cases, formatting, or formulas are considered to be
    duplicates. This request also removes duplicate rows hidden from view (for example, due to a filter). When removing
    duplicates, the first instance of each duplicate row scanning from the top downwards is kept in the resulting range.
    Content outside of the specified range isn't removed, and rows considered duplicates do not have to be adjacent to
    each other in the range.

        Attributes:
            comparison_columns (list[DimensionRange] | Unset): The columns in the range to analyze for duplicate values. If
                no columns are selected then all columns are analyzed for duplicates.
            range_ (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
     """

    comparison_columns: list[DimensionRange] | Unset = UNSET
    range_: GridRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_range import DimensionRange
        from ..models.grid_range import GridRange
        comparison_columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comparison_columns, Unset):
            comparison_columns = []
            for comparison_columns_item_data in self.comparison_columns:
                comparison_columns_item = comparison_columns_item_data.to_dict()
                comparison_columns.append(comparison_columns_item)



        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comparison_columns is not UNSET:
            field_dict["comparisonColumns"] = comparison_columns
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_range import DimensionRange
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _comparison_columns = d.pop("comparisonColumns", UNSET)
        comparison_columns: list[DimensionRange] | Unset = UNSET
        if _comparison_columns is not UNSET:
            comparison_columns = []
            for comparison_columns_item_data in _comparison_columns:
                comparison_columns_item = DimensionRange.from_dict(comparison_columns_item_data)



                comparison_columns.append(comparison_columns_item)


        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        delete_duplicates_request = cls(
            comparison_columns=comparison_columns,
            range_=range_,
        )


        delete_duplicates_request.additional_properties = d
        return delete_duplicates_request

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
