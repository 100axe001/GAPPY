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





T = TypeVar("T", bound="DataSourceColumn")



@_attrs_define
class DataSourceColumn:
    """ A column in a data source.

        Attributes:
            formula (str | Unset): The formula of the calculated column.
            reference (DataSourceColumnReference | Unset): An unique identifier that references a data source column.
     """

    formula: str | Unset = UNSET
    reference: DataSourceColumnReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_column_reference import DataSourceColumnReference
        formula = self.formula

        reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if formula is not UNSET:
            field_dict["formula"] = formula
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_column_reference import DataSourceColumnReference
        d = dict(src_dict)
        formula = d.pop("formula", UNSET)

        _reference = d.pop("reference", UNSET)
        reference: DataSourceColumnReference | Unset
        if isinstance(_reference,  Unset):
            reference = UNSET
        else:
            reference = DataSourceColumnReference.from_dict(_reference)




        data_source_column = cls(
            formula=formula,
            reference=reference,
        )


        data_source_column.additional_properties = d
        return data_source_column

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
