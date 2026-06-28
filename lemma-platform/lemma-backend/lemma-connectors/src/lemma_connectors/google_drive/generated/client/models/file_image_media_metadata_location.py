from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileImageMediaMetadataLocation")



@_attrs_define
class FileImageMediaMetadataLocation:
    """ Geographic location information stored in the image.

        Attributes:
            altitude (float | Unset): The altitude stored in the image.
            latitude (float | Unset): The latitude stored in the image.
            longitude (float | Unset): The longitude stored in the image.
     """

    altitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        altitude = self.altitude

        latitude = self.latitude

        longitude = self.longitude


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        altitude = d.pop("altitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        file_image_media_metadata_location = cls(
            altitude=altitude,
            latitude=latitude,
            longitude=longitude,
        )


        file_image_media_metadata_location.additional_properties = d
        return file_image_media_metadata_location

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
