from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_issue_create_metadata import ProjectIssueCreateMetadata





T = TypeVar("T", bound="IssueCreateMetadata")



@_attrs_define
class IssueCreateMetadata:
    """ The wrapper for the issue creation metadata for a list of projects.

        Attributes:
            expand (str | Unset): Expand options that include additional project details in the response.
            projects (list[ProjectIssueCreateMetadata] | Unset): List of projects and their issue creation metadata.
     """

    expand: str | Unset = UNSET
    projects: list[ProjectIssueCreateMetadata] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_issue_create_metadata import ProjectIssueCreateMetadata
        expand = self.expand

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_issue_create_metadata import ProjectIssueCreateMetadata
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        _projects = d.pop("projects", UNSET)
        projects: list[ProjectIssueCreateMetadata] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = ProjectIssueCreateMetadata.from_dict(projects_item_data)



                projects.append(projects_item)


        issue_create_metadata = cls(
            expand=expand,
            projects=projects,
        )

        return issue_create_metadata

