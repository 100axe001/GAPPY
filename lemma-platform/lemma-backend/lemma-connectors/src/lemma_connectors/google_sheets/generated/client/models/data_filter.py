from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.developer_metadata_lookup import DeveloperMetadataLookup
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="DataFilter")



@_attrs_define
class DataFilter:
    """ Filter that describes what data should be selected or returned from a request.

        Attributes:
            a_1_range (str | Unset): Selects data that matches the specified A1 range.
            developer_metadata_lookup (DeveloperMetadataLookup | Unset): Selects DeveloperMetadata that matches all of the
                specified fields. For example, if only a metadata ID is specified this considers the DeveloperMetadata with that
                particular unique ID. If a metadata key is specified, this considers all developer metadata with that key. If a
                key, visibility, and location type are all specified, this considers all developer metadata with that key and
                visibility that are associated with a location of that type. In general, this selects all DeveloperMetadata that
                matches the intersection of all the specified fields; any field or combination of fields may be specified.
            grid_range (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
     """

    a_1_range: str | Unset = UNSET
    developer_metadata_lookup: DeveloperMetadataLookup | Unset = UNSET
    grid_range: GridRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata_lookup import DeveloperMetadataLookup
        from ..models.grid_range import GridRange
        a_1_range = self.a_1_range

        developer_metadata_lookup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.developer_metadata_lookup, Unset):
            developer_metadata_lookup = self.developer_metadata_lookup.to_dict()

        grid_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grid_range, Unset):
            grid_range = self.grid_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if a_1_range is not UNSET:
            field_dict["a1Range"] = a_1_range
        if developer_metadata_lookup is not UNSET:
            field_dict["developerMetadataLookup"] = developer_metadata_lookup
        if grid_range is not UNSET:
            field_dict["gridRange"] = grid_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_metadata_lookup import DeveloperMetadataLookup
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        a_1_range = d.pop("a1Range", UNSET)

        _developer_metadata_lookup = d.pop("developerMetadataLookup", UNSET)
        developer_metadata_lookup: DeveloperMetadataLookup | Unset
        if isinstance(_developer_metadata_lookup,  Unset):
            developer_metadata_lookup = UNSET
        else:
            developer_metadata_lookup = DeveloperMetadataLookup.from_dict(_developer_metadata_lookup)




        _grid_range = d.pop("gridRange", UNSET)
        grid_range: GridRange | Unset
        if isinstance(_grid_range,  Unset):
            grid_range = UNSET
        else:
            grid_range = GridRange.from_dict(_grid_range)




        data_filter = cls(
            a_1_range=a_1_range,
            developer_metadata_lookup=developer_metadata_lookup,
            grid_range=grid_range,
        )


        data_filter.additional_properties = d
        return data_filter

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
