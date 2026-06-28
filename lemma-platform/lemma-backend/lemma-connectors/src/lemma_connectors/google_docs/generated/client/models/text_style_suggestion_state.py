from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TextStyleSuggestionState")



@_attrs_define
class TextStyleSuggestionState:
    """ A mask that indicates which of the fields on the base TextStyle have been changed in this suggestion. For any field
    set to true, there's a new suggested value.

        Attributes:
            background_color_suggested (bool | Unset): Indicates if there was a suggested change to background_color.
            baseline_offset_suggested (bool | Unset): Indicates if there was a suggested change to baseline_offset.
            bold_suggested (bool | Unset): Indicates if there was a suggested change to bold.
            font_size_suggested (bool | Unset): Indicates if there was a suggested change to font_size.
            foreground_color_suggested (bool | Unset): Indicates if there was a suggested change to foreground_color.
            italic_suggested (bool | Unset): Indicates if there was a suggested change to italic.
            link_suggested (bool | Unset): Indicates if there was a suggested change to link.
            small_caps_suggested (bool | Unset): Indicates if there was a suggested change to small_caps.
            strikethrough_suggested (bool | Unset): Indicates if there was a suggested change to strikethrough.
            underline_suggested (bool | Unset): Indicates if there was a suggested change to underline.
            weighted_font_family_suggested (bool | Unset): Indicates if there was a suggested change to
                weighted_font_family.
     """

    background_color_suggested: bool | Unset = UNSET
    baseline_offset_suggested: bool | Unset = UNSET
    bold_suggested: bool | Unset = UNSET
    font_size_suggested: bool | Unset = UNSET
    foreground_color_suggested: bool | Unset = UNSET
    italic_suggested: bool | Unset = UNSET
    link_suggested: bool | Unset = UNSET
    small_caps_suggested: bool | Unset = UNSET
    strikethrough_suggested: bool | Unset = UNSET
    underline_suggested: bool | Unset = UNSET
    weighted_font_family_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        background_color_suggested = self.background_color_suggested

        baseline_offset_suggested = self.baseline_offset_suggested

        bold_suggested = self.bold_suggested

        font_size_suggested = self.font_size_suggested

        foreground_color_suggested = self.foreground_color_suggested

        italic_suggested = self.italic_suggested

        link_suggested = self.link_suggested

        small_caps_suggested = self.small_caps_suggested

        strikethrough_suggested = self.strikethrough_suggested

        underline_suggested = self.underline_suggested

        weighted_font_family_suggested = self.weighted_font_family_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color_suggested is not UNSET:
            field_dict["backgroundColorSuggested"] = background_color_suggested
        if baseline_offset_suggested is not UNSET:
            field_dict["baselineOffsetSuggested"] = baseline_offset_suggested
        if bold_suggested is not UNSET:
            field_dict["boldSuggested"] = bold_suggested
        if font_size_suggested is not UNSET:
            field_dict["fontSizeSuggested"] = font_size_suggested
        if foreground_color_suggested is not UNSET:
            field_dict["foregroundColorSuggested"] = foreground_color_suggested
        if italic_suggested is not UNSET:
            field_dict["italicSuggested"] = italic_suggested
        if link_suggested is not UNSET:
            field_dict["linkSuggested"] = link_suggested
        if small_caps_suggested is not UNSET:
            field_dict["smallCapsSuggested"] = small_caps_suggested
        if strikethrough_suggested is not UNSET:
            field_dict["strikethroughSuggested"] = strikethrough_suggested
        if underline_suggested is not UNSET:
            field_dict["underlineSuggested"] = underline_suggested
        if weighted_font_family_suggested is not UNSET:
            field_dict["weightedFontFamilySuggested"] = weighted_font_family_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background_color_suggested = d.pop("backgroundColorSuggested", UNSET)

        baseline_offset_suggested = d.pop("baselineOffsetSuggested", UNSET)

        bold_suggested = d.pop("boldSuggested", UNSET)

        font_size_suggested = d.pop("fontSizeSuggested", UNSET)

        foreground_color_suggested = d.pop("foregroundColorSuggested", UNSET)

        italic_suggested = d.pop("italicSuggested", UNSET)

        link_suggested = d.pop("linkSuggested", UNSET)

        small_caps_suggested = d.pop("smallCapsSuggested", UNSET)

        strikethrough_suggested = d.pop("strikethroughSuggested", UNSET)

        underline_suggested = d.pop("underlineSuggested", UNSET)

        weighted_font_family_suggested = d.pop("weightedFontFamilySuggested", UNSET)

        text_style_suggestion_state = cls(
            background_color_suggested=background_color_suggested,
            baseline_offset_suggested=baseline_offset_suggested,
            bold_suggested=bold_suggested,
            font_size_suggested=font_size_suggested,
            foreground_color_suggested=foreground_color_suggested,
            italic_suggested=italic_suggested,
            link_suggested=link_suggested,
            small_caps_suggested=small_caps_suggested,
            strikethrough_suggested=strikethrough_suggested,
            underline_suggested=underline_suggested,
            weighted_font_family_suggested=weighted_font_family_suggested,
        )


        text_style_suggestion_state.additional_properties = d
        return text_style_suggestion_state

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
