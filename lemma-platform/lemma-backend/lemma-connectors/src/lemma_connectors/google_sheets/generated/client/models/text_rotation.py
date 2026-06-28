from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TextRotation")



@_attrs_define
class TextRotation:
    """ The rotation applied to text in a cell.

        Attributes:
            angle (int | Unset): The angle between the standard orientation and the desired orientation. Measured in
                degrees. Valid values are between -90 and 90. Positive angles are angled upwards, negative are angled downwards.
                Note: For LTR text direction positive angles are in the counterclockwise direction, whereas for RTL they are in
                the clockwise direction
            vertical (bool | Unset): If true, text reads top to bottom, but the orientation of individual characters is
                unchanged. For example: | V | | e | | r | | t | | i | | c | | a | | l |
     """

    angle: int | Unset = UNSET
    vertical: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        angle = self.angle

        vertical = self.vertical


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if angle is not UNSET:
            field_dict["angle"] = angle
        if vertical is not UNSET:
            field_dict["vertical"] = vertical

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        vertical = d.pop("vertical", UNSET)

        text_rotation = cls(
            angle=angle,
            vertical=vertical,
        )


        text_rotation.additional_properties = d
        return text_rotation

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
