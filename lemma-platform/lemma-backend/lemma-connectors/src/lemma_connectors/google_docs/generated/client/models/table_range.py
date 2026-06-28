from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_cell_location import TableCellLocation





T = TypeVar("T", bound="TableRange")



@_attrs_define
class TableRange:
    """ A table range represents a reference to a subset of a table. It's important to note that the cells specified by a
    table range do not necessarily form a rectangle. For example, let's say we have a 3 x 3 table where all the cells of
    the last row are merged together. The table looks like this: [ ] A table range with table cell location =
    (table_start_location, row = 0, column = 0), row span = 3 and column span = 2 specifies the following cells: x x [ x
    x x ]

        Attributes:
            column_span (int | Unset): The column span of the table range.
            row_span (int | Unset): The row span of the table range.
            table_cell_location (TableCellLocation | Unset): Location of a single cell within a table.
     """

    column_span: int | Unset = UNSET
    row_span: int | Unset = UNSET
    table_cell_location: TableCellLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_cell_location import TableCellLocation
        column_span = self.column_span

        row_span = self.row_span

        table_cell_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_location, Unset):
            table_cell_location = self.table_cell_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_span is not UNSET:
            field_dict["columnSpan"] = column_span
        if row_span is not UNSET:
            field_dict["rowSpan"] = row_span
        if table_cell_location is not UNSET:
            field_dict["tableCellLocation"] = table_cell_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell_location import TableCellLocation
        d = dict(src_dict)
        column_span = d.pop("columnSpan", UNSET)

        row_span = d.pop("rowSpan", UNSET)

        _table_cell_location = d.pop("tableCellLocation", UNSET)
        table_cell_location: TableCellLocation | Unset
        if isinstance(_table_cell_location,  Unset):
            table_cell_location = UNSET
        else:
            table_cell_location = TableCellLocation.from_dict(_table_cell_location)




        table_range = cls(
            column_span=column_span,
            row_span=row_span,
            table_cell_location=table_cell_location,
        )


        table_range.additional_properties = d
        return table_range

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
