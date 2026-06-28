from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.developer_metadata_lookup_location_matching_strategy import DeveloperMetadataLookupLocationMatchingStrategy
from ..models.developer_metadata_lookup_location_type import DeveloperMetadataLookupLocationType
from ..models.developer_metadata_lookup_visibility import DeveloperMetadataLookupVisibility
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.developer_metadata_location import DeveloperMetadataLocation





T = TypeVar("T", bound="DeveloperMetadataLookup")



@_attrs_define
class DeveloperMetadataLookup:
    """ Selects DeveloperMetadata that matches all of the specified fields. For example, if only a metadata ID is specified
    this considers the DeveloperMetadata with that particular unique ID. If a metadata key is specified, this considers
    all developer metadata with that key. If a key, visibility, and location type are all specified, this considers all
    developer metadata with that key and visibility that are associated with a location of that type. In general, this
    selects all DeveloperMetadata that matches the intersection of all the specified fields; any field or combination of
    fields may be specified.

        Attributes:
            location_matching_strategy (DeveloperMetadataLookupLocationMatchingStrategy | Unset): Determines how this lookup
                matches the location. If this field is specified as EXACT, only developer metadata associated on the exact
                location specified is matched. If this field is specified to INTERSECTING, developer metadata associated on
                intersecting locations is also matched. If left unspecified, this field assumes a default value of INTERSECTING.
                If this field is specified, a metadataLocation must also be specified.
            location_type (DeveloperMetadataLookupLocationType | Unset): Limits the selected developer metadata to those
                entries which are associated with locations of the specified type. For example, when this field is specified as
                ROW this lookup only considers developer metadata associated on rows. If the field is left unspecified, all
                location types are considered. This field cannot be specified as SPREADSHEET when the locationMatchingStrategy
                is specified as INTERSECTING or when the metadataLocation is specified as a non-spreadsheet location:
                spreadsheet metadata cannot intersect any other developer metadata location. This field also must be left
                unspecified when the locationMatchingStrategy is specified as EXACT.
            metadata_id (int | Unset): Limits the selected developer metadata to that which has a matching
                DeveloperMetadata.metadata_id.
            metadata_key (str | Unset): Limits the selected developer metadata to that which has a matching
                DeveloperMetadata.metadata_key.
            metadata_location (DeveloperMetadataLocation | Unset): A location where metadata may be associated in a
                spreadsheet.
            metadata_value (str | Unset): Limits the selected developer metadata to that which has a matching
                DeveloperMetadata.metadata_value.
            visibility (DeveloperMetadataLookupVisibility | Unset): Limits the selected developer metadata to that which has
                a matching DeveloperMetadata.visibility. If left unspecified, all developer metadata visibile to the requesting
                project is considered.
     """

    location_matching_strategy: DeveloperMetadataLookupLocationMatchingStrategy | Unset = UNSET
    location_type: DeveloperMetadataLookupLocationType | Unset = UNSET
    metadata_id: int | Unset = UNSET
    metadata_key: str | Unset = UNSET
    metadata_location: DeveloperMetadataLocation | Unset = UNSET
    metadata_value: str | Unset = UNSET
    visibility: DeveloperMetadataLookupVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.developer_metadata_location import DeveloperMetadataLocation
        location_matching_strategy: str | Unset = UNSET
        if not isinstance(self.location_matching_strategy, Unset):
            location_matching_strategy = self.location_matching_strategy.value


        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value


        metadata_id = self.metadata_id

        metadata_key = self.metadata_key

        metadata_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_location, Unset):
            metadata_location = self.metadata_location.to_dict()

        metadata_value = self.metadata_value

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if location_matching_strategy is not UNSET:
            field_dict["locationMatchingStrategy"] = location_matching_strategy
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if metadata_id is not UNSET:
            field_dict["metadataId"] = metadata_id
        if metadata_key is not UNSET:
            field_dict["metadataKey"] = metadata_key
        if metadata_location is not UNSET:
            field_dict["metadataLocation"] = metadata_location
        if metadata_value is not UNSET:
            field_dict["metadataValue"] = metadata_value
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_metadata_location import DeveloperMetadataLocation
        d = dict(src_dict)
        _location_matching_strategy = d.pop("locationMatchingStrategy", UNSET)
        location_matching_strategy: DeveloperMetadataLookupLocationMatchingStrategy | Unset
        if isinstance(_location_matching_strategy,  Unset):
            location_matching_strategy = UNSET
        else:
            location_matching_strategy = DeveloperMetadataLookupLocationMatchingStrategy(_location_matching_strategy)




        _location_type = d.pop("locationType", UNSET)
        location_type: DeveloperMetadataLookupLocationType | Unset
        if isinstance(_location_type,  Unset):
            location_type = UNSET
        else:
            location_type = DeveloperMetadataLookupLocationType(_location_type)




        metadata_id = d.pop("metadataId", UNSET)

        metadata_key = d.pop("metadataKey", UNSET)

        _metadata_location = d.pop("metadataLocation", UNSET)
        metadata_location: DeveloperMetadataLocation | Unset
        if isinstance(_metadata_location,  Unset):
            metadata_location = UNSET
        else:
            metadata_location = DeveloperMetadataLocation.from_dict(_metadata_location)




        metadata_value = d.pop("metadataValue", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: DeveloperMetadataLookupVisibility | Unset
        if isinstance(_visibility,  Unset):
            visibility = UNSET
        else:
            visibility = DeveloperMetadataLookupVisibility(_visibility)




        developer_metadata_lookup = cls(
            location_matching_strategy=location_matching_strategy,
            location_type=location_type,
            metadata_id=metadata_id,
            metadata_key=metadata_key,
            metadata_location=metadata_location,
            metadata_value=metadata_value,
            visibility=visibility,
        )


        developer_metadata_lookup.additional_properties = d
        return developer_metadata_lookup

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
