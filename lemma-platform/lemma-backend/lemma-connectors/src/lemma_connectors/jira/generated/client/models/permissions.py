from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permissions_permissions import PermissionsPermissions





T = TypeVar("T", bound="Permissions")



@_attrs_define
class Permissions:
    """ Details about permissions.

        Attributes:
            permissions (PermissionsPermissions | Unset): List of permissions.
     """

    permissions: PermissionsPermissions | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permissions_permissions import PermissionsPermissions
        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permissions_permissions import PermissionsPermissions
        d = dict(src_dict)
        _permissions = d.pop("permissions", UNSET)
        permissions: PermissionsPermissions | Unset
        if isinstance(_permissions,  Unset):
            permissions = UNSET
        else:
            permissions = PermissionsPermissions.from_dict(_permissions)




        permissions = cls(
            permissions=permissions,
        )

        return permissions

