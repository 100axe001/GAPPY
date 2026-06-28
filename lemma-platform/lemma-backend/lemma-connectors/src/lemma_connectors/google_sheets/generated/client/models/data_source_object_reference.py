from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_coordinate import GridCoordinate





T = TypeVar("T", bound="DataSourceObjectReference")



@_attrs_define
class DataSourceObjectReference:
    """ Reference to a data source object.

        Attributes:
            chart_id (int | Unset): References to a data source chart.
            data_source_formula_cell (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-based.
            data_source_pivot_table_anchor_cell (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-
                based.
            data_source_table_anchor_cell (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-based.
            sheet_id (str | Unset): References to a DATA_SOURCE sheet.
     """

    chart_id: int | Unset = UNSET
    data_source_formula_cell: GridCoordinate | Unset = UNSET
    data_source_pivot_table_anchor_cell: GridCoordinate | Unset = UNSET
    data_source_table_anchor_cell: GridCoordinate | Unset = UNSET
    sheet_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_coordinate import GridCoordinate
        chart_id = self.chart_id

        data_source_formula_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_formula_cell, Unset):
            data_source_formula_cell = self.data_source_formula_cell.to_dict()

        data_source_pivot_table_anchor_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_pivot_table_anchor_cell, Unset):
            data_source_pivot_table_anchor_cell = self.data_source_pivot_table_anchor_cell.to_dict()

        data_source_table_anchor_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_table_anchor_cell, Unset):
            data_source_table_anchor_cell = self.data_source_table_anchor_cell.to_dict()

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chart_id is not UNSET:
            field_dict["chartId"] = chart_id
        if data_source_formula_cell is not UNSET:
            field_dict["dataSourceFormulaCell"] = data_source_formula_cell
        if data_source_pivot_table_anchor_cell is not UNSET:
            field_dict["dataSourcePivotTableAnchorCell"] = data_source_pivot_table_anchor_cell
        if data_source_table_anchor_cell is not UNSET:
            field_dict["dataSourceTableAnchorCell"] = data_source_table_anchor_cell
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_coordinate import GridCoordinate
        d = dict(src_dict)
        chart_id = d.pop("chartId", UNSET)

        _data_source_formula_cell = d.pop("dataSourceFormulaCell", UNSET)
        data_source_formula_cell: GridCoordinate | Unset
        if isinstance(_data_source_formula_cell,  Unset):
            data_source_formula_cell = UNSET
        else:
            data_source_formula_cell = GridCoordinate.from_dict(_data_source_formula_cell)




        _data_source_pivot_table_anchor_cell = d.pop("dataSourcePivotTableAnchorCell", UNSET)
        data_source_pivot_table_anchor_cell: GridCoordinate | Unset
        if isinstance(_data_source_pivot_table_anchor_cell,  Unset):
            data_source_pivot_table_anchor_cell = UNSET
        else:
            data_source_pivot_table_anchor_cell = GridCoordinate.from_dict(_data_source_pivot_table_anchor_cell)




        _data_source_table_anchor_cell = d.pop("dataSourceTableAnchorCell", UNSET)
        data_source_table_anchor_cell: GridCoordinate | Unset
        if isinstance(_data_source_table_anchor_cell,  Unset):
            data_source_table_anchor_cell = UNSET
        else:
            data_source_table_anchor_cell = GridCoordinate.from_dict(_data_source_table_anchor_cell)




        sheet_id = d.pop("sheetId", UNSET)

        data_source_object_reference = cls(
            chart_id=chart_id,
            data_source_formula_cell=data_source_formula_cell,
            data_source_pivot_table_anchor_cell=data_source_pivot_table_anchor_cell,
            data_source_table_anchor_cell=data_source_table_anchor_cell,
            sheet_id=sheet_id,
        )


        data_source_object_reference.additional_properties = d
        return data_source_object_reference

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
