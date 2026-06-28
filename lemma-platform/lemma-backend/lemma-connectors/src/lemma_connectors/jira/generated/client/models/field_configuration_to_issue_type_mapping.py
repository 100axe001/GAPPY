from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FieldConfigurationToIssueTypeMapping")



@_attrs_define
class FieldConfigurationToIssueTypeMapping:
    """ The field configuration to issue type mapping.

        Attributes:
            field_configuration_id (str): The ID of the field configuration.
            issue_type_id (str): The ID of the issue type or *default*. When set to *default* this field configuration issue
                type item applies to all issue types without a field configuration. An issue type can be included only once in a
                request.
     """

    field_configuration_id: str
    issue_type_id: str





    def to_dict(self) -> dict[str, Any]:
        field_configuration_id = self.field_configuration_id

        issue_type_id = self.issue_type_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fieldConfigurationId": field_configuration_id,
            "issueTypeId": issue_type_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_configuration_id = d.pop("fieldConfigurationId")

        issue_type_id = d.pop("issueTypeId")

        field_configuration_to_issue_type_mapping = cls(
            field_configuration_id=field_configuration_id,
            issue_type_id=issue_type_id,
        )

        return field_configuration_to_issue_type_mapping

