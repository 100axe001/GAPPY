from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.developer_metadata_location_location_type import DeveloperMetadataLocationLocationType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension_range import DimensionRange





T = TypeVar("T", bound="DeveloperMetadataLocation")



@_attrs_define
class DeveloperMetadataLocation:
    """ A location where metadata may be associated in a spreadsheet.

        Attributes:
            dimension_range (DimensionRange | Unset): A range along a single dimension on a sheet. All indexes are zero-
                based. Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes
                indicate the range is unbounded on that side.
            location_type (DeveloperMetadataLocationLocationType | Unset): The type of location this object represents. This
                field is read-only.
            sheet_id (int | Unset): The ID of the sheet when metadata is associated with an entire sheet.
            spreadsheet (bool | Unset): True when metadata is associated with an entire spreadsheet.
     """

    dimension_range: DimensionRange | Unset = UNSET
    location_type: DeveloperMetadataLocationLocationType | Unset = UNSET
    sheet_id: int | Unset = UNSET
    spreadsheet: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension_range import DimensionRange
        dimension_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension_range, Unset):
            dimension_range = self.dimension_range.to_dict()

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value


        sheet_id = self.sheet_id

        spreadsheet = self.spreadsheet


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension_range is not UNSET:
            field_dict["dimensionRange"] = dimension_range
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id
        if spreadsheet is not UNSET:
            field_dict["spreadsheet"] = spreadsheet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_range import DimensionRange
        d = dict(src_dict)
        _dimension_range = d.pop("dimensionRange", UNSET)
        dimension_range: DimensionRange | Unset
        if isinstance(_dimension_range,  Unset):
            dimension_range = UNSET
        else:
            dimension_range = DimensionRange.from_dict(_dimension_range)




        _location_type = d.pop("locationType", UNSET)
        location_type: DeveloperMetadataLocationLocationType | Unset
        if isinstance(_location_type,  Unset):
            location_type = UNSET
        else:
            location_type = DeveloperMetadataLocationLocationType(_location_type)




        sheet_id = d.pop("sheetId", UNSET)

        spreadsheet = d.pop("spreadsheet", UNSET)

        developer_metadata_location = cls(
            dimension_range=dimension_range,
            location_type=location_type,
            sheet_id=sheet_id,
            spreadsheet=spreadsheet,
        )


        developer_metadata_location.additional_properties = d
        return developer_metadata_location

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
