from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.batch_get_values_by_data_filter_request_date_time_render_option import BatchGetValuesByDataFilterRequestDateTimeRenderOption
from ..models.batch_get_values_by_data_filter_request_major_dimension import BatchGetValuesByDataFilterRequestMajorDimension
from ..models.batch_get_values_by_data_filter_request_value_render_option import BatchGetValuesByDataFilterRequestValueRenderOption
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_filter import DataFilter





T = TypeVar("T", bound="BatchGetValuesByDataFilterRequest")



@_attrs_define
class BatchGetValuesByDataFilterRequest:
    """ The request for retrieving a range of values in a spreadsheet selected by a set of DataFilters.

        Attributes:
            data_filters (list[DataFilter] | Unset): The data filters used to match the ranges of values to retrieve. Ranges
                that match any of the specified data filters are included in the response.
            date_time_render_option (BatchGetValuesByDataFilterRequestDateTimeRenderOption | Unset): How dates, times, and
                durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The
                default dateTime render option is SERIAL_NUMBER.
            major_dimension (BatchGetValuesByDataFilterRequestMajorDimension | Unset): The major dimension that results
                should use. For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`, then a request that selects that
                range and sets `majorDimension=ROWS` returns `[[1,2],[3,4]]`, whereas a request that sets
                `majorDimension=COLUMNS` returns `[[1,3],[2,4]]`.
            value_render_option (BatchGetValuesByDataFilterRequestValueRenderOption | Unset): How values should be
                represented in the output. The default render option is FORMATTED_VALUE.
     """

    data_filters: list[DataFilter] | Unset = UNSET
    date_time_render_option: BatchGetValuesByDataFilterRequestDateTimeRenderOption | Unset = UNSET
    major_dimension: BatchGetValuesByDataFilterRequestMajorDimension | Unset = UNSET
    value_render_option: BatchGetValuesByDataFilterRequestValueRenderOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_filter import DataFilter
        data_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)



        date_time_render_option: str | Unset = UNSET
        if not isinstance(self.date_time_render_option, Unset):
            date_time_render_option = self.date_time_render_option.value


        major_dimension: str | Unset = UNSET
        if not isinstance(self.major_dimension, Unset):
            major_dimension = self.major_dimension.value


        value_render_option: str | Unset = UNSET
        if not isinstance(self.value_render_option, Unset):
            value_render_option = self.value_render_option.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters
        if date_time_render_option is not UNSET:
            field_dict["dateTimeRenderOption"] = date_time_render_option
        if major_dimension is not UNSET:
            field_dict["majorDimension"] = major_dimension
        if value_render_option is not UNSET:
            field_dict["valueRenderOption"] = value_render_option

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


        _date_time_render_option = d.pop("dateTimeRenderOption", UNSET)
        date_time_render_option: BatchGetValuesByDataFilterRequestDateTimeRenderOption | Unset
        if isinstance(_date_time_render_option,  Unset):
            date_time_render_option = UNSET
        else:
            date_time_render_option = BatchGetValuesByDataFilterRequestDateTimeRenderOption(_date_time_render_option)




        _major_dimension = d.pop("majorDimension", UNSET)
        major_dimension: BatchGetValuesByDataFilterRequestMajorDimension | Unset
        if isinstance(_major_dimension,  Unset):
            major_dimension = UNSET
        else:
            major_dimension = BatchGetValuesByDataFilterRequestMajorDimension(_major_dimension)




        _value_render_option = d.pop("valueRenderOption", UNSET)
        value_render_option: BatchGetValuesByDataFilterRequestValueRenderOption | Unset
        if isinstance(_value_render_option,  Unset):
            value_render_option = UNSET
        else:
            value_render_option = BatchGetValuesByDataFilterRequestValueRenderOption(_value_render_option)




        batch_get_values_by_data_filter_request = cls(
            data_filters=data_filters,
            date_time_render_option=date_time_render_option,
            major_dimension=major_dimension,
            value_render_option=value_render_option,
        )


        batch_get_values_by_data_filter_request.additional_properties = d
        return batch_get_values_by_data_filter_request

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
