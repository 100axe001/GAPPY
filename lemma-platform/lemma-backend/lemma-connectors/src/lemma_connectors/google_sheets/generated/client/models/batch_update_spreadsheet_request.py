from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.request import Request





T = TypeVar("T", bound="BatchUpdateSpreadsheetRequest")



@_attrs_define
class BatchUpdateSpreadsheetRequest:
    """ The request for updating any aspect of a spreadsheet.

        Attributes:
            include_spreadsheet_in_response (bool | Unset): Determines if the update response should include the spreadsheet
                resource.
            requests (list[Request] | Unset): A list of updates to apply to the spreadsheet. Requests will be applied in the
                order they are specified. If any request is not valid, no requests will be applied.
            response_include_grid_data (bool | Unset): True if grid data should be returned. Meaningful only if
                include_spreadsheet_in_response is 'true'. This parameter is ignored if a field mask was set in the request.
            response_ranges (list[str] | Unset): Limits the ranges included in the response spreadsheet. Meaningful only if
                include_spreadsheet_in_response is 'true'.
     """

    include_spreadsheet_in_response: bool | Unset = UNSET
    requests: list[Request] | Unset = UNSET
    response_include_grid_data: bool | Unset = UNSET
    response_ranges: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.request import Request
        include_spreadsheet_in_response = self.include_spreadsheet_in_response

        requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requests, Unset):
            requests = []
            for requests_item_data in self.requests:
                requests_item = requests_item_data.to_dict()
                requests.append(requests_item)



        response_include_grid_data = self.response_include_grid_data

        response_ranges: list[str] | Unset = UNSET
        if not isinstance(self.response_ranges, Unset):
            response_ranges = self.response_ranges




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if include_spreadsheet_in_response is not UNSET:
            field_dict["includeSpreadsheetInResponse"] = include_spreadsheet_in_response
        if requests is not UNSET:
            field_dict["requests"] = requests
        if response_include_grid_data is not UNSET:
            field_dict["responseIncludeGridData"] = response_include_grid_data
        if response_ranges is not UNSET:
            field_dict["responseRanges"] = response_ranges

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request import Request
        d = dict(src_dict)
        include_spreadsheet_in_response = d.pop("includeSpreadsheetInResponse", UNSET)

        _requests = d.pop("requests", UNSET)
        requests: list[Request] | Unset = UNSET
        if _requests is not UNSET:
            requests = []
            for requests_item_data in _requests:
                requests_item = Request.from_dict(requests_item_data)



                requests.append(requests_item)


        response_include_grid_data = d.pop("responseIncludeGridData", UNSET)

        response_ranges = cast(list[str], d.pop("responseRanges", UNSET))


        batch_update_spreadsheet_request = cls(
            include_spreadsheet_in_response=include_spreadsheet_in_response,
            requests=requests,
            response_include_grid_data=response_include_grid_data,
            response_ranges=response_ranges,
        )


        batch_update_spreadsheet_request.additional_properties = d
        return batch_update_spreadsheet_request

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
