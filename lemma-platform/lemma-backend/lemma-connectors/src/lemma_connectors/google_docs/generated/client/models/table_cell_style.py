from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.table_cell_style_content_alignment import TableCellStyleContentAlignment
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.optional_color import OptionalColor
  from ..models.table_cell_border import TableCellBorder





T = TypeVar("T", bound="TableCellStyle")



@_attrs_define
class TableCellStyle:
    """ The style of a TableCell. Inherited table cell styles are represented as unset fields in this message. A table cell
    style can inherit from the table's style.

        Attributes:
            background_color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
            border_bottom (TableCellBorder | Unset): A border around a table cell. Table cell borders cannot be transparent.
                To hide a table cell border, make its width 0.
            border_left (TableCellBorder | Unset): A border around a table cell. Table cell borders cannot be transparent.
                To hide a table cell border, make its width 0.
            border_right (TableCellBorder | Unset): A border around a table cell. Table cell borders cannot be transparent.
                To hide a table cell border, make its width 0.
            border_top (TableCellBorder | Unset): A border around a table cell. Table cell borders cannot be transparent. To
                hide a table cell border, make its width 0.
            column_span (int | Unset): The column span of the cell. This property is read-only.
            content_alignment (TableCellStyleContentAlignment | Unset): The alignment of the content in the table cell. The
                default alignment matches the alignment for newly created table cells in the Docs editor.
            padding_bottom (Dimension | Unset): A magnitude in a single direction in the specified units.
            padding_left (Dimension | Unset): A magnitude in a single direction in the specified units.
            padding_right (Dimension | Unset): A magnitude in a single direction in the specified units.
            padding_top (Dimension | Unset): A magnitude in a single direction in the specified units.
            row_span (int | Unset): The row span of the cell. This property is read-only.
     """

    background_color: OptionalColor | Unset = UNSET
    border_bottom: TableCellBorder | Unset = UNSET
    border_left: TableCellBorder | Unset = UNSET
    border_right: TableCellBorder | Unset = UNSET
    border_top: TableCellBorder | Unset = UNSET
    column_span: int | Unset = UNSET
    content_alignment: TableCellStyleContentAlignment | Unset = UNSET
    padding_bottom: Dimension | Unset = UNSET
    padding_left: Dimension | Unset = UNSET
    padding_right: Dimension | Unset = UNSET
    padding_top: Dimension | Unset = UNSET
    row_span: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.optional_color import OptionalColor
        from ..models.table_cell_border import TableCellBorder
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()

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

        column_span = self.column_span

        content_alignment: str | Unset = UNSET
        if not isinstance(self.content_alignment, Unset):
            content_alignment = self.content_alignment.value


        padding_bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding_bottom, Unset):
            padding_bottom = self.padding_bottom.to_dict()

        padding_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding_left, Unset):
            padding_left = self.padding_left.to_dict()

        padding_right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding_right, Unset):
            padding_right = self.padding_right.to_dict()

        padding_top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding_top, Unset):
            padding_top = self.padding_top.to_dict()

        row_span = self.row_span


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if border_bottom is not UNSET:
            field_dict["borderBottom"] = border_bottom
        if border_left is not UNSET:
            field_dict["borderLeft"] = border_left
        if border_right is not UNSET:
            field_dict["borderRight"] = border_right
        if border_top is not UNSET:
            field_dict["borderTop"] = border_top
        if column_span is not UNSET:
            field_dict["columnSpan"] = column_span
        if content_alignment is not UNSET:
            field_dict["contentAlignment"] = content_alignment
        if padding_bottom is not UNSET:
            field_dict["paddingBottom"] = padding_bottom
        if padding_left is not UNSET:
            field_dict["paddingLeft"] = padding_left
        if padding_right is not UNSET:
            field_dict["paddingRight"] = padding_right
        if padding_top is not UNSET:
            field_dict["paddingTop"] = padding_top
        if row_span is not UNSET:
            field_dict["rowSpan"] = row_span

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.optional_color import OptionalColor
        from ..models.table_cell_border import TableCellBorder
        d = dict(src_dict)
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: OptionalColor | Unset
        if isinstance(_background_color,  Unset):
            background_color = UNSET
        else:
            background_color = OptionalColor.from_dict(_background_color)




        _border_bottom = d.pop("borderBottom", UNSET)
        border_bottom: TableCellBorder | Unset
        if isinstance(_border_bottom,  Unset):
            border_bottom = UNSET
        else:
            border_bottom = TableCellBorder.from_dict(_border_bottom)




        _border_left = d.pop("borderLeft", UNSET)
        border_left: TableCellBorder | Unset
        if isinstance(_border_left,  Unset):
            border_left = UNSET
        else:
            border_left = TableCellBorder.from_dict(_border_left)




        _border_right = d.pop("borderRight", UNSET)
        border_right: TableCellBorder | Unset
        if isinstance(_border_right,  Unset):
            border_right = UNSET
        else:
            border_right = TableCellBorder.from_dict(_border_right)




        _border_top = d.pop("borderTop", UNSET)
        border_top: TableCellBorder | Unset
        if isinstance(_border_top,  Unset):
            border_top = UNSET
        else:
            border_top = TableCellBorder.from_dict(_border_top)




        column_span = d.pop("columnSpan", UNSET)

        _content_alignment = d.pop("contentAlignment", UNSET)
        content_alignment: TableCellStyleContentAlignment | Unset
        if isinstance(_content_alignment,  Unset):
            content_alignment = UNSET
        else:
            content_alignment = TableCellStyleContentAlignment(_content_alignment)




        _padding_bottom = d.pop("paddingBottom", UNSET)
        padding_bottom: Dimension | Unset
        if isinstance(_padding_bottom,  Unset):
            padding_bottom = UNSET
        else:
            padding_bottom = Dimension.from_dict(_padding_bottom)




        _padding_left = d.pop("paddingLeft", UNSET)
        padding_left: Dimension | Unset
        if isinstance(_padding_left,  Unset):
            padding_left = UNSET
        else:
            padding_left = Dimension.from_dict(_padding_left)




        _padding_right = d.pop("paddingRight", UNSET)
        padding_right: Dimension | Unset
        if isinstance(_padding_right,  Unset):
            padding_right = UNSET
        else:
            padding_right = Dimension.from_dict(_padding_right)




        _padding_top = d.pop("paddingTop", UNSET)
        padding_top: Dimension | Unset
        if isinstance(_padding_top,  Unset):
            padding_top = UNSET
        else:
            padding_top = Dimension.from_dict(_padding_top)




        row_span = d.pop("rowSpan", UNSET)

        table_cell_style = cls(
            background_color=background_color,
            border_bottom=border_bottom,
            border_left=border_left,
            border_right=border_right,
            border_top=border_top,
            column_span=column_span,
            content_alignment=content_alignment,
            padding_bottom=padding_bottom,
            padding_left=padding_left,
            padding_right=padding_right,
            padding_top=padding_top,
            row_span=row_span,
        )


        table_cell_style.additional_properties = d
        return table_cell_style

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
