from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_object_suggestion_state import EmbeddedObjectSuggestionState
  from ..models.positioned_object_positioning_suggestion_state import PositionedObjectPositioningSuggestionState





T = TypeVar("T", bound="PositionedObjectPropertiesSuggestionState")



@_attrs_define
class PositionedObjectPropertiesSuggestionState:
    """ A mask that indicates which of the fields on the base PositionedObjectProperties have been changed in this
    suggestion. For any field set to true, there's a new suggested value.

        Attributes:
            embedded_object_suggestion_state (EmbeddedObjectSuggestionState | Unset): A mask that indicates which of the
                fields on the base EmbeddedObject have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
            positioning_suggestion_state (PositionedObjectPositioningSuggestionState | Unset): A mask that indicates which
                of the fields on the base PositionedObjectPositioning have been changed in this suggestion. For any field set to
                true, there's a new suggested value.
     """

    embedded_object_suggestion_state: EmbeddedObjectSuggestionState | Unset = UNSET
    positioning_suggestion_state: PositionedObjectPositioningSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_object_suggestion_state import EmbeddedObjectSuggestionState
        from ..models.positioned_object_positioning_suggestion_state import PositionedObjectPositioningSuggestionState
        embedded_object_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_object_suggestion_state, Unset):
            embedded_object_suggestion_state = self.embedded_object_suggestion_state.to_dict()

        positioning_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioning_suggestion_state, Unset):
            positioning_suggestion_state = self.positioning_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if embedded_object_suggestion_state is not UNSET:
            field_dict["embeddedObjectSuggestionState"] = embedded_object_suggestion_state
        if positioning_suggestion_state is not UNSET:
            field_dict["positioningSuggestionState"] = positioning_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_object_suggestion_state import EmbeddedObjectSuggestionState
        from ..models.positioned_object_positioning_suggestion_state import PositionedObjectPositioningSuggestionState
        d = dict(src_dict)
        _embedded_object_suggestion_state = d.pop("embeddedObjectSuggestionState", UNSET)
        embedded_object_suggestion_state: EmbeddedObjectSuggestionState | Unset
        if isinstance(_embedded_object_suggestion_state,  Unset):
            embedded_object_suggestion_state = UNSET
        else:
            embedded_object_suggestion_state = EmbeddedObjectSuggestionState.from_dict(_embedded_object_suggestion_state)




        _positioning_suggestion_state = d.pop("positioningSuggestionState", UNSET)
        positioning_suggestion_state: PositionedObjectPositioningSuggestionState | Unset
        if isinstance(_positioning_suggestion_state,  Unset):
            positioning_suggestion_state = UNSET
        else:
            positioning_suggestion_state = PositionedObjectPositioningSuggestionState.from_dict(_positioning_suggestion_state)




        positioned_object_properties_suggestion_state = cls(
            embedded_object_suggestion_state=embedded_object_suggestion_state,
            positioning_suggestion_state=positioning_suggestion_state,
        )


        positioned_object_properties_suggestion_state.additional_properties = d
        return positioned_object_properties_suggestion_state

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
