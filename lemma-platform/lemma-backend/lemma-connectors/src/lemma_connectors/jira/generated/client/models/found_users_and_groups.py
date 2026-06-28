from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.found_groups import FoundGroups
  from ..models.found_users import FoundUsers





T = TypeVar("T", bound="FoundUsersAndGroups")



@_attrs_define
class FoundUsersAndGroups:
    """ List of users and groups found in a search.

        Attributes:
            groups (FoundGroups | Unset): The list of groups found in a search, including header text (Showing X of Y
                matching groups) and total of matched groups.
            users (FoundUsers | Unset): The list of users found in a search, including header text (Showing X of Y matching
                users) and total of matched users.
     """

    groups: FoundGroups | Unset = UNSET
    users: FoundUsers | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.found_groups import FoundGroups
        from ..models.found_users import FoundUsers
        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.found_groups import FoundGroups
        from ..models.found_users import FoundUsers
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: FoundGroups | Unset
        if isinstance(_groups,  Unset):
            groups = UNSET
        else:
            groups = FoundGroups.from_dict(_groups)




        _users = d.pop("users", UNSET)
        users: FoundUsers | Unset
        if isinstance(_users,  Unset):
            users = UNSET
        else:
            users = FoundUsers.from_dict(_users)




        found_users_and_groups = cls(
            groups=groups,
            users=users,
        )

        return found_users_and_groups

