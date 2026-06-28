from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shading_suggestion_state import ShadingSuggestionState





T = TypeVar("T", bound="ParagraphStyleSuggestionState")



@_attrs_define
class ParagraphStyleSuggestionState:
    """ A mask that indicates which of the fields on the base ParagraphStyle have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            alignment_suggested (bool | Unset): Indicates if there was a suggested change to alignment.
            avoid_widow_and_orphan_suggested (bool | Unset): Indicates if there was a suggested change to
                avoid_widow_and_orphan.
            border_between_suggested (bool | Unset): Indicates if there was a suggested change to border_between.
            border_bottom_suggested (bool | Unset): Indicates if there was a suggested change to border_bottom.
            border_left_suggested (bool | Unset): Indicates if there was a suggested change to border_left.
            border_right_suggested (bool | Unset): Indicates if there was a suggested change to border_right.
            border_top_suggested (bool | Unset): Indicates if there was a suggested change to border_top.
            direction_suggested (bool | Unset): Indicates if there was a suggested change to direction.
            heading_id_suggested (bool | Unset): Indicates if there was a suggested change to heading_id.
            indent_end_suggested (bool | Unset): Indicates if there was a suggested change to indent_end.
            indent_first_line_suggested (bool | Unset): Indicates if there was a suggested change to indent_first_line.
            indent_start_suggested (bool | Unset): Indicates if there was a suggested change to indent_start.
            keep_lines_together_suggested (bool | Unset): Indicates if there was a suggested change to keep_lines_together.
            keep_with_next_suggested (bool | Unset): Indicates if there was a suggested change to keep_with_next.
            line_spacing_suggested (bool | Unset): Indicates if there was a suggested change to line_spacing.
            named_style_type_suggested (bool | Unset): Indicates if there was a suggested change to named_style_type.
            page_break_before_suggested (bool | Unset): Indicates if there was a suggested change to page_break_before.
            shading_suggestion_state (ShadingSuggestionState | Unset): A mask that indicates which of the fields on the base
                Shading have been changed in this suggested change. For any field set to true, there's a new suggested value.
            space_above_suggested (bool | Unset): Indicates if there was a suggested change to space_above.
            space_below_suggested (bool | Unset): Indicates if there was a suggested change to space_below.
            spacing_mode_suggested (bool | Unset): Indicates if there was a suggested change to spacing_mode.
     """

    alignment_suggested: bool | Unset = UNSET
    avoid_widow_and_orphan_suggested: bool | Unset = UNSET
    border_between_suggested: bool | Unset = UNSET
    border_bottom_suggested: bool | Unset = UNSET
    border_left_suggested: bool | Unset = UNSET
    border_right_suggested: bool | Unset = UNSET
    border_top_suggested: bool | Unset = UNSET
    direction_suggested: bool | Unset = UNSET
    heading_id_suggested: bool | Unset = UNSET
    indent_end_suggested: bool | Unset = UNSET
    indent_first_line_suggested: bool | Unset = UNSET
    indent_start_suggested: bool | Unset = UNSET
    keep_lines_together_suggested: bool | Unset = UNSET
    keep_with_next_suggested: bool | Unset = UNSET
    line_spacing_suggested: bool | Unset = UNSET
    named_style_type_suggested: bool | Unset = UNSET
    page_break_before_suggested: bool | Unset = UNSET
    shading_suggestion_state: ShadingSuggestionState | Unset = UNSET
    space_above_suggested: bool | Unset = UNSET
    space_below_suggested: bool | Unset = UNSET
    spacing_mode_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shading_suggestion_state import ShadingSuggestionState
        alignment_suggested = self.alignment_suggested

        avoid_widow_and_orphan_suggested = self.avoid_widow_and_orphan_suggested

        border_between_suggested = self.border_between_suggested

        border_bottom_suggested = self.border_bottom_suggested

        border_left_suggested = self.border_left_suggested

        border_right_suggested = self.border_right_suggested

        border_top_suggested = self.border_top_suggested

        direction_suggested = self.direction_suggested

        heading_id_suggested = self.heading_id_suggested

        indent_end_suggested = self.indent_end_suggested

        indent_first_line_suggested = self.indent_first_line_suggested

        indent_start_suggested = self.indent_start_suggested

        keep_lines_together_suggested = self.keep_lines_together_suggested

        keep_with_next_suggested = self.keep_with_next_suggested

        line_spacing_suggested = self.line_spacing_suggested

        named_style_type_suggested = self.named_style_type_suggested

        page_break_before_suggested = self.page_break_before_suggested

        shading_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shading_suggestion_state, Unset):
            shading_suggestion_state = self.shading_suggestion_state.to_dict()

        space_above_suggested = self.space_above_suggested

        space_below_suggested = self.space_below_suggested

        spacing_mode_suggested = self.spacing_mode_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alignment_suggested is not UNSET:
            field_dict["alignmentSuggested"] = alignment_suggested
        if avoid_widow_and_orphan_suggested is not UNSET:
            field_dict["avoidWidowAndOrphanSuggested"] = avoid_widow_and_orphan_suggested
        if border_between_suggested is not UNSET:
            field_dict["borderBetweenSuggested"] = border_between_suggested
        if border_bottom_suggested is not UNSET:
            field_dict["borderBottomSuggested"] = border_bottom_suggested
        if border_left_suggested is not UNSET:
            field_dict["borderLeftSuggested"] = border_left_suggested
        if border_right_suggested is not UNSET:
            field_dict["borderRightSuggested"] = border_right_suggested
        if border_top_suggested is not UNSET:
            field_dict["borderTopSuggested"] = border_top_suggested
        if direction_suggested is not UNSET:
            field_dict["directionSuggested"] = direction_suggested
        if heading_id_suggested is not UNSET:
            field_dict["headingIdSuggested"] = heading_id_suggested
        if indent_end_suggested is not UNSET:
            field_dict["indentEndSuggested"] = indent_end_suggested
        if indent_first_line_suggested is not UNSET:
            field_dict["indentFirstLineSuggested"] = indent_first_line_suggested
        if indent_start_suggested is not UNSET:
            field_dict["indentStartSuggested"] = indent_start_suggested
        if keep_lines_together_suggested is not UNSET:
            field_dict["keepLinesTogetherSuggested"] = keep_lines_together_suggested
        if keep_with_next_suggested is not UNSET:
            field_dict["keepWithNextSuggested"] = keep_with_next_suggested
        if line_spacing_suggested is not UNSET:
            field_dict["lineSpacingSuggested"] = line_spacing_suggested
        if named_style_type_suggested is not UNSET:
            field_dict["namedStyleTypeSuggested"] = named_style_type_suggested
        if page_break_before_suggested is not UNSET:
            field_dict["pageBreakBeforeSuggested"] = page_break_before_suggested
        if shading_suggestion_state is not UNSET:
            field_dict["shadingSuggestionState"] = shading_suggestion_state
        if space_above_suggested is not UNSET:
            field_dict["spaceAboveSuggested"] = space_above_suggested
        if space_below_suggested is not UNSET:
            field_dict["spaceBelowSuggested"] = space_below_suggested
        if spacing_mode_suggested is not UNSET:
            field_dict["spacingModeSuggested"] = spacing_mode_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shading_suggestion_state import ShadingSuggestionState
        d = dict(src_dict)
        alignment_suggested = d.pop("alignmentSuggested", UNSET)

        avoid_widow_and_orphan_suggested = d.pop("avoidWidowAndOrphanSuggested", UNSET)

        border_between_suggested = d.pop("borderBetweenSuggested", UNSET)

        border_bottom_suggested = d.pop("borderBottomSuggested", UNSET)

        border_left_suggested = d.pop("borderLeftSuggested", UNSET)

        border_right_suggested = d.pop("borderRightSuggested", UNSET)

        border_top_suggested = d.pop("borderTopSuggested", UNSET)

        direction_suggested = d.pop("directionSuggested", UNSET)

        heading_id_suggested = d.pop("headingIdSuggested", UNSET)

        indent_end_suggested = d.pop("indentEndSuggested", UNSET)

        indent_first_line_suggested = d.pop("indentFirstLineSuggested", UNSET)

        indent_start_suggested = d.pop("indentStartSuggested", UNSET)

        keep_lines_together_suggested = d.pop("keepLinesTogetherSuggested", UNSET)

        keep_with_next_suggested = d.pop("keepWithNextSuggested", UNSET)

        line_spacing_suggested = d.pop("lineSpacingSuggested", UNSET)

        named_style_type_suggested = d.pop("namedStyleTypeSuggested", UNSET)

        page_break_before_suggested = d.pop("pageBreakBeforeSuggested", UNSET)

        _shading_suggestion_state = d.pop("shadingSuggestionState", UNSET)
        shading_suggestion_state: ShadingSuggestionState | Unset
        if isinstance(_shading_suggestion_state,  Unset):
            shading_suggestion_state = UNSET
        else:
            shading_suggestion_state = ShadingSuggestionState.from_dict(_shading_suggestion_state)




        space_above_suggested = d.pop("spaceAboveSuggested", UNSET)

        space_below_suggested = d.pop("spaceBelowSuggested", UNSET)

        spacing_mode_suggested = d.pop("spacingModeSuggested", UNSET)

        paragraph_style_suggestion_state = cls(
            alignment_suggested=alignment_suggested,
            avoid_widow_and_orphan_suggested=avoid_widow_and_orphan_suggested,
            border_between_suggested=border_between_suggested,
            border_bottom_suggested=border_bottom_suggested,
            border_left_suggested=border_left_suggested,
            border_right_suggested=border_right_suggested,
            border_top_suggested=border_top_suggested,
            direction_suggested=direction_suggested,
            heading_id_suggested=heading_id_suggested,
            indent_end_suggested=indent_end_suggested,
            indent_first_line_suggested=indent_first_line_suggested,
            indent_start_suggested=indent_start_suggested,
            keep_lines_together_suggested=keep_lines_together_suggested,
            keep_with_next_suggested=keep_with_next_suggested,
            line_spacing_suggested=line_spacing_suggested,
            named_style_type_suggested=named_style_type_suggested,
            page_break_before_suggested=page_break_before_suggested,
            shading_suggestion_state=shading_suggestion_state,
            space_above_suggested=space_above_suggested,
            space_below_suggested=space_below_suggested,
            spacing_mode_suggested=spacing_mode_suggested,
        )


        paragraph_style_suggestion_state.additional_properties = d
        return paragraph_style_suggestion_state

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
