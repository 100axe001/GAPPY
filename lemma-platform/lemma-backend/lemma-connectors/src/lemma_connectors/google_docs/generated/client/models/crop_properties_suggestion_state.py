from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CropPropertiesSuggestionState")



@_attrs_define
class CropPropertiesSuggestionState:
    """ A mask that indicates which of the fields on the base CropProperties have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            angle_suggested (bool | Unset): Indicates if there was a suggested change to angle.
            offset_bottom_suggested (bool | Unset): Indicates if there was a suggested change to offset_bottom.
            offset_left_suggested (bool | Unset): Indicates if there was a suggested change to offset_left.
            offset_right_suggested (bool | Unset): Indicates if there was a suggested change to offset_right.
            offset_top_suggested (bool | Unset): Indicates if there was a suggested change to offset_top.
     """

    angle_suggested: bool | Unset = UNSET
    offset_bottom_suggested: bool | Unset = UNSET
    offset_left_suggested: bool | Unset = UNSET
    offset_right_suggested: bool | Unset = UNSET
    offset_top_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        angle_suggested = self.angle_suggested

        offset_bottom_suggested = self.offset_bottom_suggested

        offset_left_suggested = self.offset_left_suggested

        offset_right_suggested = self.offset_right_suggested

        offset_top_suggested = self.offset_top_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if angle_suggested is not UNSET:
            field_dict["angleSuggested"] = angle_suggested
        if offset_bottom_suggested is not UNSET:
            field_dict["offsetBottomSuggested"] = offset_bottom_suggested
        if offset_left_suggested is not UNSET:
            field_dict["offsetLeftSuggested"] = offset_left_suggested
        if offset_right_suggested is not UNSET:
            field_dict["offsetRightSuggested"] = offset_right_suggested
        if offset_top_suggested is not UNSET:
            field_dict["offsetTopSuggested"] = offset_top_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle_suggested = d.pop("angleSuggested", UNSET)

        offset_bottom_suggested = d.pop("offsetBottomSuggested", UNSET)

        offset_left_suggested = d.pop("offsetLeftSuggested", UNSET)

        offset_right_suggested = d.pop("offsetRightSuggested", UNSET)

        offset_top_suggested = d.pop("offsetTopSuggested", UNSET)

        crop_properties_suggestion_state = cls(
            angle_suggested=angle_suggested,
            offset_bottom_suggested=offset_bottom_suggested,
            offset_left_suggested=offset_left_suggested,
            offset_right_suggested=offset_right_suggested,
            offset_top_suggested=offset_top_suggested,
        )


        crop_properties_suggestion_state.additional_properties = d
        return crop_properties_suggestion_state

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
