from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FieldConfigurationIssueTypeItem")



@_attrs_define
class FieldConfigurationIssueTypeItem:
    """ The field configuration for an issue type.

        Attributes:
            field_configuration_id (str): The ID of the field configuration.
            field_configuration_scheme_id (str): The ID of the field configuration scheme.
            issue_type_id (str): The ID of the issue type or *default*. When set to *default* this field configuration issue
                type item applies to all issue types without a field configuration.
     """

    field_configuration_id: str
    field_configuration_scheme_id: str
    issue_type_id: str





    def to_dict(self) -> dict[str, Any]:
        field_configuration_id = self.field_configuration_id

        field_configuration_scheme_id = self.field_configuration_scheme_id

        issue_type_id = self.issue_type_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fieldConfigurationId": field_configuration_id,
            "fieldConfigurationSchemeId": field_configuration_scheme_id,
            "issueTypeId": issue_type_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_configuration_id = d.pop("fieldConfigurationId")

        field_configuration_scheme_id = d.pop("fieldConfigurationSchemeId")

        issue_type_id = d.pop("issueTypeId")

        field_configuration_issue_type_item = cls(
            field_configuration_id=field_configuration_id,
            field_configuration_scheme_id=field_configuration_scheme_id,
            issue_type_id=issue_type_id,
        )

        return field_configuration_issue_type_item

