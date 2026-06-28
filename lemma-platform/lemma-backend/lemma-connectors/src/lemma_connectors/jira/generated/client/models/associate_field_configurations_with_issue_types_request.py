from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.field_configuration_to_issue_type_mapping import FieldConfigurationToIssueTypeMapping





T = TypeVar("T", bound="AssociateFieldConfigurationsWithIssueTypesRequest")



@_attrs_define
class AssociateFieldConfigurationsWithIssueTypesRequest:
    """ Details of a field configuration to issue type mappings.

        Attributes:
            mappings (list[FieldConfigurationToIssueTypeMapping]): Field configuration to issue type mappings.
     """

    mappings: list[FieldConfigurationToIssueTypeMapping]





    def to_dict(self) -> dict[str, Any]:
        from ..models.field_configuration_to_issue_type_mapping import FieldConfigurationToIssueTypeMapping
        mappings = []
        for mappings_item_data in self.mappings:
            mappings_item = mappings_item_data.to_dict()
            mappings.append(mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mappings": mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_configuration_to_issue_type_mapping import FieldConfigurationToIssueTypeMapping
        d = dict(src_dict)
        mappings = []
        _mappings = d.pop("mappings")
        for mappings_item_data in (_mappings):
            mappings_item = FieldConfigurationToIssueTypeMapping.from_dict(mappings_item_data)



            mappings.append(mappings_item)


        associate_field_configurations_with_issue_types_request = cls(
            mappings=mappings,
        )

        return associate_field_configurations_with_issue_types_request

