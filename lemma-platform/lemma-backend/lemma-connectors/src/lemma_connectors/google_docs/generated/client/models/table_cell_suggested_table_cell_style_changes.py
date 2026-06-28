from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.suggested_table_cell_style import SuggestedTableCellStyle





T = TypeVar("T", bound="TableCellSuggestedTableCellStyleChanges")



@_attrs_define
class TableCellSuggestedTableCellStyleChanges:
    """ The suggested changes to the table cell style, keyed by suggestion ID.

     """

    additional_properties: dict[str, SuggestedTableCellStyle] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.suggested_table_cell_style import SuggestedTableCellStyle
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suggested_table_cell_style import SuggestedTableCellStyle
        d = dict(src_dict)
        table_cell_suggested_table_cell_style_changes = cls(
        )


        from ..models.table_cell_style import TableCellStyle
        from ..models.table_cell_style_suggestion_state import TableCellStyleSuggestionState
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = SuggestedTableCellStyle.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        table_cell_suggested_table_cell_style_changes.additional_properties = additional_properties
        return table_cell_suggested_table_cell_style_changes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> SuggestedTableCellStyle:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: SuggestedTableCellStyle) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
