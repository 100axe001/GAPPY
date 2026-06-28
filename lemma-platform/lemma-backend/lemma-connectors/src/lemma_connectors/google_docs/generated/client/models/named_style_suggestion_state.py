from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.named_style_suggestion_state_named_style_type import NamedStyleSuggestionStateNamedStyleType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState
  from ..models.text_style_suggestion_state import TextStyleSuggestionState





T = TypeVar("T", bound="NamedStyleSuggestionState")



@_attrs_define
class NamedStyleSuggestionState:
    """ A suggestion state of a NamedStyle message.

        Attributes:
            named_style_type (NamedStyleSuggestionStateNamedStyleType | Unset): The named style type that this suggestion
                state corresponds to. This field is provided as a convenience for matching the NamedStyleSuggestionState with
                its corresponding NamedStyle.
            paragraph_style_suggestion_state (ParagraphStyleSuggestionState | Unset): A mask that indicates which of the
                fields on the base ParagraphStyle have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
            text_style_suggestion_state (TextStyleSuggestionState | Unset): A mask that indicates which of the fields on the
                base TextStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
     """

    named_style_type: NamedStyleSuggestionStateNamedStyleType | Unset = UNSET
    paragraph_style_suggestion_state: ParagraphStyleSuggestionState | Unset = UNSET
    text_style_suggestion_state: TextStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        named_style_type: str | Unset = UNSET
        if not isinstance(self.named_style_type, Unset):
            named_style_type = self.named_style_type.value


        paragraph_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style_suggestion_state, Unset):
            paragraph_style_suggestion_state = self.paragraph_style_suggestion_state.to_dict()

        text_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style_suggestion_state, Unset):
            text_style_suggestion_state = self.text_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if named_style_type is not UNSET:
            field_dict["namedStyleType"] = named_style_type
        if paragraph_style_suggestion_state is not UNSET:
            field_dict["paragraphStyleSuggestionState"] = paragraph_style_suggestion_state
        if text_style_suggestion_state is not UNSET:
            field_dict["textStyleSuggestionState"] = text_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paragraph_style_suggestion_state import ParagraphStyleSuggestionState
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        d = dict(src_dict)
        _named_style_type = d.pop("namedStyleType", UNSET)
        named_style_type: NamedStyleSuggestionStateNamedStyleType | Unset
        if isinstance(_named_style_type,  Unset):
            named_style_type = UNSET
        else:
            named_style_type = NamedStyleSuggestionStateNamedStyleType(_named_style_type)




        _paragraph_style_suggestion_state = d.pop("paragraphStyleSuggestionState", UNSET)
        paragraph_style_suggestion_state: ParagraphStyleSuggestionState | Unset
        if isinstance(_paragraph_style_suggestion_state,  Unset):
            paragraph_style_suggestion_state = UNSET
        else:
            paragraph_style_suggestion_state = ParagraphStyleSuggestionState.from_dict(_paragraph_style_suggestion_state)




        _text_style_suggestion_state = d.pop("textStyleSuggestionState", UNSET)
        text_style_suggestion_state: TextStyleSuggestionState | Unset
        if isinstance(_text_style_suggestion_state,  Unset):
            text_style_suggestion_state = UNSET
        else:
            text_style_suggestion_state = TextStyleSuggestionState.from_dict(_text_style_suggestion_state)




        named_style_suggestion_state = cls(
            named_style_type=named_style_type,
            paragraph_style_suggestion_state=paragraph_style_suggestion_state,
            text_style_suggestion_state=text_style_suggestion_state,
        )


        named_style_suggestion_state.additional_properties = d
        return named_style_suggestion_state

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
