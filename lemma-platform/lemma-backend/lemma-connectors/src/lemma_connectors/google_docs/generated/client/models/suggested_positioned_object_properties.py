from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.positioned_object_properties import PositionedObjectProperties
  from ..models.positioned_object_properties_suggestion_state import PositionedObjectPropertiesSuggestionState





T = TypeVar("T", bound="SuggestedPositionedObjectProperties")



@_attrs_define
class SuggestedPositionedObjectProperties:
    """ A suggested change to PositionedObjectProperties.

        Attributes:
            positioned_object_properties (PositionedObjectProperties | Unset): Properties of a PositionedObject.
            positioned_object_properties_suggestion_state (PositionedObjectPropertiesSuggestionState | Unset): A mask that
                indicates which of the fields on the base PositionedObjectProperties have been changed in this suggestion. For
                any field set to true, there's a new suggested value.
     """

    positioned_object_properties: PositionedObjectProperties | Unset = UNSET
    positioned_object_properties_suggestion_state: PositionedObjectPropertiesSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.positioned_object_properties import PositionedObjectProperties
        from ..models.positioned_object_properties_suggestion_state import PositionedObjectPropertiesSuggestionState
        positioned_object_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioned_object_properties, Unset):
            positioned_object_properties = self.positioned_object_properties.to_dict()

        positioned_object_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positioned_object_properties_suggestion_state, Unset):
            positioned_object_properties_suggestion_state = self.positioned_object_properties_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if positioned_object_properties is not UNSET:
            field_dict["positionedObjectProperties"] = positioned_object_properties
        if positioned_object_properties_suggestion_state is not UNSET:
            field_dict["positionedObjectPropertiesSuggestionState"] = positioned_object_properties_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.positioned_object_properties import PositionedObjectProperties
        from ..models.positioned_object_properties_suggestion_state import PositionedObjectPropertiesSuggestionState
        d = dict(src_dict)
        _positioned_object_properties = d.pop("positionedObjectProperties", UNSET)
        positioned_object_properties: PositionedObjectProperties | Unset
        if isinstance(_positioned_object_properties,  Unset):
            positioned_object_properties = UNSET
        else:
            positioned_object_properties = PositionedObjectProperties.from_dict(_positioned_object_properties)




        _positioned_object_properties_suggestion_state = d.pop("positionedObjectPropertiesSuggestionState", UNSET)
        positioned_object_properties_suggestion_state: PositionedObjectPropertiesSuggestionState | Unset
        if isinstance(_positioned_object_properties_suggestion_state,  Unset):
            positioned_object_properties_suggestion_state = UNSET
        else:
            positioned_object_properties_suggestion_state = PositionedObjectPropertiesSuggestionState.from_dict(_positioned_object_properties_suggestion_state)




        suggested_positioned_object_properties = cls(
            positioned_object_properties=positioned_object_properties,
            positioned_object_properties_suggestion_state=positioned_object_properties_suggestion_state,
        )


        suggested_positioned_object_properties.additional_properties = d
        return suggested_positioned_object_properties

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
