from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.theme_color_pair import ThemeColorPair





T = TypeVar("T", bound="SpreadsheetTheme")



@_attrs_define
class SpreadsheetTheme:
    """ Represents spreadsheet theme

        Attributes:
            primary_font_family (str | Unset): Name of the primary font family.
            theme_colors (list[ThemeColorPair] | Unset): The spreadsheet theme color pairs. To update you must provide all
                theme color pairs.
     """

    primary_font_family: str | Unset = UNSET
    theme_colors: list[ThemeColorPair] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.theme_color_pair import ThemeColorPair
        primary_font_family = self.primary_font_family

        theme_colors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.theme_colors, Unset):
            theme_colors = []
            for theme_colors_item_data in self.theme_colors:
                theme_colors_item = theme_colors_item_data.to_dict()
                theme_colors.append(theme_colors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if primary_font_family is not UNSET:
            field_dict["primaryFontFamily"] = primary_font_family
        if theme_colors is not UNSET:
            field_dict["themeColors"] = theme_colors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_color_pair import ThemeColorPair
        d = dict(src_dict)
        primary_font_family = d.pop("primaryFontFamily", UNSET)

        _theme_colors = d.pop("themeColors", UNSET)
        theme_colors: list[ThemeColorPair] | Unset = UNSET
        if _theme_colors is not UNSET:
            theme_colors = []
            for theme_colors_item_data in _theme_colors:
                theme_colors_item = ThemeColorPair.from_dict(theme_colors_item_data)



                theme_colors.append(theme_colors_item)


        spreadsheet_theme = cls(
            primary_font_family=primary_font_family,
            theme_colors=theme_colors,
        )


        spreadsheet_theme.additional_properties = d
        return spreadsheet_theme

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
