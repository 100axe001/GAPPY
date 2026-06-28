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
  from ..models.grid_range import GridRange
  from ..models.row_data import RowData





T = TypeVar("T", bound="UpdateCellsRequest")



@_attrs_define
class UpdateCellsRequest:
    """ Updates all cells in a range with new data.

        Attributes:
            fields (str | Unset): The fields of CellData that should be updated. At least one field must be specified. The
                root is the CellData; 'row.values.' should not be specified. A single `"*"` can be used as short-hand for
                listing every field.
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
            rows (list[RowData] | Unset): The data to write.
            start (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-based.
     """

    fields: str | Unset = UNSET
    range_: GridRange | Unset = UNSET
    rows: list[RowData] | Unset = UNSET
    start: GridCoordinate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_coordinate import GridCoordinate
        from ..models.grid_range import GridRange
        from ..models.row_data import RowData
        fields = self.fields

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if range_ is not UNSET:
            field_dict["range"] = range_
        if rows is not UNSET:
            field_dict["rows"] = rows
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_coordinate import GridCoordinate
        from ..models.grid_range import GridRange
        from ..models.row_data import RowData
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        _rows = d.pop("rows", UNSET)
        rows: list[RowData] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = RowData.from_dict(rows_item_data)



                rows.append(rows_item)


        _start = d.pop("start", UNSET)
        start: GridCoordinate | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = GridCoordinate.from_dict(_start)




        update_cells_request = cls(
            fields=fields,
            range_=range_,
            rows=rows,
            start=start,
        )


        update_cells_request.additional_properties = d
        return update_cells_request

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
