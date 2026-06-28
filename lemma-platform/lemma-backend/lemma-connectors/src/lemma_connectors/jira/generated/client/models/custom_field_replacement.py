from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldReplacement")



@_attrs_define
class CustomFieldReplacement:
    """ Details about the replacement for a deleted version.

        Attributes:
            custom_field_id (int | Unset): The ID of the custom field in which to replace the version number.
            move_to (int | Unset): The version number to use as a replacement for the deleted version.
     """

    custom_field_id: int | Unset = UNSET
    move_to: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        custom_field_id = self.custom_field_id

        move_to = self.move_to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom_field_id is not UNSET:
            field_dict["customFieldId"] = custom_field_id
        if move_to is not UNSET:
            field_dict["moveTo"] = move_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_field_id = d.pop("customFieldId", UNSET)

        move_to = d.pop("moveTo", UNSET)

        custom_field_replacement = cls(
            custom_field_id=custom_field_id,
            move_to=move_to,
        )

        return custom_field_replacement

