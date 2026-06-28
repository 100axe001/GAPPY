from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TableCellStyleSuggestionState")



@_attrs_define
class TableCellStyleSuggestionState:
    """ A mask that indicates which of the fields on the base TableCellStyle have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            background_color_suggested (bool | Unset): Indicates if there was a suggested change to background_color.
            border_bottom_suggested (bool | Unset): Indicates if there was a suggested change to border_bottom.
            border_left_suggested (bool | Unset): Indicates if there was a suggested change to border_left.
            border_right_suggested (bool | Unset): Indicates if there was a suggested change to border_right.
            border_top_suggested (bool | Unset): Indicates if there was a suggested change to border_top.
            column_span_suggested (bool | Unset): Indicates if there was a suggested change to column_span.
            content_alignment_suggested (bool | Unset): Indicates if there was a suggested change to content_alignment.
            padding_bottom_suggested (bool | Unset): Indicates if there was a suggested change to padding_bottom.
            padding_left_suggested (bool | Unset): Indicates if there was a suggested change to padding_left.
            padding_right_suggested (bool | Unset): Indicates if there was a suggested change to padding_right.
            padding_top_suggested (bool | Unset): Indicates if there was a suggested change to padding_top.
            row_span_suggested (bool | Unset): Indicates if there was a suggested change to row_span.
     """

    background_color_suggested: bool | Unset = UNSET
    border_bottom_suggested: bool | Unset = UNSET
    border_left_suggested: bool | Unset = UNSET
    border_right_suggested: bool | Unset = UNSET
    border_top_suggested: bool | Unset = UNSET
    column_span_suggested: bool | Unset = UNSET
    content_alignment_suggested: bool | Unset = UNSET
    padding_bottom_suggested: bool | Unset = UNSET
    padding_left_suggested: bool | Unset = UNSET
    padding_right_suggested: bool | Unset = UNSET
    padding_top_suggested: bool | Unset = UNSET
    row_span_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        background_color_suggested = self.background_color_suggested

        border_bottom_suggested = self.border_bottom_suggested

        border_left_suggested = self.border_left_suggested

        border_right_suggested = self.border_right_suggested

        border_top_suggested = self.border_top_suggested

        column_span_suggested = self.column_span_suggested

        content_alignment_suggested = self.content_alignment_suggested

        padding_bottom_suggested = self.padding_bottom_suggested

        padding_left_suggested = self.padding_left_suggested

        padding_right_suggested = self.padding_right_suggested

        padding_top_suggested = self.padding_top_suggested

        row_span_suggested = self.row_span_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color_suggested is not UNSET:
            field_dict["backgroundColorSuggested"] = background_color_suggested
        if border_bottom_suggested is not UNSET:
            field_dict["borderBottomSuggested"] = border_bottom_suggested
        if border_left_suggested is not UNSET:
            field_dict["borderLeftSuggested"] = border_left_suggested
        if border_right_suggested is not UNSET:
            field_dict["borderRightSuggested"] = border_right_suggested
        if border_top_suggested is not UNSET:
            field_dict["borderTopSuggested"] = border_top_suggested
        if column_span_suggested is not UNSET:
            field_dict["columnSpanSuggested"] = column_span_suggested
        if content_alignment_suggested is not UNSET:
            field_dict["contentAlignmentSuggested"] = content_alignment_suggested
        if padding_bottom_suggested is not UNSET:
            field_dict["paddingBottomSuggested"] = padding_bottom_suggested
        if padding_left_suggested is not UNSET:
            field_dict["paddingLeftSuggested"] = padding_left_suggested
        if padding_right_suggested is not UNSET:
            field_dict["paddingRightSuggested"] = padding_right_suggested
        if padding_top_suggested is not UNSET:
            field_dict["paddingTopSuggested"] = padding_top_suggested
        if row_span_suggested is not UNSET:
            field_dict["rowSpanSuggested"] = row_span_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background_color_suggested = d.pop("backgroundColorSuggested", UNSET)

        border_bottom_suggested = d.pop("borderBottomSuggested", UNSET)

        border_left_suggested = d.pop("borderLeftSuggested", UNSET)

        border_right_suggested = d.pop("borderRightSuggested", UNSET)

        border_top_suggested = d.pop("borderTopSuggested", UNSET)

        column_span_suggested = d.pop("columnSpanSuggested", UNSET)

        content_alignment_suggested = d.pop("contentAlignmentSuggested", UNSET)

        padding_bottom_suggested = d.pop("paddingBottomSuggested", UNSET)

        padding_left_suggested = d.pop("paddingLeftSuggested", UNSET)

        padding_right_suggested = d.pop("paddingRightSuggested", UNSET)

        padding_top_suggested = d.pop("paddingTopSuggested", UNSET)

        row_span_suggested = d.pop("rowSpanSuggested", UNSET)

        table_cell_style_suggestion_state = cls(
            background_color_suggested=background_color_suggested,
            border_bottom_suggested=border_bottom_suggested,
            border_left_suggested=border_left_suggested,
            border_right_suggested=border_right_suggested,
            border_top_suggested=border_top_suggested,
            column_span_suggested=column_span_suggested,
            content_alignment_suggested=content_alignment_suggested,
            padding_bottom_suggested=padding_bottom_suggested,
            padding_left_suggested=padding_left_suggested,
            padding_right_suggested=padding_right_suggested,
            padding_top_suggested=padding_top_suggested,
            row_span_suggested=row_span_suggested,
        )


        table_cell_style_suggestion_state.additional_properties = d
        return table_cell_style_suggestion_state

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
