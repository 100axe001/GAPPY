from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.table_column_properties import TableColumnProperties





T = TypeVar("T", bound="TableStyle")



@_attrs_define
class TableStyle:
    """ Styles that apply to a table.

        Attributes:
            table_column_properties (list[TableColumnProperties] | Unset): The properties of each column. Note that in Docs,
                tables contain rows and rows contain cells, similar to HTML. So the properties for a row can be found on the
                row's table_row_style.
     """

    table_column_properties: list[TableColumnProperties] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_column_properties import TableColumnProperties
        table_column_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_column_properties, Unset):
            table_column_properties = []
            for table_column_properties_item_data in self.table_column_properties:
                table_column_properties_item = table_column_properties_item_data.to_dict()
                table_column_properties.append(table_column_properties_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if table_column_properties is not UNSET:
            field_dict["tableColumnProperties"] = table_column_properties

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column_properties import TableColumnProperties
        d = dict(src_dict)
        _table_column_properties = d.pop("tableColumnProperties", UNSET)
        table_column_properties: list[TableColumnProperties] | Unset = UNSET
        if _table_column_properties is not UNSET:
            table_column_properties = []
            for table_column_properties_item_data in _table_column_properties:
                table_column_properties_item = TableColumnProperties.from_dict(table_column_properties_item_data)



                table_column_properties.append(table_column_properties_item)


        table_style = cls(
            table_column_properties=table_column_properties,
        )


        table_style.additional_properties = d
        return table_style

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
