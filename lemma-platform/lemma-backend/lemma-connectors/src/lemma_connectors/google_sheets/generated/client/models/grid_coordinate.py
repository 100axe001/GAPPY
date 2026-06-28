from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GridCoordinate")



@_attrs_define
class GridCoordinate:
    """ A coordinate in a sheet. All indexes are zero-based.

        Attributes:
            column_index (int | Unset): The column index of the coordinate.
            row_index (int | Unset): The row index of the coordinate.
            sheet_id (int | Unset): The sheet this coordinate is on.
     """

    column_index: int | Unset = UNSET
    row_index: int | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        column_index = self.column_index

        row_index = self.row_index

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_index is not UNSET:
            field_dict["columnIndex"] = column_index
        if row_index is not UNSET:
            field_dict["rowIndex"] = row_index
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_index = d.pop("columnIndex", UNSET)

        row_index = d.pop("rowIndex", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        grid_coordinate = cls(
            column_index=column_index,
            row_index=row_index,
            sheet_id=sheet_id,
        )


        grid_coordinate.additional_properties = d
        return grid_coordinate

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
