from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.paragraph_style_alignment import ParagraphStyleAlignment
from ..models.paragraph_style_direction import ParagraphStyleDirection
from ..models.paragraph_style_named_style_type import ParagraphStyleNamedStyleType
from ..models.paragraph_style_spacing_mode import ParagraphStyleSpacingMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.paragraph_border import ParagraphBorder
  from ..models.shading import Shading
  from ..models.tab_stop import TabStop





T = TypeVar("T", bound="ParagraphStyle")



@_attrs_define
class ParagraphStyle:
    """ Styles that apply to a whole paragraph. Inherited paragraph styles are represented as unset fields in this message.
    A paragraph style's parent depends on where the paragraph style is defined: * The ParagraphStyle on a Paragraph
    inherits from the paragraph's corresponding named style type. * The ParagraphStyle on a named style inherits from
    the normal text named style. * The ParagraphStyle of the normal text named style inherits from the default paragraph
    style in the Docs editor. * The ParagraphStyle on a Paragraph element that's contained in a table may inherit its
    paragraph style from the table style. If the paragraph style does not inherit from a parent, unsetting fields will
    revert the style to a value matching the defaults in the Docs editor.

        Attributes:
            alignment (ParagraphStyleAlignment | Unset): The text alignment for this paragraph.
            avoid_widow_and_orphan (bool | Unset): Whether to avoid widows and orphans for the paragraph. If unset, the
                value is inherited from the parent.
            border_between (ParagraphBorder | Unset): A border around a paragraph.
            border_bottom (ParagraphBorder | Unset): A border around a paragraph.
            border_left (ParagraphBorder | Unset): A border around a paragraph.
            border_right (ParagraphBorder | Unset): A border around a paragraph.
            border_top (ParagraphBorder | Unset): A border around a paragraph.
            direction (ParagraphStyleDirection | Unset): The text direction of this paragraph. If unset, the value defaults
                to LEFT_TO_RIGHT since paragraph direction is not inherited.
            heading_id (str | Unset): The heading ID of the paragraph. If empty, then this paragraph is not a heading. This
                property is read-only.
            indent_end (Dimension | Unset): A magnitude in a single direction in the specified units.
            indent_first_line (Dimension | Unset): A magnitude in a single direction in the specified units.
            indent_start (Dimension | Unset): A magnitude in a single direction in the specified units.
            keep_lines_together (bool | Unset): Whether all lines of the paragraph should be laid out on the same page or
                column if possible. If unset, the value is inherited from the parent.
            keep_with_next (bool | Unset): Whether at least a part of this paragraph should be laid out on the same page or
                column as the next paragraph if possible. If unset, the value is inherited from the parent.
            line_spacing (float | Unset): The amount of space between lines, as a percentage of normal, where normal is
                represented as 100.0. If unset, the value is inherited from the parent.
            named_style_type (ParagraphStyleNamedStyleType | Unset): The named style type of the paragraph. Since updating
                the named style type affects other properties within ParagraphStyle, the named style type is applied before the
                other properties are updated.
            page_break_before (bool | Unset): Whether the current paragraph should always start at the beginning of a page.
                If unset, the value is inherited from the parent. Attempting to update page_break_before for paragraphs in
                unsupported regions, including Table, Header, Footer and Footnote, can result in an invalid document state that
                returns a 400 bad request error.
            shading (Shading | Unset): The shading of a paragraph.
            space_above (Dimension | Unset): A magnitude in a single direction in the specified units.
            space_below (Dimension | Unset): A magnitude in a single direction in the specified units.
            spacing_mode (ParagraphStyleSpacingMode | Unset): The spacing mode for the paragraph.
            tab_stops (list[TabStop] | Unset): A list of the tab stops for this paragraph. The list of tab stops is not
                inherited. This property is read-only.
     """

    alignment: ParagraphStyleAlignment | Unset = UNSET
    avoid_widow_and_orphan: bool | Unset = UNSET
    border_between: ParagraphBorder | Unset = UNSET
    border_bottom: ParagraphBorder | Unset = UNSET
    border_left: ParagraphBorder | Unset = UNSET
    border_right: ParagraphBorder | Unset = UNSET
    border_top: ParagraphBorder | Unset = UNSET
    direction: ParagraphStyleDirection | Unset = UNSET
    heading_id: str | Unset = UNSET
    indent_end: Dimension | Unset = UNSET
    indent_first_line: Dimension | Unset = UNSET
    indent_start: Dimension | Unset = UNSET
    keep_lines_together: bool | Unset = UNSET
    keep_with_next: bool | Unset = UNSET
    line_spacing: float | Unset = UNSET
    named_style_type: ParagraphStyleNamedStyleType | Unset = UNSET
    page_break_before: bool | Unset = UNSET
    shading: Shading | Unset = UNSET
    space_above: Dimension | Unset = UNSET
    space_below: Dimension | Unset = UNSET
    spacing_mode: ParagraphStyleSpacingMode | Unset = UNSET
    tab_stops: list[TabStop] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.paragraph_border import ParagraphBorder
        from ..models.shading import Shading
        from ..models.tab_stop import TabStop
        alignment: str | Unset = UNSET
        if not isinstance(self.alignment, Unset):
            alignment = self.alignment.value


        avoid_widow_and_orphan = self.avoid_widow_and_orphan

        border_between: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border_between, Unset):
            border_between = self.border_between.to_dict()

        border_bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border_bottom, Unset):
            border_bottom = self.border_bottom.to_dict()

        border_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border_left, Unset):
            border_left = self.border_left.to_dict()

        border_right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border_right, Unset):
            border_right = self.border_right.to_dict()

        border_top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border_top, Unset):
            border_top = self.border_top.to_dict()

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value


        heading_id = self.heading_id

        indent_end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indent_end, Unset):
            indent_end = self.indent_end.to_dict()

        indent_first_line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indent_first_line, Unset):
            indent_first_line = self.indent_first_line.to_dict()

        indent_start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indent_start, Unset):
            indent_start = self.indent_start.to_dict()

        keep_lines_together = self.keep_lines_together

        keep_with_next = self.keep_with_next

        line_spacing = self.line_spacing

        named_style_type: str | Unset = UNSET
        if not isinstance(self.named_style_type, Unset):
            named_style_type = self.named_style_type.value


        page_break_before = self.page_break_before

        shading: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shading, Unset):
            shading = self.shading.to_dict()

        space_above: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_above, Unset):
            space_above = self.space_above.to_dict()

        space_below: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_below, Unset):
            space_below = self.space_below.to_dict()

        spacing_mode: str | Unset = UNSET
        if not isinstance(self.spacing_mode, Unset):
            spacing_mode = self.spacing_mode.value


        tab_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tab_stops, Unset):
            tab_stops = []
            for tab_stops_item_data in self.tab_stops:
                tab_stops_item = tab_stops_item_data.to_dict()
                tab_stops.append(tab_stops_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alignment is not UNSET:
            field_dict["alignment"] = alignment
        if avoid_widow_and_orphan is not UNSET:
            field_dict["avoidWidowAndOrphan"] = avoid_widow_and_orphan
        if border_between is not UNSET:
            field_dict["borderBetween"] = border_between
        if border_bottom is not UNSET:
            field_dict["borderBottom"] = border_bottom
        if border_left is not UNSET:
            field_dict["borderLeft"] = border_left
        if border_right is not UNSET:
            field_dict["borderRight"] = border_right
        if border_top is not UNSET:
            field_dict["borderTop"] = border_top
        if direction is not UNSET:
            field_dict["direction"] = direction
        if heading_id is not UNSET:
            field_dict["headingId"] = heading_id
        if indent_end is not UNSET:
            field_dict["indentEnd"] = indent_end
        if indent_first_line is not UNSET:
            field_dict["indentFirstLine"] = indent_first_line
        if indent_start is not UNSET:
            field_dict["indentStart"] = indent_start
        if keep_lines_together is not UNSET:
            field_dict["keepLinesTogether"] = keep_lines_together
        if keep_with_next is not UNSET:
            field_dict["keepWithNext"] = keep_with_next
        if line_spacing is not UNSET:
            field_dict["lineSpacing"] = line_spacing
        if named_style_type is not UNSET:
            field_dict["namedStyleType"] = named_style_type
        if page_break_before is not UNSET:
            field_dict["pageBreakBefore"] = page_break_before
        if shading is not UNSET:
            field_dict["shading"] = shading
        if space_above is not UNSET:
            field_dict["spaceAbove"] = space_above
        if space_below is not UNSET:
            field_dict["spaceBelow"] = space_below
        if spacing_mode is not UNSET:
            field_dict["spacingMode"] = spacing_mode
        if tab_stops is not UNSET:
            field_dict["tabStops"] = tab_stops

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.paragraph_border import ParagraphBorder
        from ..models.shading import Shading
        from ..models.tab_stop import TabStop
        d = dict(src_dict)
        _alignment = d.pop("alignment", UNSET)
        alignment: ParagraphStyleAlignment | Unset
        if isinstance(_alignment,  Unset):
            alignment = UNSET
        else:
            alignment = ParagraphStyleAlignment(_alignment)




        avoid_widow_and_orphan = d.pop("avoidWidowAndOrphan", UNSET)

        _border_between = d.pop("borderBetween", UNSET)
        border_between: ParagraphBorder | Unset
        if isinstance(_border_between,  Unset):
            border_between = UNSET
        else:
            border_between = ParagraphBorder.from_dict(_border_between)




        _border_bottom = d.pop("borderBottom", UNSET)
        border_bottom: ParagraphBorder | Unset
        if isinstance(_border_bottom,  Unset):
            border_bottom = UNSET
        else:
            border_bottom = ParagraphBorder.from_dict(_border_bottom)




        _border_left = d.pop("borderLeft", UNSET)
        border_left: ParagraphBorder | Unset
        if isinstance(_border_left,  Unset):
            border_left = UNSET
        else:
            border_left = ParagraphBorder.from_dict(_border_left)




        _border_right = d.pop("borderRight", UNSET)
        border_right: ParagraphBorder | Unset
        if isinstance(_border_right,  Unset):
            border_right = UNSET
        else:
            border_right = ParagraphBorder.from_dict(_border_right)




        _border_top = d.pop("borderTop", UNSET)
        border_top: ParagraphBorder | Unset
        if isinstance(_border_top,  Unset):
            border_top = UNSET
        else:
            border_top = ParagraphBorder.from_dict(_border_top)




        _direction = d.pop("direction", UNSET)
        direction: ParagraphStyleDirection | Unset
        if isinstance(_direction,  Unset):
            direction = UNSET
        else:
            direction = ParagraphStyleDirection(_direction)




        heading_id = d.pop("headingId", UNSET)

        _indent_end = d.pop("indentEnd", UNSET)
        indent_end: Dimension | Unset
        if isinstance(_indent_end,  Unset):
            indent_end = UNSET
        else:
            indent_end = Dimension.from_dict(_indent_end)




        _indent_first_line = d.pop("indentFirstLine", UNSET)
        indent_first_line: Dimension | Unset
        if isinstance(_indent_first_line,  Unset):
            indent_first_line = UNSET
        else:
            indent_first_line = Dimension.from_dict(_indent_first_line)




        _indent_start = d.pop("indentStart", UNSET)
        indent_start: Dimension | Unset
        if isinstance(_indent_start,  Unset):
            indent_start = UNSET
        else:
            indent_start = Dimension.from_dict(_indent_start)




        keep_lines_together = d.pop("keepLinesTogether", UNSET)

        keep_with_next = d.pop("keepWithNext", UNSET)

        line_spacing = d.pop("lineSpacing", UNSET)

        _named_style_type = d.pop("namedStyleType", UNSET)
        named_style_type: ParagraphStyleNamedStyleType | Unset
        if isinstance(_named_style_type,  Unset):
            named_style_type = UNSET
        else:
            named_style_type = ParagraphStyleNamedStyleType(_named_style_type)




        page_break_before = d.pop("pageBreakBefore", UNSET)

        _shading = d.pop("shading", UNSET)
        shading: Shading | Unset
        if isinstance(_shading,  Unset):
            shading = UNSET
        else:
            shading = Shading.from_dict(_shading)




        _space_above = d.pop("spaceAbove", UNSET)
        space_above: Dimension | Unset
        if isinstance(_space_above,  Unset):
            space_above = UNSET
        else:
            space_above = Dimension.from_dict(_space_above)




        _space_below = d.pop("spaceBelow", UNSET)
        space_below: Dimension | Unset
        if isinstance(_space_below,  Unset):
            space_below = UNSET
        else:
            space_below = Dimension.from_dict(_space_below)




        _spacing_mode = d.pop("spacingMode", UNSET)
        spacing_mode: ParagraphStyleSpacingMode | Unset
        if isinstance(_spacing_mode,  Unset):
            spacing_mode = UNSET
        else:
            spacing_mode = ParagraphStyleSpacingMode(_spacing_mode)




        _tab_stops = d.pop("tabStops", UNSET)
        tab_stops: list[TabStop] | Unset = UNSET
        if _tab_stops is not UNSET:
            tab_stops = []
            for tab_stops_item_data in _tab_stops:
                tab_stops_item = TabStop.from_dict(tab_stops_item_data)



                tab_stops.append(tab_stops_item)


        paragraph_style = cls(
            alignment=alignment,
            avoid_widow_and_orphan=avoid_widow_and_orphan,
            border_between=border_between,
            border_bottom=border_bottom,
            border_left=border_left,
            border_right=border_right,
            border_top=border_top,
            direction=direction,
            heading_id=heading_id,
            indent_end=indent_end,
            indent_first_line=indent_first_line,
            indent_start=indent_start,
            keep_lines_together=keep_lines_together,
            keep_with_next=keep_with_next,
            line_spacing=line_spacing,
            named_style_type=named_style_type,
            page_break_before=page_break_before,
            shading=shading,
            space_above=space_above,
            space_below=space_below,
            spacing_mode=spacing_mode,
            tab_stops=tab_stops,
        )


        paragraph_style.additional_properties = d
        return paragraph_style

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
