from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.value_range import ValueRange





T = TypeVar("T", bound="UpdateValuesResponse")



@_attrs_define
class UpdateValuesResponse:
    """ The response when updating a range of values in a spreadsheet.

        Attributes:
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
            updated_cells (int | Unset): The number of cells updated.
            updated_columns (int | Unset): The number of columns where at least one cell in the column was updated.
            updated_data (ValueRange | Unset): Data within a range of the spreadsheet.
            updated_range (str | Unset): The range (in A1 notation) that updates were applied to.
            updated_rows (int | Unset): The number of rows where at least one cell in the row was updated.
     """

    spreadsheet_id: str | Unset = UNSET
    updated_cells: int | Unset = UNSET
    updated_columns: int | Unset = UNSET
    updated_data: ValueRange | Unset = UNSET
    updated_range: str | Unset = UNSET
    updated_rows: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.value_range import ValueRange
        spreadsheet_id = self.spreadsheet_id

        updated_cells = self.updated_cells

        updated_columns = self.updated_columns

        updated_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_data, Unset):
            updated_data = self.updated_data.to_dict()

        updated_range = self.updated_range

        updated_rows = self.updated_rows


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if updated_cells is not UNSET:
            field_dict["updatedCells"] = updated_cells
        if updated_columns is not UNSET:
            field_dict["updatedColumns"] = updated_columns
        if updated_data is not UNSET:
            field_dict["updatedData"] = updated_data
        if updated_range is not UNSET:
            field_dict["updatedRange"] = updated_range
        if updated_rows is not UNSET:
            field_dict["updatedRows"] = updated_rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.value_range import ValueRange
        d = dict(src_dict)
        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        updated_cells = d.pop("updatedCells", UNSET)

        updated_columns = d.pop("updatedColumns", UNSET)

        _updated_data = d.pop("updatedData", UNSET)
        updated_data: ValueRange | Unset
        if isinstance(_updated_data,  Unset):
            updated_data = UNSET
        else:
            updated_data = ValueRange.from_dict(_updated_data)




        updated_range = d.pop("updatedRange", UNSET)

        updated_rows = d.pop("updatedRows", UNSET)

        update_values_response = cls(
            spreadsheet_id=spreadsheet_id,
            updated_cells=updated_cells,
            updated_columns=updated_columns,
            updated_data=updated_data,
            updated_range=updated_range,
            updated_rows=updated_rows,
        )


        update_values_response.additional_properties = d
        return update_values_response

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
