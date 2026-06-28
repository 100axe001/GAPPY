from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="TableRowStyle")



@_attrs_define
class TableRowStyle:
    """ Styles that apply to a table row.

        Attributes:
            min_row_height (Dimension | Unset): A magnitude in a single direction in the specified units.
            prevent_overflow (bool | Unset): Whether the row cannot overflow across page or column boundaries.
            table_header (bool | Unset): Whether the row is a table header.
     """

    min_row_height: Dimension | Unset = UNSET
    prevent_overflow: bool | Unset = UNSET
    table_header: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        min_row_height: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_row_height, Unset):
            min_row_height = self.min_row_height.to_dict()

        prevent_overflow = self.prevent_overflow

        table_header = self.table_header


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_row_height is not UNSET:
            field_dict["minRowHeight"] = min_row_height
        if prevent_overflow is not UNSET:
            field_dict["preventOverflow"] = prevent_overflow
        if table_header is not UNSET:
            field_dict["tableHeader"] = table_header

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _min_row_height = d.pop("minRowHeight", UNSET)
        min_row_height: Dimension | Unset
        if isinstance(_min_row_height,  Unset):
            min_row_height = UNSET
        else:
            min_row_height = Dimension.from_dict(_min_row_height)




        prevent_overflow = d.pop("preventOverflow", UNSET)

        table_header = d.pop("tableHeader", UNSET)

        table_row_style = cls(
            min_row_height=min_row_height,
            prevent_overflow=prevent_overflow,
            table_header=table_header,
        )


        table_row_style.additional_properties = d
        return table_row_style

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
