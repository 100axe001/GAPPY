from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.batch_update_values_request_response_date_time_render_option import BatchUpdateValuesRequestResponseDateTimeRenderOption
from ..models.batch_update_values_request_response_value_render_option import BatchUpdateValuesRequestResponseValueRenderOption
from ..models.batch_update_values_request_value_input_option import BatchUpdateValuesRequestValueInputOption
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.value_range import ValueRange





T = TypeVar("T", bound="BatchUpdateValuesRequest")



@_attrs_define
class BatchUpdateValuesRequest:
    """ The request for updating more than one range of values in a spreadsheet.

        Attributes:
            data (list[ValueRange] | Unset): The new values to apply to the spreadsheet.
            include_values_in_response (bool | Unset): Determines if the update response should include the values of the
                cells that were updated. By default, responses do not include the updated values. The `updatedData` field within
                each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger
                than the range actually written, the response includes all values in the requested range (excluding trailing
                empty rows and columns).
            response_date_time_render_option (BatchUpdateValuesRequestResponseDateTimeRenderOption | Unset): Determines how
                dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option
                is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.
            response_value_render_option (BatchUpdateValuesRequestResponseValueRenderOption | Unset): Determines how values
                in the response should be rendered. The default render option is FORMATTED_VALUE.
            value_input_option (BatchUpdateValuesRequestValueInputOption | Unset): How the input data should be interpreted.
     """

    data: list[ValueRange] | Unset = UNSET
    include_values_in_response: bool | Unset = UNSET
    response_date_time_render_option: BatchUpdateValuesRequestResponseDateTimeRenderOption | Unset = UNSET
    response_value_render_option: BatchUpdateValuesRequestResponseValueRenderOption | Unset = UNSET
    value_input_option: BatchUpdateValuesRequestValueInputOption | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.value_range import ValueRange
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        include_values_in_response = self.include_values_in_response

        response_date_time_render_option: str | Unset = UNSET
        if not isinstance(self.response_date_time_render_option, Unset):
            response_date_time_render_option = self.response_date_time_render_option.value


        response_value_render_option: str | Unset = UNSET
        if not isinstance(self.response_value_render_option, Unset):
            response_value_render_option = self.response_value_render_option.value


        value_input_option: str | Unset = UNSET
        if not isinstance(self.value_input_option, Unset):
            value_input_option = self.value_input_option.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if include_values_in_response is not UNSET:
            field_dict["includeValuesInResponse"] = include_values_in_response
        if response_date_time_render_option is not UNSET:
            field_dict["responseDateTimeRenderOption"] = response_date_time_render_option
        if response_value_render_option is not UNSET:
            field_dict["responseValueRenderOption"] = response_value_render_option
        if value_input_option is not UNSET:
            field_dict["valueInputOption"] = value_input_option

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.value_range import ValueRange
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[ValueRange] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ValueRange.from_dict(data_item_data)



                data.append(data_item)


        include_values_in_response = d.pop("includeValuesInResponse", UNSET)

        _response_date_time_render_option = d.pop("responseDateTimeRenderOption", UNSET)
        response_date_time_render_option: BatchUpdateValuesRequestResponseDateTimeRenderOption | Unset
        if isinstance(_response_date_time_render_option,  Unset):
            response_date_time_render_option = UNSET
        else:
            response_date_time_render_option = BatchUpdateValuesRequestResponseDateTimeRenderOption(_response_date_time_render_option)




        _response_value_render_option = d.pop("responseValueRenderOption", UNSET)
        response_value_render_option: BatchUpdateValuesRequestResponseValueRenderOption | Unset
        if isinstance(_response_value_render_option,  Unset):
            response_value_render_option = UNSET
        else:
            response_value_render_option = BatchUpdateValuesRequestResponseValueRenderOption(_response_value_render_option)




        _value_input_option = d.pop("valueInputOption", UNSET)
        value_input_option: BatchUpdateValuesRequestValueInputOption | Unset
        if isinstance(_value_input_option,  Unset):
            value_input_option = UNSET
        else:
            value_input_option = BatchUpdateValuesRequestValueInputOption(_value_input_option)




        batch_update_values_request = cls(
            data=data,
            include_values_in_response=include_values_in_response,
            response_date_time_render_option=response_date_time_render_option,
            response_value_render_option=response_value_render_option,
            value_input_option=value_input_option,
        )


        batch_update_values_request.additional_properties = d
        return batch_update_values_request

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
