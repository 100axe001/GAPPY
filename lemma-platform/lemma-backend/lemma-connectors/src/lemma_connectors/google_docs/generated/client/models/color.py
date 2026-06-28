from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rgb_color import RgbColor





T = TypeVar("T", bound="Color")



@_attrs_define
class Color:
    """ A solid color.

        Attributes:
            rgb_color (RgbColor | Unset): An RGB color.
     """

    rgb_color: RgbColor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rgb_color import RgbColor
        rgb_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rgb_color, Unset):
            rgb_color = self.rgb_color.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rgb_color is not UNSET:
            field_dict["rgbColor"] = rgb_color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rgb_color import RgbColor
        d = dict(src_dict)
        _rgb_color = d.pop("rgbColor", UNSET)
        rgb_color: RgbColor | Unset
        if isinstance(_rgb_color,  Unset):
            rgb_color = UNSET
        else:
            rgb_color = RgbColor.from_dict(_rgb_color)




        color = cls(
            rgb_color=rgb_color,
        )


        color.additional_properties = d
        return color

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
