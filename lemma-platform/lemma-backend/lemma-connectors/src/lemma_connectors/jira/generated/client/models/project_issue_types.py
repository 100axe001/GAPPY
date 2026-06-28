from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_id import ProjectId





T = TypeVar("T", bound="ProjectIssueTypes")



@_attrs_define
class ProjectIssueTypes:
    """ Projects and issue types where the status is used. Only available if the `usages` expand is requested.

        Attributes:
            issue_types (list[str] | Unset): IDs of the issue types
            project (ProjectId | Unset): Project ID details.
     """

    issue_types: list[str] | Unset = UNSET
    project: ProjectId | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_id import ProjectId
        issue_types: list[str] | Unset = UNSET
        if not isinstance(self.issue_types, Unset):
            issue_types = self.issue_types



        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_types is not UNSET:
            field_dict["issueTypes"] = issue_types
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_id import ProjectId
        d = dict(src_dict)
        issue_types = cast(list[str], d.pop("issueTypes", UNSET))


        _project = d.pop("project", UNSET)
        project: ProjectId | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = ProjectId.from_dict(_project)




        project_issue_types = cls(
            issue_types=issue_types,
            project=project,
        )

        return project_issue_types

