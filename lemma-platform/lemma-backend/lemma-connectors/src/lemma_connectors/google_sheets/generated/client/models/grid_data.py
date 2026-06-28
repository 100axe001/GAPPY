from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension_properties import DimensionProperties
  from ..models.row_data import RowData





T = TypeVar("T", bound="GridData")



@_attrs_define
class GridData:
    """ Data in the grid, as well as metadata about the dimensions.

        Attributes:
            column_metadata (list[DimensionProperties] | Unset): Metadata about the requested columns in the grid, starting
                with the column in start_column.
            row_data (list[RowData] | Unset): The data in the grid, one entry per row, starting with the row in startRow.
                The values in RowData will correspond to columns starting at start_column.
            row_metadata (list[DimensionProperties] | Unset): Metadata about the requested rows in the grid, starting with
                the row in start_row.
            start_column (int | Unset): The first column this GridData refers to, zero-based.
            start_row (int | Unset): The first row this GridData refers to, zero-based.
     """

    column_metadata: list[DimensionProperties] | Unset = UNSET
    row_data: list[RowData] | Unset = UNSET
    row_metadata: list[DimensionProperties] | Unset = UNSET
    start_column: int | Unset = UNSET
    start_row: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_properties import DimensionProperties
        from ..models.row_data import RowData
        column_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.column_metadata, Unset):
            column_metadata = []
            for column_metadata_item_data in self.column_metadata:
                column_metadata_item = column_metadata_item_data.to_dict()
                column_metadata.append(column_metadata_item)



        row_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row_data, Unset):
            row_data = []
            for row_data_item_data in self.row_data:
                row_data_item = row_data_item_data.to_dict()
                row_data.append(row_data_item)



        row_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row_metadata, Unset):
            row_metadata = []
            for row_metadata_item_data in self.row_metadata:
                row_metadata_item = row_metadata_item_data.to_dict()
                row_metadata.append(row_metadata_item)



        start_column = self.start_column

        start_row = self.start_row


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_metadata is not UNSET:
            field_dict["columnMetadata"] = column_metadata
        if row_data is not UNSET:
            field_dict["rowData"] = row_data
        if row_metadata is not UNSET:
            field_dict["rowMetadata"] = row_metadata
        if start_column is not UNSET:
            field_dict["startColumn"] = start_column
        if start_row is not UNSET:
            field_dict["startRow"] = start_row

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_properties import DimensionProperties
        from ..models.row_data import RowData
        d = dict(src_dict)
        _column_metadata = d.pop("columnMetadata", UNSET)
        column_metadata: list[DimensionProperties] | Unset = UNSET
        if _column_metadata is not UNSET:
            column_metadata = []
            for column_metadata_item_data in _column_metadata:
                column_metadata_item = DimensionProperties.from_dict(column_metadata_item_data)



                column_metadata.append(column_metadata_item)


        _row_data = d.pop("rowData", UNSET)
        row_data: list[RowData] | Unset = UNSET
        if _row_data is not UNSET:
            row_data = []
            for row_data_item_data in _row_data:
                row_data_item = RowData.from_dict(row_data_item_data)



                row_data.append(row_data_item)


        _row_metadata = d.pop("rowMetadata", UNSET)
        row_metadata: list[DimensionProperties] | Unset = UNSET
        if _row_metadata is not UNSET:
            row_metadata = []
            for row_metadata_item_data in _row_metadata:
                row_metadata_item = DimensionProperties.from_dict(row_metadata_item_data)



                row_metadata.append(row_metadata_item)


        start_column = d.pop("startColumn", UNSET)

        start_row = d.pop("startRow", UNSET)

        grid_data = cls(
            column_metadata=column_metadata,
            row_data=row_data,
            row_metadata=row_metadata,
            start_column=start_column,
            start_row=start_row,
        )


        grid_data.additional_properties = d
        return grid_data

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
