from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.row_data import RowData





T = TypeVar("T", bound="AppendCellsRequest")



@_attrs_define
class AppendCellsRequest:
    """ Adds new cells after the last row with data in a sheet, inserting new rows into the sheet if necessary.

        Attributes:
            fields (str | Unset): The fields of CellData that should be updated. At least one field must be specified. The
                root is the CellData; 'row.values.' should not be specified. A single `"*"` can be used as short-hand for
                listing every field.
            rows (list[RowData] | Unset): The data to append.
            sheet_id (int | Unset): The sheet ID to append the data to.
     """

    fields: str | Unset = UNSET
    rows: list[RowData] | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.row_data import RowData
        fields = self.fields

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if rows is not UNSET:
            field_dict["rows"] = rows
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_data import RowData
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[RowData] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = RowData.from_dict(rows_item_data)



                rows.append(rows_item)


        sheet_id = d.pop("sheetId", UNSET)

        append_cells_request = cls(
            fields=fields,
            rows=rows,
            sheet_id=sheet_id,
        )


        append_cells_request.additional_properties = d
        return append_cells_request

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
