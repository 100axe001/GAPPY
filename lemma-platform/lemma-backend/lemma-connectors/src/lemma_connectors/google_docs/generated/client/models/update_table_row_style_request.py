from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location import Location
  from ..models.table_row_style import TableRowStyle





T = TypeVar("T", bound="UpdateTableRowStyleRequest")



@_attrs_define
class UpdateTableRowStyleRequest:
    """ Updates the TableRowStyle of rows in a table.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `tableRowStyle` is implied and should not be specified. A single `"*"` can be used as short-hand for listing
                every field. For example to update the minimum row height, set `fields` to `"min_row_height"`.
            row_indices (list[int] | Unset): The list of zero-based row indices whose style should be updated. If no indices
                are specified, all rows will be updated.
            table_row_style (TableRowStyle | Unset): Styles that apply to a table row.
            table_start_location (Location | Unset): A particular location in the document.
     """

    fields: str | Unset = UNSET
    row_indices: list[int] | Unset = UNSET
    table_row_style: TableRowStyle | Unset = UNSET
    table_start_location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        from ..models.table_row_style import TableRowStyle
        fields = self.fields

        row_indices: list[int] | Unset = UNSET
        if not isinstance(self.row_indices, Unset):
            row_indices = self.row_indices



        table_row_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_row_style, Unset):
            table_row_style = self.table_row_style.to_dict()

        table_start_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_start_location, Unset):
            table_start_location = self.table_start_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if row_indices is not UNSET:
            field_dict["rowIndices"] = row_indices
        if table_row_style is not UNSET:
            field_dict["tableRowStyle"] = table_row_style
        if table_start_location is not UNSET:
            field_dict["tableStartLocation"] = table_start_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        from ..models.table_row_style import TableRowStyle
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        row_indices = cast(list[int], d.pop("rowIndices", UNSET))


        _table_row_style = d.pop("tableRowStyle", UNSET)
        table_row_style: TableRowStyle | Unset
        if isinstance(_table_row_style,  Unset):
            table_row_style = UNSET
        else:
            table_row_style = TableRowStyle.from_dict(_table_row_style)




        _table_start_location = d.pop("tableStartLocation", UNSET)
        table_start_location: Location | Unset
        if isinstance(_table_start_location,  Unset):
            table_start_location = UNSET
        else:
            table_start_location = Location.from_dict(_table_start_location)




        update_table_row_style_request = cls(
            fields=fields,
            row_indices=row_indices,
            table_row_style=table_row_style,
            table_start_location=table_start_location,
        )


        update_table_row_style_request.additional_properties = d
        return update_table_row_style_request

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
