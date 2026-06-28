from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_values_response import UpdateValuesResponse





T = TypeVar("T", bound="AppendValuesResponse")



@_attrs_define
class AppendValuesResponse:
    """ The response when updating a range of values in a spreadsheet.

        Attributes:
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
            table_range (str | Unset): The range (in A1 notation) of the table that values are being appended to (before the
                values were appended). Empty if no table was found.
            updates (UpdateValuesResponse | Unset): The response when updating a range of values in a spreadsheet.
     """

    spreadsheet_id: str | Unset = UNSET
    table_range: str | Unset = UNSET
    updates: UpdateValuesResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_values_response import UpdateValuesResponse
        spreadsheet_id = self.spreadsheet_id

        table_range = self.table_range

        updates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updates, Unset):
            updates = self.updates.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if table_range is not UNSET:
            field_dict["tableRange"] = table_range
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_values_response import UpdateValuesResponse
        d = dict(src_dict)
        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        table_range = d.pop("tableRange", UNSET)

        _updates = d.pop("updates", UNSET)
        updates: UpdateValuesResponse | Unset
        if isinstance(_updates,  Unset):
            updates = UNSET
        else:
            updates = UpdateValuesResponse.from_dict(_updates)




        append_values_response = cls(
            spreadsheet_id=spreadsheet_id,
            table_range=table_range,
            updates=updates,
        )


        append_values_response.additional_properties = d
        return append_values_response

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
