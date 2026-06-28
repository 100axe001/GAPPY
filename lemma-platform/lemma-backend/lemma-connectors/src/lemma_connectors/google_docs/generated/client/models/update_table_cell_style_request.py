from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location import Location
  from ..models.table_cell_style import TableCellStyle
  from ..models.table_range import TableRange





T = TypeVar("T", bound="UpdateTableCellStyleRequest")



@_attrs_define
class UpdateTableCellStyleRequest:
    """ Updates the style of a range of table cells.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `tableCellStyle` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field. For example to update the table cell background color, set `fields` to `"backgroundColor"`. To
                reset a property to its default value, include its field name in the field mask but leave the field itself
                unset.
            table_cell_style (TableCellStyle | Unset): The style of a TableCell. Inherited table cell styles are represented
                as unset fields in this message. A table cell style can inherit from the table's style.
            table_range (TableRange | Unset): A table range represents a reference to a subset of a table. It's important to
                note that the cells specified by a table range do not necessarily form a rectangle. For example, let's say we
                have a 3 x 3 table where all the cells of the last row are merged together. The table looks like this: [ ] A
                table range with table cell location = (table_start_location, row = 0, column = 0), row span = 3 and column span
                = 2 specifies the following cells: x x [ x x x ]
            table_start_location (Location | Unset): A particular location in the document.
     """

    fields: str | Unset = UNSET
    table_cell_style: TableCellStyle | Unset = UNSET
    table_range: TableRange | Unset = UNSET
    table_start_location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_range import TableRange
        fields = self.fields

        table_cell_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_style, Unset):
            table_cell_style = self.table_cell_style.to_dict()

        table_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_range, Unset):
            table_range = self.table_range.to_dict()

        table_start_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_start_location, Unset):
            table_start_location = self.table_start_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if table_cell_style is not UNSET:
            field_dict["tableCellStyle"] = table_cell_style
        if table_range is not UNSET:
            field_dict["tableRange"] = table_range
        if table_start_location is not UNSET:
            field_dict["tableStartLocation"] = table_start_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_range import TableRange
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _table_cell_style = d.pop("tableCellStyle", UNSET)
        table_cell_style: TableCellStyle | Unset
        if isinstance(_table_cell_style,  Unset):
            table_cell_style = UNSET
        else:
            table_cell_style = TableCellStyle.from_dict(_table_cell_style)




        _table_range = d.pop("tableRange", UNSET)
        table_range: TableRange | Unset
        if isinstance(_table_range,  Unset):
            table_range = UNSET
        else:
            table_range = TableRange.from_dict(_table_range)




        _table_start_location = d.pop("tableStartLocation", UNSET)
        table_start_location: Location | Unset
        if isinstance(_table_start_location,  Unset):
            table_start_location = UNSET
        else:
            table_start_location = Location.from_dict(_table_start_location)




        update_table_cell_style_request = cls(
            fields=fields,
            table_cell_style=table_cell_style,
            table_range=table_range,
            table_start_location=table_start_location,
        )


        update_table_cell_style_request.additional_properties = d
        return update_table_cell_style_request

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
