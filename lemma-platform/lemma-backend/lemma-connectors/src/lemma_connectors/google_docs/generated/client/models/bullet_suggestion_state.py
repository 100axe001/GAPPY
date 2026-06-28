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





T = TypeVar("T", bound="BulletSuggestionState")



@_attrs_define
class BulletSuggestionState:
    """ A mask that indicates which of the fields on the base Bullet have been changed in this suggestion. For any field set
    to true, there's a new suggested value.

        Attributes:
            list_id_suggested (bool | Unset): Indicates if there was a suggested change to the list_id.
            nesting_level_suggested (bool | Unset): Indicates if there was a suggested change to the nesting_level.
            text_style_suggestion_state (TextStyleSuggestionState | Unset): A mask that indicates which of the fields on the
                base TextStyle have been changed in this suggestion. For any field set to true, there's a new suggested value.
     """

    list_id_suggested: bool | Unset = UNSET
    nesting_level_suggested: bool | Unset = UNSET
    text_style_suggestion_state: TextStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        list_id_suggested = self.list_id_suggested

        nesting_level_suggested = self.nesting_level_suggested

        text_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style_suggestion_state, Unset):
            text_style_suggestion_state = self.text_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if list_id_suggested is not UNSET:
            field_dict["listIdSuggested"] = list_id_suggested
        if nesting_level_suggested is not UNSET:
            field_dict["nestingLevelSuggested"] = nesting_level_suggested
        if text_style_suggestion_state is not UNSET:
            field_dict["textStyleSuggestionState"] = text_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_style_suggestion_state import TextStyleSuggestionState
        d = dict(src_dict)
        list_id_suggested = d.pop("listIdSuggested", UNSET)

        nesting_level_suggested = d.pop("nestingLevelSuggested", UNSET)

        _text_style_suggestion_state = d.pop("textStyleSuggestionState", UNSET)
        text_style_suggestion_state: TextStyleSuggestionState | Unset
        if isinstance(_text_style_suggestion_state,  Unset):
            text_style_suggestion_state = UNSET
        else:
            text_style_suggestion_state = TextStyleSuggestionState.from_dict(_text_style_suggestion_state)




        bullet_suggestion_state = cls(
            list_id_suggested=list_id_suggested,
            nesting_level_suggested=nesting_level_suggested,
            text_style_suggestion_state=text_style_suggestion_state,
        )


        bullet_suggestion_state.additional_properties = d
        return bullet_suggestion_state

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
