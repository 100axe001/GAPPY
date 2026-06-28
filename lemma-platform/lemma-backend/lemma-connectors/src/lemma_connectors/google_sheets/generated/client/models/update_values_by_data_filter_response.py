from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_filter import DataFilter
  from ..models.value_range import ValueRange





T = TypeVar("T", bound="UpdateValuesByDataFilterResponse")



@_attrs_define
class UpdateValuesByDataFilterResponse:
    """ The response when updating a range of values by a data filter in a spreadsheet.

        Attributes:
            data_filter (DataFilter | Unset): Filter that describes what data should be selected or returned from a request.
            updated_cells (int | Unset): The number of cells updated.
            updated_columns (int | Unset): The number of columns where at least one cell in the column was updated.
            updated_data (ValueRange | Unset): Data within a range of the spreadsheet.
            updated_range (str | Unset): The range (in [A1 notation](/sheets/api/guides/concepts#cell)) that updates were
                applied to.
            updated_rows (int | Unset): The number of rows where at least one cell in the row was updated.
     """

    data_filter: DataFilter | Unset = UNSET
    updated_cells: int | Unset = UNSET
    updated_columns: int | Unset = UNSET
    updated_data: ValueRange | Unset = UNSET
    updated_range: str | Unset = UNSET
    updated_rows: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        from ..models.value_range import ValueRange
        data_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_filter, Unset):
            data_filter = self.data_filter.to_dict()

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
        if data_filter is not UNSET:
            field_dict["dataFilter"] = data_filter
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
        from ..models.data_filter import DataFilter
        from ..models.value_range import ValueRange
        d = dict(src_dict)
        _data_filter = d.pop("dataFilter", UNSET)
        data_filter: DataFilter | Unset
        if isinstance(_data_filter,  Unset):
            data_filter = UNSET
        else:
            data_filter = DataFilter.from_dict(_data_filter)




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

        update_values_by_data_filter_response = cls(
            data_filter=data_filter,
            updated_cells=updated_cells,
            updated_columns=updated_columns,
            updated_data=updated_data,
            updated_range=updated_range,
            updated_rows=updated_rows,
        )


        update_values_by_data_filter_response.additional_properties = d
        return update_values_by_data_filter_response

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
