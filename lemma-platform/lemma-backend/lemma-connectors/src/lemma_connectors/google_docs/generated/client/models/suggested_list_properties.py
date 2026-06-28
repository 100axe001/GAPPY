from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_properties import ListProperties
  from ..models.list_properties_suggestion_state import ListPropertiesSuggestionState





T = TypeVar("T", bound="SuggestedListProperties")



@_attrs_define
class SuggestedListProperties:
    """ A suggested change to ListProperties.

        Attributes:
            list_properties (ListProperties | Unset): The properties of a list that describe the look and feel of bullets
                belonging to paragraphs associated with a list.
            list_properties_suggestion_state (ListPropertiesSuggestionState | Unset): A mask that indicates which of the
                fields on the base ListProperties have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
     """

    list_properties: ListProperties | Unset = UNSET
    list_properties_suggestion_state: ListPropertiesSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_properties import ListProperties
        from ..models.list_properties_suggestion_state import ListPropertiesSuggestionState
        list_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_properties, Unset):
            list_properties = self.list_properties.to_dict()

        list_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_properties_suggestion_state, Unset):
            list_properties_suggestion_state = self.list_properties_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if list_properties is not UNSET:
            field_dict["listProperties"] = list_properties
        if list_properties_suggestion_state is not UNSET:
            field_dict["listPropertiesSuggestionState"] = list_properties_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_properties import ListProperties
        from ..models.list_properties_suggestion_state import ListPropertiesSuggestionState
        d = dict(src_dict)
        _list_properties = d.pop("listProperties", UNSET)
        list_properties: ListProperties | Unset
        if isinstance(_list_properties,  Unset):
            list_properties = UNSET
        else:
            list_properties = ListProperties.from_dict(_list_properties)




        _list_properties_suggestion_state = d.pop("listPropertiesSuggestionState", UNSET)
        list_properties_suggestion_state: ListPropertiesSuggestionState | Unset
        if isinstance(_list_properties_suggestion_state,  Unset):
            list_properties_suggestion_state = UNSET
        else:
            list_properties_suggestion_state = ListPropertiesSuggestionState.from_dict(_list_properties_suggestion_state)




        suggested_list_properties = cls(
            list_properties=list_properties,
            list_properties_suggestion_state=list_properties_suggestion_state,
        )


        suggested_list_properties.additional_properties = d
        return suggested_list_properties

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
