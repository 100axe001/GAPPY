from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PositionedObjectPositioningSuggestionState")



@_attrs_define
class PositionedObjectPositioningSuggestionState:
    """ A mask that indicates which of the fields on the base PositionedObjectPositioning have been changed in this
    suggestion. For any field set to true, there's a new suggested value.

        Attributes:
            layout_suggested (bool | Unset): Indicates if there was a suggested change to layout.
            left_offset_suggested (bool | Unset): Indicates if there was a suggested change to left_offset.
            top_offset_suggested (bool | Unset): Indicates if there was a suggested change to top_offset.
     """

    layout_suggested: bool | Unset = UNSET
    left_offset_suggested: bool | Unset = UNSET
    top_offset_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        layout_suggested = self.layout_suggested

        left_offset_suggested = self.left_offset_suggested

        top_offset_suggested = self.top_offset_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if layout_suggested is not UNSET:
            field_dict["layoutSuggested"] = layout_suggested
        if left_offset_suggested is not UNSET:
            field_dict["leftOffsetSuggested"] = left_offset_suggested
        if top_offset_suggested is not UNSET:
            field_dict["topOffsetSuggested"] = top_offset_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layout_suggested = d.pop("layoutSuggested", UNSET)

        left_offset_suggested = d.pop("leftOffsetSuggested", UNSET)

        top_offset_suggested = d.pop("topOffsetSuggested", UNSET)

        positioned_object_positioning_suggestion_state = cls(
            layout_suggested=layout_suggested,
            left_offset_suggested=left_offset_suggested,
            top_offset_suggested=top_offset_suggested,
        )


        positioned_object_positioning_suggestion_state.additional_properties = d
        return positioned_object_positioning_suggestion_state

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
