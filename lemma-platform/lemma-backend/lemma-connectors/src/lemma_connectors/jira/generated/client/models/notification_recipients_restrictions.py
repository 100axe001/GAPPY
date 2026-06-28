from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.group_name import GroupName
  from ..models.restricted_permission import RestrictedPermission





T = TypeVar("T", bound="NotificationRecipientsRestrictions")



@_attrs_define
class NotificationRecipientsRestrictions:
    """ Details of the group membership or permissions needed to receive the notification.

        Attributes:
            group_ids (list[str] | Unset): List of groupId memberships required to receive the notification.
            groups (list[GroupName] | Unset): List of group memberships required to receive the notification.
            permissions (list[RestrictedPermission] | Unset): List of permissions required to receive the notification.
     """

    group_ids: list[str] | Unset = UNSET
    groups: list[GroupName] | Unset = UNSET
    permissions: list[RestrictedPermission] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.group_name import GroupName
        from ..models.restricted_permission import RestrictedPermission
        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids



        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)



        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if groups is not UNSET:
            field_dict["groups"] = groups
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_name import GroupName
        from ..models.restricted_permission import RestrictedPermission
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("groupIds", UNSET))


        _groups = d.pop("groups", UNSET)
        groups: list[GroupName] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GroupName.from_dict(groups_item_data)



                groups.append(groups_item)


        _permissions = d.pop("permissions", UNSET)
        permissions: list[RestrictedPermission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = RestrictedPermission.from_dict(permissions_item_data)



                permissions.append(permissions_item)


        notification_recipients_restrictions = cls(
            group_ids=group_ids,
            groups=groups,
            permissions=permissions,
        )

        return notification_recipients_restrictions

