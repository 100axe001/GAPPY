from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BatchClearValuesByDataFilterResponse")



@_attrs_define
class BatchClearValuesByDataFilterResponse:
    """ The response when clearing a range of values selected with DataFilters in a spreadsheet.

        Attributes:
            cleared_ranges (list[str] | Unset): The ranges that were cleared, in [A1
                notation](/sheets/api/guides/concepts#cell). If the requests are for an unbounded range or a ranger larger than
                the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet's limits.
            spreadsheet_id (str | Unset): The spreadsheet the updates were applied to.
     """

    cleared_ranges: list[str] | Unset = UNSET
    spreadsheet_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cleared_ranges: list[str] | Unset = UNSET
        if not isinstance(self.cleared_ranges, Unset):
            cleared_ranges = self.cleared_ranges



        spreadsheet_id = self.spreadsheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cleared_ranges is not UNSET:
            field_dict["clearedRanges"] = cleared_ranges
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cleared_ranges = cast(list[str], d.pop("clearedRanges", UNSET))


        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        batch_clear_values_by_data_filter_response = cls(
            cleared_ranges=cleared_ranges,
            spreadsheet_id=spreadsheet_id,
        )


        batch_clear_values_by_data_filter_response.additional_properties = d
        return batch_clear_values_by_data_filter_response

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
