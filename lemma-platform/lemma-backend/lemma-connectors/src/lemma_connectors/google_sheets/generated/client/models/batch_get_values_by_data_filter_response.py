from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.matched_value_range import MatchedValueRange





T = TypeVar("T", bound="BatchGetValuesByDataFilterResponse")



@_attrs_define
class BatchGetValuesByDataFilterResponse:
    """ The response when retrieving more than one range of values in a spreadsheet selected by DataFilters.

        Attributes:
            spreadsheet_id (str | Unset): The ID of the spreadsheet the data was retrieved from.
            value_ranges (list[MatchedValueRange] | Unset): The requested values with the list of data filters that matched
                them.
     """

    spreadsheet_id: str | Unset = UNSET
    value_ranges: list[MatchedValueRange] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.matched_value_range import MatchedValueRange
        spreadsheet_id = self.spreadsheet_id

        value_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_ranges, Unset):
            value_ranges = []
            for value_ranges_item_data in self.value_ranges:
                value_ranges_item = value_ranges_item_data.to_dict()
                value_ranges.append(value_ranges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spreadsheet_id is not UNSET:
            field_dict["spreadsheetId"] = spreadsheet_id
        if value_ranges is not UNSET:
            field_dict["valueRanges"] = value_ranges

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matched_value_range import MatchedValueRange
        d = dict(src_dict)
        spreadsheet_id = d.pop("spreadsheetId", UNSET)

        _value_ranges = d.pop("valueRanges", UNSET)
        value_ranges: list[MatchedValueRange] | Unset = UNSET
        if _value_ranges is not UNSET:
            value_ranges = []
            for value_ranges_item_data in _value_ranges:
                value_ranges_item = MatchedValueRange.from_dict(value_ranges_item_data)



                value_ranges.append(value_ranges_item)


        batch_get_values_by_data_filter_response = cls(
            spreadsheet_id=spreadsheet_id,
            value_ranges=value_ranges,
        )


        batch_get_values_by_data_filter_response.additional_properties = d
        return batch_get_values_by_data_filter_response

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
