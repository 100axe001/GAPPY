from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.global_scope_bean import GlobalScopeBean
  from ..models.project_scope_bean import ProjectScopeBean





T = TypeVar("T", bound="IssueFieldOptionScopeBean")



@_attrs_define
class IssueFieldOptionScopeBean:
    """ 
        Attributes:
            global_ (GlobalScopeBean | Unset):
            projects (list[int] | Unset): DEPRECATED
            projects2 (list[ProjectScopeBean] | Unset): Defines the projects in which the option is available and the
                behavior of the option within each project. Specify one object per project. The behavior of the option in a
                project context overrides the behavior in the global context.
     """

    global_: GlobalScopeBean | Unset = UNSET
    projects: list[int] | Unset = UNSET
    projects2: list[ProjectScopeBean] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.global_scope_bean import GlobalScopeBean
        from ..models.project_scope_bean import ProjectScopeBean
        global_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_, Unset):
            global_ = self.global_.to_dict()

        projects: list[int] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects



        projects2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects2, Unset):
            projects2 = []
            for projects2_item_data in self.projects2:
                projects2_item = projects2_item_data.to_dict()
                projects2.append(projects2_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if global_ is not UNSET:
            field_dict["global"] = global_
        if projects is not UNSET:
            field_dict["projects"] = projects
        if projects2 is not UNSET:
            field_dict["projects2"] = projects2

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_scope_bean import GlobalScopeBean
        from ..models.project_scope_bean import ProjectScopeBean
        d = dict(src_dict)
        _global_ = d.pop("global", UNSET)
        global_: GlobalScopeBean | Unset
        if isinstance(_global_,  Unset):
            global_ = UNSET
        else:
            global_ = GlobalScopeBean.from_dict(_global_)




        projects = cast(list[int], d.pop("projects", UNSET))


        _projects2 = d.pop("projects2", UNSET)
        projects2: list[ProjectScopeBean] | Unset = UNSET
        if _projects2 is not UNSET:
            projects2 = []
            for projects2_item_data in _projects2:
                projects2_item = ProjectScopeBean.from_dict(projects2_item_data)



                projects2.append(projects2_item)


        issue_field_option_scope_bean = cls(
            global_=global_,
            projects=projects,
            projects2=projects2,
        )

        return issue_field_option_scope_bean

