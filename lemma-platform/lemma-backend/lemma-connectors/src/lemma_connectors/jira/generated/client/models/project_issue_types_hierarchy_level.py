from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.issue_type_info import IssueTypeInfo





T = TypeVar("T", bound="ProjectIssueTypesHierarchyLevel")



@_attrs_define
class ProjectIssueTypesHierarchyLevel:
    """ Details of an issue type hierarchy level.

        Attributes:
            entity_id (UUID | Unset): The ID of the issue type hierarchy level. This property is deprecated, see [Change
                notice: Removing hierarchy level IDs from next-gen
                APIs](https://developer.atlassian.com/cloud/jira/platform/change-notice-removing-hierarchy-level-ids-from-next-
                gen-apis/).
            issue_types (list[IssueTypeInfo] | Unset): The list of issue types in the hierarchy level.
            level (int | Unset): The level of the issue type hierarchy level.
            name (str | Unset): The name of the issue type hierarchy level.
     """

    entity_id: UUID | Unset = UNSET
    issue_types: list[IssueTypeInfo] | Unset = UNSET
    level: int | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_type_info import IssueTypeInfo
        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        issue_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issue_types, Unset):
            issue_types = []
            for issue_types_item_data in self.issue_types:
                issue_types_item = issue_types_item_data.to_dict()
                issue_types.append(issue_types_item)



        level = self.level

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if issue_types is not UNSET:
            field_dict["issueTypes"] = issue_types
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_type_info import IssueTypeInfo
        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        _issue_types = d.pop("issueTypes", UNSET)
        issue_types: list[IssueTypeInfo] | Unset = UNSET
        if _issue_types is not UNSET:
            issue_types = []
            for issue_types_item_data in _issue_types:
                issue_types_item = IssueTypeInfo.from_dict(issue_types_item_data)



                issue_types.append(issue_types_item)


        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        project_issue_types_hierarchy_level = cls(
            entity_id=entity_id,
            issue_types=issue_types,
            level=level,
            name=name,
        )

        return project_issue_types_hierarchy_level

