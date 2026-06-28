from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ClearValuesResponse")



@_attrs_define
class ClearValuesResponse:
    """ The response when clearing a range of values in a spreadsheet.

        Attributes:
            cleared_range (str | Unset): The range (in A1 notation) that was cleared. (If the request was for an unbounded
                range or a ranger larger than the bounds of the sheet, this will be the actual range that was cleared, bounded
                to the sheet's limits.)
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
     """

    cleared_range: str | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cleared_range = self.cleared_range

        spreadsheet_id = self.spreadsheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cleared_range is not UNSET:
            field_dict["clearedRange"] = cleared_range
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cleared_range = d.pop("clearedRange", UNSET)

        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        clear_values_response = cls(
            cleared_range=cleared_range,
            spreadsheet_id=spreadsheet_id,
        )


        clear_values_response.additional_properties = d
        return clear_values_response

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
