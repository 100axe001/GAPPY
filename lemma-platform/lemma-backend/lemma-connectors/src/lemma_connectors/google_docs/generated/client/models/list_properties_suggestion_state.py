from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.nesting_level_suggestion_state import NestingLevelSuggestionState





T = TypeVar("T", bound="ListPropertiesSuggestionState")



@_attrs_define
class ListPropertiesSuggestionState:
    """ A mask that indicates which of the fields on the base ListProperties have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            nesting_levels_suggestion_states (list[NestingLevelSuggestionState] | Unset): A mask that indicates which of the
                fields on the corresponding NestingLevel in nesting_levels have been changed in this suggestion. The nesting
                level suggestion states are returned in ascending order of the nesting level with the least nested returned
                first.
     """

    nesting_levels_suggestion_states: list[NestingLevelSuggestionState] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.nesting_level_suggestion_state import NestingLevelSuggestionState
        nesting_levels_suggestion_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nesting_levels_suggestion_states, Unset):
            nesting_levels_suggestion_states = []
            for nesting_levels_suggestion_states_item_data in self.nesting_levels_suggestion_states:
                nesting_levels_suggestion_states_item = nesting_levels_suggestion_states_item_data.to_dict()
                nesting_levels_suggestion_states.append(nesting_levels_suggestion_states_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nesting_levels_suggestion_states is not UNSET:
            field_dict["nestingLevelsSuggestionStates"] = nesting_levels_suggestion_states

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nesting_level_suggestion_state import NestingLevelSuggestionState
        d = dict(src_dict)
        _nesting_levels_suggestion_states = d.pop("nestingLevelsSuggestionStates", UNSET)
        nesting_levels_suggestion_states: list[NestingLevelSuggestionState] | Unset = UNSET
        if _nesting_levels_suggestion_states is not UNSET:
            nesting_levels_suggestion_states = []
            for nesting_levels_suggestion_states_item_data in _nesting_levels_suggestion_states:
                nesting_levels_suggestion_states_item = NestingLevelSuggestionState.from_dict(nesting_levels_suggestion_states_item_data)



                nesting_levels_suggestion_states.append(nesting_levels_suggestion_states_item)


        list_properties_suggestion_state = cls(
            nesting_levels_suggestion_states=nesting_levels_suggestion_states,
        )


        list_properties_suggestion_state.additional_properties = d
        return list_properties_suggestion_state

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
