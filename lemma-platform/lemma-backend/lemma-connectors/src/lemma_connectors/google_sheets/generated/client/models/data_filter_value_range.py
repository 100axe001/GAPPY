from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_filter_value_range_major_dimension import DataFilterValueRangeMajorDimension
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_filter import DataFilter





T = TypeVar("T", bound="DataFilterValueRange")



@_attrs_define
class DataFilterValueRange:
    """ A range of values whose location is specified by a DataFilter.

        Attributes:
            data_filter (DataFilter | Unset): Filter that describes what data should be selected or returned from a request.
            major_dimension (DataFilterValueRangeMajorDimension | Unset): The major dimension of the values.
            values (list[list[Any]] | Unset): The data to be written. If the provided values exceed any of the ranges
                matched by the data filter then the request fails. If the provided values are less than the matched ranges only
                the specified values are written, existing values in the matched ranges remain unaffected.
     """

    data_filter: DataFilter | Unset = UNSET
    major_dimension: DataFilterValueRangeMajorDimension | Unset = UNSET
    values: list[list[Any]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        data_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_filter, Unset):
            data_filter = self.data_filter.to_dict()

        major_dimension: str | Unset = UNSET
        if not isinstance(self.major_dimension, Unset):
            major_dimension = self.major_dimension.value


        values: list[list[Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data


                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filter is not UNSET:
            field_dict["dataFilter"] = data_filter
        if major_dimension is not UNSET:
            field_dict["majorDimension"] = major_dimension
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_filter import DataFilter
        d = dict(src_dict)
        _data_filter = d.pop("dataFilter", UNSET)
        data_filter: DataFilter | Unset
        if isinstance(_data_filter,  Unset):
            data_filter = UNSET
        else:
            data_filter = DataFilter.from_dict(_data_filter)




        _major_dimension = d.pop("majorDimension", UNSET)
        major_dimension: DataFilterValueRangeMajorDimension | Unset
        if isinstance(_major_dimension,  Unset):
            major_dimension = UNSET
        else:
            major_dimension = DataFilterValueRangeMajorDimension(_major_dimension)




        _values = d.pop("values", UNSET)
        values: list[list[Any]] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = cast(list[Any], values_item_data)

                values.append(values_item)


        data_filter_value_range = cls(
            data_filter=data_filter,
            major_dimension=major_dimension,
            values=values,
        )


        data_filter_value_range.additional_properties = d
        return data_filter_value_range

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
