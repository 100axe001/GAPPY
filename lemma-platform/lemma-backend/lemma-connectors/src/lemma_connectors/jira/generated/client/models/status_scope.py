from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.status_scope_type import StatusScopeType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_id import ProjectId





T = TypeVar("T", bound="StatusScope")



@_attrs_define
class StatusScope:
    """ The scope of the status.

        Attributes:
            type_ (StatusScopeType): The scope of the status. `GLOBAL` for company-managed projects and `PROJECT` for team-
                managed projects.
            project (ProjectId | Unset): Project ID details.
     """

    type_: StatusScopeType
    project: ProjectId | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_id import ProjectId
        type_ = self.type_.value

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_id import ProjectId
        d = dict(src_dict)
        type_ = StatusScopeType(d.pop("type"))




        _project = d.pop("project", UNSET)
        project: ProjectId | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = ProjectId.from_dict(_project)




        status_scope = cls(
            type_=type_,
            project=project,
        )

        return status_scope

