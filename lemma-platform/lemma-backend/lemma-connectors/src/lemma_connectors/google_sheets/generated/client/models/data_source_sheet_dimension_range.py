from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_column_reference import DataSourceColumnReference





T = TypeVar("T", bound="DataSourceSheetDimensionRange")



@_attrs_define
class DataSourceSheetDimensionRange:
    """ A range along a single dimension on a DATA_SOURCE sheet.

        Attributes:
            column_references (list[DataSourceColumnReference] | Unset): The columns on the data source sheet.
            sheet_id (int | Unset): The ID of the data source sheet the range is on.
     """

    column_references: list[DataSourceColumnReference] | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        column_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.column_references, Unset):
            column_references = []
            for column_references_item_data in self.column_references:
                column_references_item = column_references_item_data.to_dict()
                column_references.append(column_references_item)



        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_references is not UNSET:
            field_dict["columnReferences"] = column_references
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        d = dict(src_dict)
        _column_references = d.pop("columnReferences", UNSET)
        column_references: list[DataSourceColumnReference] | Unset = UNSET
        if _column_references is not UNSET:
            column_references = []
            for column_references_item_data in _column_references:
                column_references_item = DataSourceColumnReference.from_dict(column_references_item_data)



                column_references.append(column_references_item)


        sheet_id = d.pop("sheetId", UNSET)

        data_source_sheet_dimension_range = cls(
            column_references=column_references,
            sheet_id=sheet_id,
        )


        data_source_sheet_dimension_range.additional_properties = d
        return data_source_sheet_dimension_range

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
