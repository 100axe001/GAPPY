from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.developer_metadata_visibility import DeveloperMetadataVisibility
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.developer_metadata_location import DeveloperMetadataLocation





T = TypeVar("T", bound="DeveloperMetadata")



@_attrs_define
class DeveloperMetadata:
    """ Developer metadata associated with a location or object in a spreadsheet. Developer metadata may be used to
    associate arbitrary data with various parts of a spreadsheet and will remain associated at those locations as they
    move around and the spreadsheet is edited. For example, if developer metadata is associated with row 5 and another
    row is then subsequently inserted above row 5, that original metadata will still be associated with the row it was
    first associated with (what is now row 6). If the associated object is deleted its metadata is deleted too.

        Attributes:
            location (DeveloperMetadataLocation | Unset): A location where metadata may be associated in a spreadsheet.
            metadata_id (int | Unset): The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified
                when metadata is created, otherwise one will be randomly generated and assigned. Must be positive.
            metadata_key (str | Unset): The metadata key. There may be multiple metadata in a spreadsheet with the same key.
                Developer metadata must always have a key specified.
            metadata_value (str | Unset): Data associated with the metadata's key.
            visibility (DeveloperMetadataVisibility | Unset): The metadata visibility. Developer metadata must always have a
                visibility specified.
     """

    location: DeveloperMetadataLocation | Unset = UNSET
    metadata_id: int | Unset = UNSET
    metadata_key: str | Unset = UNSET
    metadata_value: str | Unset = UNSET
    visibility: DeveloperMetadataVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata_location import DeveloperMetadataLocation
        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        metadata_id = self.metadata_id

        metadata_key = self.metadata_key

        metadata_value = self.metadata_value

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location is not UNSET:
            field_dict["location"] = location
        if metadata_id is not UNSET:
            field_dict["metadataId"] = metadata_id
        if metadata_key is not UNSET:
            field_dict["metadataKey"] = metadata_key
        if metadata_value is not UNSET:
            field_dict["metadataValue"] = metadata_value
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_metadata_location import DeveloperMetadataLocation
        d = dict(src_dict)
        _location = d.pop("location", UNSET)
        location: DeveloperMetadataLocation | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = DeveloperMetadataLocation.from_dict(_location)




        metadata_id = d.pop("metadataId", UNSET)

        metadata_key = d.pop("metadataKey", UNSET)

        metadata_value = d.pop("metadataValue", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: DeveloperMetadataVisibility | Unset
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = DeveloperMetadataVisibility(_visibility)




        developer_metadata = cls(
            location=location,
            metadata_id=metadata_id,
            metadata_key=metadata_key,
            metadata_value=metadata_value,
            visibility=visibility,
        )


        developer_metadata.additional_properties = d
        return developer_metadata

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
