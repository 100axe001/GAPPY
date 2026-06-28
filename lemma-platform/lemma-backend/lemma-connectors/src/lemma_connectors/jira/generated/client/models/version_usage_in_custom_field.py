from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VersionUsageInCustomField")



@_attrs_define
class VersionUsageInCustomField:
    """ List of custom fields using the version.

        Attributes:
            custom_field_id (int | Unset): The ID of the custom field.
            field_name (str | Unset): The name of the custom field.
            issue_count_with_version_in_custom_field (int | Unset): Count of the issues where the custom field contains the
                version.
     """

    custom_field_id: int | Unset = UNSET
    field_name: str | Unset = UNSET
    issue_count_with_version_in_custom_field: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        custom_field_id = self.custom_field_id

        field_name = self.field_name

        issue_count_with_version_in_custom_field = self.issue_count_with_version_in_custom_field


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom_field_id is not UNSET:
            field_dict["customFieldId"] = custom_field_id
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if issue_count_with_version_in_custom_field is not UNSET:
            field_dict["issueCountWithVersionInCustomField"] = issue_count_with_version_in_custom_field

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_field_id = d.pop("customFieldId", UNSET)

        field_name = d.pop("fieldName", UNSET)

        issue_count_with_version_in_custom_field = d.pop("issueCountWithVersionInCustomField", UNSET)

        version_usage_in_custom_field = cls(
            custom_field_id=custom_field_id,
            field_name=field_name,
            issue_count_with_version_in_custom_field=issue_count_with_version_in_custom_field,
        )

        return version_usage_in_custom_field

