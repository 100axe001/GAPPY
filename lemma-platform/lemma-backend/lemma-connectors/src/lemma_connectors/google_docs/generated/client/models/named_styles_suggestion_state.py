from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.named_style_suggestion_state import NamedStyleSuggestionState





T = TypeVar("T", bound="NamedStylesSuggestionState")



@_attrs_define
class NamedStylesSuggestionState:
    """ The suggestion state of a NamedStyles message.

        Attributes:
            styles_suggestion_states (list[NamedStyleSuggestionState] | Unset): A mask that indicates which of the fields on
                the corresponding NamedStyle in styles have been changed in this suggestion. The order of these named style
                suggestion states matches the order of the corresponding named style within the named styles suggestion.
     """

    styles_suggestion_states: list[NamedStyleSuggestionState] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.named_style_suggestion_state import NamedStyleSuggestionState
        styles_suggestion_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.styles_suggestion_states, Unset):
            styles_suggestion_states = []
            for styles_suggestion_states_item_data in self.styles_suggestion_states:
                styles_suggestion_states_item = styles_suggestion_states_item_data.to_dict()
                styles_suggestion_states.append(styles_suggestion_states_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if styles_suggestion_states is not UNSET:
            field_dict["stylesSuggestionStates"] = styles_suggestion_states

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_style_suggestion_state import NamedStyleSuggestionState
        d = dict(src_dict)
        _styles_suggestion_states = d.pop("stylesSuggestionStates", UNSET)
        styles_suggestion_states: list[NamedStyleSuggestionState] | Unset = UNSET
        if _styles_suggestion_states is not UNSET:
            styles_suggestion_states = []
            for styles_suggestion_states_item_data in _styles_suggestion_states:
                styles_suggestion_states_item = NamedStyleSuggestionState.from_dict(styles_suggestion_states_item_data)



                styles_suggestion_states.append(styles_suggestion_states_item)


        named_styles_suggestion_state = cls(
            styles_suggestion_states=styles_suggestion_states,
        )


        named_styles_suggestion_state.additional_properties = d
        return named_styles_suggestion_state

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
