from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.usergroup_object import UsergroupObject





T = TypeVar("T", bound="UsergroupsListUsergroupsListSchema")



@_attrs_define
class UsergroupsListUsergroupsListSchema:
    """ Schema for successful response from usergroups.list method

        Attributes:
            ok (bool):
            usergroups (list[UsergroupObject]):
     """

    ok: bool
    usergroups: list[UsergroupObject]





    def to_dict(self) -> dict[str, Any]:
        from ..models.usergroup_object import UsergroupObject
        ok = self.ok

        usergroups = []
        for usergroups_item_data in self.usergroups:
            usergroups_item = usergroups_item_data.to_dict()
            usergroups.append(usergroups_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "usergroups": usergroups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usergroup_object import UsergroupObject
        d = dict(src_dict)
        ok = d.pop("ok")

        usergroups = []
        _usergroups = d.pop("usergroups")
        for usergroups_item_data in (_usergroups):
            usergroups_item = UsergroupObject.from_dict(usergroups_item_data)



            usergroups.append(usergroups_item)


        usergroups_list_usergroups_list_schema = cls(
            ok=ok,
            usergroups=usergroups,
        )

        return usergroups_list_usergroups_list_schema

