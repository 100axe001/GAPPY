from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DriveBackgroundImageFile")



@_attrs_define
class DriveBackgroundImageFile:
    """ An image file and cropping parameters from which a background image for this shared drive is set. This is a write-
    only field; it can only be set on drive.drives.update requests that don't set themeId. When specified, all fields of
    the backgroundImageFile must be set.

        Attributes:
            id (str | Unset): The ID of an image file in Google Drive to use for the background image.
            width (float | Unset): The width of the cropped image in the closed range of 0 to 1. This value represents the
                width of the cropped image divided by the width of the entire image. The height is computed by applying a width
                to height aspect ratio of 80 to 9. The resulting image must be at least 1280 pixels wide and 144 pixels high.
            x_coordinate (float | Unset): The X coordinate of the upper left corner of the cropping area in the background
                image. This is a value in the closed range of 0 to 1. This value represents the horizontal distance from the
                left side of the entire image to the left side of the cropping area divided by the width of the entire image.
            y_coordinate (float | Unset): The Y coordinate of the upper left corner of the cropping area in the background
                image. This is a value in the closed range of 0 to 1. This value represents the vertical distance from the top
                side of the entire image to the top side of the cropping area divided by the height of the entire image.
     """

    id: str | Unset = UNSET
    width: float | Unset = UNSET
    x_coordinate: float | Unset = UNSET
    y_coordinate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        width = self.width

        x_coordinate = self.x_coordinate

        y_coordinate = self.y_coordinate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if width is not UNSET:
            field_dict["width"] = width
        if x_coordinate is not UNSET:
            field_dict["xCoordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["yCoordinate"] = y_coordinate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        width = d.pop("width", UNSET)

        x_coordinate = d.pop("xCoordinate", UNSET)

        y_coordinate = d.pop("yCoordinate", UNSET)

        drive_background_image_file = cls(
            id=id,
            width=width,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
        )


        drive_background_image_file.additional_properties = d
        return drive_background_image_file

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
