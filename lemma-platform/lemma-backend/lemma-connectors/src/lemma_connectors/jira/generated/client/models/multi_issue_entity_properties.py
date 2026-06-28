from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_entity_properties_for_multi_update import IssueEntityPropertiesForMultiUpdate





T = TypeVar("T", bound="MultiIssueEntityProperties")



@_attrs_define
class MultiIssueEntityProperties:
    """ A list of issues and their respective properties to set or update. See [Entity
    properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/) for more information.

        Attributes:
            issues (list[IssueEntityPropertiesForMultiUpdate] | Unset): A list of issue IDs and their respective properties.
     """

    issues: list[IssueEntityPropertiesForMultiUpdate] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_entity_properties_for_multi_update import IssueEntityPropertiesForMultiUpdate
        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_entity_properties_for_multi_update import IssueEntityPropertiesForMultiUpdate
        d = dict(src_dict)
        _issues = d.pop("issues", UNSET)
        issues: list[IssueEntityPropertiesForMultiUpdate] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = IssueEntityPropertiesForMultiUpdate.from_dict(issues_item_data)



                issues.append(issues_item)


        multi_issue_entity_properties = cls(
            issues=issues,
        )

        return multi_issue_entity_properties

