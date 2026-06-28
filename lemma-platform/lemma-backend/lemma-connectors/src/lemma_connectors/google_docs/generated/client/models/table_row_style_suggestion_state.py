from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TableRowStyleSuggestionState")



@_attrs_define
class TableRowStyleSuggestionState:
    """ A mask that indicates which of the fields on the base TableRowStyle have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            min_row_height_suggested (bool | Unset): Indicates if there was a suggested change to min_row_height.
     """

    min_row_height_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_row_height_suggested = self.min_row_height_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_row_height_suggested is not UNSET:
            field_dict["minRowHeightSuggested"] = min_row_height_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_row_height_suggested = d.pop("minRowHeightSuggested", UNSET)

        table_row_style_suggestion_state = cls(
            min_row_height_suggested=min_row_height_suggested,
        )


        table_row_style_suggestion_state.additional_properties = d
        return table_row_style_suggestion_state

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
