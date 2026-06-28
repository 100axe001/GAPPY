from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.structural_element import StructuralElement
  from ..models.table_cell_style import TableCellStyle
  from ..models.table_cell_suggested_table_cell_style_changes import TableCellSuggestedTableCellStyleChanges





T = TypeVar("T", bound="TableCell")



@_attrs_define
class TableCell:
    """ The contents and style of a cell in a Table.

        Attributes:
            content (list[StructuralElement] | Unset): The content of the cell.
            end_index (int | Unset): The zero-based end index of this cell, exclusive, in UTF-16 code units.
            start_index (int | Unset): The zero-based start index of this cell, in UTF-16 code units.
            suggested_deletion_ids (list[str] | Unset): The suggested deletion IDs. If empty, then there are no suggested
                deletions of this content.
            suggested_insertion_ids (list[str] | Unset): The suggested insertion IDs. A TableCell may have multiple
                insertion IDs if it's a nested suggested change. If empty, then this is not a suggested insertion.
            suggested_table_cell_style_changes (TableCellSuggestedTableCellStyleChanges | Unset): The suggested changes to
                the table cell style, keyed by suggestion ID.
            table_cell_style (TableCellStyle | Unset): The style of a TableCell. Inherited table cell styles are represented
                as unset fields in this message. A table cell style can inherit from the table's style.
     """

    content: list[StructuralElement] | Unset = UNSET
    end_index: int | Unset = UNSET
    start_index: int | Unset = UNSET
    suggested_deletion_ids: list[str] | Unset = UNSET
    suggested_insertion_ids: list[str] | Unset = UNSET
    suggested_table_cell_style_changes: TableCellSuggestedTableCellStyleChanges | Unset = UNSET
    table_cell_style: TableCellStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.structural_element import StructuralElement
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_cell_suggested_table_cell_style_changes import TableCellSuggestedTableCellStyleChanges
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)



        end_index = self.end_index

        start_index = self.start_index

        suggested_deletion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_deletion_ids, Unset):
            suggested_deletion_ids = self.suggested_deletion_ids



        suggested_insertion_ids: list[str] | Unset = UNSET
        if not isinstance(self.suggested_insertion_ids, Unset):
            suggested_insertion_ids = self.suggested_insertion_ids



        suggested_table_cell_style_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_table_cell_style_changes, Unset):
            suggested_table_cell_style_changes = self.suggested_table_cell_style_changes.to_dict()

        table_cell_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_style, Unset):
            table_cell_style = self.table_cell_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if suggested_deletion_ids is not UNSET:
            field_dict["suggestedDeletionIds"] = suggested_deletion_ids
        if suggested_insertion_ids is not UNSET:
            field_dict["suggestedInsertionIds"] = suggested_insertion_ids
        if suggested_table_cell_style_changes is not UNSET:
            field_dict["suggestedTableCellStyleChanges"] = suggested_table_cell_style_changes
        if table_cell_style is not UNSET:
            field_dict["tableCellStyle"] = table_cell_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structural_element import StructuralElement
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_cell_suggested_table_cell_style_changes import TableCellSuggestedTableCellStyleChanges
        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[StructuralElement] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = StructuralElement.from_dict(content_item_data)



                content.append(content_item)


        end_index = d.pop("endIndex", UNSET)

        start_index = d.pop("startIndex", UNSET)

        suggested_deletion_ids = cast(list[str], d.pop("suggestedDeletionIds", UNSET))


        suggested_insertion_ids = cast(list[str], d.pop("suggestedInsertionIds", UNSET))


        _suggested_table_cell_style_changes = d.pop("suggestedTableCellStyleChanges", UNSET)
        suggested_table_cell_style_changes: TableCellSuggestedTableCellStyleChanges | Unset
        if isinstance(_suggested_table_cell_style_changes,  Unset):
            suggested_table_cell_style_changes = UNSET
        else:
            suggested_table_cell_style_changes = TableCellSuggestedTableCellStyleChanges.from_dict(_suggested_table_cell_style_changes)




        _table_cell_style = d.pop("tableCellStyle", UNSET)
        table_cell_style: TableCellStyle | Unset
        if isinstance(_table_cell_style,  Unset):
            table_cell_style = UNSET
        else:
            table_cell_style = TableCellStyle.from_dict(_table_cell_style)




        table_cell = cls(
            content=content,
            end_index=end_index,
            start_index=start_index,
            suggested_deletion_ids=suggested_deletion_ids,
            suggested_insertion_ids=suggested_insertion_ids,
            suggested_table_cell_style_changes=suggested_table_cell_style_changes,
            table_cell_style=table_cell_style,
        )


        table_cell.additional_properties = d
        return table_cell

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
