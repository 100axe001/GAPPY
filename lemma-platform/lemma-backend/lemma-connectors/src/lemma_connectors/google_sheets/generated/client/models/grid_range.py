from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GridRange")



@_attrs_define
class GridRange:
    """ A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the start index is inclusive and the end
    index is exclusive -- [start_index, end_index). Missing indexes indicate the range is unbounded on that side. For
    example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 == sheet_id: 123456, start_row_index: 0,
    end_row_index: 1, start_column_index: 0, end_column_index: 1` `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2,
    end_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index:
    0, end_column_index: 2` `Sheet1!A5:B == sheet_id: 123456, start_row_index: 4, start_column_index: 0,
    end_column_index: 2` `Sheet1 == sheet_id: 123456` The start index must always be less than or equal to the end
    index. If the start index equals the end index, then the range is empty. Empty ranges are typically not meaningful
    and are usually rendered in the UI as `#REF!`.

        Attributes:
            end_column_index (int | Unset): The end column (exclusive) of the range, or not set if unbounded.
            end_row_index (int | Unset): The end row (exclusive) of the range, or not set if unbounded.
            sheet_id (int | Unset): The sheet this range is on.
            start_column_index (int | Unset): The start column (inclusive) of the range, or not set if unbounded.
            start_row_index (int | Unset): The start row (inclusive) of the range, or not set if unbounded.
     """

    end_column_index: int | Unset = UNSET
    end_row_index: int | Unset = UNSET
    sheet_id: int | Unset = UNSET
    start_column_index: int | Unset = UNSET
    start_row_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_column_index = self.end_column_index

        end_row_index = self.end_row_index

        sheet_id = self.sheet_id

        start_column_index = self.start_column_index

        start_row_index = self.start_row_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_column_index is not UNSET:
            field_dict["endColumnIndex"] = end_column_index
        if end_row_index is not UNSET:
            field_dict["endRowIndex"] = end_row_index
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id
        if start_column_index is not UNSET:
            field_dict["startColumnIndex"] = start_column_index
        if start_row_index is not UNSET:
            field_dict["startRowIndex"] = start_row_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_column_index = d.pop("endColumnIndex", UNSET)

        end_row_index = d.pop("endRowIndex", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        start_column_index = d.pop("startColumnIndex", UNSET)

        start_row_index = d.pop("startRowIndex", UNSET)

        grid_range = cls(
            end_column_index=end_column_index,
            end_row_index=end_row_index,
            sheet_id=sheet_id,
            start_column_index=start_column_index,
            start_row_index=start_row_index,
        )


        grid_range.additional_properties = d
        return grid_range

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
