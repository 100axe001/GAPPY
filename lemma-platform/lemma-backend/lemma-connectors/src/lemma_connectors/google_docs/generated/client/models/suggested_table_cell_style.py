from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_cell_style import TableCellStyle
  from ..models.table_cell_style_suggestion_state import TableCellStyleSuggestionState





T = TypeVar("T", bound="SuggestedTableCellStyle")



@_attrs_define
class SuggestedTableCellStyle:
    """ A suggested change to a TableCellStyle.

        Attributes:
            table_cell_style (TableCellStyle | Unset): The style of a TableCell. Inherited table cell styles are represented
                as unset fields in this message. A table cell style can inherit from the table's style.
            table_cell_style_suggestion_state (TableCellStyleSuggestionState | Unset): A mask that indicates which of the
                fields on the base TableCellStyle have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
     """

    table_cell_style: TableCellStyle | Unset = UNSET
    table_cell_style_suggestion_state: TableCellStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_cell_style_suggestion_state import TableCellStyleSuggestionState
        table_cell_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_style, Unset):
            table_cell_style = self.table_cell_style.to_dict()

        table_cell_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_cell_style_suggestion_state, Unset):
            table_cell_style_suggestion_state = self.table_cell_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if table_cell_style is not UNSET:
            field_dict["tableCellStyle"] = table_cell_style
        if table_cell_style_suggestion_state is not UNSET:
            field_dict["tableCellStyleSuggestionState"] = table_cell_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_cell_style import TableCellStyle
        from ..models.table_cell_style_suggestion_state import TableCellStyleSuggestionState
        d = dict(src_dict)
        _table_cell_style = d.pop("tableCellStyle", UNSET)
        table_cell_style: TableCellStyle | Unset
        if isinstance(_table_cell_style,  Unset):
            table_cell_style = UNSET
        else:
            table_cell_style = TableCellStyle.from_dict(_table_cell_style)




        _table_cell_style_suggestion_state = d.pop("tableCellStyleSuggestionState", UNSET)
        table_cell_style_suggestion_state: TableCellStyleSuggestionState | Unset
        if isinstance(_table_cell_style_suggestion_state,  Unset):
            table_cell_style_suggestion_state = UNSET
        else:
            table_cell_style_suggestion_state = TableCellStyleSuggestionState.from_dict(_table_cell_style_suggestion_state)




        suggested_table_cell_style = cls(
            table_cell_style=table_cell_style,
            table_cell_style_suggestion_state=table_cell_style_suggestion_state,
        )


        suggested_table_cell_style.additional_properties = d
        return suggested_table_cell_style

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
