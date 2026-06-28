from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_scheme import PermissionScheme





T = TypeVar("T", bound="PermissionSchemes")



@_attrs_define
class PermissionSchemes:
    """ List of all permission schemes.

        Attributes:
            permission_schemes (list[PermissionScheme] | Unset): Permission schemes list.
     """

    permission_schemes: list[PermissionScheme] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_scheme import PermissionScheme
        permission_schemes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permission_schemes, Unset):
            permission_schemes = []
            for permission_schemes_item_data in self.permission_schemes:
                permission_schemes_item = permission_schemes_item_data.to_dict()
                permission_schemes.append(permission_schemes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if permission_schemes is not UNSET:
            field_dict["permissionSchemes"] = permission_schemes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_scheme import PermissionScheme
        d = dict(src_dict)
        _permission_schemes = d.pop("permissionSchemes", UNSET)
        permission_schemes: list[PermissionScheme] | Unset = UNSET
        if _permission_schemes is not UNSET:
            permission_schemes = []
            for permission_schemes_item_data in _permission_schemes:
                permission_schemes_item = PermissionScheme.from_dict(permission_schemes_item_data)



                permission_schemes.append(permission_schemes_item)


        permission_schemes = cls(
            permission_schemes=permission_schemes,
        )

        return permission_schemes

