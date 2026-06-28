from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paragraph_style import ParagraphStyle
  from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState





T = TypeVar("T", bound="SuggestedParagraphStyle")



@_attrs_define
class SuggestedParagraphStyle:
    """ A suggested change to a ParagraphStyle.

        Attributes:
            paragraph_style (ParagraphStyle | Unset): Styles that apply to a whole paragraph. Inherited paragraph styles are
                represented as unset fields in this message. A paragraph style's parent depends on where the paragraph style is
                defined: * The ParagraphStyle on a Paragraph inherits from the paragraph's corresponding named style type. * The
                ParagraphStyle on a named style inherits from the normal text named style. * The ParagraphStyle of the normal
                text named style inherits from the default paragraph style in the Docs editor. * The ParagraphStyle on a
                Paragraph element that's contained in a table may inherit its paragraph style from the table style. If the
                paragraph style does not inherit from a parent, unsetting fields will revert the style to a value matching the
                defaults in the Docs editor.
            paragraph_style_suggestion_state (ParagraphStyleSuggestionState | Unset): A mask that indicates which of the
                fields on the base ParagraphStyle have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
     """

    paragraph_style: ParagraphStyle | Unset = UNSET
    paragraph_style_suggestion_state: ParagraphStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState
        paragraph_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style, Unset):
            paragraph_style = self.paragraph_style.to_dict()

        paragraph_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style_suggestion_state, Unset):
            paragraph_style_suggestion_state = self.paragraph_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if paragraph_style is not UNSET:
            field_dict["paragraphStyle"] = paragraph_style
        if paragraph_style_suggestion_state is not UNSET:
            field_dict["paragraphStyleSuggestionState"] = paragraph_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paragraph_style import ParagraphStyle
        from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState
        d = dict(src_dict)
        _paragraph_style = d.pop("paragraphStyle", UNSET)
        paragraph_style: ParagraphStyle | Unset
        if isinstance(_paragraph_style,  Unset):
            paragraph_style = UNSET
        else:
            paragraph_style = ParagraphStyle.from_dict(_paragraph_style)




        _paragraph_style_suggestion_state = d.pop("paragraphStyleSuggestionState", UNSET)
        paragraph_style_suggestion_state: ParagraphStyleSuggestionState | Unset
        if isinstance(_paragraph_style_suggestion_state,  Unset):
            paragraph_style_suggestion_state = UNSET
        else:
            paragraph_style_suggestion_state = ParagraphStyleSuggestionState.from_dict(_paragraph_style_suggestion_state)




        suggested_paragraph_style = cls(
            paragraph_style=paragraph_style,
            paragraph_style_suggestion_state=paragraph_style_suggestion_state,
        )


        suggested_paragraph_style.additional_properties = d
        return suggested_paragraph_style

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
