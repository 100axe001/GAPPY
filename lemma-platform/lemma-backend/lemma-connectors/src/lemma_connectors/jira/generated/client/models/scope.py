from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scope_type import ScopeType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_details import ProjectDetails





T = TypeVar("T", bound="Scope")



@_attrs_define
class Scope:
    """ The projects the item is associated with. Indicated for items associated with [next-gen
    projects](https://confluence.atlassian.com/x/loMyO).

        Attributes:
            project (ProjectDetails | Unset): Details about a project.
            type_ (ScopeType | Unset): The type of scope.
     """

    project: ProjectDetails | Unset = UNSET
    type_: ScopeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_details import ProjectDetails
        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if project is not UNSET:
            field_dict["project"] = project
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_details import ProjectDetails
        d = dict(src_dict)
        _project = d.pop("project", UNSET)
        project: ProjectDetails | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = ProjectDetails.from_dict(_project)




        _type_ = d.pop("type", UNSET)
        type_: ScopeType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ScopeType(_type_)




        scope = cls(
            project=project,
            type_=type_,
        )


        scope.additional_properties = d
        return scope

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
