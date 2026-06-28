from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.crop_properties import CropProperties





T = TypeVar("T", bound="ImageProperties")



@_attrs_define
class ImageProperties:
    """ The properties of an image.

        Attributes:
            angle (float | Unset): The clockwise rotation angle of the image, in radians.
            brightness (float | Unset): The brightness effect of the image. The value should be in the interval [-1.0, 1.0],
                where 0 means no effect.
            content_uri (str | Unset): A URI to the image with a default lifetime of 30 minutes. This URI is tagged with the
                account of the requester. Anyone with the URI effectively accesses the image as the original requester. Access
                to the image may be lost if the document's sharing settings change.
            contrast (float | Unset): The contrast effect of the image. The value should be in the interval [-1.0, 1.0],
                where 0 means no effect.
            crop_properties (CropProperties | Unset): The crop properties of an image. The crop rectangle is represented
                using fractional offsets from the original content's 4 edges. - If the offset is in the interval (0, 1), the
                corresponding edge of crop rectangle is positioned inside of the image's original bounding rectangle. - If the
                offset is negative or greater than 1, the corresponding edge of crop rectangle is positioned outside of the
                image's original bounding rectangle. - If all offsets and rotation angle are 0, the image is not cropped.
            source_uri (str | Unset): The source URI is the URI used to insert the image. The source URI can be empty.
            transparency (float | Unset): The transparency effect of the image. The value should be in the interval [0.0,
                1.0], where 0 means no effect and 1 means transparent.
     """

    angle: float | Unset = UNSET
    brightness: float | Unset = UNSET
    content_uri: str | Unset = UNSET
    contrast: float | Unset = UNSET
    crop_properties: CropProperties | Unset = UNSET
    source_uri: str | Unset = UNSET
    transparency: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.crop_properties import CropProperties
        angle = self.angle

        brightness = self.brightness

        content_uri = self.content_uri

        contrast = self.contrast

        crop_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crop_properties, Unset):
            crop_properties = self.crop_properties.to_dict()

        source_uri = self.source_uri

        transparency = self.transparency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if angle is not UNSET:
            field_dict["angle"] = angle
        if brightness is not UNSET:
            field_dict["brightness"] = brightness
        if content_uri is not UNSET:
            field_dict["contentUri"] = content_uri
        if contrast is not UNSET:
            field_dict["contrast"] = contrast
        if crop_properties is not UNSET:
            field_dict["cropProperties"] = crop_properties
        if source_uri is not UNSET:
            field_dict["sourceUri"] = source_uri
        if transparency is not UNSET:
            field_dict["transparency"] = transparency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crop_properties import CropProperties
        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        brightness = d.pop("brightness", UNSET)

        content_uri = d.pop("contentUri", UNSET)

        contrast = d.pop("contrast", UNSET)

        _crop_properties = d.pop("cropProperties", UNSET)
        crop_properties: CropProperties | Unset
        if isinstance(_crop_properties,  Unset):
            crop_properties = UNSET
        else:
            crop_properties = CropProperties.from_dict(_crop_properties)




        source_uri = d.pop("sourceUri", UNSET)

        transparency = d.pop("transparency", UNSET)

        image_properties = cls(
            angle=angle,
            brightness=brightness,
            content_uri=content_uri,
            contrast=contrast,
            crop_properties=crop_properties,
            source_uri=source_uri,
            transparency=transparency,
        )


        image_properties.additional_properties = d
        return image_properties

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
