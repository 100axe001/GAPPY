from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.theme_color_pair_color_type import ThemeColorPairColorType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color_style import ColorStyle





T = TypeVar("T", bound="ThemeColorPair")



@_attrs_define
class ThemeColorPair:
    """ A pair mapping a spreadsheet theme color type to the concrete color it represents.

        Attributes:
            color (ColorStyle | Unset): A color value.
            color_type (ThemeColorPairColorType | Unset): The type of the spreadsheet theme color.
     """

    color: ColorStyle | Unset = UNSET
    color_type: ThemeColorPairColorType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color_style import ColorStyle
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        color_type: str | Unset = UNSET
        if not isinstance(self.color_type, Unset):
            color_type = self.color_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if color_type is not UNSET:
            field_dict["colorType"] = color_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_style import ColorStyle
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: ColorStyle | Unset
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = ColorStyle.from_dict(_color)




        _color_type = d.pop("colorType", UNSET)
        color_type: ThemeColorPairColorType | Unset
        if isinstance(_color_type,  Unset):
            color_type = UNSET
        else:
            color_type = ThemeColorPairColorType(_color_type)




        theme_color_pair = cls(
            color=color,
            color_type=color_type,
        )


        theme_color_pair.additional_properties = d
        return theme_color_pair

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
