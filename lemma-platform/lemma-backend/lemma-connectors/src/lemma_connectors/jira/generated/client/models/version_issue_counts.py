from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.version_usage_in_custom_field import VersionUsageInCustomField





T = TypeVar("T", bound="VersionIssueCounts")



@_attrs_define
class VersionIssueCounts:
    """ Various counts of issues within a version.

        Attributes:
            custom_field_usage (list[VersionUsageInCustomField] | Unset): List of custom fields using the version.
            issue_count_with_custom_fields_showing_version (int | Unset): Count of issues where a version custom field is
                set to the version.
            issues_affected_count (int | Unset): Count of issues where the `affectedVersion` is set to the version.
            issues_fixed_count (int | Unset): Count of issues where the `fixVersion` is set to the version.
            self_ (str | Unset): The URL of these count details.
     """

    custom_field_usage: list[VersionUsageInCustomField] | Unset = UNSET
    issue_count_with_custom_fields_showing_version: int | Unset = UNSET
    issues_affected_count: int | Unset = UNSET
    issues_fixed_count: int | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.version_usage_in_custom_field import VersionUsageInCustomField
        custom_field_usage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_field_usage, Unset):
            custom_field_usage = []
            for custom_field_usage_item_data in self.custom_field_usage:
                custom_field_usage_item = custom_field_usage_item_data.to_dict()
                custom_field_usage.append(custom_field_usage_item)



        issue_count_with_custom_fields_showing_version = self.issue_count_with_custom_fields_showing_version

        issues_affected_count = self.issues_affected_count

        issues_fixed_count = self.issues_fixed_count

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom_field_usage is not UNSET:
            field_dict["customFieldUsage"] = custom_field_usage
        if issue_count_with_custom_fields_showing_version is not UNSET:
            field_dict["issueCountWithCustomFieldsShowingVersion"] = issue_count_with_custom_fields_showing_version
        if issues_affected_count is not UNSET:
            field_dict["issuesAffectedCount"] = issues_affected_count
        if issues_fixed_count is not UNSET:
            field_dict["issuesFixedCount"] = issues_fixed_count
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.version_usage_in_custom_field import VersionUsageInCustomField
        d = dict(src_dict)
        _custom_field_usage = d.pop("customFieldUsage", UNSET)
        custom_field_usage: list[VersionUsageInCustomField] | Unset = UNSET
        if _custom_field_usage is not UNSET:
            custom_field_usage = []
            for custom_field_usage_item_data in _custom_field_usage:
                custom_field_usage_item = VersionUsageInCustomField.from_dict(custom_field_usage_item_data)



                custom_field_usage.append(custom_field_usage_item)


        issue_count_with_custom_fields_showing_version = d.pop("issueCountWithCustomFieldsShowingVersion", UNSET)

        issues_affected_count = d.pop("issuesAffectedCount", UNSET)

        issues_fixed_count = d.pop("issuesFixedCount", UNSET)

        self_ = d.pop("self", UNSET)

        version_issue_counts = cls(
            custom_field_usage=custom_field_usage,
            issue_count_with_custom_fields_showing_version=issue_count_with_custom_fields_showing_version,
            issues_affected_count=issues_affected_count,
            issues_fixed_count=issues_fixed_count,
            self_=self_,
        )

        return version_issue_counts

