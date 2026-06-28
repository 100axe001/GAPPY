from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ColorDefinition")



@_attrs_define
class ColorDefinition:
    """ 
        Attributes:
            background (str | Unset): The background color associated with this color definition.
            foreground (str | Unset): The foreground color that can be used to write on top of a background with
                'background' color.
     """

    background: str | Unset = UNSET
    foreground: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        background = self.background

        foreground = self.foreground


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background is not UNSET:
            field_dict["background"] = background
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background = d.pop("background", UNSET)

        foreground = d.pop("foreground", UNSET)

        color_definition = cls(
            background=background,
            foreground=foreground,
        )


        color_definition.additional_properties = d
        return color_definition

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
