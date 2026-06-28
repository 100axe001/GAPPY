from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.inline_object_properties import InlineObjectProperties
  from ..models.inline_object_properties_suggestion_state import InlineObjectPropertiesSuggestionState





T = TypeVar("T", bound="SuggestedInlineObjectProperties")



@_attrs_define
class SuggestedInlineObjectProperties:
    """ A suggested change to InlineObjectProperties.

        Attributes:
            inline_object_properties (InlineObjectProperties | Unset): Properties of an InlineObject.
            inline_object_properties_suggestion_state (InlineObjectPropertiesSuggestionState | Unset): A mask that indicates
                which of the fields on the base InlineObjectProperties have been changed in this suggestion. For any field set
                to true, there's a new suggested value.
     """

    inline_object_properties: InlineObjectProperties | Unset = UNSET
    inline_object_properties_suggestion_state: InlineObjectPropertiesSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inline_object_properties import InlineObjectProperties
        from ..models.inline_object_properties_suggestion_state import InlineObjectPropertiesSuggestionState
        inline_object_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline_object_properties, Unset):
            inline_object_properties = self.inline_object_properties.to_dict()

        inline_object_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline_object_properties_suggestion_state, Unset):
            inline_object_properties_suggestion_state = self.inline_object_properties_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inline_object_properties is not UNSET:
            field_dict["inlineObjectProperties"] = inline_object_properties
        if inline_object_properties_suggestion_state is not UNSET:
            field_dict["inlineObjectPropertiesSuggestionState"] = inline_object_properties_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inline_object_properties import InlineObjectProperties
        from ..models.inline_object_properties_suggestion_state import InlineObjectPropertiesSuggestionState
        d = dict(src_dict)
        _inline_object_properties = d.pop("inlineObjectProperties", UNSET)
        inline_object_properties: InlineObjectProperties | Unset
        if isinstance(_inline_object_properties,  Unset):
            inline_object_properties = UNSET
        else:
            inline_object_properties = InlineObjectProperties.from_dict(_inline_object_properties)




        _inline_object_properties_suggestion_state = d.pop("inlineObjectPropertiesSuggestionState", UNSET)
        inline_object_properties_suggestion_state: InlineObjectPropertiesSuggestionState | Unset
        if isinstance(_inline_object_properties_suggestion_state,  Unset):
            inline_object_properties_suggestion_state = UNSET
        else:
            inline_object_properties_suggestion_state = InlineObjectPropertiesSuggestionState.from_dict(_inline_object_properties_suggestion_state)




        suggested_inline_object_properties = cls(
            inline_object_properties=inline_object_properties,
            inline_object_properties_suggestion_state=inline_object_properties_suggestion_state,
        )


        suggested_inline_object_properties.additional_properties = d
        return suggested_inline_object_properties

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
