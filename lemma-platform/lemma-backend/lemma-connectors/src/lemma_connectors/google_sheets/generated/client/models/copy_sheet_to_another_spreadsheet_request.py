from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CopySheetToAnotherSpreadsheetRequest")



@_attrs_define
class CopySheetToAnotherSpreadsheetRequest:
    """ The request to copy a sheet across spreadsheets.

        Attributes:
            destination_spreadsheet_id (str | Unset): The ID of the spreadsheet to copy the sheet to.
     """

    destination_spreadsheet_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        destination_spreadsheet_id = self.destination_spreadsheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if destination_spreadsheet_id is not UNSET:
            field_dict["destinationSpreadsheetId"] = destination_spreadsheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_spreadsheet_id = d.pop("destinationSpreadsheetId", UNSET)

        copy_sheet_to_another_spreadsheet_request = cls(
            destination_spreadsheet_id=destination_spreadsheet_id,
        )


        copy_sheet_to_another_spreadsheet_request.additional_properties = d
        return copy_sheet_to_another_spreadsheet_request

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
