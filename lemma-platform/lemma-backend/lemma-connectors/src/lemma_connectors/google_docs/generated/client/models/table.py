from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_row import TableRow
  from ..models.table_style import TableStyle





T = TypeVar("T", bound="Table")



@_attrs_define
class Table:
    """ A StructuralElement representing a table.

        Attributes:
            columns (int | Unset): Number of columns in the table. It's possible for a table to be non-rectangular, so some
                rows may have a different number of cells.
            rows (int | Unset): Number of rows in the table.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_ids (list[str] | Unset): The suggested insertion IDs. A Table may have multiple insertion
                IDs if it's a nested suggested change. If empty, then this is not a suggested insertion.
            table_rows (list[TableRow] | Unset): The contents and style of each row.
            table_style (TableStyle | Unset): Styles that apply to a table.
     """

    columns: int | Unset = UNSET
    rows: int | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    table_rows: list[TableRow] | Unset = UNSET
    table_style: TableStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_row import TableRow
        from ..models.table_style import TableStyle
        columns = self.columns

        rows = self.rows

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_insertion_ids, Unset):
            suggested_insertion_ids = self.suggested_insertion_ids



        table_rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_rows, Unset):
            table_rows = []
            for table_rows_item_data in self.table_rows:
                table_rows_item = table_rows_item_data.to_dict()
                table_rows.append(table_rows_item)



        table_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_style, Unset):
            table_style = self.table_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if columns is not UNSET:
            field_dict["columns"] = columns
        if rows is not UNSET:
            field_dict["rows"] = rows
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_ids is not UNSET:
            field_dict["suggestedInsertionIds"] = suggested_insertion_ids
        if table_rows is not UNSET:
            field_dict["tableRows"] = table_rows
        if table_style is not UNSET:
            field_dict["tableStyle"] = table_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_row import TableRow
        from ..models.table_style import TableStyle
        d = dict(src_dict)
        columns = d.pop("columns", UNSET)

        rows = d.pop("rows", UNSET)

        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _table_rows = d.pop("tableRows", UNSET)
        table_rows: list[TableRow] | Unset = UNSET
        if _table_rows is not UNSET:
            table_rows = []
            for table_rows_item_data in _table_rows:
                table_rows_item = TableRow.from_dict(table_rows_item_data)



                table_rows.append(table_rows_item)


        _table_style = d.pop("tableStyle", UNSET)
        table_style: TableStyle | Unset
        if isinstance(_table_style,  Unset):
            table_style = UNSET
        else:
            table_style = TableStyle.from_dict(_table_style)




        table = cls(
            columns=columns,
            rows=rows,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            table_rows=table_rows,
            table_style=table_style,
        )


        table.additional_properties = d
        return table

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
