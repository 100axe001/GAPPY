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
  from ..models.scope import Scope





T = TypeVar("T", bound="PermissionScheme")



@_attrs_define
class PermissionScheme:
    """ Details of a permission scheme.

        Attributes:
            name (str): The name of the permission scheme. Must be unique.
            description (str | Unset): A description for the permission scheme.
            expand (str | Unset): The expand options available for the permission scheme.
            id (int | Unset): The ID of the permission scheme.
            permissions (list[PermissionGrant] | Unset): The permission scheme to create or update. See [About permission
                schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more information.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            self_ (str | Unset): The URL of the permission scheme.
     """

    name: str
    description: str | Unset = UNSET
    expand: str | Unset = UNSET
    id: int | Unset = UNSET
    permissions: list[PermissionGrant] | Unset = UNSET
    scope: Scope | Unset = UNSET
    self_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_grant import PermissionGrant
        from ..models.scope import Scope
        name = self.name

        description = self.description

        expand = self.expand

        id = self.id

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)



        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        self_ = self.self_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if expand is not UNSET:
            field_dict["expand"] = expand
        if id is not UNSET:
            field_dict["id"] = id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if scope is not UNSET:
            field_dict["scope"] = scope
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_grant import PermissionGrant
        from ..models.scope import Scope
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        expand = d.pop("expand", UNSET)

        id = d.pop("id", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionGrant] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = PermissionGrant.from_dict(permissions_item_data)



                permissions.append(permissions_item)


        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        self_ = d.pop("self", UNSET)

        permission_scheme = cls(
            name=name,
            description=description,
            expand=expand,
            id=id,
            permissions=permissions,
            scope=scope,
            self_=self_,
        )


        permission_scheme.additional_properties = d
        return permission_scheme

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
