from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsergroupsUsersUpdateDataBody")



@_attrs_define
class UsergroupsUsersUpdateDataBody:
    """ 
        Attributes:
            usergroup (str): The encoded ID of the User Group to update.
            users (str): A comma separated string of encoded user IDs that represent the entire list of users for the User
                Group.
            include_count (bool | Unset): Include the number of users in the User Group.
     """

    usergroup: str
    users: str
    include_count: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        usergroup = self.usergroup

        users = self.users

        include_count = self.include_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "usergroup": usergroup,
            "users": users,
        })
        if include_count is not UNSET:
            field_dict["include_count"] = include_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usergroup = d.pop("usergroup")

        users = d.pop("users")

        include_count = d.pop("include_count", UNSET)

        usergroups_users_update_data_body = cls(
            usergroup=usergroup,
            users=users,
            include_count=include_count,
        )


        usergroups_users_update_data_body.additional_properties = d
        return usergroups_users_update_data_body

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
