from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_values_by_data_filter_response import UpdateValuesByDataFilterResponse





T = TypeVar("T", bound="BatchUpdateValuesByDataFilterResponse")



@_attrs_define
class BatchUpdateValuesByDataFilterResponse:
    """ The response when updating a range of values in a spreadsheet.

        Attributes:
            responses (list[UpdateValuesByDataFilterResponse] | Unset): The response for each range updated.
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
            total_updated_cells (int | Unset): The total number of cells updated.
            total_updated_columns (int | Unset): The total number of columns where at least one cell in the column was
                updated.
            total_updated_rows (int | Unset): The total number of rows where at least one cell in the row was updated.
            total_updated_sheets (int | Unset): The total number of sheets where at least one cell in the sheet was updated.
     """

    responses: list[UpdateValuesByDataFilterResponse] | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    total_updated_cells: int | Unset = UNSET
    total_updated_columns: int | Unset = UNSET
    total_updated_rows: int | Unset = UNSET
    total_updated_sheets: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_values_by_data_filter_response import UpdateValuesByDataFilterResponse
        responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)



        spreadsheet_id = self.spreadsheet_id

        total_updated_cells = self.total_updated_cells

        total_updated_columns = self.total_updated_columns

        total_updated_rows = self.total_updated_rows

        total_updated_sheets = self.total_updated_sheets


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if responses is not UNSET:
            field_dict["responses"] = responses
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if total_updated_cells is not UNSET:
            field_dict["totalUpdatedCells"] = total_updated_cells
        if total_updated_columns is not UNSET:
            field_dict["totalUpdatedColumns"] = total_updated_columns
        if total_updated_rows is not UNSET:
            field_dict["totalUpdatedRows"] = total_updated_rows
        if total_updated_sheets is not UNSET:
            field_dict["totalUpdatedSheets"] = total_updated_sheets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_values_by_data_filter_response import UpdateValuesByDataFilterResponse
        d = dict(src_dict)
        _responses = d.pop("responses", UNSET)
        responses: list[UpdateValuesByDataFilterResponse] | Unset = UNSET
        if _responses is not UNSET:
            responses = []
            for responses_item_data in _responses:
                responses_item = UpdateValuesByDataFilterResponse.from_dict(responses_item_data)



                responses.append(responses_item)


        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        total_updated_cells = d.pop("totalUpdatedCells", UNSET)

        total_updated_columns = d.pop("totalUpdatedColumns", UNSET)

        total_updated_rows = d.pop("totalUpdatedRows", UNSET)

        total_updated_sheets = d.pop("totalUpdatedSheets", UNSET)

        batch_update_values_by_data_filter_response = cls(
            responses=responses,
            spreadsheet_id=spreadsheet_id,
            total_updated_cells=total_updated_cells,
            total_updated_columns=total_updated_columns,
            total_updated_rows=total_updated_rows,
            total_updated_sheets=total_updated_sheets,
        )


        batch_update_values_by_data_filter_response.additional_properties = d
        return batch_update_values_by_data_filter_response

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
