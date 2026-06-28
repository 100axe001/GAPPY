from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_cell import TableCell
  from ..models.table_row_style import TableRowStyle
  from ..models.table_row_suggested_table_row_style_changes import TableRowSuggestedTableRowStyleChanges





T = TypeVar("T", bound="TableRow")



@_attrs_define
class TableRow:
    """ The contents and style of a row in a Table.

        Attributes:
            end_index (int | Unset): The zero-based end index of this row, exclusive, in UTF-16 code units.
            start_index (int | Unset): The zero-based start index of this row, in UTF-16 code units.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_ids (list[str] | Unset): The suggested insertion IDs. A TableRow may have multiple insertion
                IDs if it's a nested suggested change. If empty, then this is not a suggested insertion.
            suggested_table_row_style_changes (TableRowSuggestedTableRowStyleChanges | Unset): The suggested style changes
                to this row, keyed by suggestion ID.
            table_cells (list[TableCell] | Unset): The contents and style of each cell in this row. It's possible for a
                table to be non-rectangular, so some rows may have a different number of cells than other rows in the same
                table.
            table_row_style (TableRowStyle | Unset): Styles that apply to a table row.
     """

    end_index: int | Unset = UNSET
    start_index: int | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    suggested_table_row_style_changes: TableRowSuggestedTableRowStyleChanges | Unset = UNSET
    table_cells: list[TableCell] | Unset = UNSET
    table_row_style: TableRowStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_cell import TableCell
        from ..models.table_row_style import TableRowStyle
        from ..models.table_row_suggested_table_row_style_changes import TableRowSuggestedTableRowStyleChanges
        end_index = self.end_index

        start_index = self.start_index

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_insertion_ids, Unset):
            suggested_insertion_ids = self.suggested_insertion_ids



        suggested_table_row_style_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_table_row_style_changes, Unset):
            suggested_table_row_style_changes = self.suggested_table_row_style_changes.to_dict()

        table_cells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_cells, Unset):
            table_cells = []
            for table_cells_item_data in self.table_cells:
                table_cells_item = table_cells_item_data.to_dict()
                table_cells.append(table_cells_item)



        table_row_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_row_style, Unset):
            table_row_style = self.table_row_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_ids is not UNSET:
            field_dict["suggestedInsertionIds"] = suggested_insertion_ids
        if suggested_table_row_style_changes is not UNSET:
            field_dict["suggestedTableRowStyleChanges"] = suggested_table_row_style_changes
        if table_cells is not UNSET:
            field_dict["tableCells"] = table_cells
        if table_row_style is not UNSET:
            field_dict["tableRowStyle"] = table_row_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell import TableCell
        from ..models.table_row_style import TableRowStyle
        from ..models.table_row_suggested_table_row_style_changes import TableRowSuggestedTableRowStyleChanges
        d = dict(src_dict)
        end_index = d.pop("endIndex", UNSET)

        start_index = d.pop("startIndex", UNSET)

        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _suggested_table_row_style_changes = d.pop("suggestedTableRowStyleChanges", UNSET)
        suggested_table_row_style_changes: TableRowSuggestedTableRowStyleChanges | Unset
        if isinstance(_suggested_table_row_style_changes,  Unset):
            suggested_table_row_style_changes = UNSET
        else:
            suggested_table_row_style_changes = TableRowSuggestedTableRowStyleChanges.from_dict(_suggested_table_row_style_changes)




        _table_cells = d.pop("tableCells", UNSET)
        table_cells: list[TableCell] | Unset = UNSET
        if _table_cells is not UNSET:
            table_cells = []
            for table_cells_item_data in _table_cells:
                table_cells_item = TableCell.from_dict(table_cells_item_data)



                table_cells.append(table_cells_item)


        _table_row_style = d.pop("tableRowStyle", UNSET)
        table_row_style: TableRowStyle | Unset
        if isinstance(_table_row_style,  Unset):
            table_row_style = UNSET
        else:
            table_row_style = TableRowStyle.from_dict(_table_row_style)




        table_row = cls(
            end_index=end_index,
            start_index=start_index,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            suggested_table_row_style_changes=suggested_table_row_style_changes,
            table_cells=table_cells,
            table_row_style=table_row_style,
        )


        table_row.additional_properties = d
        return table_row

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
