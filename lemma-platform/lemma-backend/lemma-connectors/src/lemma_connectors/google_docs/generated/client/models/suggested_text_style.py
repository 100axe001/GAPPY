from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.text_style import TextStyle
  from ..models.text_style_suggestion_state import TextStyleSuggestionState





T = TypeVar("T", bound="SuggestedTextStyle")



@_attrs_define
class SuggestedTextStyle:
    """ A suggested change to a TextStyle.

        Attributes:
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
            text_style_suggestion_state (TextStyleSuggestionState | Unset): A mask that indicates which of the fields on the
                base TextStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
     """

    text_style: TextStyle | Unset = UNSET
    text_style_suggestion_state: TextStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_style import TextStyle
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()

        text_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style_suggestion_state, Unset):
            text_style_suggestion_state = self.text_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style
        if text_style_suggestion_state is not UNSET:
            field_dict["textStyleSuggestionState"] = text_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_style import TextStyle
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        d = dict(src_dict)
        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        _text_style_suggestion_state = d.pop("textStyleSuggestionState", UNSET)
        text_style_suggestion_state: TextStyleSuggestionState | Unset
        if isinstance(_text_style_suggestion_state,  Unset):
            text_style_suggestion_state = UNSET
        else:
            text_style_suggestion_state = TextStyleSuggestionState.from_dict(_text_style_suggestion_state)




        suggested_text_style = cls(
            text_style=text_style,
            text_style_suggestion_state=text_style_suggestion_state,
        )


        suggested_text_style.additional_properties = d
        return suggested_text_style

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
