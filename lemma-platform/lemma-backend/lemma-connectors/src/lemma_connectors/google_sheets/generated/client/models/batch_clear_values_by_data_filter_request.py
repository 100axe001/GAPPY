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





T = TypeVar("T", bound="BatchClearValuesByDataFilterRequest")



@_attrs_define
class BatchClearValuesByDataFilterRequest:
    """ The request for clearing more than one range selected by a DataFilter in a spreadsheet.

        Attributes:
            data_filters (list[DataFilter] | Unset): The DataFilters used to determine which ranges to clear.
     """

    data_filters: list[DataFilter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        data_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_filter import DataFilter
        d = dict(src_dict)
        _data_filters = d.pop("dataFilters", UNSET)
        data_filters: list[DataFilter] | Unset = UNSET
        if _data_filters is not UNSET:
            data_filters = []
            for data_filters_item_data in _data_filters:
                data_filters_item = DataFilter.from_dict(data_filters_item_data)



                data_filters.append(data_filters_item)


        batch_clear_values_by_data_filter_request = cls(
            data_filters=data_filters,
        )


        batch_clear_values_by_data_filter_request.additional_properties = d
        return batch_clear_values_by_data_filter_request

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
