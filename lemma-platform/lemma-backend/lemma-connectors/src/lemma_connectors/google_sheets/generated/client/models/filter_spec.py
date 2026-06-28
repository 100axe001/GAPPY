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
  from ..models.filter_criteria import FilterCriteria





T = TypeVar("T", bound="FilterSpec")



@_attrs_define
class FilterSpec:
    """ The filter criteria associated with a specific column.

        Attributes:
            column_index (int | Unset): The column index.
            data_source_column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data
                source column.
            filter_criteria (FilterCriteria | Unset): Criteria for showing/hiding rows in a filter or filter view.
     """

    column_index: int | Unset = UNSET
    data_source_column_reference: DataSourceColumnReference | Unset = UNSET
    filter_criteria: FilterCriteria | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.filter_criteria import FilterCriteria
        column_index = self.column_index

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
        if column_index is not UNSET:
            field_dict["columnIndex"] = column_index
        if data_source_column_reference is not UNSET:
            field_dict["dataSourceColumnReference"] = data_source_column_reference
        if filter_criteria is not UNSET:
            field_dict["filterCriteria"] = filter_criteria

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        from ..models.filter_criteria import FilterCriteria
        d = dict(src_dict)
        column_index = d.pop("columnIndex", UNSET)

        _data_source_column_reference = d.pop("dataSourceColumnReference", UNSET)
        data_source_column_reference: DataSourceColumnReference | Unset
        if isinstance(_data_source_column_reference,  Unset):
            data_source_column_reference = UNSET
        else:
            data_source_column_reference = DataSourceColumnReference.from_dict(_data_source_column_reference)




        _filter_criteria = d.pop("filterCriteria", UNSET)
        filter_criteria: FilterCriteria | Unset
        if isinstance(_filter_criteria,  Unset):
            filter_criteria = UNSET
        else:
            filter_criteria = FilterCriteria.from_dict(_filter_criteria)




        filter_spec = cls(
            column_index=column_index,
            data_source_column_reference=data_source_column_reference,
            filter_criteria=filter_criteria,
        )


        filter_spec.additional_properties = d
        return filter_spec

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
