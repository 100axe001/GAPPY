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





T = TypeVar("T", bound="TableCellLocation")



@_attrs_define
class TableCellLocation:
    """ Location of a single cell within a table.

        Attributes:
            column_index (int | Unset): The zero-based column index. For example, the second column in the table has a
                column index of 1.
            row_index (int | Unset): The zero-based row index. For example, the second row in the table has a row index of
                1.
            table_start_location (Location | Unset): A particular location in the document.
     """

    column_index: int | Unset = UNSET
    row_index: int | Unset = UNSET
    table_start_location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        column_index = self.column_index

        row_index = self.row_index

        table_start_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_start_location, Unset):
            table_start_location = self.table_start_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_index is not UNSET:
            field_dict["columnIndex"] = column_index
        if row_index is not UNSET:
            field_dict["rowIndex"] = row_index
        if table_start_location is not UNSET:
            field_dict["tableStartLocation"] = table_start_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        d = dict(src_dict)
        column_index = d.pop("columnIndex", UNSET)

        row_index = d.pop("rowIndex", UNSET)

        _table_start_location = d.pop("tableStartLocation", UNSET)
        table_start_location: Location | Unset
        if isinstance(_table_start_location,  Unset):
            table_start_location = UNSET
        else:
            table_start_location = Location.from_dict(_table_start_location)




        table_cell_location = cls(
            column_index=column_index,
            row_index=row_index,
            table_start_location=table_start_location,
        )


        table_cell_location.additional_properties = d
        return table_cell_location

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
