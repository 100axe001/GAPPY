from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location import Location





T = TypeVar("T", bound="PinTableHeaderRowsRequest")



@_attrs_define
class PinTableHeaderRowsRequest:
    """ Updates the number of pinned table header rows in a table.

        Attributes:
            pinned_header_rows_count (int | Unset): The number of table rows to pin, where 0 implies that all rows are
                unpinned.
            table_start_location (Location | Unset): A particular location in the document.
     """

    pinned_header_rows_count: int | Unset = UNSET
    table_start_location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        pinned_header_rows_count = self.pinned_header_rows_count

        table_start_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_start_location, Unset):
            table_start_location = self.table_start_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pinned_header_rows_count is not UNSET:
            field_dict["pinnedHeaderRowsCount"] = pinned_header_rows_count
        if table_start_location is not UNSET:
            field_dict["tableStartLocation"] = table_start_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        d = dict(src_dict)
        pinned_header_rows_count = d.pop("pinnedHeaderRowsCount", UNSET)

        _table_start_location = d.pop("tableStartLocation", UNSET)
        table_start_location: Location | Unset
        if isinstance(_table_start_location,  Unset):
            table_start_location = UNSET
        else:
            table_start_location = Location.from_dict(_table_start_location)




        pin_table_header_rows_request = cls(
            pinned_header_rows_count=pinned_header_rows_count,
            table_start_location=table_start_location,
        )


        pin_table_header_rows_request.additional_properties = d
        return pin_table_header_rows_request

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
