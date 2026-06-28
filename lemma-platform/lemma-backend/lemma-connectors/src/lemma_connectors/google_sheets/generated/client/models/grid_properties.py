from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GridProperties")



@_attrs_define
class GridProperties:
    """ Properties of a grid.

        Attributes:
            column_count (int | Unset): The number of columns in the grid.
            column_group_control_after (bool | Unset): True if the column grouping control toggle is shown after the group.
            frozen_column_count (int | Unset): The number of columns that are frozen in the grid.
            frozen_row_count (int | Unset): The number of rows that are frozen in the grid.
            hide_gridlines (bool | Unset): True if the grid isn't showing gridlines in the UI.
            row_count (int | Unset): The number of rows in the grid.
            row_group_control_after (bool | Unset): True if the row grouping control toggle is shown after the group.
     """

    column_count: int | Unset = UNSET
    column_group_control_after: bool | Unset = UNSET
    frozen_column_count: int | Unset = UNSET
    frozen_row_count: int | Unset = UNSET
    hide_gridlines: bool | Unset = UNSET
    row_count: int | Unset = UNSET
    row_group_control_after: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        column_count = self.column_count

        column_group_control_after = self.column_group_control_after

        frozen_column_count = self.frozen_column_count

        frozen_row_count = self.frozen_row_count

        hide_gridlines = self.hide_gridlines

        row_count = self.row_count

        row_group_control_after = self.row_group_control_after


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_count is not UNSET:
            field_dict["columnCount"] = column_count
        if column_group_control_after is not UNSET:
            field_dict["columnGroupControlAfter"] = column_group_control_after
        if frozen_column_count is not UNSET:
            field_dict["frozenColumnCount"] = frozen_column_count
        if frozen_row_count is not UNSET:
            field_dict["frozenRowCount"] = frozen_row_count
        if hide_gridlines is not UNSET:
            field_dict["hideGridlines"] = hide_gridlines
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if row_group_control_after is not UNSET:
            field_dict["rowGroupControlAfter"] = row_group_control_after

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_count = d.pop("columnCount", UNSET)

        column_group_control_after = d.pop("columnGroupControlAfter", UNSET)

        frozen_column_count = d.pop("frozenColumnCount", UNSET)

        frozen_row_count = d.pop("frozenRowCount", UNSET)

        hide_gridlines = d.pop("hideGridlines", UNSET)

        row_count = d.pop("rowCount", UNSET)

        row_group_control_after = d.pop("rowGroupControlAfter", UNSET)

        grid_properties = cls(
            column_count=column_count,
            column_group_control_after=column_group_control_after,
            frozen_column_count=frozen_column_count,
            frozen_row_count=frozen_row_count,
            hide_gridlines=hide_gridlines,
            row_count=row_count,
            row_group_control_after=row_group_control_after,
        )


        grid_properties.additional_properties = d
        return grid_properties

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
