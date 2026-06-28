from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.share_permission import SharePermission





T = TypeVar("T", bound="DashboardDetails")



@_attrs_define
class DashboardDetails:
    """ Details of a dashboard.

        Attributes:
            edit_permissions (list[SharePermission]): The edit permissions for the dashboard.
            name (str): The name of the dashboard.
            share_permissions (list[SharePermission]): The share permissions for the dashboard.
            description (str | Unset): The description of the dashboard.
     """

    edit_permissions: list[SharePermission]
    name: str
    share_permissions: list[SharePermission]
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.share_permission import SharePermission
        edit_permissions = []
        for edit_permissions_item_data in self.edit_permissions:
            edit_permissions_item = edit_permissions_item_data.to_dict()
            edit_permissions.append(edit_permissions_item)



        name = self.name

        share_permissions = []
        for share_permissions_item_data in self.share_permissions:
            share_permissions_item = share_permissions_item_data.to_dict()
            share_permissions.append(share_permissions_item)



        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "editPermissions": edit_permissions,
            "name": name,
            "sharePermissions": share_permissions,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_permission import SharePermission
        d = dict(src_dict)
        edit_permissions = []
        _edit_permissions = d.pop("editPermissions")
        for edit_permissions_item_data in (_edit_permissions):
            edit_permissions_item = SharePermission.from_dict(edit_permissions_item_data)



            edit_permissions.append(edit_permissions_item)


        name = d.pop("name")

        share_permissions = []
        _share_permissions = d.pop("sharePermissions")
        for share_permissions_item_data in (_share_permissions):
            share_permissions_item = SharePermission.from_dict(share_permissions_item_data)



            share_permissions.append(share_permissions_item)


        description = d.pop("description", UNSET)

        dashboard_details = cls(
            edit_permissions=edit_permissions,
            name=name,
            share_permissions=share_permissions,
            description=description,
        )

        return dashboard_details

