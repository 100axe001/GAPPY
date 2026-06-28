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
  from ..models.table_column_properties import TableColumnProperties





T = TypeVar("T", bound="UpdateTableColumnPropertiesRequest")



@_attrs_define
class UpdateTableColumnPropertiesRequest:
    """ Updates the TableColumnProperties of columns in a table.

        Attributes:
            column_indices (list[int] | Unset): The list of zero-based column indices whose property should be updated. If
                no indices are specified, all columns will be updated.
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `tableColumnProperties` is implied and should not be specified. A single `"*"` can be used as short-hand for
                listing every field. For example to update the column width, set `fields` to `"width"`.
            table_column_properties (TableColumnProperties | Unset): The properties of a column in a table.
            table_start_location (Location | Unset): A particular location in the document.
     """

    column_indices: list[int] | Unset = UNSET
    fields: str | Unset = UNSET
    table_column_properties: TableColumnProperties | Unset = UNSET
    table_start_location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.location import Location
        from ..models.table_column_properties import TableColumnProperties
        column_indices: list[int] | Unset = UNSET
        if not isinstance(self.column_indices, Unset):
            column_indices = self.column_indices



        fields = self.fields

        table_column_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_column_properties, Unset):
            table_column_properties = self.table_column_properties.to_dict()

        table_start_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_start_location, Unset):
            table_start_location = self.table_start_location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_indices is not UNSET:
            field_dict["columnIndices"] = column_indices
        if fields is not UNSET:
            field_dict["fields"] = fields
        if table_column_properties is not UNSET:
            field_dict["tableColumnProperties"] = table_column_properties
        if table_start_location is not UNSET:
            field_dict["tableStartLocation"] = table_start_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location
        from ..models.table_column_properties import TableColumnProperties
        d = dict(src_dict)
        column_indices = cast(list[int], d.pop("columnIndices", UNSET))


        fields = d.pop("fields", UNSET)

        _table_column_properties = d.pop("tableColumnProperties", UNSET)
        table_column_properties: TableColumnProperties | Unset
        if isinstance(_table_column_properties,  Unset):
            table_column_properties = UNSET
        else:
            table_column_properties = TableColumnProperties.from_dict(_table_column_properties)




        _table_start_location = d.pop("tableStartLocation", UNSET)
        table_start_location: Location | Unset
        if isinstance(_table_start_location,  Unset):
            table_start_location = UNSET
        else:
            table_start_location = Location.from_dict(_table_start_location)




        update_table_column_properties_request = cls(
            column_indices=column_indices,
            fields=fields,
            table_column_properties=table_column_properties,
            table_start_location=table_start_location,
        )


        update_table_column_properties_request.additional_properties = d
        return update_table_column_properties_request

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
