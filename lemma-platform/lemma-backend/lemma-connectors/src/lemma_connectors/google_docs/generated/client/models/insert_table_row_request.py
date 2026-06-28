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





T = TypeVar("T", bound="InsertTableRowRequest")



@_attrs_define
class InsertTableRowRequest:
    """ Inserts an empty row into a table.

        Attributes:
            insert_below (bool | Unset): Whether to insert new row below the reference cell location. - `True`: insert below
                the cell. - `False`: insert above the cell.
            table_cell_location (TableCellLocation | Unset): Location of a single cell within a table.
     """

    insert_below: bool | Unset = UNSET
    table_cell_location: TableCellLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_cell_location import TableCellLocation
        insert_below = self.insert_below

        table_cell_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_location, Unset):
            table_cell_location = self.table_cell_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if insert_below is not UNSET:
            field_dict["insertBelow"] = insert_below
        if table_cell_location is not UNSET:
            field_dict["tableCellLocation"] = table_cell_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell_location import TableCellLocation
        d = dict(src_dict)
        insert_below = d.pop("insertBelow", UNSET)

        _table_cell_location = d.pop("tableCellLocation", UNSET)
        table_cell_location: TableCellLocation | Unset
        if isinstance(_table_cell_location,  Unset):
            table_cell_location = UNSET
        else:
            table_cell_location = TableCellLocation.from_dict(_table_cell_location)




        insert_table_row_request = cls(
            insert_below=insert_below,
            table_cell_location=table_cell_location,
        )


        insert_table_row_request.additional_properties = d
        return insert_table_row_request

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
