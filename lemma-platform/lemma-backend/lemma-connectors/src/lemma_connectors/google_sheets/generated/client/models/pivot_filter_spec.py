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
  from ..models.pivot_filter_criteria import PivotFilterCriteria





T = TypeVar("T", bound="PivotFilterSpec")



@_attrs_define
class PivotFilterSpec:
    """ The pivot table filter criteria associated with a specific source column offset.

        Attributes:
            column_offset_index (int | Unset): The column offset of the source range.
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            filter_criteria (PivotFilterCriteria | Unset): Criteria for showing/hiding rows in a pivot table.
     """

    column_offset_index: int | Unset = UNSET
    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    filter_criteria: PivotFilterCriteria | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.pivot_filter_criteria import PivotFilterCriteria
        column_offset_index = self.column_offset_index

        data_source_column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_source_column_reference, Unset):
            data_source_column_reference = self.data_source_column_reference.to_dict()

        filter_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_criteria, Unset):
            filter_criteria = self.filter_criteria.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_offset_index is not UNSET:
            field_dict["columnOffsetIndex"] = column_offset_index
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if filter_criteria is not UNSET:
            field_dict["filterCriteria"] = filter_criteria

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.pivot_filter_criteria import PivotFilterCriteria
        d = dict(src_dict)
        column_offset_index = d.pop("columnOffsetIndex", UNSET)

        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        _filter_criteria = d.pop("filterCriteria", UNSET)
        filter_criteria: PivotFilterCriteria | Unset
        if isinstance(_filter_criteria,  Unset):
            filter_criteria = UNSET
        else:
            filter_criteria = PivotFilterCriteria.from_dict(_filter_criteria)




        pivot_filter_spec = cls(
            column_offset_index=column_offset_index,
            data_source_column_reference=data_source_column_reference,
            filter_criteria=filter_criteria,
        )


        pivot_filter_spec.additional_properties = d
        return pivot_filter_spec

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
