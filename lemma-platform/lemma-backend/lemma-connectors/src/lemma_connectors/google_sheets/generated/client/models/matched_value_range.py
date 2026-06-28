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





T = TypeVar("T", bound="MatchedValueRange")



@_attrs_define
class MatchedValueRange:
    """ A value range that was matched by one or more data filers.

        Attributes:
            data_filters (list[DataFilter] | Unset): The DataFilters from the request that matched the range of values.
            value_range (ValueRange | Unset): Data within a range of the spreadsheet.
     """

    data_filters: list[DataFilter] | Unset = UNSET
    value_range: ValueRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        from ..models.value_range import ValueRange
        data_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)



        value_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_range, Unset):
            value_range = self.value_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters
        if value_range is not UNSET:
            field_dict["valueRange"] = value_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_filter import DataFilter
        from ..models.value_range import ValueRange
        d = dict(src_dict)
        _data_filters = d.pop("dataFilters", UNSET)
        data_filters: list[DataFilter] | Unset = UNSET
        if _data_filters is not UNSET:
            data_filters = []
            for data_filters_item_data in _data_filters:
                data_filters_item = DataFilter.from_dict(data_filters_item_data)



                data_filters.append(data_filters_item)


        _value_range = d.pop("valueRange", UNSET)
        value_range: ValueRange | Unset
        if isinstance(_value_range,  Unset):
            value_range = UNSET
        else:
            value_range = ValueRange.from_dict(_value_range)




        matched_value_range = cls(
            data_filters=data_filters,
            value_range=value_range,
        )


        matched_value_range.additional_properties = d
        return matched_value_range

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
