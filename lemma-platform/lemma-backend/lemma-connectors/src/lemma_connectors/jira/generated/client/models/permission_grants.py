from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_grant import PermissionGrant





T = TypeVar("T", bound="PermissionGrants")



@_attrs_define
class PermissionGrants:
    """ List of permission grants.

        Attributes:
            expand (str | Unset): Expand options that include additional permission grant details in the response.
            permissions (list[PermissionGrant] | Unset): Permission grants list.
     """

    expand: str | Unset = UNSET
    permissions: list[PermissionGrant] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_grant import PermissionGrant
        expand = self.expand

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_grant import PermissionGrant
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionGrant] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = PermissionGrant.from_dict(permissions_item_data)



                permissions.append(permissions_item)


        permission_grants = cls(
            expand=expand,
            permissions=permissions,
        )

        return permission_grants

