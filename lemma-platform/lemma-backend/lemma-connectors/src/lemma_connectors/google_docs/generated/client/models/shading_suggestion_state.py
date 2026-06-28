from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShadingSuggestionState")



@_attrs_define
class ShadingSuggestionState:
    """ A mask that indicates which of the fields on the base Shading have been changed in this suggested change. For any
    field set to true, there's a new suggested value.

        Attributes:
            background_color_suggested (bool | Unset): Indicates if there was a suggested change to the Shading.
     """

    background_color_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        background_color_suggested = self.background_color_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color_suggested is not UNSET:
            field_dict["backgroundColorSuggested"] = background_color_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background_color_suggested = d.pop("backgroundColorSuggested", UNSET)

        shading_suggestion_state = cls(
            background_color_suggested=background_color_suggested,
        )


        shading_suggestion_state.additional_properties = d
        return shading_suggestion_state

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
