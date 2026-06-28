from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.table_column_properties_width_type import TableColumnPropertiesWidthType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="TableColumnProperties")



@_attrs_define
class TableColumnProperties:
    """ The properties of a column in a table.

        Attributes:
            width (Dimension | Unset): A magnitude in a single direction in the specified units.
            width_type (TableColumnPropertiesWidthType | Unset): The width type of the column.
     """

    width: Dimension | Unset = UNSET
    width_type: TableColumnPropertiesWidthType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        width_type: str | Unset = UNSET
        if not isinstance(self.width_type, Unset):
            width_type = self.width_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if width is not UNSET:
            field_dict["width"] = width
        if width_type is not UNSET:
            field_dict["widthType"] = width_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _width = d.pop("width", UNSET)
        width: Dimension | Unset
        if isinstance(_width,  Unset):
            width = UNSET
        else:
            width = Dimension.from_dict(_width)




        _width_type = d.pop("widthType", UNSET)
        width_type: TableColumnPropertiesWidthType | Unset
        if isinstance(_width_type,  Unset):
            width_type = UNSET
        else:
            width_type = TableColumnPropertiesWidthType(_width_type)




        table_column_properties = cls(
            width=width,
            width_type=width_type,
        )


        table_column_properties.additional_properties = d
        return table_column_properties

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
