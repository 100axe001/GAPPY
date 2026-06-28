from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BulkProjectPermissions")



@_attrs_define
class BulkProjectPermissions:
    """ Details of project permissions and associated issues and projects to look up.

        Attributes:
            permissions (list[str]): List of project permissions.
            issues (list[int] | Unset): List of issue IDs.
            projects (list[int] | Unset): List of project IDs.
     """

    permissions: list[str]
    issues: list[int] | Unset = UNSET
    projects: list[int] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions



        issues: list[int] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues



        projects: list[int] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permissions": permissions,
        })
        if issues is not UNSET:
            field_dict["issues"] = issues
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))


        issues = cast(list[int], d.pop("issues", UNSET))


        projects = cast(list[int], d.pop("projects", UNSET))


        bulk_project_permissions = cls(
            permissions=permissions,
            issues=issues,
            projects=projects,
        )

        return bulk_project_permissions

