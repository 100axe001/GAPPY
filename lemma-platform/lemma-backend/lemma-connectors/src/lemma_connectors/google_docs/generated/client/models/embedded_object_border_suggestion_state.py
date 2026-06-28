from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="EmbeddedObjectBorderSuggestionState")



@_attrs_define
class EmbeddedObjectBorderSuggestionState:
    """ A mask that indicates which of the fields on the base EmbeddedObjectBorder have been changed in this suggestion. For
    any field set to true, there's a new suggested value.

        Attributes:
            color_suggested (bool | Unset): Indicates if there was a suggested change to color.
            dash_style_suggested (bool | Unset): Indicates if there was a suggested change to dash_style.
            property_state_suggested (bool | Unset): Indicates if there was a suggested change to property_state.
            width_suggested (bool | Unset): Indicates if there was a suggested change to width.
     """

    color_suggested: bool | Unset = UNSET
    dash_style_suggested: bool | Unset = UNSET
    property_state_suggested: bool | Unset = UNSET
    width_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color_suggested = self.color_suggested

        dash_style_suggested = self.dash_style_suggested

        property_state_suggested = self.property_state_suggested

        width_suggested = self.width_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color_suggested is not UNSET:
            field_dict["colorSuggested"] = color_suggested
        if dash_style_suggested is not UNSET:
            field_dict["dashStyleSuggested"] = dash_style_suggested
        if property_state_suggested is not UNSET:
            field_dict["propertyStateSuggested"] = property_state_suggested
        if width_suggested is not UNSET:
            field_dict["widthSuggested"] = width_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color_suggested = d.pop("colorSuggested", UNSET)

        dash_style_suggested = d.pop("dashStyleSuggested", UNSET)

        property_state_suggested = d.pop("propertyStateSuggested", UNSET)

        width_suggested = d.pop("widthSuggested", UNSET)

        embedded_object_border_suggestion_state = cls(
            color_suggested=color_suggested,
            dash_style_suggested=dash_style_suggested,
            property_state_suggested=property_state_suggested,
            width_suggested=width_suggested,
        )


        embedded_object_border_suggestion_state.additional_properties = d
        return embedded_object_border_suggestion_state

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
