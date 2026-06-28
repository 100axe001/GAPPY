from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_project_permission_grants import BulkProjectPermissionGrants





T = TypeVar("T", bound="BulkPermissionGrants")



@_attrs_define
class BulkPermissionGrants:
    """ Details of global and project permissions granted to the user.

        Attributes:
            global_permissions (list[str]): List of permissions granted to the user.
            project_permissions (list[BulkProjectPermissionGrants]): List of project permissions and the projects and issues
                those permissions provide access to.
     """

    global_permissions: list[str]
    project_permissions: list[BulkProjectPermissionGrants]





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_project_permission_grants import BulkProjectPermissionGrants
        global_permissions = self.global_permissions



        project_permissions = []
        for project_permissions_item_data in self.project_permissions:
            project_permissions_item = project_permissions_item_data.to_dict()
            project_permissions.append(project_permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "globalPermissions": global_permissions,
            "projectPermissions": project_permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_project_permission_grants import BulkProjectPermissionGrants
        d = dict(src_dict)
        global_permissions = cast(list[str], d.pop("globalPermissions"))


        project_permissions = []
        _project_permissions = d.pop("projectPermissions")
        for project_permissions_item_data in (_project_permissions):
            project_permissions_item = BulkProjectPermissionGrants.from_dict(project_permissions_item_data)



            project_permissions.append(project_permissions_item)


        bulk_permission_grants = cls(
            global_permissions=global_permissions,
            project_permissions=project_permissions,
        )

        return bulk_permission_grants

