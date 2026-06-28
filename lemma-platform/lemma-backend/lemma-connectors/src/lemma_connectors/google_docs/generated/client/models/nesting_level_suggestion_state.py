from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.text_style_suggestion_state import TextStyleSuggestionState





T = TypeVar("T", bound="NestingLevelSuggestionState")



@_attrs_define
class NestingLevelSuggestionState:
    """ A mask that indicates which of the fields on the base NestingLevel have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            bullet_alignment_suggested (bool | Unset): Indicates if there was a suggested change to bullet_alignment.
            glyph_format_suggested (bool | Unset): Indicates if there was a suggested change to glyph_format.
            glyph_symbol_suggested (bool | Unset): Indicates if there was a suggested change to glyph_symbol.
            glyph_type_suggested (bool | Unset): Indicates if there was a suggested change to glyph_type.
            indent_first_line_suggested (bool | Unset): Indicates if there was a suggested change to indent_first_line.
            indent_start_suggested (bool | Unset): Indicates if there was a suggested change to indent_start.
            start_number_suggested (bool | Unset): Indicates if there was a suggested change to start_number.
            text_style_suggestion_state (TextStyleSuggestionState | Unset): A mask that indicates which of the fields on the
                base TextStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
     """

    bullet_alignment_suggested: bool | Unset = UNSET
    glyph_format_suggested: bool | Unset = UNSET
    glyph_symbol_suggested: bool | Unset = UNSET
    glyph_type_suggested: bool | Unset = UNSET
    indent_first_line_suggested: bool | Unset = UNSET
    indent_start_suggested: bool | Unset = UNSET
    start_number_suggested: bool | Unset = UNSET
    text_style_suggestion_state: TextStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        bullet_alignment_suggested = self.bullet_alignment_suggested

        glyph_format_suggested = self.glyph_format_suggested

        glyph_symbol_suggested = self.glyph_symbol_suggested

        glyph_type_suggested = self.glyph_type_suggested

        indent_first_line_suggested = self.indent_first_line_suggested

        indent_start_suggested = self.indent_start_suggested

        start_number_suggested = self.start_number_suggested

        text_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style_suggestion_state, Unset):
            text_style_suggestion_state = self.text_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bullet_alignment_suggested is not UNSET:
            field_dict["bulletAlignmentSuggested"] = bullet_alignment_suggested
        if glyph_format_suggested is not UNSET:
            field_dict["glyphFormatSuggested"] = glyph_format_suggested
        if glyph_symbol_suggested is not UNSET:
            field_dict["glyphSymbolSuggested"] = glyph_symbol_suggested
        if glyph_type_suggested is not UNSET:
            field_dict["glyphTypeSuggested"] = glyph_type_suggested
        if indent_first_line_suggested is not UNSET:
            field_dict["indentFirstLineSuggested"] = indent_first_line_suggested
        if indent_start_suggested is not UNSET:
            field_dict["indentStartSuggested"] = indent_start_suggested
        if start_number_suggested is not UNSET:
            field_dict["startNumberSuggested"] = start_number_suggested
        if text_style_suggestion_state is not UNSET:
            field_dict["textStyleSuggestionState"] = text_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        d = dict(src_dict)
        bullet_alignment_suggested = d.pop("bulletAlignmentSuggested", UNSET)

        glyph_format_suggested = d.pop("glyphFormatSuggested", UNSET)

        glyph_symbol_suggested = d.pop("glyphSymbolSuggested", UNSET)

        glyph_type_suggested = d.pop("glyphTypeSuggested", UNSET)

        indent_first_line_suggested = d.pop("indentFirstLineSuggested", UNSET)

        indent_start_suggested = d.pop("indentStartSuggested", UNSET)

        start_number_suggested = d.pop("startNumberSuggested", UNSET)

        _text_style_suggestion_state = d.pop("textStyleSuggestionState", UNSET)
        text_style_suggestion_state: TextStyleSuggestionState | Unset
        if isinstance(_text_style_suggestion_state,  Unset):
            text_style_suggestion_state = UNSET
        else:
            text_style_suggestion_state = TextStyleSuggestionState.from_dict(_text_style_suggestion_state)




        nesting_level_suggestion_state = cls(
            bullet_alignment_suggested=bullet_alignment_suggested,
            glyph_format_suggested=glyph_format_suggested,
            glyph_symbol_suggested=glyph_symbol_suggested,
            glyph_type_suggested=glyph_type_suggested,
            indent_first_line_suggested=indent_first_line_suggested,
            indent_start_suggested=indent_start_suggested,
            start_number_suggested=start_number_suggested,
            text_style_suggestion_state=text_style_suggestion_state,
        )


        nesting_level_suggestion_state.additional_properties = d
        return nesting_level_suggestion_state

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
