from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_range import TableRange





T = TypeVar("T", bound="MergeTableCellsRequest")



@_attrs_define
class MergeTableCellsRequest:
    """ Merges cells in a Table.

        Attributes:
            table_range (TableRange | Unset): A table range represents a reference to a subset of a table. It's important to
                note that the cells specified by a table range do not necessarily form a rectangle. For example, let's say we
                have a 3 x 3 table where all the cells of the last row are merged together. The table looks like this: [ ] A
                table range with table cell location = (table_start_location, row = 0, column = 0), row span = 3 and column span
                = 2 specifies the following cells: x x [ x x x ]
     """

    table_range: TableRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_range import TableRange
        table_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_range, Unset):
            table_range = self.table_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if table_range is not UNSET:
            field_dict["tableRange"] = table_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_range import TableRange
        d = dict(src_dict)
        _table_range = d.pop("tableRange", UNSET)
        table_range: TableRange | Unset
        if isinstance(_table_range,  Unset):
            table_range = UNSET
        else:
            table_range = TableRange.from_dict(_table_range)




        merge_table_cells_request = cls(
            table_range=table_range,
        )


        merge_table_cells_request.additional_properties = d
        return merge_table_cells_request

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
