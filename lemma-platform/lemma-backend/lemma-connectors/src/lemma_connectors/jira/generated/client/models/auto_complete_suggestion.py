from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AutoCompleteSuggestion")



@_attrs_define
class AutoCompleteSuggestion:
    """ A field auto-complete suggestion.

        Attributes:
            display_name (str | Unset): The display name of a suggested item. If `fieldValue` or `predicateValue` are
                provided, the matching text is highlighted with the HTML bold tag.
            value (str | Unset): The value of a suggested item.
     """

    display_name: str | Unset = UNSET
    value: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        value = d.pop("value", UNSET)

        auto_complete_suggestion = cls(
            display_name=display_name,
            value=value,
        )

        return auto_complete_suggestion

