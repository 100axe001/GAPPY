from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CropProperties")



@_attrs_define
class CropProperties:
    """ The crop properties of an image. The crop rectangle is represented using fractional offsets from the original
    content's 4 edges. - If the offset is in the interval (0, 1), the corresponding edge of crop rectangle is positioned
    inside of the image's original bounding rectangle. - If the offset is negative or greater than 1, the corresponding
    edge of crop rectangle is positioned outside of the image's original bounding rectangle. - If all offsets and
    rotation angle are 0, the image is not cropped.

        Attributes:
            angle (float | Unset): The clockwise rotation angle of the crop rectangle around its center, in radians.
                Rotation is applied after the offsets.
            offset_bottom (float | Unset): The offset specifies how far inwards the bottom edge of the crop rectangle is
                from the bottom edge of the original content as a fraction of the original content's height.
            offset_left (float | Unset): The offset specifies how far inwards the left edge of the crop rectangle is from
                the left edge of the original content as a fraction of the original content's width.
            offset_right (float | Unset): The offset specifies how far inwards the right edge of the crop rectangle is from
                the right edge of the original content as a fraction of the original content's width.
            offset_top (float | Unset): The offset specifies how far inwards the top edge of the crop rectangle is from the
                top edge of the original content as a fraction of the original content's height.
     """

    angle: float | Unset = UNSET
    offset_bottom: float | Unset = UNSET
    offset_left: float | Unset = UNSET
    offset_right: float | Unset = UNSET
    offset_top: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        angle = self.angle

        offset_bottom = self.offset_bottom

        offset_left = self.offset_left

        offset_right = self.offset_right

        offset_top = self.offset_top


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if angle is not UNSET:
            field_dict["angle"] = angle
        if offset_bottom is not UNSET:
            field_dict["offsetBottom"] = offset_bottom
        if offset_left is not UNSET:
            field_dict["offsetLeft"] = offset_left
        if offset_right is not UNSET:
            field_dict["offsetRight"] = offset_right
        if offset_top is not UNSET:
            field_dict["offsetTop"] = offset_top

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        offset_bottom = d.pop("offsetBottom", UNSET)

        offset_left = d.pop("offsetLeft", UNSET)

        offset_right = d.pop("offsetRight", UNSET)

        offset_top = d.pop("offsetTop", UNSET)

        crop_properties = cls(
            angle=angle,
            offset_bottom=offset_bottom,
            offset_left=offset_left,
            offset_right=offset_right,
            offset_top=offset_top,
        )


        crop_properties.additional_properties = d
        return crop_properties

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
