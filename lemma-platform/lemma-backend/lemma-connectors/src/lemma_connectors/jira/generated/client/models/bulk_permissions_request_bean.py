from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_project_permissions import BulkProjectPermissions





T = TypeVar("T", bound="BulkPermissionsRequestBean")



@_attrs_define
class BulkPermissionsRequestBean:
    """ Details of global permissions to look up and project permissions with associated projects and issues to look up.

        Attributes:
            account_id (str | Unset): The account ID of a user.
            global_permissions (list[str] | Unset): Global permissions to look up.
            project_permissions (list[BulkProjectPermissions] | Unset): Project permissions with associated projects and
                issues to look up.
     """

    account_id: str | Unset = UNSET
    global_permissions: list[str] | Unset = UNSET
    project_permissions: list[BulkProjectPermissions] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_project_permissions import BulkProjectPermissions
        account_id = self.account_id

        global_permissions: list[str] | Unset = UNSET
        if not isinstance(self.global_permissions, Unset):
            global_permissions = self.global_permissions



        project_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = []
            for project_permissions_item_data in self.project_permissions:
                project_permissions_item = project_permissions_item_data.to_dict()
                project_permissions.append(project_permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions
        if project_permissions is not UNSET:
            field_dict["projectPermissions"] = project_permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_project_permissions import BulkProjectPermissions
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        global_permissions = cast(list[str], d.pop("globalPermissions", UNSET))


        _project_permissions = d.pop("projectPermissions", UNSET)
        project_permissions: list[BulkProjectPermissions] | Unset = UNSET
        if _project_permissions is not UNSET:
            project_permissions = []
            for project_permissions_item_data in _project_permissions:
                project_permissions_item = BulkProjectPermissions.from_dict(project_permissions_item_data)



                project_permissions.append(project_permissions_item)


        bulk_permissions_request_bean = cls(
            account_id=account_id,
            global_permissions=global_permissions,
            project_permissions=project_permissions,
        )

        return bulk_permissions_request_bean

