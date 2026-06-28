from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_row_style import TableRowStyle
  from ..models.table_row_style_suggestion_state import TableRowStyleSuggestionState





T = TypeVar("T", bound="SuggestedTableRowStyle")



@_attrs_define
class SuggestedTableRowStyle:
    """ A suggested change to a TableRowStyle.

        Attributes:
            table_row_style (TableRowStyle | Unset): Styles that apply to a table row.
            table_row_style_suggestion_state (TableRowStyleSuggestionState | Unset): A mask that indicates which of the
                fields on the base TableRowStyle have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
     """

    table_row_style: TableRowStyle | Unset = UNSET
    table_row_style_suggestion_state: TableRowStyleSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_row_style import TableRowStyle
        from ..models.table_row_style_suggestion_state import TableRowStyleSuggestionState
        table_row_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_row_style, Unset):
            table_row_style = self.table_row_style.to_dict()

        table_row_style_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_row_style_suggestion_state, Unset):
            table_row_style_suggestion_state = self.table_row_style_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if table_row_style is not UNSET:
            field_dict["tableRowStyle"] = table_row_style
        if table_row_style_suggestion_state is not UNSET:
            field_dict["tableRowStyleSuggestionState"] = table_row_style_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_row_style import TableRowStyle
        from ..models.table_row_style_suggestion_state import TableRowStyleSuggestionState
        d = dict(src_dict)
        _table_row_style = d.pop("tableRowStyle", UNSET)
        table_row_style: TableRowStyle | Unset
        if isinstance(_table_row_style,  Unset):
            table_row_style = UNSET
        else:
            table_row_style = TableRowStyle.from_dict(_table_row_style)




        _table_row_style_suggestion_state = d.pop("tableRowStyleSuggestionState", UNSET)
        table_row_style_suggestion_state: TableRowStyleSuggestionState | Unset
        if isinstance(_table_row_style_suggestion_state,  Unset):
            table_row_style_suggestion_state = UNSET
        else:
            table_row_style_suggestion_state = TableRowStyleSuggestionState.from_dict(_table_row_style_suggestion_state)




        suggested_table_row_style = cls(
            table_row_style=table_row_style,
            table_row_style_suggestion_state=table_row_style_suggestion_state,
        )


        suggested_table_row_style.additional_properties = d
        return suggested_table_row_style

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
