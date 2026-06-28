from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="BulkProjectPermissionGrants")



@_attrs_define
class BulkProjectPermissionGrants:
    """ List of project permissions and the projects and issues those permissions grant access to.

        Attributes:
            issues (list[int]): IDs of the issues the user has the permission for.
            permission (str): A project permission,
            projects (list[int]): IDs of the projects the user has the permission for.
     """

    issues: list[int]
    permission: str
    projects: list[int]





    def to_dict(self) -> dict[str, Any]:
        issues = self.issues



        permission = self.permission

        projects = self.projects




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issues": issues,
            "permission": permission,
            "projects": projects,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issues = cast(list[int], d.pop("issues"))


        permission = d.pop("permission")

        projects = cast(list[int], d.pop("projects"))


        bulk_project_permission_grants = cls(
            issues=issues,
            permission=permission,
            projects=projects,
        )

        return bulk_project_permission_grants

