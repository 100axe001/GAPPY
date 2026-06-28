from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cell_data import CellData
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="RepeatCellRequest")



@_attrs_define
class RepeatCellRequest:
    """ Updates all cells in the range to the values in the given Cell object. Only the fields listed in the fields field
    are updated; others are unchanged. If writing a cell with a formula, the formula's ranges will automatically
    increment for each field in the range. For example, if writing a cell with formula `=A1` into range B2:C4, B2 would
    be `=A1`, B3 would be `=A2`, B4 would be `=A3`, C2 would be `=B1`, C3 would be `=B2`, C4 would be `=B3`. To keep the
    formula's ranges static, use the `$` indicator. For example, use the formula `=$A$1` to prevent both the row and the
    column from incrementing.

        Attributes:
            cell (CellData | Unset): Data about a specific cell.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root `cell`
                is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.
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

    cell: CellData | Unset = UNSET
    fields: str | Unset = UNSET
    range_: GridRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cell_data import CellData
        from ..models.grid_range import GridRange
        cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cell, Unset):
            cell = self.cell.to_dict()

        fields = self.fields

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cell is not UNSET:
            field_dict["cell"] = cell
        if fields is not UNSET:
            field_dict["fields"] = fields
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_data import CellData
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _cell = d.pop("cell", UNSET)
        cell: CellData | Unset
        if isinstance(_cell,  Unset):
            cell = UNSET
        else:
            cell = CellData.from_dict(_cell)




        fields = d.pop("fields", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        repeat_cell_request = cls(
            cell=cell,
            fields=fields,
            range_=range_,
        )


        repeat_cell_request.additional_properties = d
        return repeat_cell_request

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
