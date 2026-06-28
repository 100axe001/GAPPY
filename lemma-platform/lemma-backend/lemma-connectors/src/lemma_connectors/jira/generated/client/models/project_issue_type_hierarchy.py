from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_issue_types_hierarchy_level import ProjectIssueTypesHierarchyLevel





T = TypeVar("T", bound="ProjectIssueTypeHierarchy")



@_attrs_define
class ProjectIssueTypeHierarchy:
    """ The hierarchy of issue types within a project.

        Attributes:
            hierarchy (list[ProjectIssueTypesHierarchyLevel] | Unset): Details of an issue type hierarchy level.
            project_id (int | Unset): The ID of the project.
     """

    hierarchy: list[ProjectIssueTypesHierarchyLevel] | Unset = UNSET
    project_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_issue_types_hierarchy_level import ProjectIssueTypesHierarchyLevel
        hierarchy: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hierarchy, Unset):
            hierarchy = []
            for hierarchy_item_data in self.hierarchy:
                hierarchy_item = hierarchy_item_data.to_dict()
                hierarchy.append(hierarchy_item)



        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hierarchy is not UNSET:
            field_dict["hierarchy"] = hierarchy
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_issue_types_hierarchy_level import ProjectIssueTypesHierarchyLevel
        d = dict(src_dict)
        _hierarchy = d.pop("hierarchy", UNSET)
        hierarchy: list[ProjectIssueTypesHierarchyLevel] | Unset = UNSET
        if _hierarchy is not UNSET:
            hierarchy = []
            for hierarchy_item_data in _hierarchy:
                hierarchy_item = ProjectIssueTypesHierarchyLevel.from_dict(hierarchy_item_data)



                hierarchy.append(hierarchy_item)


        project_id = d.pop("projectId", UNSET)

        project_issue_type_hierarchy = cls(
            hierarchy=hierarchy,
            project_id=project_id,
        )

        return project_issue_type_hierarchy

