from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_source_object_reference import DataSourceObjectReference





T = TypeVar("T", bound="DataSourceObjectReferences")



@_attrs_define
class DataSourceObjectReferences:
    """ A list of references to data source objects.

        Attributes:
            references (list[DataSourceObjectReference] | Unset): The references.
     """

    references: list[DataSourceObjectReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_source_object_reference import DataSourceObjectReference
        references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_object_reference import DataSourceObjectReference
        d = dict(src_dict)
        _references = d.pop("references", UNSET)
        references: list[DataSourceObjectReference] | Unset = UNSET
        if _references is not UNSET:
            references = []
            for references_item_data in _references:
                references_item = DataSourceObjectReference.from_dict(references_item_data)



                references.append(references_item)


        data_source_object_references = cls(
            references=references,
        )


        data_source_object_references.additional_properties = d
        return data_source_object_references

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
