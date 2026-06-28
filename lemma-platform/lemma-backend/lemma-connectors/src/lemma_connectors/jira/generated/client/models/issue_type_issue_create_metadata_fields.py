from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.field_metadata import FieldMetadata





T = TypeVar("T", bound="IssueTypeIssueCreateMetadataFields")



@_attrs_define
class IssueTypeIssueCreateMetadataFields:
    """ List of the fields available when creating an issue for the issue type.

     """

    additional_properties: dict[str, FieldMetadata] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_metadata import FieldMetadata
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_metadata import FieldMetadata
        d = dict(src_dict)
        issue_type_issue_create_metadata_fields = cls(
        )


        from ..models.field_metadata_configuration import FieldMetadataConfiguration
        from ..models.json_type_bean import JsonTypeBean
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FieldMetadata.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        issue_type_issue_create_metadata_fields.additional_properties = additional_properties
        return issue_type_issue_create_metadata_fields

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FieldMetadata:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FieldMetadata) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
