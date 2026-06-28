from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_holder import PermissionHolder





T = TypeVar("T", bound="PermissionGrant")



@_attrs_define
class PermissionGrant:
    """ Details about a permission granted to a user or group.

        Attributes:
            holder (PermissionHolder | Unset): Details of a user, group, field, or project role that holds a permission. See
                [Holder object](../api-group-permission-schemes/#holder-object) in *Get all permission schemes* for more
                information.
            id (int | Unset): The ID of the permission granted details.
            permission (str | Unset): The permission to grant. This permission can be one of the built-in permissions or a
                custom permission added by an app. See [Built-in permissions](../api-group-permission-schemes/#built-in-
                permissions) in *Get all permission schemes* for more information about the built-in permissions. See the
                [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and
                [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module
                documentation for more information about custom permissions.
            self_ (str | Unset): The URL of the permission granted details.
     """

    holder: PermissionHolder | Unset = UNSET
    id: int | Unset = UNSET
    permission: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_holder import PermissionHolder
        holder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.holder, Unset):
            holder = self.holder.to_dict()

        id = self.id

        permission = self.permission

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if holder is not UNSET:
            field_dict["holder"] = holder
        if id is not UNSET:
            field_dict["id"] = id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_holder import PermissionHolder
        d = dict(src_dict)
        _holder = d.pop("holder", UNSET)
        holder: PermissionHolder | Unset
        if isinstance(_holder,  Unset):
            holder = UNSET
        else:
            holder = PermissionHolder.from_dict(_holder)




        id = d.pop("id", UNSET)

        permission = d.pop("permission", UNSET)

        self_ = d.pop("self", UNSET)

        permission_grant = cls(
            holder=holder,
            id=id,
            permission=permission,
            self_=self_,
        )

        return permission_grant

