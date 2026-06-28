from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_identifier_bean import ProjectIdentifierBean





T = TypeVar("T", bound="PermittedProjects")



@_attrs_define
class PermittedProjects:
    """ A list of projects in which a user is granted permissions.

        Attributes:
            projects (list[ProjectIdentifierBean] | Unset): A list of projects.
     """

    projects: list[ProjectIdentifierBean] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_identifier_bean import ProjectIdentifierBean
        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_identifier_bean import ProjectIdentifierBean
        d = dict(src_dict)
        _projects = d.pop("projects", UNSET)
        projects: list[ProjectIdentifierBean] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = ProjectIdentifierBean.from_dict(projects_item_data)



                projects.append(projects_item)


        permitted_projects = cls(
            projects=projects,
        )

        return permitted_projects

